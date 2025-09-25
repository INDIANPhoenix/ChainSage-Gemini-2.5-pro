"""
LLM provider abstraction for ChainSage.

Follows research/openai patterns for client initialization, rate limiting,
and error handling. Supports multiple providers with fallback mechanisms.
"""

import asyncio
import logging
from typing import Dict, List, Optional, Any, Union
from datetime import datetime, timedelta
from contextlib import asynccontextmanager

try:
    from openai import AsyncOpenAI
    from openai.types.chat import ChatCompletion, ChatCompletionMessage
    from openai.types.chat.chat_completion import Choice
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    # Mock types for development
    AsyncOpenAI = None
    ChatCompletion = None
    ChatCompletionMessage = None
    Choice = None

from ..core.config import Settings, get_settings

logger = logging.getLogger(__name__)


class RateLimiter:
    """
    Simple rate limiter for API calls.

    Follows research patterns for handling OpenAI rate limits.
    """

    def __init__(self, max_requests_per_minute: int = 50):
        self.max_requests = max_requests_per_minute
        self.requests = []
        self.lock = asyncio.Lock()

    async def acquire(self):
        """Acquire rate limit permission."""
        async with self.lock:
            now = datetime.now()
            # Remove requests older than 1 minute
            self.requests = [req_time for req_time in self.requests
                           if now - req_time < timedelta(minutes=1)]

            if len(self.requests) >= self.max_requests:
                # Calculate wait time
                oldest_request = min(self.requests)
                wait_time = (oldest_request + timedelta(minutes=1) - now).total_seconds()
                if wait_time > 0:
                    logger.info(f"Rate limit reached, waiting {wait_time:.2f} seconds")
                    await asyncio.sleep(wait_time)
                    return await self.acquire()

            self.requests.append(now)


class LLMProvider:
    """Abstract base class for LLM providers."""

    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str,
        tools: Optional[List[Dict]] = None,
        **kwargs
    ) -> ChatCompletion:
        """Create chat completion."""
        raise NotImplementedError

    async def stream_completion(
        self,
        messages: List[Dict[str, str]],
        model: str,
        **kwargs
    ):
        """Create streaming chat completion."""
        raise NotImplementedError


class OpenAIProvider(LLMProvider):
    """
    OpenAI provider implementation.

    Follows research/openai patterns for client setup and function calling.
    """

    def __init__(self, settings: Settings):
        if not OPENAI_AVAILABLE:
            raise ImportError("OpenAI package not available. Install with: pip install openai")

        self.settings = settings
        self.client = AsyncOpenAI(
            api_key=settings.openai.api_key,
            timeout=settings.openai.timeout
        )
        self.rate_limiter = RateLimiter(max_requests_per_minute=50)

    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        tools: Optional[List[Dict]] = None,
        tool_choice: str = "auto",
        **kwargs
    ) -> ChatCompletion:
        """
        Create chat completion with function calling support.

        Follows research/openai/page8_function_calling.md patterns.
        """
        await self.rate_limiter.acquire()

        model = model or self.settings.openai.model

        # Prepare request parameters
        params = {
            "model": model,
            "messages": messages,
            "max_tokens": kwargs.get("max_tokens", self.settings.openai.max_tokens),
            "temperature": kwargs.get("temperature", self.settings.openai.temperature),
        }

        # Add function calling if tools provided
        if tools:
            params["tools"] = tools
            params["tool_choice"] = tool_choice

        try:
            response = await self.client.chat.completions.create(**params)
            logger.debug(f"OpenAI API call successful: {response.usage}")
            return response

        except Exception as e:
            logger.error(f"OpenAI API error: {str(e)}")
            raise

    async def stream_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        **kwargs
    ):
        """Create streaming chat completion."""
        await self.rate_limiter.acquire()

        model = model or self.settings.openai.model

        params = {
            "model": model,
            "messages": messages,
            "stream": True,
            "max_tokens": kwargs.get("max_tokens", self.settings.openai.max_tokens),
            "temperature": kwargs.get("temperature", self.settings.openai.temperature),
        }

        try:
            async for chunk in await self.client.chat.completions.create(**params):
                yield chunk
        except Exception as e:
            logger.error(f"OpenAI streaming error: {str(e)}")
            raise


class MockProvider(LLMProvider):
    """Mock provider for testing and development."""

    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str,
        tools: Optional[List[Dict]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        """Mock chat completion for testing."""
        # Simulate API delay
        await asyncio.sleep(0.1)

        # Generate mock response based on last message
        last_message = messages[-1]["content"] if messages else "test"

        # Mock Solidity contract response
        if "solidity" in last_message.lower() or "contract" in last_message.lower():
            mock_content = '''pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MockToken is ERC20, Ownable {
    constructor() ERC20("MockToken", "MOCK") {
        _mint(msg.sender, 1000000 * 10**decimals());
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}'''
        else:
            mock_content = f"Mock response to: {last_message[:100]}..."

        return {
            "id": "mock-response",
            "object": "chat.completion",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": mock_content
                    },
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": 50,
                "completion_tokens": 100,
                "total_tokens": 150
            }
        }

    async def stream_completion(
        self,
        messages: List[Dict[str, str]],
        model: str,
        **kwargs
    ):
        """Mock streaming completion."""
        response = await self.chat_completion(messages, model, **kwargs)
        content = response["choices"][0]["message"]["content"]

        # Stream content word by word
        words = content.split()
        for word in words:
            yield {
                "id": "mock-stream",
                "choices": [
                    {
                        "delta": {"content": word + " "},
                        "finish_reason": None
                    }
                ]
            }
            await asyncio.sleep(0.01)

        # Final chunk
        yield {
            "id": "mock-stream",
            "choices": [{"delta": {}, "finish_reason": "stop"}]
        }


class LLMProviderManager:
    """
    Manager for LLM providers with fallback support.

    Follows dependency injection patterns from research/fastapi.
    """

    def __init__(self, settings: Settings):
        self.settings = settings
        self.providers: Dict[str, LLMProvider] = {}
        self.primary_provider = "openai"

        # Initialize providers
        self._initialize_providers()

    def _initialize_providers(self):
        """Initialize available providers."""
        try:
            # Try to initialize OpenAI provider
            if OPENAI_AVAILABLE and self.settings.openai.api_key:
                self.providers["openai"] = OpenAIProvider(self.settings)
                logger.info("OpenAI provider initialized successfully")
            else:
                logger.warning("OpenAI provider not available")
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI provider: {e}")

        # Always have mock provider for testing
        self.providers["mock"] = MockProvider()

        if not self.providers:
            raise ValueError("No LLM providers available")

    def get_provider(self, provider_name: Optional[str] = None) -> LLMProvider:
        """Get LLM provider by name or return primary provider."""
        provider_name = provider_name or self.primary_provider

        if provider_name in self.providers:
            return self.providers[provider_name]

        # Fallback to any available provider
        if self.providers:
            fallback = next(iter(self.providers.values()))
            logger.warning(f"Provider {provider_name} not found, using fallback")
            return fallback

        raise ValueError(f"No providers available")

    async def chat_completion(
        self,
        messages: List[Dict[str, str]],
        provider: Optional[str] = None,
        **kwargs
    ) -> ChatCompletion:
        """Create chat completion with automatic provider selection."""
        llm_provider = self.get_provider(provider)
        return await llm_provider.chat_completion(messages, **kwargs)

    async def stream_completion(
        self,
        messages: List[Dict[str, str]],
        provider: Optional[str] = None,
        **kwargs
    ):
        """Create streaming completion with automatic provider selection."""
        llm_provider = self.get_provider(provider)
        async for chunk in llm_provider.stream_completion(messages, **kwargs):
            yield chunk

    @asynccontextmanager
    async def get_client(self, provider: Optional[str] = None):
        """
        Context manager for getting LLM client.

        Usage:
            async with provider_manager.get_client() as client:
                response = await client.chat_completion(messages)
        """
        llm_provider = self.get_provider(provider)
        try:
            yield llm_provider
        except Exception as e:
            logger.error(f"LLM provider error: {e}")
            raise
        finally:
            # Cleanup if needed
            pass


# Global provider manager instance
_provider_manager: Optional[LLMProviderManager] = None


def get_llm_provider_manager() -> LLMProviderManager:
    """
    Get LLM provider manager singleton.

    Used for dependency injection in FastAPI and agents.
    """
    global _provider_manager
    if _provider_manager is None:
        settings = get_settings()
        _provider_manager = LLMProviderManager(settings)
    return _provider_manager


def reset_provider_manager():
    """Reset provider manager (useful for testing)."""
    global _provider_manager
    _provider_manager = None


if __name__ == "__main__":
    # Test provider initialization
    import asyncio

    async def test_providers():
        try:
            settings = get_settings()
            manager = LLMProviderManager(settings)

            print("✅ Provider manager initialized")
            print(f"📋 Available providers: {list(manager.providers.keys())}")

            # Test mock provider
            messages = [{"role": "user", "content": "Create a simple ERC20 token"}]
            response = await manager.chat_completion(messages, provider="mock")
            print(f"🤖 Mock response: {response['choices'][0]['message']['content'][:100]}...")

        except Exception as e:
            print(f"❌ Provider error: {e}")

    asyncio.run(test_providers())