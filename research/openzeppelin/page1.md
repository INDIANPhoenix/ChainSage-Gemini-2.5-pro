Title: Contracts - OpenZeppelin Docs

URL Source: https://docs.openzeppelin.com/contracts

Markdown Content:
**A library for secure smart contract development.** Build on a solid foundation of community-vetted code.

*   Implementations of standards like [ERC20](https://docs.openzeppelin.com/contracts/5.x/erc20) and [ERC721](https://docs.openzeppelin.com/contracts/5.x/erc721).

*   Flexible [role-based permissioning](https://docs.openzeppelin.com/contracts/5.x/access-control) scheme.

*   Reusable [Solidity components](https://docs.openzeppelin.com/contracts/5.x/utilities) to build custom contracts and complex decentralized systems.

OpenZeppelin Contracts uses semantic versioning to communicate backwards compatibility of its API and storage layout. For upgradeable contracts, the storage layout of different major versions should be assumed incompatible, for example, it is unsafe to upgrade from 4.9.3 to 5.0.0. Learn more at [Backwards Compatibility](https://docs.openzeppelin.com/contracts/5.x/backwards-compatibility).

[](https://docs.openzeppelin.com/contracts#overview)Overview
------------------------------------------------------------

### [](https://docs.openzeppelin.com/contracts#install)Installation

#### [](https://docs.openzeppelin.com/contracts#hardhat_npm)Hardhat (npm)

`$ npm install @openzeppelin/contracts`

#### [](https://docs.openzeppelin.com/contracts#foundry_git)Foundry (git)

When installing via git, it is a common error to use the `master` branch. This is a development branch that should be avoided in favor of tagged releases. The release process involves security measures that the `master` branch does not guarantee.

Foundry installs the latest version initially, but subsequent `forge update` commands will use the `master` branch.

`$ forge install OpenZeppelin/openzeppelin-contracts`

Add `@openzeppelin/contracts/=lib/openzeppelin-contracts/contracts/` in `remappings.txt.`

### [](https://docs.openzeppelin.com/contracts#usage)Usage

Once installed, you can use the contracts in the library by importing them:

```
// contracts/MyNFT.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract MyNFT is ERC721 {
    constructor() ERC721("MyNFT", "MNFT") {}
}
```

If you’re new to smart contract development, head to [Developing Smart Contracts](https://docs.openzeppelin.com/learn/developing-smart-contracts) to learn about creating a new project and compiling your contracts.

To keep your system secure, you should **always** use the installed code as-is, and neither copy-paste it from online sources, nor modify it yourself. The library is designed so that only the contracts and functions you use are deployed, so you don’t need to worry about it needlessly increasing gas costs.

[](https://docs.openzeppelin.com/contracts#security)Security
------------------------------------------------------------

The [Security Center](https://contracts.openzeppelin.com/security) contains more details about the secure development process.

[](https://docs.openzeppelin.com/contracts#next-steps)Learn More
----------------------------------------------------------------

The guides in the sidebar will teach about different concepts, and how to use the related contracts that OpenZeppelin Contracts provides:

*   [Access Control](https://docs.openzeppelin.com/contracts/5.x/access-control): decide who can perform each of the actions on your system.

*   [Tokens](https://docs.openzeppelin.com/contracts/5.x/tokens): create tradable assets or collectibles, like the well known [ERC20](https://docs.openzeppelin.com/contracts/5.x/erc20) and [ERC721](https://docs.openzeppelin.com/contracts/5.x/erc721) standards.

*   [Utilities](https://docs.openzeppelin.com/contracts/5.x/utilities): generic useful tools, including non-overflowing math, signature verification, and trustless paying systems.

The [full API](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20) is also thoroughly documented, and serves as a great reference when developing your smart contract application. You can also ask for help or follow Contracts' development in the [community forum](https://forum.openzeppelin.com/).

The following articles provide great background reading, though please note, some of the referenced tools have changed as the tooling in the ecosystem continues to rapidly evolve.

*   [The Hitchhiker’s Guide to Smart Contracts in Ethereum](https://blog.openzeppelin.com/the-hitchhikers-guide-to-smart-contracts-in-ethereum-848f08001f05) will help you get an overview of the various tools available for smart contract development, and help you set up your environment.

*   [A Gentle Introduction to Ethereum Programming, Part 1](https://blog.openzeppelin.com/a-gentle-introduction-to-ethereum-programming-part-1-783cc7796094) provides very useful information on an introductory level, including many basic concepts from the Ethereum platform.

*   For a more in-depth dive, you may read the guide [Designing the architecture for your Ethereum application](https://blog.openzeppelin.com/designing-the-architecture-for-your-ethereum-application-9cec086f8317), which discusses how to better structure your application and its relationship to the real world.
