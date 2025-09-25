Title: Extending Contracts - OpenZeppelin Docs

URL Source: https://docs.openzeppelin.com/contracts/5.x/extending-contracts

Markdown Content:
Extending Contracts - OpenZeppelin Docs

===============

[Home](https://docs.openzeppelin.com/)

Contracts

 5.x 

Current version

*   [5.x](https://docs.openzeppelin.com/contracts/5.x/)

Other versions

*   [4.x](https://docs.openzeppelin.com/contracts/4.x/)
*   [3.x](https://docs.openzeppelin.com/contracts/3.x/)
*   [2.x](https://docs.openzeppelin.com/contracts/2.x/)

1.   [Overview](https://docs.openzeppelin.com/contracts/5.x/)
2.   [Wizard](https://docs.openzeppelin.com/contracts/5.x/wizard)
3.   [Extending Contracts](https://docs.openzeppelin.com/contracts/5.x/extending-contracts)
4.   [Using with Upgrades](https://docs.openzeppelin.com/contracts/5.x/upgradeable)
5.   [Backwards Compatibility](https://docs.openzeppelin.com/contracts/5.x/backwards-compatibility)
6.   [Access Control](https://docs.openzeppelin.com/contracts/5.x/access-control)
7.   ![Image 1](https://docs.openzeppelin.com/_/images/icons/arrow.svg)[Account Abstraction](https://docs.openzeppelin.com/contracts/5.x/account-abstraction)
    1.   ![Image 2](https://docs.openzeppelin.com/_/images/icons/arrow.svg)[Accounts](https://docs.openzeppelin.com/contracts/5.x/accounts)
        1.   [EOA Delegation](https://docs.openzeppelin.com/contracts/5.x/eoa-delegation)
        2.   [Multisig](https://docs.openzeppelin.com/contracts/5.x/multisig)

8.   ![Image 3](https://docs.openzeppelin.com/_/images/icons/arrow.svg)[Tokens](https://docs.openzeppelin.com/contracts/5.x/tokens)
    1.   ![Image 4](https://docs.openzeppelin.com/_/images/icons/arrow.svg)[ERC-20](https://docs.openzeppelin.com/contracts/5.x/erc20)
        1.   [Creating Supply](https://docs.openzeppelin.com/contracts/5.x/erc20-supply)

    2.   [ERC-721](https://docs.openzeppelin.com/contracts/5.x/erc721)
    3.   [ERC-1155](https://docs.openzeppelin.com/contracts/5.x/erc1155)
    4.   [ERC-4626](https://docs.openzeppelin.com/contracts/5.x/erc4626)
    5.   [ERC-6909](https://docs.openzeppelin.com/contracts/5.x/erc6909)

9.   [Governance](https://docs.openzeppelin.com/contracts/5.x/governance)
10.   [Utilities](https://docs.openzeppelin.com/contracts/5.x/utilities)
11.   [Subgraphs](https://docs.openzeppelin.com/subgraphs/0.1.x/)
12.   [FAQ](https://docs.openzeppelin.com/contracts/5.x/faq)
13.   ![Image 5](https://docs.openzeppelin.com/_/images/icons/arrow.svg)API
    1.   [Access](https://docs.openzeppelin.com/contracts/5.x/api/access)
    2.   [Account](https://docs.openzeppelin.com/contracts/5.x/api/account)
    3.   [Finance](https://docs.openzeppelin.com/contracts/5.x/api/finance)
    4.   [Governance](https://docs.openzeppelin.com/contracts/5.x/api/governance)
    5.   [Interfaces](https://docs.openzeppelin.com/contracts/5.x/api/interfaces)
    6.   [Meta Transactions](https://docs.openzeppelin.com/contracts/5.x/api/metatx)
    7.   [Proxy](https://docs.openzeppelin.com/contracts/5.x/api/proxy)
    8.   ![Image 6](https://docs.openzeppelin.com/_/images/icons/arrow.svg)Tokens
        1.   [Common](https://docs.openzeppelin.com/contracts/5.x/api/token/common)
        2.   [ERC 20](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20)
        3.   [ERC 721](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721)
        4.   [ERC 1155](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155)
        5.   [ERC 6909](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC6909)

    9.   ![Image 7](https://docs.openzeppelin.com/_/images/icons/arrow.svg)[Utils](https://docs.openzeppelin.com/contracts/5.x/api/utils)
        1.   [Cryptography](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography)

[](https://docs.openzeppelin.com/)

- [x] 

[GitHub](https://github.com/OpenZeppelin)[Forum](https://forum.openzeppelin.com/)[Blog](https://blog.openzeppelin.com/)[Website](https://openzeppelin.com/)

Extending Contracts
===================

Most of the OpenZeppelin Contracts are expected to be used via [inheritance](https://solidity.readthedocs.io/en/latest/contracts.html#inheritance): you will _inherit_ from them when writing your own contracts.

This is the commonly found `is` syntax, like in `contract MyToken is ERC20`.

Unlike `contract`s, Solidity `library`s are not inherited from and instead rely on the [`using for`](https://solidity.readthedocs.io/en/latest/contracts.html#using-for) syntax.

OpenZeppelin Contracts has some `library`s: most are in the [Utils](https://docs.openzeppelin.com/contracts/5.x/api/utils) directory.

[](https://docs.openzeppelin.com/contracts/5.x/extending-contracts#overriding)Overriding
----------------------------------------------------------------------------------------

Inheritance is often used to add the parent contract’s functionality to your own contract, but that’s not all it can do. You can also _change_ how some parts of the parent behave using _overrides_.

For example, imagine you want to change [`AccessControl`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessControl) so that [`revokeRole`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessControl-revokeRole-bytes32-address-) can no longer be called. This can be achieved using overrides:

```solidity
// contracts/AccessControlModified.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {AccessControl} from "@openzeppelin/contracts/access/AccessControl.sol";

contract AccessControlModified is AccessControl {
    error AccessControlNonRevocable();

    // Override the revokeRole function
    function revokeRole(bytes32, address) public pure override {
        revert AccessControlNonRevocable();
    }
}
```

The old `revokeRole` is then replaced by our override, and any calls to it will immediately revert. We cannot _remove_ the function from the contract, but reverting on all calls is good enough.

### [](https://docs.openzeppelin.com/contracts/5.x/extending-contracts#calling_super)Calling `super`

Sometimes you want to _extend_ a parent’s behavior, instead of outright changing it to something else. This is where `super` comes in.

The `super` keyword will let you call functions defined in a parent contract, even if they are overridden. This mechanism can be used to add additional checks to a function, emit events, or otherwise add functionality as you see fit.

For more information on how overrides work, head over to the [official Solidity documentation](https://solidity.readthedocs.io/en/latest/contracts.html#index-17).

Here is a modified version of [`AccessControl`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessControl) where [`revokeRole`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessControl-revokeRole-bytes32-address-) cannot be used to revoke the `DEFAULT_ADMIN_ROLE`:

```solidity
Unresolved include directive in modules/ROOT/pages/extending-contracts.adoc - include::api:example$access-control/AccessControlNonRevokableAdmin.sol[]
```

The `super.revokeRole` statement at the end will invoke `AccessControl`'s original version of `revokeRole`, the same code that would’ve run if there were no overrides in place.

The same rule is implemented and extended in [`AccessControlDefaultAdminRules`](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessControlDefaultAdminRules), an extension that also adds enforced security measures for the `DEFAULT_ADMIN_ROLE`.

[](https://docs.openzeppelin.com/contracts/5.x/extending-contracts#security)Security
------------------------------------------------------------------------------------

The maintainers of OpenZeppelin Contracts are mainly concerned with the correctness and security of the code as published in the library, and the combinations of base contracts with the official extensions from the library.

Custom overrides, especially to hooks, can disrupt important assumptions and may introduce security risks in the code that was previously secure. While we try to ensure the contracts remain secure in the face of a wide range of potential customizations, this is done in a best-effort manner. While we try to document all important assumptions, this should not be relied upon. Custom overrides should be carefully reviewed and checked against the source code of the contract they are customizing to fully understand their impact and guarantee their security.

The way functions interact internally should not be assumed to stay stable across releases of the library. For example, a function that is used in one context in a particular release may not be used in the same context in the next release. Contracts that override functions should revalidate their assumptions when updating the version of OpenZeppelin Contracts they are built on.

[← Wizard](https://docs.openzeppelin.com/contracts/5.x/wizard)

[Using with Upgrades →](https://docs.openzeppelin.com/contracts/5.x/upgradeable)

### Extending Contracts

*   [Overriding](https://docs.openzeppelin.com/contracts/5.x/extending-contracts#overriding)
    *   [Calling `super`](https://docs.openzeppelin.com/contracts/5.x/extending-contracts#calling_super)

*   [Security](https://docs.openzeppelin.com/contracts/5.x/extending-contracts#security)

© OpenZeppelin 2017-[Privacy](https://openzeppelin.com/privacy)[Terms of Use](https://openzeppelin.com/tos)
