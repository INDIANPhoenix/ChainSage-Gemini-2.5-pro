// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title SecureDEX
 * @dev A secure DEX contract with vulnerabilities fixed by ChainSage
 * Security improvements applied:
 * - Added reentrancy protection
 * - Fixed access control issues
 * - Added slippage protection
 * - Protected against integer overflow
 * - Fixed function visibility issues
 */
contract SecureDEX is Ownable, ReentrancyGuard {

    struct LiquidityPool {
        address tokenA;
        address tokenB;
        uint256 reserveA;
        uint256 reserveB;
        uint256 totalShares;
    }

    mapping(bytes32 => LiquidityPool) public pools;
    mapping(bytes32 => mapping(address => uint256)) public userShares;
    mapping(address => uint256) public balances;

    uint256 public feeRate = 30; // 0.3%
    uint256 public constant FEE_DENOMINATOR = 10000;
    uint256 public constant MINIMUM_LIQUIDITY = 1000; // Minimum liquidity requirement

    event Swap(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);
    event LiquidityAdded(address indexed user, bytes32 indexed poolId, uint256 shares);
    event LiquidityRemoved(address indexed user, bytes32 indexed poolId, uint256 shares);

    constructor(address initialOwner) Ownable(initialOwner) {}

    function getPoolId(address tokenA, address tokenB) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(tokenA, tokenB));
    }

    // FIXED: Added reentrancy protection and slippage protection
    function swap(address tokenIn, address tokenOut, uint256 amountIn, uint256 minAmountOut) external nonReentrant {
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token addresses");
        require(amountIn > 0, "Amount must be greater than 0");
        require(tokenIn != tokenOut, "Cannot swap same token");

        bytes32 poolId = getPoolId(tokenIn, tokenOut);
        LiquidityPool storage pool = pools[poolId];

        require(pool.tokenA != address(0), "Pool does not exist");

        // Transfer tokens from user
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Calculate output amount (improved constant product formula with fee)
        uint256 amountOut;
        uint256 amountInWithFee = amountIn * (FEE_DENOMINATOR - feeRate);

        if (tokenIn == pool.tokenA) {
            amountOut = (amountInWithFee * pool.reserveB) / (pool.reserveA * FEE_DENOMINATOR + amountInWithFee);
            pool.reserveA += amountIn;
            pool.reserveB -= amountOut;
        } else {
            amountOut = (amountInWithFee * pool.reserveA) / (pool.reserveB * FEE_DENOMINATOR + amountInWithFee);
            pool.reserveB += amountIn;
            pool.reserveA -= amountOut;
        }

        // FIXED: Added slippage protection
        require(amountOut >= minAmountOut, "Slippage too high");

        // Transfer output tokens to user
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit Swap(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // FIXED: Added minimum liquidity requirement
    function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external nonReentrant {
        require(tokenA != address(0) && tokenB != address(0), "Invalid token addresses");
        require(amountA > 0 && amountB > 0, "Amounts must be greater than 0");
        require(tokenA != tokenB, "Cannot create pool with same token");

        bytes32 poolId = getPoolId(tokenA, tokenB);
        LiquidityPool storage pool = pools[poolId];

        if (pool.tokenA == address(0)) {
            // Initialize new pool
            pool.tokenA = tokenA;
            pool.tokenB = tokenB;
        }

        // Transfer tokens
        IERC20(tokenA).transferFrom(msg.sender, address(this), amountA);
        IERC20(tokenB).transferFrom(msg.sender, address(this), amountB);

        uint256 shares;
        if (pool.totalShares == 0) {
            shares = sqrt(amountA * amountB);
            require(shares >= MINIMUM_LIQUIDITY, "Insufficient liquidity provided");
        } else {
            shares = min(
                (amountA * pool.totalShares) / pool.reserveA,
                (amountB * pool.totalShares) / pool.reserveB
            );
        }

        pool.reserveA += amountA;
        pool.reserveB += amountB;
        pool.totalShares += shares;
        userShares[poolId][msg.sender] += shares;

        emit LiquidityAdded(msg.sender, poolId, shares);
    }

    // FIXED: Added proper access control and validation
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner nonReentrant {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        IERC20(token).transfer(msg.sender, amount);
    }

    // FIXED: Protected against integer overflow
    function collectFees() external onlyOwner {
        uint256 currentBalance = address(this).balance;
        require(balances[owner()] <= type(uint256).max - currentBalance, "Overflow protection");
        balances[owner()] = balances[owner()] + currentBalance;
    }

    // Helper functions
    function sqrt(uint256 x) internal pure returns (uint256) {
        if (x == 0) return 0;
        uint256 z = (x + 1) / 2;
        uint256 y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
        return y;
    }

    function min(uint256 a, uint256 b) internal pure returns (uint256) {
        return a < b ? a : b;
    }

    // FIXED: Changed visibility from public to internal for security
    function updateReserves(bytes32 poolId, uint256 reserveA, uint256 reserveB) internal {
        pools[poolId].reserveA = reserveA;
        pools[poolId].reserveB = reserveB;
    }

    // Additional security functions
    function pauseContract() external onlyOwner {
        // Emergency pause functionality can be added here
    }

    function getPoolReserves(bytes32 poolId) external view returns (uint256 reserveA, uint256 reserveB) {
        LiquidityPool memory pool = pools[poolId];
        return (pool.reserveA, pool.reserveB);
    }
}