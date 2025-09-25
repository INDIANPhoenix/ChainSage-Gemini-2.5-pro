Title: ERC-1155 - OpenZeppelin Docs

URL Source: https://docs.openzeppelin.com/contracts/5.x/erc1155

Markdown Content:
ERC-1155 is a novel token standard that aims to take the best from previous standards to create a [**fungibility-agnostic**](https://docs.openzeppelin.com/contracts/5.x/tokens#different-kinds-of-tokens) and **gas-efficient**[token contract](https://docs.openzeppelin.com/contracts/5.x/tokens#but_first_coffee_a_primer_on_token_contracts).

ERC-1155 draws ideas from all of [ERC-20](https://docs.openzeppelin.com/contracts/5.x/erc20), [ERC-721](https://docs.openzeppelin.com/contracts/5.x/erc721), and [ERC-777](https://eips.ethereum.org/EIPS/eip-777). If you’re unfamiliar with those standards, head to their guides before moving on.

[](https://docs.openzeppelin.com/contracts/5.x/erc1155#multi-token-standard)Multi Token Standard
------------------------------------------------------------------------------------------------

The distinctive feature of ERC-1155 is that it uses a single smart contract to represent multiple tokens at once. This is why its [`balanceOf`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#IERC1155-balanceOf-address-uint256-) function differs from ERC-20’s and ERC-777’s: it has an additional `id` argument for the identifier of the token that you want to query the balance of.

This is similar to how ERC-721 does things, but in that standard a token `id` has no concept of balance: each token is non-fungible and exists or doesn’t. The ERC-721 [`balanceOf`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#IERC721-balanceOf-address-) function refers to _how many different tokens_ an account has, not how many of each. On the other hand, in ERC-1155 accounts have a distinct balance for each token `id`, and non-fungible tokens are implemented by simply minting a single one of them.

This approach leads to massive gas savings for projects that require multiple tokens. Instead of deploying a new contract for each token type, a single ERC-1155 token contract can hold the entire system state, reducing deployment costs and complexity.

[](https://docs.openzeppelin.com/contracts/5.x/erc1155#batch-operations)Batch Operations
----------------------------------------------------------------------------------------

Because all state is held in a single contract, it is possible to operate over multiple tokens in a single transaction very efficiently. The standard provides two functions, [`balanceOfBatch`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#IERC1155-balanceOfBatch-address---uint256---) and [`safeBatchTransferFrom`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#IERC1155-safeBatchTransferFrom-address-address-uint256---uint256---bytes-), that make querying multiple balances and transferring multiple tokens simpler and less gas-intensive.

In the spirit of the standard, we’ve also included batch operations in the non-standard functions, such as [`_mintBatch`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#ERC1155-_mintBatch-address-uint256---uint256---bytes-).

[](https://docs.openzeppelin.com/contracts/5.x/erc1155#constructing_an_erc_1155_token_contract)Constructing an ERC-1155 Token Contract
--------------------------------------------------------------------------------------------------------------------------------------

We’ll use ERC-1155 to track multiple items in our game, which will each have their own unique attributes. We mint all items to the deployer of the contract, which we can later transfer to players. Players are free to keep their tokens or trade them with other people as they see fit, as they would any other asset on the blockchain!

For simplicity, we will mint all items in the constructor, but you could add minting functionality to the contract to mint on demand to players.

Here’s what a contract for tokenized items might look like:

```
// contracts/GameItems.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC1155} from "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";

contract GameItems is ERC1155 {
    uint256 public constant GOLD = 0;
    uint256 public constant SILVER = 1;
    uint256 public constant THORS_HAMMER = 2;
    uint256 public constant SWORD = 3;
    uint256 public constant SHIELD = 4;

    constructor() ERC1155("https://game.example/api/item/{id}.json") {
        _mint(msg.sender, GOLD, 10 ** 18, "");
        _mint(msg.sender, SILVER, 10 ** 27, "");
        _mint(msg.sender, THORS_HAMMER, 1, "");
        _mint(msg.sender, SWORD, 10 ** 9, "");
        _mint(msg.sender, SHIELD, 10 ** 9, "");
    }
}
```

Note that for our Game Items, Gold is a fungible token whilst Thor’s Hammer is a non-fungible token as we minted only one.

The [`ERC1155`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#ERC1155) contract includes the optional extension [`IERC1155MetadataURI`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#IERC1155MetadataURI). That’s where the [`uri`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#IERC1155MetadataURI-uri-uint256-) function comes from: we use it to retrieve the metadata uri.

Also note that, unlike ERC-20, ERC-1155 lacks a `decimals` field, since each token is distinct and cannot be partitioned.

Once deployed, we will be able to query the deployer’s balance:

```
> gameItems.balanceOf(deployerAddress,3)
1000000000
```

We can transfer items to player accounts:

```
> gameItems.safeTransferFrom(deployerAddress, playerAddress, 2, 1, "0x0")
> gameItems.balanceOf(playerAddress, 2)
1
> gameItems.balanceOf(deployerAddress, 2)
0
```

We can also batch transfer items to player accounts and get the balance of batches:

```
> gameItems.safeBatchTransferFrom(deployerAddress, playerAddress, [0,1,3,4], [50,100,1,1], "0x0")
> gameItems.balanceOfBatch([playerAddress,playerAddress,playerAddress,playerAddress,playerAddress], [0,1,2,3,4])
[50,100,1,1,1]
```

The metadata uri can be obtained:

```
> gameItems.uri(2)
"https://game.example/api/item/{id}.json"
```

The `uri` can include the string `{id}` which clients must replace with the actual token ID, in lowercase hexadecimal (with no 0x prefix) and leading zero padded to 64 hex characters.

The JSON document for token ID 2 might look something like:

```
{
    "name": "Thor's hammer",
    "description": "Mjölnir, the legendary hammer of the Norse god of thunder.",
    "image": "https://game.example/item-id-8u5h2m.png",
    "strength": 20
}
```

You’ll notice that the item’s information is included in the metadata, but that information isn’t on-chain! So a game developer could change the underlying metadata, changing the rules of the game!

If you’d like to put all item information on-chain, you can extend ERC-721 to do so (though it will be rather costly) by providing a [`Base64`](https://docs.openzeppelin.com/contracts/5.x/utilities#base64) Data URI with the JSON schema encoded. You could also leverage IPFS to store the URI information, but these techniques are out of the scope of this overview guide

[](https://docs.openzeppelin.com/contracts/5.x/erc1155#sending-to-contracts)Sending Tokens to Contracts
-------------------------------------------------------------------------------------------------------

A key difference when using [`safeTransferFrom`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#IERC1155-safeTransferFrom-address-address-uint256-uint256-bytes-) is that token transfers to other contracts may revert with the following custom error:

`ERC1155InvalidReceiver("<ADDRESS>")`

This is a good thing! It means that the recipient contract has not registered itself as aware of the ERC-1155 protocol, so transfers to it are disabled to **prevent tokens from being locked forever**. As an example, [the Golem contract currently holds over 350k `GNT` tokens](https://etherscan.io/token/0xa74476443119A942dE498590Fe1f2454d7D4aC0d?a=0xa74476443119A942dE498590Fe1f2454d7D4aC0d), and lacks methods to get them out of there. This has happened to virtually every ERC20-backed project, usually due to user error.

In order for our contract to receive ERC-1155 tokens we can inherit from the convenience contract [`ERC1155Holder`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#ERC1155Holder) which handles the registering for us. However, we need to remember to implement functionality to allow tokens to be transferred out of our contract:

```
// contracts/MyERC115HolderContract.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC1155Holder} from "@openzeppelin/contracts/token/ERC1155/utils/ERC1155Holder.sol";

contract MyERC115HolderContract is ERC1155Holder {}
```
