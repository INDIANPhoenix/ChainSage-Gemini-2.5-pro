"""
Configuration management for ChainSage using pydantic-settings.

Follows patterns from research/fastapi for environment variable validation
and research/openai for API configuration.
"""

import os
from pathlib import Path
from typing import Optional
from pydantic import BaseModel, Field, validator
from pydantic_settings import BaseSettings


class OpenAIConfig(BaseModel):
    """OpenAI API configuration."""
    api_key: str = Field(..., description="OpenAI API key")
    model: str = Field("gpt-4o-2024-11-20", description="Model name from research")
    max_tokens: int = Field(4096, description="Maximum tokens per response")
    temperature: float = Field(0.1, description="Temperature for generation")
    timeout: int = Field(60, description="Request timeout in seconds")


class StaticAnalysisConfig(BaseModel):
    """Static analysis tools configuration."""
    slither_path: str = Field("/usr/local/bin/slither", description="Path to Slither executable")
    surya_path: str = Field("/usr/local/bin/surya", description="Path to Surya executable")
    use_docker: bool = Field(True, description="Use Docker for consistent environments")
    eth_security_toolbox_image: str = Field(
        "trailofbits/eth-security-toolbox",
        description="Docker image for security tools"
    )


class OutputConfig(BaseModel):
    """Output directory configuration."""
    base_dir: Path = Field(Path("./out"), description="Base output directory")
    contracts_dir: Path = Field(Path("./out/contracts"), description="Generated contracts directory")
    audits_dir: Path = Field(Path("./out/audits"), description="Audit reports directory")
    patches_dir: Path = Field(Path("./out/patches"), description="Patch files directory")
    tests_dir: Path = Field(Path("./out/tests"), description="Generated test files directory")

    def __init__(self, **data):
        super().__init__(**data)
        # Ensure all directories exist
        for dir_path in [self.base_dir, self.contracts_dir, self.audits_dir,
                        self.patches_dir, self.tests_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)


class APIConfig(BaseModel):
    """API server configuration."""
    host: str = Field("0.0.0.0", description="API host")
    port: int = Field(8000, description="API port")
    frontend_url: str = Field("http://localhost:3000", description="Frontend URL for CORS")
    debug: bool = Field(False, description="Debug mode")


class Settings(BaseSettings):
    """
    Main application settings using pydantic-settings.

    Follows research/fastapi patterns for environment variable management.
    """
    # OpenAI Configuration
    openai: OpenAIConfig = Field(default_factory=lambda: OpenAIConfig(
        api_key=os.getenv("OPENAI_API_KEY", ""),
        model=os.getenv("OPENAI_MODEL", "gpt-4o-2024-11-20")
    ))

    # Static Analysis Configuration
    static_analysis: StaticAnalysisConfig = Field(default_factory=StaticAnalysisConfig)

    # Output Configuration
    output: OutputConfig = Field(default_factory=OutputConfig)

    # API Configuration
    api: APIConfig = Field(default_factory=APIConfig)

    # Environment
    environment: str = Field("development", description="Environment (development/production)")
    log_level: str = Field("INFO", description="Logging level")

    @validator('openai')
    def validate_openai_config(cls, v):
        """Validate OpenAI configuration."""
        if not v.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        if not v.api_key.startswith(('sk-', 'sk-proj-')):
            raise ValueError("Invalid OpenAI API key format")
        return v

    @validator('static_analysis')
    def validate_static_analysis_config(cls, v):
        """Validate static analysis tools availability."""
        if not v.use_docker:
            # Check if tools are available locally
            if not Path(v.slither_path).exists():
                raise ValueError(f"Slither not found at {v.slither_path}")
            if not Path(v.surya_path).exists():
                raise ValueError(f"Surya not found at {v.surya_path}")
        return v

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False
        # Allow nested environment variables like OPENAI__API_KEY
        env_nested_delimiter = "__"


# Global settings instance
settings = Settings()


def get_settings() -> Settings:
    """
    Get application settings.

    Used for dependency injection in FastAPI following research patterns.
    """
    return settings


def validate_environment() -> bool:
    """
    Validate that all required environment variables and tools are available.

    Returns:
        bool: True if environment is valid, raises exceptions otherwise
    """
    try:
        # Validate settings initialization
        settings = get_settings()

        # Additional validation checks
        if settings.static_analysis.use_docker:
            # Check Docker availability
            import subprocess
            try:
                subprocess.run(["docker", "--version"],
                              capture_output=True, check=True, timeout=10)
            except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
                raise ValueError("Docker is required but not available")

        # Validate output directories are writable
        test_file = settings.output.base_dir / "test_write_permissions"
        try:
            test_file.write_text("test")
            test_file.unlink()
        except Exception:
            raise ValueError(f"Output directory {settings.output.base_dir} is not writable")

        return True

    except Exception as e:
        raise ValueError(f"Environment validation failed: {str(e)}")


if __name__ == "__main__":
    # Test configuration loading
    try:
        validate_environment()
        settings = get_settings()
        print("✅ Configuration loaded successfully")
        print(f"📁 Output directory: {settings.output.base_dir}")
        print(f"🤖 OpenAI model: {settings.openai.model}")
        print(f"🔍 Use Docker for static analysis: {settings.static_analysis.use_docker}")
    except Exception as e:
        print(f"❌ Configuration error: {e}")