// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";


/**
 * @title YieldFarming Protocol
 * @notice This contract allows users to stake tokens and earn yield.
 * @dev This contract uses OpenZeppelin libraries for security and best practices.
 */
contract YieldFarming is ERC20, AccessControl, Pausable, ReentrancyGuard {
    using SafeMath for uint256;

    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");

    uint256 public totalStaked;
    uint256 public rewardRate; // Rewards per block


    mapping(address => uint256) public stakedBalances;


    /**
     * @notice Constructor for the YieldFarming contract.
     * @param name_ The name of the ERC20 token.
     * @param symbol_ The symbol of the ERC20 token.
     * @param initialSupply_ The initial supply of the ERC20 token.
     * @param rewardRate_ The reward rate (per block).
     */
    constructor(string memory name_, string memory symbol_, uint256 initialSupply_, uint256 rewardRate_) ERC20(name_, symbol_) {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(ADMIN_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);
        _mint(msg.sender, initialSupply_);
        rewardRate = rewardRate_;

    }

    /**
     * @notice Stakes tokens and increases the total staked amount.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external whenNotPaused nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        _transfer(msg.sender, address(this), amount);
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
    }

    /**
     * @notice Unstakes tokens and decreases the total staked amount.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external whenNotPaused nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        _transfer(address(this), msg.sender, amount);

    }

     /**
     * @notice Allows the admin to pause the contract.
     */
    function pause() external onlyRole(ADMIN_ROLE) {
        _pause();
    }

    /**
     * @notice Allows the admin to unpause the contract.
     */
    function unpause() external onlyRole(ADMIN_ROLE) {
        _unpause();
    }


    /**
     * @notice Allows the minter to mint new tokens.
     * @param to The recipient of the minted tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) external onlyRole(MINTER_ROLE) {
        _mint(to, amount);
    }


    /**
     * @notice Returns the staked balance of a user.
     * @param user The address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    //Add further functionalities like claiming rewards as needed.  This is a basic framework.
}