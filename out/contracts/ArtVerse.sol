// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";


contract ArtVerse is ERC721, ERC721Enumerable, AccessControl, ReentrancyGuard {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");
    bytes32 public constant PAUSER_ROLE = keccak256("PAUSER_ROLE");

    Counters.Counter private _tokenIdCounter;
    mapping(uint256 => uint256) public startingPrice; //Starting price of Dutch Auction
    mapping(uint256 => uint256) public endingPrice; //Ending price of Dutch Auction
    mapping(uint256 => uint256) public auctionDuration; //Duration of Dutch Auction in seconds
    mapping(uint256 => uint256) public auctionStartTime; //Start time of Dutch Auction
    mapping(uint256 => address payable) public royaltyRecipient; //Recipient of royalties
    mapping(uint256 => uint256) public royaltyPercentage;  //Royalty percentage (e.g., 1000 for 10%)

    bool public paused;


    constructor() ERC721("ArtVerse", "ARTV") {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _grantRole(MINTER_ROLE, msg.sender);
        _grantRole(PAUSER_ROLE, msg.sender);
        paused = false;
    }

    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        require(!paused, "ERC721Pausable: token transfer while paused");
        super._beforeTokenTransfer(from, to, tokenId);
    }

    /**
     * @dev Mints a new NFT with a Dutch auction setup.
     * @param to Recipient of the NFT.
     * @param _startingPrice Starting price of the auction in wei.
     * @param _endingPrice Ending price of the auction in wei.
     * @param _auctionDuration Duration of the auction in seconds.
     * @param _royaltyRecipient Address to receive royalties.
     * @param _royaltyPercentage Royalty percentage (e.g., 1000 for 10%).
     */
    function mintNFT(
        address to,
        uint256 _startingPrice,
        uint256 _endingPrice,
        uint256 _auctionDuration,
        address payable _royaltyRecipient,
        uint256 _royaltyPercentage
    ) external onlyRole(MINTER_ROLE) {
        uint256 newItemId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, newItemId);

        startingPrice[newItemId] = _startingPrice;
        endingPrice[newItemId] = _endingPrice;
        auctionDuration[newItemId] = _auctionDuration;
        auctionStartTime[newItemId] = block.timestamp;
        royaltyRecipient[newItemId] = _royaltyRecipient;
        royaltyPercentage[newItemId] = _royaltyPercentage;

    }

    /**
     * @dev Purchases an NFT during a Dutch auction.
     * @param tokenId The ID of the NFT to purchase.
     */
    function buyNFT(uint256 tokenId) external payable nonReentrant {
        require(ownerOf(tokenId) == address(this), "NFT not available for purchase");
        require(block.timestamp <= auctionStartTime[tokenId] + auctionDuration[tokenId], "Auction has ended");

        uint256 currentPrice = calculateCurrentPrice(tokenId);
        require(msg.value >= currentPrice, "Insufficient funds");

        _transfer(address(this), msg.sender, tokenId);

        //Pay Royalties
        uint256 royaltyAmount = currentPrice.mul(_royaltyPercentage).div(10000);
        royaltyRecipient[tokenId].transfer(royaltyAmount);

        //Send remaining funds to artist
        uint256 artistAmount = currentPrice.sub(royaltyAmount);
        payable(msg.sender).transfer(artistAmount);


    }

    /**
     * @dev Calculates the current price of an NFT during a Dutch auction.
     * @param tokenId The ID of the NFT.
     * @return The current price of the NFT in wei.
     */
    function calculateCurrentPrice(uint256 tokenId) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - auctionStartTime[tokenId];
        if (timeElapsed >= auctionDuration[tokenId]) {
            return endingPrice[tokenId];
        }
        uint256 priceDifference = startingPrice[tokenId] - endingPrice[tokenId];
        uint256 priceReduction = priceDifference.mul(timeElapsed).div(auctionDuration[tokenId]);
        return startingPrice[tokenId] - priceReduction;
    }


    /**
     * @dev Pauses the contract. Only callable by the pauser role.
     */
    function pause() external onlyRole(PAUSER_ROLE) {
        paused = true;
    }

    /**
     * @dev Unpauses the contract. Only callable by the pauser role.
     */
    function unpause() external onlyRole(PAUSER_ROLE) {
        paused = false;
    }

    /**
     * @dev Burns a token. Only callable by the token owner.
     */
    function burn(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "ERC721Burnable: caller is not owner nor approved");
        _burn(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        virtual
        override(ERC721, ERC721Enumerable, AccessControl)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}