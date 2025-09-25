// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";


/**
 * @title TestCoin
 * @dev A simple ERC20 token with minting, burning, pausing, and reward distribution capabilities.
 */
contract TestCoin is ERC20, AccessControl, Pausable {
    using SafeMath for uint256;

    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");


    /**
     * @dev Grants the minter and pauser roles to the deployer.
     */
    constructor() ERC20("TestCoin", "TEST") {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(MINTER_ROLE, msg.sender);
        _grantRole(PAUSER_ROLE, msg.sender);
    }

    /**
     * @dev Mints new tokens. Only callable by accounts with the `MINTER_ROLE`.
     * @param to The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address to, uint256 amount) public onlyRole(MINTER_ROLE) whenNotPaused {
        _mint(to, amount);
    }

    /**
     * @dev Burns tokens. Anyone can burn their own tokens.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public whenNotPaused {
        _burn(_msgSender(), amount);
    }

    /**
     * @dev Pauses the contract. Only callable by accounts with the `PAUSER_ROLE`.
     */
    function pause() public onlyRole(PAUSER_ROLE) {
        _pause();
    }

    /**
     * @dev Unpauses the contract. Only callable by accounts with the `PAUSER_ROLE`.
     */
    function unpause() public onlyRole(PAUSER_ROLE) {
        _unpause();
    }


    /**
     * @dev Function to distribute rewards (example). This needs to be implemented according to the reward system logic.
     *      This example distributes rewards proportionally to the balance.
     * @param rewardAmount The total reward amount to distribute.
     */
    function distributeRewards(uint256 rewardAmount) public onlyRole(DEFAULT_ADMIN_ROLE) whenNotPaused {
        uint256 totalSupply = totalSupply();
        if (totalSupply == 0) return; // Avoid division by zero

        for (uint i = 0; i < address(this).balance; i++) {
            address holder = address(i);
            uint256 balance = balanceOf(holder);
            uint256 reward = (balance.mul(rewardAmount)).div(totalSupply);
            _mint(holder, reward);

        }

    }


    //Modifier to prevent reentrancy (Not strictly necessary with OpenZeppelin's Pausable, but good practice)
    modifier nonReentrant() {
        _nonReentrantBefore();
        _;
        _nonReentrantAfter();
    }

    uint256 private _reentrancyGuard;

    function _nonReentrantBefore() private {
        require(_reentrancyGuard == 0, "ReentrancyGuard: reentrant call");
        _reentrancyGuard = 1;
    }

    function _nonReentrantAfter() private {
        _reentrancyGuard = 0;
    }

    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC20, AccessControl) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}