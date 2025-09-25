Title: Utilities - OpenZeppelin Docs

URL Source: https://docs.openzeppelin.com/contracts/5.x/utilities

Markdown Content:
### [](https://docs.openzeppelin.com/contracts/5.x/utilities#packing)Packing

The storage in the EVM is shaped in chunks of 32 bytes, each of this chunks is known as a _slot_, and can hold multiple values together as long as these values don’t exceed its size. These properties of the storage allow for a technique known as _packing_, that consists of placing values together on a single storage slot to reduce the costs associated to reading and writing to multiple slots instead of just one.

Commonly, developers pack values using structs that place values together so they fit better in storage. However, this approach requires to load such struct from either calldata or memory. Although sometimes necessary, it may be useful to pack values in a single slot and treat it as a packed value without involving calldata or memory.

The [`Packing`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing) library is a set of utilities for packing values that fit in 32 bytes. The library includes 3 main functionalities:

*   Packing 2 `bytesXX` values

*   Extracting a packed `bytesXX` value from a `bytesYY`

*   Replacing a packed `bytesXX` value from a `bytesYY`

With these primitives, one can build custom functions to create custom packed types. For example, suppose you need to pack an `address` of 20 bytes with a `bytes4` selector and an `uint64` time period:

```
function _pack(address account, bytes4 selector, uint64 period) external pure returns (bytes32) {
    bytes12 subpack = Packing.pack_4_8(selector, bytes8(period));
    return Packing.pack_20_12(bytes20(account), subpack);
}

function _unpack(bytes32 pack) external pure returns (address, bytes4, uint64) {
    return (
        address(Packing.extract_32_20(pack, 0)),
        Packing.extract_32_4(pack, 20),
        uint64(Packing.extract_32_8(pack, 24))
    );
}
```

### [](https://docs.openzeppelin.com/contracts/5.x/utilities#storage_slots)Storage Slots

Solidity allocates a storage pointer for each variable declared in a contract. However, there are cases when it’s required to access storage pointers that can’t be derived by using regular Solidity. For those cases, the [`StorageSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot) library allows for manipulating storage slots directly.

```
bytes32 internal constant _IMPLEMENTATION_SLOT = 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc;

function _getImplementation() internal view returns (address) {
    return StorageSlot.getAddressSlot(_IMPLEMENTATION_SLOT).value;
}

function _setImplementation(address newImplementation) internal {
    require(newImplementation.code.length > 0);
    StorageSlot.getAddressSlot(_IMPLEMENTATION_SLOT).value = newImplementation;
}
```

The [`TransientSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot) library supports transient storage through user defined value types ([UDVTs](https://docs.soliditylang.org/en/latest/types.html#user-defined-value-types)), which enables the same value types as in Solidity.

```
bytes32 internal constant _LOCK_SLOT = 0xf4678858b2b588224636b8522b729e7722d32fc491da849ed75b3fdf3c84f542;

function _getTransientLock() internal view returns (bool) {
    return _LOCK_SLOT.asBoolean().tload();
}

function _setTransientLock(bool lock) internal {
    _LOCK_SLOT.asBoolean().tstore(lock);
}
```

Manipulating storage slots directly is an advanced practice. Developers MUST make sure that the storage pointer is not colliding with other variables.

One of the most common use cases for writing directly to storage slots is ERC-7201 for namespaced storage, which is guaranteed to not collide with other storage slots derived by Solidity.

Users can leverage this standard using the [`SlotDerivation`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation) library.

```
using SlotDerivation for bytes32;
string private constant _NAMESPACE = "<namespace>" // eg. example.main

function erc7201Pointer() internal view returns (bytes32) {
    return _NAMESPACE.erc7201Slot();
}
```

### [](https://docs.openzeppelin.com/contracts/5.x/utilities#base64)Base64

[`Base64`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64) util allows you to transform `bytes32` data into its Base64 `string` representation.

This is especially useful for building URL-safe tokenURIs for both [`ERC-721`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#IERC721Metadata-tokenURI-uint256-) or [`ERC-1155`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC1155#IERC1155MetadataURI-uri-uint256-). This library provides a clever way to serve URL-safe [Data URI](https://developer.mozilla.org/docs/Web/HTTP/Basics_of_HTTP/Data_URIs/) compliant strings to serve on-chain data structures.

Here is an example to send JSON Metadata through a Base64 Data URI using an ERC-721:

```
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import {Strings} from "@openzeppelin/contracts/utils/Strings.sol";
import {Base64} from "@openzeppelin/contracts/utils/Base64.sol";

contract Base64NFT is ERC721 {
    using Strings for uint256;

    constructor() ERC721("Base64NFT", "MTK") {}

    // ...

    function tokenURI(uint256 tokenId) public pure override returns (string memory) {
        // Equivalent to:
        // {
        //   "name": "Base64NFT #1",
        //   // Replace with extra ERC-721 Metadata properties
        // }
        // prettier-ignore
        string memory dataURI = string.concat("{\"name\": \"Base64NFT #", tokenId.toString(), "\"}");

        return string.concat("data:application/json;base64,", Base64.encode(bytes(dataURI)));
    }
}
```

### [](https://docs.openzeppelin.com/contracts/5.x/utilities#multicall)Multicall

The `Multicall` abstract contract comes with a `multicall` function that bundles together multiple calls in a single external call. With it, external accounts may perform atomic operations comprising several function calls. This is not only useful for EOAs to make multiple calls in a single transaction, it’s also a way to revert a previous call if a later one fails.

Consider this dummy contract:

```
// contracts/Box.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Multicall} from "@openzeppelin/contracts/utils/Multicall.sol";

contract Box is Multicall {
    function foo() public {
        // ...
    }

    function bar() public {
        // ...
    }
}
```

This is how to call the `multicall` function using Ethers.js, allowing `foo` and `bar` to be called in a single transaction:

```
// scripts/foobar.js

const instance = await ethers.deployContract("Box");

await instance.multicall([
    instance.interface.encodeFunctionData("foo"),
    instance.interface.encodeFunctionData("bar")
]);
```

### [](https://docs.openzeppelin.com/contracts/5.x/utilities#historical_block_hashes)Historical Block Hashes

[`Blockhash`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Blockhash) provides L2 protocol developers with extended access to historical block hashes beyond Ethereum’s native 256-block limit. By leveraging [EIP-2935](https://eips.ethereum.org/EIPS/eip-2935)'s history storage contract, the library enables access to block hashes up to 8,191 blocks in the past, making it invaluable for L2 fraud proofs and state verification systems.

The library seamlessly combines native `BLOCKHASH` opcode access for recent blocks (≤256) with EIP-2935 history storage queries for older blocks (257-8,191). It handles edge cases gracefully by returning zero for future blocks or those beyond the history window, matching the EVM’s behavior. The implementation uses gas-efficient assembly for static calls to the history storage contract.

```
contract L1Inbox {
    using Blockhash for uint256;

    function verifyBlockHash(uint256 blockNumber, bytes32 expectedHash) public view returns (bool) {
        return blockNumber.blockHash() == expectedHash;
    }
}
```

After EIP-2935 activation, it takes 8,191 blocks to completely fill the history storage. Before that, only block hashes since the fork block will be available.

### [](https://docs.openzeppelin.com/contracts/5.x/utilities#time)Time

The [`Time`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time) library provides helpers for manipulating time-related objects in a type-safe manner. It uses `uint48` for timepoints and `uint32` for durations, helping to reduce gas costs while providing adequate precision.

One of its key features is the `Delay` type, which represents a duration that can automatically change its value at a specified point in the future while maintaining delay guarantees. For example, when reducing a delay value (e.g., from 7 days to 1 day), the change only takes effect after the difference between the old and new delay (i.e. a 6 days) or a minimum setback period, preventing an attacker who gains admin access from immediately reducing security timeouts and executing sensitive operations. This is particularly useful for governance and security mechanisms where timelock periods need to be enforced.

Consider this example for using and safely updating Delays:

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {Time} from "contracts/utils/types/Time.sol";

contract MyDelayedContract {
    using Time for *;

    Time.Delay private _delay;

    constructor() {
        _delay = Time.toDelay(3 days);
    }

    function schedule(bytes32 operationId) external {
        // Get the current `_delay` value, respecting any pending delay changes if they've taken effect
        uint32 currentDelay = _delay.get();
        uint48 executionTime = Time.timestamp() + currentDelay;

        // ... schedule the operation at `executionTime`
    }

    function execute(bytes32 operationId) external {
        uint48 executionTime = getExecutionTime(operationId);
        require(executionTime > 0, "Operation not scheduled");
        require(Time.timestamp() >= executionTime, "Delay not elapsed yet");

        // ... execute the operation
    }

    // Update the delay with `Time`'s safety mechanism
    function updateDelay(uint32 newDelay) external {
        (Time.Delay updatedDelay, uint48 effect) = _delay.withUpdate(
            newDelay,    // The new delay value
            5 days       // Minimum setback if reducing the delay
        );

        _delay = updatedDelay;

        // ... emit events
    }

    // Get complete delay details including pending changes
    function getDelayDetails() external view returns (
        uint32 currentValue, // The current delay value
        uint32 pendingValue, // The pending delay value
        uint48 effectTime    // The timepoint when the pending delay change takes effect
    ) {
        return _delay.getFull();
    }
}
```

This pattern is used extensively in OpenZeppelin’s [AccessManager](https://docs.openzeppelin.com/contracts/5.x/api/access#AccessManager) for implementing secure time-based access control. For example, when changing an admin delay:

```
// From AccessManager.sol
function _setTargetAdminDelay(address target, uint32 newDelay) internal virtual {
    uint48 effect;
    (_targets[target].adminDelay, effect) = _targets[target].adminDelay.withUpdate(
        newDelay,
        minSetback()
    );

    emit TargetAdminDelayUpdated(target, newDelay, effect);
}
```
