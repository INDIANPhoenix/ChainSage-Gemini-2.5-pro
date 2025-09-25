// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title VulnerableDEX
 * @dev A deliberately vulnerable DEX contract to demonstrate ChainSage's analysis capabilities
 * Contains common DeFi vulnerabilities for educational purposes
 */
contract VulnerableDEX is Ownable {

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

    event Swap(address indexed user, address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut);
    event LiquidityAdded(address indexed user, bytes32 indexed poolId, uint256 shares);
    event LiquidityRemoved(address indexed user, bytes32 indexed poolId, uint256 shares);

    constructor(address initialOwner) Ownable(initialOwner) {}

    function getPoolId(address tokenA, address tokenB) public pure returns (bytes32) {
        return keccak256(abi.encodePacked(tokenA, tokenB));
    }

    // VULNERABILITY: No slippage protection
    function swap(address tokenIn, address tokenOut, uint256 amountIn, uint256 minAmountOut) external {
        bytes32 poolId = getPoolId(tokenIn, tokenOut);
        LiquidityPool storage pool = pools[poolId];

        require(pool.tokenA != address(0), "Pool does not exist");

        // Transfer tokens from user
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Calculate output amount (simplified constant product formula)
        uint256 amountOut;
        if (tokenIn == pool.tokenA) {
            amountOut = (amountIn * pool.reserveB) / (pool.reserveA + amountIn);
            pool.reserveA += amountIn;
            pool.reserveB -= amountOut;
        } else {
            amountOut = (amountIn * pool.reserveA) / (pool.reserveB + amountIn);
            pool.reserveB += amountIn;
            pool.reserveA -= amountOut;
        }

        // VULNERABILITY: No slippage check
        // require(amountOut >= minAmountOut, "Slippage too high");

        // Apply fee
        uint256 fee = (amountOut * feeRate) / FEE_DENOMINATOR;
        amountOut -= fee;

        // VULNERABILITY: No reentrancy protection
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit Swap(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    // VULNERABILITY: No minimum liquidity requirement
    function addLiquidity(address tokenA, address tokenB, uint256 amountA, uint256 amountB) external {
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

    // VULNERABILITY: No access control for emergency functions
    function emergencyWithdraw(address token, uint256 amount) external {
        // Should be onlyOwner but missing modifier
        IERC20(token).transfer(msg.sender, amount);
    }

    // VULNERABILITY: Integer overflow possibility
    function collectFees() external onlyOwner {
        // Vulnerable to overflow if balances[owner] is near max uint256
        balances[owner()] = balances[owner()] + address(this).balance;
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

    // VULNERABILITY: Public function that should be internal
    function updateReserves(bytes32 poolId, uint256 reserveA, uint256 reserveB) public {
        pools[poolId].reserveA = reserveA;
        pools[poolId].reserveB = reserveB;
    }
}