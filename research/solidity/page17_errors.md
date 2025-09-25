Title: Contracts — Solidity 0.8.31 documentation

URL Source: https://docs.soliditylang.org/en/latest/contracts.html

Published Time: Wed, 07 May 2025 17:06:12 GMT

Markdown Content:
Contracts in Solidity are similar to classes in object-oriented languages. They contain persistent data in state variables, and functions that can modify these variables. Calling a function on a different contract (instance) will perform an EVM function call and thus switch the context such that state variables in the calling contract are inaccessible. A contract and its functions need to be called for anything to happen. There is no “cron” concept in Ethereum to call a function at a particular event automatically.

Creating Contracts[](https://docs.soliditylang.org/en/latest/contracts.html#creating-contracts "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Contracts can be created “from outside” via Ethereum transactions or from within Solidity contracts.

IDEs, such as [Remix](https://remix.ethereum.org/), make the creation process seamless using UI elements.

One way to create contracts programmatically on Ethereum is via the JavaScript API [web3.js](https://github.com/web3/web3.js). It has a function called [web3.eth.Contract](https://web3js.readthedocs.io/en/1.0/web3-eth-contract.html#new-contract) to facilitate contract creation.

When a contract is created, its [constructor](https://docs.soliditylang.org/en/latest/contracts.html#constructor) (a function declared with the `constructor` keyword) is executed once.

A constructor is optional. Only one constructor is allowed, which means overloading is not supported.

After the constructor has executed, the final code of the contract is stored on the blockchain. This code includes all public and external functions and all functions that are reachable from there through function calls. The deployed code does not include the constructor code or internal functions only called from the constructor.

Internally, constructor arguments are passed [ABI encoded](https://docs.soliditylang.org/en/latest/abi-spec.html#abi) after the code of the contract itself, but you do not have to care about this if you use `web3.js`.

If a contract wants to create another contract, the source code (and the binary) of the created contract has to be known to the creator. This means that cyclic creation dependencies are impossible.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjIyIDwwLjkuMDsKCgpjb250cmFjdCBPd25lZFRva2VuIHsKICAgIC8vIGBUb2tlbkNyZWF0b3JgIGlzIGEgY29udHJhY3QgdHlwZSB0aGF0IGlzIGRlZmluZWQgYmVsb3cuCiAgICAvLyBJdCBpcyBmaW5lIHRvIHJlZmVyZW5jZSBpdCBhcyBsb25nIGFzIGl0IGlzIG5vdCB1c2VkCiAgICAvLyB0byBjcmVhdGUgYSBuZXcgY29udHJhY3QuCiAgICBUb2tlbkNyZWF0b3IgY3JlYXRvcjsKICAgIGFkZHJlc3Mgb3duZXI7CiAgICBieXRlczMyIG5hbWU7CgogICAgLy8gVGhpcyBpcyB0aGUgY29uc3RydWN0b3Igd2hpY2ggcmVnaXN0ZXJzIHRoZQogICAgLy8gY3JlYXRvciBhbmQgdGhlIGFzc2lnbmVkIG5hbWUuCiAgICBjb25zdHJ1Y3RvcihieXRlczMyIG5hbWVfKSB7CiAgICAgICAgLy8gU3RhdGUgdmFyaWFibGVzIGFyZSBhY2Nlc3NlZCB2aWEgdGhlaXIgbmFtZQogICAgICAgIC8vIGFuZCBub3QgdmlhIGUuZy4gYHRoaXMub3duZXJgLiBGdW5jdGlvbnMgY2FuCiAgICAgICAgLy8gYmUgYWNjZXNzZWQgZGlyZWN0bHkgb3IgdGhyb3VnaCBgdGhpcy5mYCwKICAgICAgICAvLyBidXQgdGhlIGxhdHRlciBwcm92aWRlcyBhbiBleHRlcm5hbCB2aWV3CiAgICAgICAgLy8gdG8gdGhlIGZ1bmN0aW9uLiBFc3BlY2lhbGx5IGluIHRoZSBjb25zdHJ1Y3RvciwKICAgICAgICAvLyB5b3Ugc2hvdWxkIG5vdCBhY2Nlc3MgZnVuY3Rpb25zIGV4dGVybmFsbHksCiAgICAgICAgLy8gYmVjYXVzZSB0aGUgZnVuY3Rpb24gZG9lcyBub3QgZXhpc3QgeWV0LgogICAgICAgIC8vIFNlZSB0aGUgbmV4dCBzZWN0aW9uIGZvciBkZXRhaWxzLgogICAgICAgIG93bmVyID0gbXNnLnNlbmRlcjsKCiAgICAgICAgLy8gV2UgcGVyZm9ybSBhbiBleHBsaWNpdCB0eXBlIGNvbnZlcnNpb24gZnJvbSBgYWRkcmVzc2AKICAgICAgICAvLyB0byBgVG9rZW5DcmVhdG9yYCBhbmQgYXNzdW1lIHRoYXQgdGhlIHR5cGUgb2YKICAgICAgICAvLyB0aGUgY2FsbGluZyBjb250cmFjdCBpcyBgVG9rZW5DcmVhdG9yYCwgdGhlcmUgaXMKICAgICAgICAvLyBubyByZWFsIHdheSB0byB2ZXJpZnkgdGhhdC4KICAgICAgICAvLyBUaGlzIGRvZXMgbm90IGNyZWF0ZSBhIG5ldyBjb250cmFjdC4KICAgICAgICBjcmVhdG9yID0gVG9rZW5DcmVhdG9yKG1zZy5zZW5kZXIpOwogICAgICAgIG5hbWUgPSBuYW1lXzsKICAgIH0KCiAgICBmdW5jdGlvbiBjaGFuZ2VOYW1lKGJ5dGVzMzIgbmV3TmFtZSkgcHVibGljIHsKICAgICAgICAvLyBPbmx5IHRoZSBjcmVhdG9yIGNhbiBhbHRlciB0aGUgbmFtZS4KICAgICAgICAvLyBXZSBjb21wYXJlIHRoZSBjb250cmFjdCBiYXNlZCBvbiBpdHMKICAgICAgICAvLyBhZGRyZXNzIHdoaWNoIGNhbiBiZSByZXRyaWV2ZWQgYnkKICAgICAgICAvLyBleHBsaWNpdCBjb252ZXJzaW9uIHRvIGFkZHJlc3MuCiAgICAgICAgaWYgKG1zZy5zZW5kZXIgPT0gYWRkcmVzcyhjcmVhdG9yKSkKICAgICAgICAgICAgbmFtZSA9IG5ld05hbWU7CiAgICB9CgogICAgZnVuY3Rpb24gdHJhbnNmZXIoYWRkcmVzcyBuZXdPd25lcikgcHVibGljIHsKICAgICAgICAvLyBPbmx5IHRoZSBjdXJyZW50IG93bmVyIGNhbiB0cmFuc2ZlciB0aGUgdG9rZW4uCiAgICAgICAgaWYgKG1zZy5zZW5kZXIgIT0gb3duZXIpIHJldHVybjsKCiAgICAgICAgLy8gV2UgYXNrIHRoZSBjcmVhdG9yIGNvbnRyYWN0IGlmIHRoZSB0cmFuc2ZlcgogICAgICAgIC8vIHNob3VsZCBwcm9jZWVkIGJ5IHVzaW5nIGEgZnVuY3Rpb24gb2YgdGhlCiAgICAgICAgLy8gYFRva2VuQ3JlYXRvcmAgY29udHJhY3QgZGVmaW5lZCBiZWxvdy4gSWYKICAgICAgICAvLyB0aGUgY2FsbCBmYWlscyAoZS5nLiBkdWUgdG8gb3V0LW9mLWdhcyksCiAgICAgICAgLy8gdGhlIGV4ZWN1dGlvbiBhbHNvIGZhaWxzIGhlcmUuCiAgICAgICAgaWYgKGNyZWF0b3IuaXNUb2tlblRyYW5zZmVyT0sob3duZXIsIG5ld093bmVyKSkKICAgICAgICAgICAgb3duZXIgPSBuZXdPd25lcjsKICAgIH0KfQoKCmNvbnRyYWN0IFRva2VuQ3JlYXRvciB7CiAgICBmdW5jdGlvbiBjcmVhdGVUb2tlbihieXRlczMyIG5hbWUpCiAgICAgICAgcHVibGljCiAgICAgICAgcmV0dXJucyAoT3duZWRUb2tlbiB0b2tlbkFkZHJlc3MpCiAgICB7CiAgICAgICAgLy8gQ3JlYXRlIGEgbmV3IGBUb2tlbmAgY29udHJhY3QgYW5kIHJldHVybiBpdHMgYWRkcmVzcy4KICAgICAgICAvLyBGcm9tIHRoZSBKYXZhU2NyaXB0IHNpZGUsIHRoZSByZXR1cm4gdHlwZQogICAgICAgIC8vIG9mIHRoaXMgZnVuY3Rpb24gaXMgYGFkZHJlc3NgLCBhcyB0aGlzIGlzCiAgICAgICAgLy8gdGhlIGNsb3Nlc3QgdHlwZSBhdmFpbGFibGUgaW4gdGhlIEFCSS4KICAgICAgICByZXR1cm4gbmV3IE93bmVkVG9rZW4obmFtZSk7CiAgICB9CgogICAgZnVuY3Rpb24gY2hhbmdlTmFtZShPd25lZFRva2VuIHRva2VuQWRkcmVzcywgYnl0ZXMzMiBuYW1lKSBwdWJsaWMgewogICAgICAgIC8vIEFnYWluLCB0aGUgZXh0ZXJuYWwgdHlwZSBvZiBgdG9rZW5BZGRyZXNzYCBpcwogICAgICAgIC8vIHNpbXBseSBgYWRkcmVzc2AuCiAgICAgICAgdG9rZW5BZGRyZXNzLmNoYW5nZU5hbWUobmFtZSk7CiAgICB9CgogICAgLy8gUGVyZm9ybSBjaGVja3MgdG8gZGV0ZXJtaW5lIGlmIHRyYW5zZmVycmluZyBhIHRva2VuIHRvIHRoZQogICAgLy8gYE93bmVkVG9rZW5gIGNvbnRyYWN0IHNob3VsZCBwcm9jZWVkCiAgICBmdW5jdGlvbiBpc1Rva2VuVHJhbnNmZXJPSyhhZGRyZXNzIGN1cnJlbnRPd25lciwgYWRkcmVzcyBuZXdPd25lcikKICAgICAgICBwdWJsaWMKICAgICAgICBwdXJlCiAgICAgICAgcmV0dXJucyAoYm9vbCBvaykKICAgIHsKICAgICAgICAvLyBDaGVjayBhbiBhcmJpdHJhcnkgY29uZGl0aW9uIHRvIHNlZSBpZiB0cmFuc2ZlciBzaG91bGQgcHJvY2VlZAogICAgICAgIHJldHVybiBrZWNjYWsyNTYoYWJpLmVuY29kZVBhY2tlZChjdXJyZW50T3duZXIsIG5ld093bmVyKSlbMF0gPT0gMHg3ZjsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.9.0;

contract OwnedToken {
 // `TokenCreator` is a contract type that is defined below.
 // It is fine to reference it as long as it is not used
 // to create a new contract.
 TokenCreator creator;
 address owner;
 bytes32 name;

 // This is the constructor which registers the
 // creator and the assigned name.
 constructor(bytes32 name_) {
 // State variables are accessed via their name
 // and not via e.g. `this.owner`. Functions can
 // be accessed directly or through `this.f`,
 // but the latter provides an external view
 // to the function. Especially in the constructor,
 // you should not access functions externally,
 // because the function does not exist yet.
 // See the next section for details.
 owner = msg.sender;

 // We perform an explicit type conversion from `address`
 // to `TokenCreator` and assume that the type of
 // the calling contract is `TokenCreator`, there is
 // no real way to verify that.
 // This does not create a new contract.
 creator = TokenCreator(msg.sender);
 name = name_;
 }

 function changeName(bytes32 newName) public {
 // Only the creator can alter the name.
 // We compare the contract based on its
 // address which can be retrieved by
 // explicit conversion to address.
 if (msg.sender == address(creator))
 name = newName;
 }

 function transfer(address newOwner) public {
 // Only the current owner can transfer the token.
 if (msg.sender != owner) return;

 // We ask the creator contract if the transfer
 // should proceed by using a function of the
 // `TokenCreator` contract defined below. If
 // the call fails (e.g. due to out-of-gas),
 // the execution also fails here.
 if (creator.isTokenTransferOK(owner, newOwner))
 owner = newOwner;
 }
}

contract TokenCreator {
 function createToken(bytes32 name)
 public
 returns (OwnedToken tokenAddress)
 {
 // Create a new `Token` contract and return its address.
 // From the JavaScript side, the return type
 // of this function is `address`, as this is
 // the closest type available in the ABI.
 return new OwnedToken(name);
 }

 function changeName(OwnedToken tokenAddress, bytes32 name) public {
 // Again, the external type of `tokenAddress` is
 // simply `address`.
 tokenAddress.changeName(name);
 }

 // Perform checks to determine if transferring a token to the
 // `OwnedToken` contract should proceed
 function isTokenTransferOK(address currentOwner, address newOwner)
 public
 pure
 returns (bool ok)
 {
 // Check an arbitrary condition to see if transfer should proceed
 return keccak256(abi.encodePacked(currentOwner, newOwner))[0] == 0x7f;
 }
}

Visibility and Getters[](https://docs.soliditylang.org/en/latest/contracts.html#visibility-and-getters "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

### State Variable Visibility[](https://docs.soliditylang.org/en/latest/contracts.html#state-variable-visibility "Link to this heading")

`public`
Public state variables differ from internal ones only in that the compiler automatically generates [getter functions](https://docs.soliditylang.org/en/latest/contracts.html#getter-functions) for them, which allows other contracts to read their values. When used within the same contract, the external access (e.g. `this.x`) invokes the getter while internal access (e.g. `x`) gets the variable value directly from storage. Setter functions are not generated so other contracts cannot directly modify their values.

`internal`
Internal state variables can only be accessed from within the contract they are defined in and in derived contracts. They cannot be accessed externally. This is the default visibility level for state variables.

`private`
Private state variables are like internal ones but they are not visible in derived contracts.

Warning

Making something `private` or `internal` only prevents other contracts from reading or modifying the information, but it will still be visible to the whole world outside of the blockchain.

### Function Visibility[](https://docs.soliditylang.org/en/latest/contracts.html#function-visibility "Link to this heading")

Solidity knows two kinds of function calls: external ones that do create an actual EVM message call and internal ones that do not. Furthermore, internal functions can be made inaccessible to derived contracts. This gives rise to four types of visibility for functions.

`external`
External functions are part of the contract interface, which means they can be called from other contracts and via transactions. An external function `f` cannot be called internally (i.e. `f()` does not work, but `this.f()` works).

`public`
Public functions are part of the contract interface and can be either called internally or via message calls.

`internal`
Internal functions can only be accessed from within the current contract or contracts deriving from it. They cannot be accessed externally. Since they are not exposed to the outside through the contract’s ABI, they can take parameters of internal types like mappings or storage references.

`private`
Private functions are like internal ones but they are not visible in derived contracts.

Warning

Making something `private` or `internal` only prevents other contracts from reading or modifying the information, but it will still be visible to the whole world outside of the blockchain.

The visibility specifier is given after the type for state variables and between parameter list and return parameter list for functions.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCmNvbnRyYWN0IEMgewogICAgZnVuY3Rpb24gZih1aW50IGEpIHByaXZhdGUgcHVyZSByZXR1cm5zICh1aW50IGIpIHsgcmV0dXJuIGEgKyAxOyB9CiAgICBmdW5jdGlvbiBzZXREYXRhKHVpbnQgYSkgaW50ZXJuYWwgeyBkYXRhID0gYTsgfQogICAgdWludCBwdWJsaWMgZGF0YTsKfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract C {
 function f(uint a) private pure returns (uint b) { return a + 1; }
 function setData(uint a) internal { data = a; }
 uint public data;
}

In the following example, `D`, can call `c.getData()` to retrieve the value of `data` in state storage, but is not able to call `f`. Contract `E` is derived from `C` and, thus, can call `compute`.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCmNvbnRyYWN0IEMgewogICAgdWludCBwcml2YXRlIGRhdGE7CgogICAgZnVuY3Rpb24gZih1aW50IGEpIHByaXZhdGUgcHVyZSByZXR1cm5zKHVpbnQgYikgeyByZXR1cm4gYSArIDE7IH0KICAgIGZ1bmN0aW9uIHNldERhdGEodWludCBhKSBwdWJsaWMgeyBkYXRhID0gYTsgfQogICAgZnVuY3Rpb24gZ2V0RGF0YSgpIHB1YmxpYyB2aWV3IHJldHVybnModWludCkgeyByZXR1cm4gZGF0YTsgfQogICAgZnVuY3Rpb24gY29tcHV0ZSh1aW50IGEsIHVpbnQgYikgaW50ZXJuYWwgcHVyZSByZXR1cm5zICh1aW50KSB7IHJldHVybiBhICsgYjsgfQp9CgovLyBUaGlzIHdpbGwgbm90IGNvbXBpbGUKY29udHJhY3QgRCB7CiAgICBmdW5jdGlvbiByZWFkRGF0YSgpIHB1YmxpYyB7CiAgICAgICAgQyBjID0gbmV3IEMoKTsKICAgICAgICB1aW50IGxvY2FsID0gYy5mKDcpOyAvLyBlcnJvcjogbWVtYmVyIGBmYCBpcyBub3QgdmlzaWJsZQogICAgICAgIGMuc2V0RGF0YSgzKTsKICAgICAgICBsb2NhbCA9IGMuZ2V0RGF0YSgpOwogICAgICAgIGxvY2FsID0gYy5jb21wdXRlKDMsIDUpOyAvLyBlcnJvcjogbWVtYmVyIGBjb21wdXRlYCBpcyBub3QgdmlzaWJsZQogICAgfQp9Cgpjb250cmFjdCBFIGlzIEMgewogICAgZnVuY3Rpb24gZygpIHB1YmxpYyB7CiAgICAgICAgQyBjID0gbmV3IEMoKTsKICAgICAgICB1aW50IHZhbCA9IGNvbXB1dGUoMywgNSk7IC8vIGFjY2VzcyB0byBpbnRlcm5hbCBtZW1iZXIgKGZyb20gZGVyaXZlZCB0byBwYXJlbnQgY29udHJhY3QpCiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract C {
 uint private data;

 function f(uint a) private pure returns(uint b) { return a + 1; }
 function setData(uint a) public { data = a; }
 function getData() public view returns(uint) { return data; }
 function compute(uint a, uint b) internal pure returns (uint) { return a + b; }
}

// This will not compile
contract D {
 function readData() public {
 C c = new C();
 uint local = c.f(7); // error: member `f` is not visible
 c.setData(3);
 local = c.getData();
 local = c.compute(3, 5); // error: member `compute` is not visible
 }
}

contract E is C {
 function g() public {
 C c = new C();
 uint val = compute(3, 5); // access to internal member (from derived to parent contract)
 }
}

### Getter Functions[](https://docs.soliditylang.org/en/latest/contracts.html#getter-functions "Link to this heading")

The compiler automatically creates getter functions for all **public** state variables. For the contract given below, the compiler will generate a function called `data` that does not take any arguments and returns a `uint`, the value of the state variable `data`. State variables can be initialized when they are declared.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCmNvbnRyYWN0IEMgewogICAgdWludCBwdWJsaWMgZGF0YSA9IDQyOwp9Cgpjb250cmFjdCBDYWxsZXIgewogICAgQyBjID0gbmV3IEMoKTsKICAgIGZ1bmN0aW9uIGYoKSBwdWJsaWMgdmlldyByZXR1cm5zICh1aW50KSB7CiAgICAgICAgcmV0dXJuIGMuZGF0YSgpOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract C {
 uint public data = 42;
}

contract Caller {
 C c = new C();
 function f() public view returns (uint) {
 return c.data();
 }
}

The getter functions have external visibility. If the symbol is accessed internally (i.e. without `this.`), it evaluates to a state variable. If it is accessed externally (i.e. with `this.`), it evaluates to a function.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjAgPDAuOS4wOwoKY29udHJhY3QgQyB7CiAgICB1aW50IHB1YmxpYyBkYXRhOwogICAgZnVuY3Rpb24geCgpIHB1YmxpYyByZXR1cm5zICh1aW50KSB7CiAgICAgICAgZGF0YSA9IDM7IC8vIGludGVybmFsIGFjY2VzcwogICAgICAgIHJldHVybiB0aGlzLmRhdGEoKTsgLy8gZXh0ZXJuYWwgYWNjZXNzCiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.0 <0.9.0;

contract C {
 uint public data;
 function x() public returns (uint) {
 data = 3; // internal access
 return this.data(); // external access
 }
}

If you have a `public` state variable of array type, then you can only retrieve single elements of the array via the generated getter function. This mechanism exists to avoid high gas costs when returning an entire array. You can use arguments to specify which individual element to return, for example `myArray(0)`. If you want to return an entire array in one call, then you need to write a function, for example:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCmNvbnRyYWN0IGFycmF5RXhhbXBsZSB7CiAgICAvLyBwdWJsaWMgc3RhdGUgdmFyaWFibGUKICAgIHVpbnRbXSBwdWJsaWMgbXlBcnJheTsKCiAgICAvLyBHZXR0ZXIgZnVuY3Rpb24gZ2VuZXJhdGVkIGJ5IHRoZSBjb21waWxlcgogICAgLyoKICAgIGZ1bmN0aW9uIG15QXJyYXkodWludCBpKSBwdWJsaWMgdmlldyByZXR1cm5zICh1aW50KSB7CiAgICAgICAgcmV0dXJuIG15QXJyYXlbaV07CiAgICB9CiAgICAqLwoKICAgIC8vIGZ1bmN0aW9uIHRoYXQgcmV0dXJucyBlbnRpcmUgYXJyYXkKICAgIGZ1bmN0aW9uIGdldEFycmF5KCkgcHVibGljIHZpZXcgcmV0dXJucyAodWludFtdIG1lbW9yeSkgewogICAgICAgIHJldHVybiBteUFycmF5OwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract arrayExample {
 // public state variable
 uint[] public myArray;

 // Getter function generated by the compiler
 /*
 function myArray(uint i) public view returns (uint) {
 return myArray[i];
 }
 */

 // function that returns entire array
 function getArray() public view returns (uint[] memory) {
 return myArray;
 }
}

Now you can use `getArray()` to retrieve the entire array, instead of `myArray(i)`, which returns a single element per call.

The next example is more complex:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjAgPDAuOS4wOwoKY29udHJhY3QgQ29tcGxleCB7CiAgICBzdHJ1Y3QgRGF0YSB7CiAgICAgICAgdWludCBhOwogICAgICAgIGJ5dGVzMyBiOwogICAgICAgIG1hcHBpbmcodWludCA9PiB1aW50KSBtYXA7CiAgICAgICAgdWludFszXSBjOwogICAgICAgIHVpbnRbXSBkOwogICAgICAgIGJ5dGVzIGU7CiAgICB9CiAgICBtYXBwaW5nKHVpbnQgPT4gbWFwcGluZyhib29sID0+IERhdGFbXSkpIHB1YmxpYyBkYXRhOwp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.0 <0.9.0;

contract Complex {
 struct Data {
 uint a;
 bytes3 b;
 mapping(uint => uint) map;
 uint[3] c;
 uint[] d;
 bytes e;
 }
 mapping(uint => mapping(bool => Data[])) public data;
}

It generates a function of the following form. The mapping and arrays (with the exception of byte arrays) in the struct are omitted because there is no good way to select individual struct members or provide a key for the mapping:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=ZnVuY3Rpb24gZGF0YSh1aW50IGFyZzEsIGJvb2wgYXJnMiwgdWludCBhcmczKQogICAgcHVibGljCiAgICByZXR1cm5zICh1aW50IGEsIGJ5dGVzMyBiLCBieXRlcyBtZW1vcnkgZSkKewogICAgYSA9IGRhdGFbYXJnMV1bYXJnMl1bYXJnM10uYTsKICAgIGIgPSBkYXRhW2FyZzFdW2FyZzJdW2FyZzNdLmI7CiAgICBlID0gZGF0YVthcmcxXVthcmcyXVthcmczXS5lOwp9)

function data(uint arg1, bool arg2, uint arg3)
 public
 returns (uint a, bytes3 b, bytes memory e)
{
 a = data[arg1][arg2][arg3].a;
 b = data[arg1][arg2][arg3].b;
 e = data[arg1][arg2][arg3].e;
}

Function Modifiers[](https://docs.soliditylang.org/en/latest/contracts.html#function-modifiers "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Modifiers can be used to change the behavior of functions in a declarative way. For example, you can use a modifier to automatically check a condition prior to executing the function.

Modifiers are inheritable properties of contracts and may be overridden by derived contracts, but only if they are marked `virtual`. For details, please see [Modifier Overriding](https://docs.soliditylang.org/en/latest/contracts.html#modifier-overriding).

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjEgPDAuOS4wOwoKY29udHJhY3Qgb3duZWQgewogICAgY29uc3RydWN0b3IoKSB7IG93bmVyID0gcGF5YWJsZShtc2cuc2VuZGVyKTsgfQogICAgYWRkcmVzcyBwYXlhYmxlIG93bmVyOwoKICAgIC8vIFRoaXMgY29udHJhY3Qgb25seSBkZWZpbmVzIGEgbW9kaWZpZXIgYnV0IGRvZXMgbm90IHVzZQogICAgLy8gaXQ6IGl0IHdpbGwgYmUgdXNlZCBpbiBkZXJpdmVkIGNvbnRyYWN0cy4KICAgIC8vIFRoZSBmdW5jdGlvbiBib2R5IGlzIGluc2VydGVkIHdoZXJlIHRoZSBzcGVjaWFsIHN5bWJvbAogICAgLy8gYF87YCBpbiB0aGUgZGVmaW5pdGlvbiBvZiBhIG1vZGlmaWVyIGFwcGVhcnMuCiAgICAvLyBUaGlzIG1lYW5zIHRoYXQgaWYgdGhlIG93bmVyIGNhbGxzIHRoaXMgZnVuY3Rpb24sIHRoZQogICAgLy8gZnVuY3Rpb24gaXMgZXhlY3V0ZWQgYW5kIG90aGVyd2lzZSwgYW4gZXhjZXB0aW9uIGlzCiAgICAvLyB0aHJvd24uCiAgICBtb2RpZmllciBvbmx5T3duZXIgewogICAgICAgIHJlcXVpcmUoCiAgICAgICAgICAgIG1zZy5zZW5kZXIgPT0gb3duZXIsCiAgICAgICAgICAgICJPbmx5IG93bmVyIGNhbiBjYWxsIHRoaXMgZnVuY3Rpb24uIgogICAgICAgICk7CiAgICAgICAgXzsKICAgIH0KfQoKY29udHJhY3QgcHJpY2VkIHsKICAgIC8vIE1vZGlmaWVycyBjYW4gcmVjZWl2ZSBhcmd1bWVudHM6CiAgICBtb2RpZmllciBjb3N0cyh1aW50IHByaWNlKSB7CiAgICAgICAgaWYgKG1zZy52YWx1ZSA+PSBwcmljZSkgewogICAgICAgICAgICBfOwogICAgICAgIH0KICAgIH0KfQoKY29udHJhY3QgUmVnaXN0ZXIgaXMgcHJpY2VkLCBvd25lZCB7CiAgICBtYXBwaW5nKGFkZHJlc3MgPT4gYm9vbCkgcmVnaXN0ZXJlZEFkZHJlc3NlczsKICAgIHVpbnQgcHJpY2U7CgogICAgY29uc3RydWN0b3IodWludCBpbml0aWFsUHJpY2UpIHsgcHJpY2UgPSBpbml0aWFsUHJpY2U7IH0KCiAgICAvLyBJdCBpcyBpbXBvcnRhbnQgdG8gYWxzbyBwcm92aWRlIHRoZQogICAgLy8gYHBheWFibGVgIGtleXdvcmQgaGVyZSwgb3RoZXJ3aXNlIHRoZSBmdW5jdGlvbiB3aWxsCiAgICAvLyBhdXRvbWF0aWNhbGx5IHJlamVjdCBhbGwgRXRoZXIgc2VudCB0byBpdC4KICAgIGZ1bmN0aW9uIHJlZ2lzdGVyKCkgcHVibGljIHBheWFibGUgY29zdHMocHJpY2UpIHsKICAgICAgICByZWdpc3RlcmVkQWRkcmVzc2VzW21zZy5zZW5kZXJdID0gdHJ1ZTsKICAgIH0KCiAgICAvLyBUaGlzIGNvbnRyYWN0IGluaGVyaXRzIHRoZSBgb25seU93bmVyYCBtb2RpZmllciBmcm9tCiAgICAvLyB0aGUgYG93bmVkYCBjb250cmFjdC4gQXMgYSByZXN1bHQsIGNhbGxzIHRvIGBjaGFuZ2VQcmljZWAgd2lsbAogICAgLy8gb25seSB0YWtlIGVmZmVjdCBpZiB0aGV5IGFyZSBtYWRlIGJ5IHRoZSBzdG9yZWQgb3duZXIuCiAgICBmdW5jdGlvbiBjaGFuZ2VQcmljZSh1aW50IHByaWNlXykgcHVibGljIG9ubHlPd25lciB7CiAgICAgICAgcHJpY2UgPSBwcmljZV87CiAgICB9Cn0KCmNvbnRyYWN0IE11dGV4IHsKICAgIGJvb2wgbG9ja2VkOwogICAgbW9kaWZpZXIgbm9SZWVudHJhbmN5KCkgewogICAgICAgIHJlcXVpcmUoCiAgICAgICAgICAgICFsb2NrZWQsCiAgICAgICAgICAgICJSZWVudHJhbnQgY2FsbC4iCiAgICAgICAgKTsKICAgICAgICBsb2NrZWQgPSB0cnVlOwogICAgICAgIF87CiAgICAgICAgbG9ja2VkID0gZmFsc2U7CiAgICB9CgogICAgLy8vIFRoaXMgZnVuY3Rpb24gaXMgcHJvdGVjdGVkIGJ5IGEgbXV0ZXgsIHdoaWNoIG1lYW5zIHRoYXQKICAgIC8vLyByZWVudHJhbnQgY2FsbHMgZnJvbSB3aXRoaW4gYG1zZy5zZW5kZXIuY2FsbGAgY2Fubm90IGNhbGwgYGZgIGFnYWluLgogICAgLy8vIFRoZSBgcmV0dXJuIDdgIHN0YXRlbWVudCBhc3NpZ25zIDcgdG8gdGhlIHJldHVybiB2YWx1ZSBidXQgc3RpbGwKICAgIC8vLyBleGVjdXRlcyB0aGUgc3RhdGVtZW50IGBsb2NrZWQgPSBmYWxzZWAgaW4gdGhlIG1vZGlmaWVyLgogICAgZnVuY3Rpb24gZigpIHB1YmxpYyBub1JlZW50cmFuY3kgcmV0dXJucyAodWludCkgewogICAgICAgIChib29sIHN1Y2Nlc3MsKSA9IG1zZy5zZW5kZXIuY2FsbCgiIik7CiAgICAgICAgcmVxdWlyZShzdWNjZXNzKTsKICAgICAgICByZXR1cm4gNzsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.1 <0.9.0;

contract owned {
 constructor() { owner = payable(msg.sender); }
 address payable owner;

 // This contract only defines a modifier but does not use
 // it: it will be used in derived contracts.
 // The function body is inserted where the special symbol
 // `_;` in the definition of a modifier appears.
 // This means that if the owner calls this function, the
 // function is executed and otherwise, an exception is
 // thrown.
 modifier onlyOwner {
 require(
 msg.sender == owner,
 "Only owner can call this function."
 );
 _;
 }
}

contract priced {
 // Modifiers can receive arguments:
 modifier costs(uint price) {
 if (msg.value >= price) {
 _;
 }
 }
}

contract Register is priced, owned {
 mapping(address => bool) registeredAddresses;
 uint price;

 constructor(uint initialPrice) { price = initialPrice; }

 // It is important to also provide the
 // `payable` keyword here, otherwise the function will
 // automatically reject all Ether sent to it.
 function register() public payable costs(price) {
 registeredAddresses[msg.sender] = true;
 }

 // This contract inherits the `onlyOwner` modifier from
 // the `owned` contract. As a result, calls to `changePrice` will
 // only take effect if they are made by the stored owner.
 function changePrice(uint price_) public onlyOwner {
 price = price_;
 }
}

contract Mutex {
 bool locked;
 modifier noReentrancy() {
 require(
 !locked,
 "Reentrant call."
 );
 locked = true;
 _;
 locked = false;
 }

 /// This function is protected by a mutex, which means that
 /// reentrant calls from within `msg.sender.call` cannot call `f` again.
 /// The `return 7` statement assigns 7 to the return value but still
 /// executes the statement `locked = false` in the modifier.
 function f() public noReentrancy returns (uint) {
 (bool success,) = msg.sender.call("");
 require(success);
 return 7;
 }
}

If you want to access a modifier `m` defined in a contract `C`, you can use `C.m` to reference it without virtual lookup. It is only possible to use modifiers defined in the current contract or its base contracts. Modifiers can also be defined in libraries but their use is limited to functions of the same library.

Multiple modifiers are applied to a function by specifying them in a whitespace-separated list and are evaluated in the order presented.

Modifiers cannot implicitly access or change the arguments and return values of functions they modify. Their values can only be passed to them explicitly at the point of invocation.

In function modifiers, it is necessary to specify when you want the function to which the modifier is applied to be run. The placeholder statement (denoted by a single underscore character `_`) is used to denote where the body of the function being modified should be inserted. Note that the placeholder operator is different from using underscores as leading or trailing characters in variable names, which is a stylistic choice.

Explicit returns from a modifier or function body only leave the current modifier or function body. Return variables are assigned and control flow continues after the `_` in the preceding modifier.

Warning

In an earlier version of Solidity, `return` statements in functions having modifiers behaved differently.

An explicit return from a modifier with `return;` does not affect the values returned by the function. The modifier can, however, choose not to execute the function body at all and in that case the return variables are set to their [default values](https://docs.soliditylang.org/en/latest/control-structures.html#default-value) just as if the function had an empty body.

The `_` symbol can appear in the modifier multiple times. Each occurrence is replaced with the function body, and the function returns the return value of the final occurrence.

Arbitrary expressions are allowed for modifier arguments and in this context, all symbols visible from the function are visible in the modifier. Symbols introduced in the modifier are not visible in the function (as they might change by overriding).

Transient Storage[](https://docs.soliditylang.org/en/latest/contracts.html#transient-storage "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

Transient storage is another data location besides memory, storage, calldata (and return-data and code) which was introduced alongside its respective opcodes `TSTORE` and `TLOAD` by [EIP-1153](https://eips.ethereum.org/EIPS/eip-1153). This new data location behaves as a key-value store similar to storage with the main difference being that data in transient storage is not permanent, but is scoped to the current transaction only, after which it will be reset to zero. Since the content of transient storage has very limited lifetime and size, it does not need to be stored permanently as a part of state and the associated gas costs are much lower than in case of storage. EVM version `cancun` or newer is required for transient storage to be available.

Transient storage variables cannot be initialized in place, i.e., they cannot be assigned to upon declaration, since the value would be cleared at the end of the creation transaction, rendering the initialization ineffective. Transient variables will be [default value](https://docs.soliditylang.org/en/latest/control-structures.html#default-value) initialized depending on their underlying type. `constant` and `immutable` variables conflict with transient storage, since their values are either inlined or directly stored in code.

Transient storage variables have completely independent address space from storage, so that the order of transient state variables does not affect the layout of storage state variables and vice-versa. They do need distinct names though because all state variables share the same namespace. It is also important to note that the values in transient storage are packed in the same fashion as those in persistent storage. See [Storage Layout](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html#storage-inplace-encoding) for more information.

Besides that, transient variables can have visibility as well and `public` ones will have a getter function generated automatically as usual.

Note that, currently, such use of `transient` as a data location is only allowed for [value type](https://docs.soliditylang.org/en/latest/types.html#value-types) state variable declarations. Reference types, such as arrays, mappings and structs, as well as local or parameter variables are not yet supported.

An expected canonical use case for transient storage is cheaper reentrancy locks, which can be readily implemented with the opcodes as showcased next.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguMjg7Cgpjb250cmFjdCBHZW5lcm9zaXR5IHsKICAgIG1hcHBpbmcoYWRkcmVzcyA9PiBib29sKSBzZW50R2lmdHM7CiAgICBib29sIHRyYW5zaWVudCBsb2NrZWQ7CgogICAgbW9kaWZpZXIgbm9uUmVlbnRyYW50IHsKICAgICAgICByZXF1aXJlKCFsb2NrZWQsICJSZWVudHJhbmN5IGF0dGVtcHQiKTsKICAgICAgICBsb2NrZWQgPSB0cnVlOwogICAgICAgIF87CiAgICAgICAgLy8gVW5sb2NrcyB0aGUgZ3VhcmQsIG1ha2luZyB0aGUgcGF0dGVybiBjb21wb3NhYmxlLgogICAgICAgIC8vIEFmdGVyIHRoZSBmdW5jdGlvbiBleGl0cywgaXQgY2FuIGJlIGNhbGxlZCBhZ2FpbiwgZXZlbiBpbiB0aGUgc2FtZSB0cmFuc2FjdGlvbi4KICAgICAgICBsb2NrZWQgPSBmYWxzZTsKICAgIH0KCiAgICBmdW5jdGlvbiBjbGFpbUdpZnQoKSBub25SZWVudHJhbnQgcHVibGljIHsKICAgICAgICByZXF1aXJlKGFkZHJlc3ModGhpcykuYmFsYW5jZSA+PSAxIGV0aGVyKTsKICAgICAgICByZXF1aXJlKCFzZW50R2lmdHNbbXNnLnNlbmRlcl0pOwogICAgICAgIChib29sIHN1Y2Nlc3MsICkgPSBtc2cuc2VuZGVyLmNhbGx7dmFsdWU6IDEgZXRoZXJ9KCIiKTsKICAgICAgICByZXF1aXJlKHN1Y2Nlc3MpOwoKICAgICAgICAvLyBJbiBhIHJlZW50cmFudCBmdW5jdGlvbiwgZG9pbmcgdGhpcyBsYXN0IHdvdWxkIG9wZW4gdXAgdGhlIHZ1bG5lcmFiaWxpdHkKICAgICAgICBzZW50R2lmdHNbbXNnLnNlbmRlcl0gPSB0cnVlOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.28;

contract Generosity {
 mapping(address => bool) sentGifts;
 bool transient locked;

 modifier nonReentrant {
 require(!locked, "Reentrancy attempt");
 locked = true;
 _;
 // Unlocks the guard, making the pattern composable.
 // After the function exits, it can be called again, even in the same transaction.
 locked = false;
 }

 function claimGift() nonReentrant public {
 require(address(this).balance >= 1 ether);
 require(!sentGifts[msg.sender]);
 (bool success, ) = msg.sender.call{value: 1 ether}("");
 require(success);

 // In a reentrant function, doing this last would open up the vulnerability
 sentGifts[msg.sender] = true;
 }
}

Transient storage is private to the contract that owns it, in the same way as persistent storage. Only owning contract frames may access their transient storage, and when they do, all the frames access the same transient store.

Transient storage is part of the EVM state and is subject to the same mutability enforcements as persistent storage. As such, any read access to it is not `pure` and writing access is not `view`.

If the `TSTORE` opcode is called within the context of a `STATICCALL`, it will result in an exception instead of performing the modification. `TLOAD` is allowed within the context of a `STATICCALL`.

When transient storage is used in the context of `DELEGATECALL` or `CALLCODE`, then the owning contract of the transient storage is the contract that issued `DELEGATECALL` or `CALLCODE` instruction (the caller) as with persistent storage. When transient storage is used in the context of `CALL` or `STATICCALL`, then the owning contract of the transient storage is the contract that is the target of the `CALL` or `STATICCALL` instruction (the callee).

Note

In the case of `DELEGATECALL`, since references to transient storage variables are currently not supported, it is not possible to pass those into library calls. In libraries, access to transient storage is only possible using inline assembly.

If a frame reverts, all writes to transient storage that took place between entry to the frame and the return are reverted, including those that took place in inner calls. The caller of an external call may employ a `try ... catch` block to prevent reverts bubbling up from the inner calls.

Composability of Smart Contracts and the Caveats of Transient Storage[](https://docs.soliditylang.org/en/latest/contracts.html#composability-of-smart-contracts-and-the-caveats-of-transient-storage "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Given the caveats mentioned in the specification of EIP-1153, in order to preserve the composability of your smart contract, utmost care is recommended for more advanced use cases of transient storage.

For smart contracts, composability is a very important design principle to achieve self-contained behaviour, such that multiple calls into individual smart contracts can be composed to more complex applications. So far the EVM largely guaranteed composable behaviour, since multiple calls into a smart contract within a complex transaction are virtually indistinguishable from multiple calls to the contract stretched over several transactions. However, transient storage allows a violation of this principle, and incorrect use may lead to complex bugs that only surface when used across several calls.

Let’s illustrate the problem with a simple example:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguMjg7Cgpjb250cmFjdCBNdWxTZXJ2aWNlIHsKICAgIHVpbnQgdHJhbnNpZW50IG11bHRpcGxpZXI7CiAgICBmdW5jdGlvbiBzZXRNdWx0aXBsaWVyKHVpbnQgbXVsKSBleHRlcm5hbCB7CiAgICAgICAgbXVsdGlwbGllciA9IG11bDsKICAgIH0KCiAgICBmdW5jdGlvbiBtdWx0aXBseSh1aW50IHZhbHVlKSBleHRlcm5hbCB2aWV3IHJldHVybnMgKHVpbnQpIHsKICAgICAgICByZXR1cm4gdmFsdWUgKiBtdWx0aXBsaWVyOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.28;

contract MulService {
 uint transient multiplier;
 function setMultiplier(uint mul) external {
 multiplier = mul;
 }

 function multiply(uint value) external view returns (uint) {
 return value * multiplier;
 }
}

and a sequence of external calls:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=c2V0TXVsdGlwbGllcig0Mik7Cm11bHRpcGx5KDEpOwptdWx0aXBseSgyKTs=)

setMultiplier(42);
multiply(1);
multiply(2);

If the example used memory or storage to store the multiplier, it would be fully composable. It would not matter whether you split the sequence into separate transactions or grouped them in some way. You would always get the same result: after `multiplier` is set to `42`, the subsequent calls would return `42` and `84` respectively. This enables use cases such as batching calls from multiple transactions together to reduce gas costs. Transient storage potentially breaks such use cases since composability can no longer be taken for granted. In the example, if the calls are not executed in the same transaction, then `multiplier` is reset and the next calls to function `multiply` would always return `0`.

As another example, since transient storage is constructed as a relatively cheap key-value store, a smart contract author may be tempted to use transient storage as a replacement for in-memory mappings without keeping track of the modified keys in the mapping and thereby without clearing the mapping at the end of the call. This, however, can easily lead to unexpected behaviour in complex transactions, in which values set by a previous call into the contract within the same transaction remain.

The use of transient storage for reentrancy locks that are cleared at the end of the call frame into the contract, is safe. However, be sure to resist the temptation to save the 100 gas used for resetting the reentrancy lock, since failing to do so, will restrict your contract to only one call within a transaction, preventing its use in complex composed transactions, which have been a cornerstone for complex applications on chain.

It is recommend to generally always clear transient storage completely at the end of a call into your smart contract to avoid these kinds of issues and to simplify the analysis of the behaviour of your contract within complex transactions. Check the [Security Considerations section of EIP-1153](https://eips.ethereum.org/EIPS/eip-1153#security-considerations) for further details.

Constant and Immutable State Variables[](https://docs.soliditylang.org/en/latest/contracts.html#constant-and-immutable-state-variables "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------

State variables can be declared as `constant` or `immutable`. In both cases, the variables cannot be modified after the contract has been constructed. For `constant` variables, the value has to be fixed at compile-time, while for `immutable`, it can still be assigned at construction time.

It is also possible to define `constant` variables at the file level.

Every occurrence of such a variable in the source is replaced by its underlying value and the compiler does not reserve a storage slot for it. It cannot be assigned a slot in transient storage using the `transient` keyword either.

Compared to regular state variables, the gas costs of constant and immutable variables are much lower. For a constant variable, the expression assigned to it is copied to all the places where it is accessed and also re-evaluated each time. This allows for local optimizations. Immutable variables are evaluated once at construction time and their value is copied to all the places in the code where they are accessed. For these values, 32 bytes are reserved, even if they would fit in fewer bytes. Due to this, constant values can sometimes be cheaper than immutable values.

Not all types for constants and immutables are implemented at this time. The only supported types are [strings](https://docs.soliditylang.org/en/latest/types.html#strings) (only for constants) and [value types](https://docs.soliditylang.org/en/latest/types.html#value-types).

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguMjE7Cgp1aW50IGNvbnN0YW50IFggPSAzMioqMjIgKyA4OwoKY29udHJhY3QgQyB7CiAgICBzdHJpbmcgY29uc3RhbnQgVEVYVCA9ICJhYmMiOwogICAgYnl0ZXMzMiBjb25zdGFudCBNWV9IQVNIID0ga2VjY2FrMjU2KCJhYmMiKTsKICAgIHVpbnQgaW1tdXRhYmxlIGRlY2ltYWxzID0gMTg7CiAgICB1aW50IGltbXV0YWJsZSBtYXhCYWxhbmNlOwogICAgYWRkcmVzcyBpbW11dGFibGUgb3duZXIgPSBtc2cuc2VuZGVyOwoKICAgIGNvbnN0cnVjdG9yKHVpbnQgZGVjaW1hbHNfLCBhZGRyZXNzIHJlZikgewogICAgICAgIGlmIChkZWNpbWFsc18gIT0gMCkKICAgICAgICAgICAgLy8gSW1tdXRhYmxlcyBhcmUgb25seSBpbW11dGFibGUgd2hlbiBkZXBsb3llZC4KICAgICAgICAgICAgLy8gQXQgY29uc3RydWN0aW9uIHRpbWUgdGhleSBjYW4gYmUgYXNzaWduZWQgdG8gYW55IG51bWJlciBvZiB0aW1lcy4KICAgICAgICAgICAgZGVjaW1hbHMgPSBkZWNpbWFsc187CgogICAgICAgIC8vIEFzc2lnbm1lbnRzIHRvIGltbXV0YWJsZXMgY2FuIGV2ZW4gYWNjZXNzIHRoZSBlbnZpcm9ubWVudC4KICAgICAgICBtYXhCYWxhbmNlID0gcmVmLmJhbGFuY2U7CiAgICB9CgogICAgZnVuY3Rpb24gaXNCYWxhbmNlVG9vSGlnaChhZGRyZXNzIG90aGVyKSBwdWJsaWMgdmlldyByZXR1cm5zIChib29sKSB7CiAgICAgICAgcmV0dXJuIG90aGVyLmJhbGFuY2UgPiBtYXhCYWxhbmNlOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.21;

uint constant X = 32**22 + 8;

contract C {
 string constant TEXT = "abc";
 bytes32 constant MY_HASH = keccak256("abc");
 uint immutable decimals = 18;
 uint immutable maxBalance;
 address immutable owner = msg.sender;

 constructor(uint decimals_, address ref) {
 if (decimals_ != 0)
 // Immutables are only immutable when deployed.
 // At construction time they can be assigned to any number of times.
 decimals = decimals_;

 // Assignments to immutables can even access the environment.
 maxBalance = ref.balance;
 }

 function isBalanceTooHigh(address other) public view returns (bool) {
 return other.balance > maxBalance;
 }
}

### Constant[](https://docs.soliditylang.org/en/latest/contracts.html#constant "Link to this heading")

For `constant` variables, the value has to be a constant at compile time and it has to be assigned where the variable is declared. Any expression that accesses storage, blockchain data (e.g. `block.timestamp`, `address(this).balance` or `block.number`) or execution data (`msg.value` or `gasleft()`) or makes calls to external contracts is disallowed. Expressions that might have a side-effect on memory allocation are allowed, but those that might have a side-effect on other memory objects are not. The built-in functions `keccak256`, `sha256`, `ripemd160`, `ecrecover`, `addmod` and `mulmod` are allowed (even though, with the exception of `keccak256`, they do call external contracts).

The reason behind allowing side-effects on the memory allocator is that it should be possible to construct complex objects like e.g. lookup-tables. This feature is not yet fully usable.

### Immutable[](https://docs.soliditylang.org/en/latest/contracts.html#immutable "Link to this heading")

Variables declared as `immutable` are a bit less restricted than those declared as `constant`: Immutable variables can be assigned a value at construction time. The value can be changed at any time before deployment and then it becomes permanent.

One additional restriction is that immutables can only be assigned to inside expressions for which there is no possibility of being executed after creation. This excludes all modifier definitions and functions other than constructors.

There are no restrictions on reading immutable variables. The read is even allowed to happen before the variable is written to for the first time because variables in Solidity always have a well-defined initial value. For this reason it is also allowed to never explicitly assign a value to an immutable.

Warning

When accessing immutables at construction time, please keep the [initialization order](https://docs.soliditylang.org/en/latest/ir-breaking-changes.html#state-variable-initialization-order) in mind. Even if you provide an explicit initializer, some expressions may end up being evaluated before that initializer, especially when they are at a different level in inheritance hierarchy.

Note

Before Solidity 0.8.21 initialization of immutable variables was more restrictive. Such variables had to be initialized exactly once at construction time and could not be read before then.

The contract creation code generated by the compiler will modify the contract’s runtime code before it is returned by replacing all references to immutables with the values assigned to them. This is important if you are comparing the runtime code generated by the compiler with the one actually stored in the blockchain. The compiler outputs where these immutables are located in the deployed bytecode in the `immutableReferences` field of the [compiler JSON standard output](https://docs.soliditylang.org/en/latest/using-the-compiler.html#compiler-api).

Custom Storage Layout[](https://docs.soliditylang.org/en/latest/contracts.html#custom-storage-layout "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

A contract can define an arbitrary location for its storage using the `layout` specifier. The contract’s state variables, including those inherited from base contracts, start from the specified base slot instead of the default slot zero.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguMjk7Cgpjb250cmFjdCBDIGxheW91dCBhdCAweEFBQUEgKyAweDExIHsKICAgIHVpbnRbM10geDsgLy8gT2NjdXBpZXMgc2xvdHMgMHhBQUJCLi4weEFBQkQKfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.29;

contract C layout at 0xAAAA + 0x11 {
 uint[3] x; // Occupies slots 0xAABB..0xAABD
}

As the above example shows, the specifier uses the `layout at <base-slot-expression>` syntax and is located in the header of a contract definition.

The layout specifier can be placed either before or after the inheritance specifier, and can appear at most once. The `base-slot-expression` must be an [integer literal](https://docs.soliditylang.org/en/latest/types.html#rational-literals) expression that can be evaluated at compilation time and yields a value in the range of `uint256`.

A custom layout cannot make contract’s storage “wrap around”. If the selected base slot would push the static variables past the end of storage, the compiler will issue an error. Note that the data areas of dynamic arrays and mappings are not affected by this check because their layout is not linear. Regardless of the base slot used, their locations are calculated in a way that always puts them within the range of `uint256` and their sizes are not known at compilation time.

While there are no other limits placed on the base slot, it is recommended to avoid locations that are too close to the end of the address space. Leaving too little space may complicate contract upgrades or cause problems for contracts that store additional values past their allocated space using inline assembly.

The storage layout can only be specified for the topmost contract of an inheritance tree, and affects locations of all the storage variables in all the contracts in that tree. Variables are laid out according to the order of their definitions and the positions of their contracts in the [linearized inheritance hierarchy](https://docs.soliditylang.org/en/latest/contracts.html#multi-inheritance) and a custom base slot preserves their relative positions, shifting them all by the same amount.

The storage layout cannot be specified for abstract contracts, interfaces and libraries. Also, it is important to note that it does _not_ affect transient state variables.

For details about storage layout and the effect of the layout specifier on it see [layout of storage variables](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html#storage-inplace-encoding).

Warning

The identifiers `layout` and `at` are not yet reserved as keywords in the language. It is strongly recommended to avoid using them since they will become reserved in a future breaking release.

Functions[](https://docs.soliditylang.org/en/latest/contracts.html#functions "Link to this heading")
-----------------------------------------------------------------------------------------------------

Functions can be defined inside and outside of contracts.

Functions outside of a contract, also called “free functions”, always have implicit `internal`[visibility](https://docs.soliditylang.org/en/latest/contracts.html#visibility-and-getters). Their code is included in all contracts that call them, similar to internal library functions.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjEgPDAuOS4wOwoKZnVuY3Rpb24gc3VtKHVpbnRbXSBtZW1vcnkgYXJyKSBwdXJlIHJldHVybnMgKHVpbnQgcykgewogICAgZm9yICh1aW50IGkgPSAwOyBpIDwgYXJyLmxlbmd0aDsgaSsrKQogICAgICAgIHMgKz0gYXJyW2ldOwp9Cgpjb250cmFjdCBBcnJheUV4YW1wbGUgewogICAgYm9vbCBmb3VuZDsKICAgIGZ1bmN0aW9uIGYodWludFtdIG1lbW9yeSBhcnIpIHB1YmxpYyB7CiAgICAgICAgLy8gVGhpcyBjYWxscyB0aGUgZnJlZSBmdW5jdGlvbiBpbnRlcm5hbGx5LgogICAgICAgIC8vIFRoZSBjb21waWxlciB3aWxsIGFkZCBpdHMgY29kZSB0byB0aGUgY29udHJhY3QuCiAgICAgICAgdWludCBzID0gc3VtKGFycik7CiAgICAgICAgcmVxdWlyZShzID49IDEwKTsKICAgICAgICBmb3VuZCA9IHRydWU7CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.1 <0.9.0;

function sum(uint[] memory arr) pure returns (uint s) {
 for (uint i = 0; i < arr.length; i++)
 s += arr[i];
}

contract ArrayExample {
 bool found;
 function f(uint[] memory arr) public {
 // This calls the free function internally.
 // The compiler will add its code to the contract.
 uint s = sum(arr);
 require(s >= 10);
 found = true;
 }
}

Note

Functions defined outside a contract are still always executed in the context of a contract. They still can call other contracts, send them Ether and destroy the contract that called them, among other things. The main difference to functions defined inside a contract is that free functions do not have direct access to the variable `this`, storage variables and functions not in their scope.

### Function Parameters and Return Variables[](https://docs.soliditylang.org/en/latest/contracts.html#function-parameters-and-return-variables "Link to this heading")

Functions take typed parameters as input and may, unlike in many other languages, also return an arbitrary number of values as output.

#### Function Parameters[](https://docs.soliditylang.org/en/latest/contracts.html#function-parameters "Link to this heading")

Function parameters are declared the same way as variables, and the name of unused parameters can be omitted.

For example, if you want your contract to accept one kind of external call with two integers, you would use something like the following:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCmNvbnRyYWN0IFNpbXBsZSB7CiAgICB1aW50IHN1bTsKICAgIGZ1bmN0aW9uIHRha2VyKHVpbnQgYSwgdWludCBiKSBwdWJsaWMgewogICAgICAgIHN1bSA9IGEgKyBiOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract Simple {
 uint sum;
 function taker(uint a, uint b) public {
 sum = a + b;
 }
}

Function parameters can be used as any other local variable and they can also be assigned to.

#### Return Variables[](https://docs.soliditylang.org/en/latest/contracts.html#return-variables "Link to this heading")

Function return variables are declared with the same syntax after the `returns` keyword.

For example, suppose you want to return two results: the sum and the product of two integers passed as function parameters, then you use something like:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCmNvbnRyYWN0IFNpbXBsZSB7CiAgICBmdW5jdGlvbiBhcml0aG1ldGljKHVpbnQgYSwgdWludCBiKQogICAgICAgIHB1YmxpYwogICAgICAgIHB1cmUKICAgICAgICByZXR1cm5zICh1aW50IHN1bSwgdWludCBwcm9kdWN0KQogICAgewogICAgICAgIHN1bSA9IGEgKyBiOwogICAgICAgIHByb2R1Y3QgPSBhICogYjsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract Simple {
 function arithmetic(uint a, uint b)
 public
 pure
 returns (uint sum, uint product)
 {
 sum = a + b;
 product = a * b;
 }
}

The names of return variables can be omitted. Return variables can be used as any other local variable and they are initialized with their [default value](https://docs.soliditylang.org/en/latest/control-structures.html#default-value) and have that value until they are (re-)assigned.

You can either explicitly assign to return variables and then leave the function as above, or you can provide return values (either a single or [multiple ones](https://docs.soliditylang.org/en/latest/contracts.html#multi-return)) directly with the `return` statement:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCmNvbnRyYWN0IFNpbXBsZSB7CiAgICBmdW5jdGlvbiBhcml0aG1ldGljKHVpbnQgYSwgdWludCBiKQogICAgICAgIHB1YmxpYwogICAgICAgIHB1cmUKICAgICAgICByZXR1cm5zICh1aW50IHN1bSwgdWludCBwcm9kdWN0KQogICAgewogICAgICAgIHJldHVybiAoYSArIGIsIGEgKiBiKTsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract Simple {
 function arithmetic(uint a, uint b)
 public
 pure
 returns (uint sum, uint product)
 {
 return (a + b, a * b);
 }
}

If you use an early `return` to leave a function that has return variables, you must provide return values together with the return statement.

Note

You cannot return some types from non-internal functions. This includes the types listed below and any composite types that recursively contain them:

*   mappings,

*   internal function types,

*   reference types with location set to `storage`,

*   multi-dimensional arrays (applies only to [ABI coder v1](https://docs.soliditylang.org/en/latest/layout-of-source-files.html#abi-coder)),

*   structs (applies only to [ABI coder v1](https://docs.soliditylang.org/en/latest/layout-of-source-files.html#abi-coder)).

This restriction does not apply to library functions because of their different [internal ABI](https://docs.soliditylang.org/en/latest/contracts.html#library-selectors).

#### Returning Multiple Values[](https://docs.soliditylang.org/en/latest/contracts.html#returning-multiple-values "Link to this heading")

When a function has multiple return types, the statement `return (v0, v1, ..., vn)` can be used to return multiple values. The number of components must be the same as the number of return variables and their types have to match, potentially after an [implicit conversion](https://docs.soliditylang.org/en/latest/types.html#types-conversion-elementary-types).

### State Mutability[](https://docs.soliditylang.org/en/latest/contracts.html#state-mutability "Link to this heading")

#### View Functions[](https://docs.soliditylang.org/en/latest/contracts.html#view-functions "Link to this heading")

Functions can be declared `view` in which case they promise not to modify the state.

Note

If the compiler’s EVM target is Byzantium or newer (default) the opcode `STATICCALL` is used when `view` functions are called, which enforces the state to stay unmodified as part of the EVM execution. For library `view` functions `DELEGATECALL` is used, because there is no combined `DELEGATECALL` and `STATICCALL`. This means library `view` functions do not have run-time checks that prevent state modifications. This should not impact security negatively because library code is usually known at compile-time and the static checker performs compile-time checks.

The following statements are considered modifying the state:

1.   Writing to state variables (storage and transient storage).

2.   [Emitting events](https://docs.soliditylang.org/en/latest/contracts.html#events).

3.   [Creating other contracts](https://docs.soliditylang.org/en/latest/control-structures.html#creating-contracts).

4.   Using `selfdestruct`.

5.   Sending Ether via calls.

6.   Calling any function not marked `view` or `pure`.

7.   Using low-level calls.

8.   Using inline assembly that contains certain opcodes.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC41LjAgPDAuOS4wOwoKY29udHJhY3QgQyB7CiAgICBmdW5jdGlvbiBmKHVpbnQgYSwgdWludCBiKSBwdWJsaWMgdmlldyByZXR1cm5zICh1aW50KSB7CiAgICAgICAgcmV0dXJuIGEgKiAoYiArIDQyKSArIGJsb2NrLnRpbWVzdGFtcDsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.5.0 <0.9.0;

contract C {
 function f(uint a, uint b) public view returns (uint) {
 return a * (b + 42) + block.timestamp;
 }
}

Note

`constant` on functions used to be an alias to `view`, but this was dropped in version 0.5.0.

Note

Getter methods are automatically marked `view`.

Note

Prior to version 0.5.0, the compiler did not use the `STATICCALL` opcode for `view` functions. This enabled state modifications in `view` functions through the use of invalid explicit type conversions. By using `STATICCALL` for `view` functions, modifications to the state are prevented on the level of the EVM.

#### Pure Functions[](https://docs.soliditylang.org/en/latest/contracts.html#pure-functions "Link to this heading")

Functions can be declared `pure` in which case they promise not to read from or modify the state. In particular, it should be possible to evaluate a `pure` function at compile-time given only its inputs and `msg.data`, but without any knowledge of the current blockchain state. This means that reading from `immutable` variables can be a non-pure operation.

Note

If the compiler’s EVM target is Byzantium or newer (default) the opcode `STATICCALL` is used, which does not guarantee that the state is not read, but at least that it is not modified.

In addition to the list of state modifying statements explained above, the following are considered reading from the state:

1.   Reading from state variables (storage and transient storage).

2.   Accessing `address(this).balance` or `<address>.balance`.

3.   Accessing any of the members of `block`, `tx`, `msg` (with the exception of `msg.sig` and `msg.data`).

4.   Calling any function not marked `pure`.

5.   Using inline assembly that contains certain opcodes.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC41LjAgPDAuOS4wOwoKY29udHJhY3QgQyB7CiAgICBmdW5jdGlvbiBmKHVpbnQgYSwgdWludCBiKSBwdWJsaWMgcHVyZSByZXR1cm5zICh1aW50KSB7CiAgICAgICAgcmV0dXJuIGEgKiAoYiArIDQyKTsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.5.0 <0.9.0;

contract C {
 function f(uint a, uint b) public pure returns (uint) {
 return a * (b + 42);
 }
}

Pure functions are able to use the `revert()` and `require()` functions to revert potential state changes when an [error occurs](https://docs.soliditylang.org/en/latest/control-structures.html#assert-and-require).

Reverting a state change is not considered a “state modification”, as only changes to the state made previously in code that did not have the `view` or `pure` restriction are reverted and that code has the option to catch the `revert` and not pass it on.

This behavior is also in line with the `STATICCALL` opcode.

Warning

It is not possible to prevent functions from reading the state at the level of the EVM, it is only possible to prevent them from writing to the state (i.e. only `view` can be enforced at the EVM level, `pure` can not).

Note

Prior to version 0.5.0, the compiler did not use the `STATICCALL` opcode for `pure` functions. This enabled state modifications in `pure` functions through the use of invalid explicit type conversions. By using `STATICCALL` for `pure` functions, modifications to the state are prevented on the level of the EVM.

Note

Prior to version 0.4.17 the compiler did not enforce that `pure` is not reading the state. It is a compile-time type check, which can be circumvented by doing invalid explicit conversions between contract types, because the compiler can verify that the type of the contract does not do state-changing operations, but it cannot check that the contract that will be called at runtime is actually of that type.

### Special Functions[](https://docs.soliditylang.org/en/latest/contracts.html#special-functions "Link to this heading")

#### Receive Ether Function[](https://docs.soliditylang.org/en/latest/contracts.html#receive-ether-function "Link to this heading")

A contract can have at most one `receive` function, declared using `receive() external payable { ... }` (without the `function` keyword). This function cannot have arguments, cannot return anything and must have `external` visibility and `payable` state mutability. It can be virtual, can override and can have modifiers.

The receive function is executed on a call to the contract with empty calldata. This is the function that is executed on plain Ether transfers (e.g. via `.send()` or `.transfer()`). If no such function exists, but a payable [fallback function](https://docs.soliditylang.org/en/latest/contracts.html#fallback-function) exists, the fallback function will be called on a plain Ether transfer. If neither a receive Ether nor a payable fallback function is present, the contract cannot receive Ether through a transaction that does not represent a payable function call and throws an exception.

In the worst case, the `receive` function can only rely on 2300 gas being available (for example when `send` or `transfer` is used), leaving little room to perform other operations except basic logging. The following operations will consume more gas than the 2300 gas stipend:

*   Writing to storage

*   Creating a contract

*   Calling an external function which consumes a large amount of gas

*   Sending Ether

Warning

When Ether is sent directly to a contract (without a function call, i.e. sender uses `send` or `transfer`) but the receiving contract does not define a receive Ether function or a payable fallback function, an exception will be thrown, sending back the Ether (this was different before Solidity v0.4.0). If you want your contract to receive Ether, you have to implement a receive Ether function (using payable fallback functions for receiving Ether is not recommended, since the fallback is invoked and would not fail for interface confusions on the part of the sender).

Warning

A contract without a receive Ether function can receive Ether as a recipient of a _coinbase transaction_ (aka _miner block reward_) or as a destination of a `selfdestruct`.

A contract cannot react to such Ether transfers and thus also cannot reject them. This is a design choice of the EVM and Solidity cannot work around it.

It also means that `address(this).balance` can be higher than the sum of some manual accounting implemented in a contract (i.e. having a counter updated in the receive Ether function).

Below you can see an example of a Sink contract that uses function `receive`.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjAgPDAuOS4wOwoKLy8gVGhpcyBjb250cmFjdCBrZWVwcyBhbGwgRXRoZXIgc2VudCB0byBpdCB3aXRoIG5vIHdheQovLyB0byBnZXQgaXQgYmFjay4KY29udHJhY3QgU2luayB7CiAgICBldmVudCBSZWNlaXZlZChhZGRyZXNzLCB1aW50KTsKICAgIHJlY2VpdmUoKSBleHRlcm5hbCBwYXlhYmxlIHsKICAgICAgICBlbWl0IFJlY2VpdmVkKG1zZy5zZW5kZXIsIG1zZy52YWx1ZSk7CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

// This contract keeps all Ether sent to it with no way
// to get it back.
contract Sink {
 event Received(address, uint);
 receive() external payable {
 emit Received(msg.sender, msg.value);
 }
}

#### Fallback Function[](https://docs.soliditylang.org/en/latest/contracts.html#fallback-function "Link to this heading")

A contract can have at most one `fallback` function, declared using either `fallback () external [payable]` or `fallback (bytes calldata input) external [payable] returns (bytes memory output)` (both without the `function` keyword). This function must have `external` visibility. A fallback function can be virtual, can override and can have modifiers.

The fallback function is executed on a call to the contract if none of the other functions match the given function signature, or if no data was supplied at all and there is no [receive Ether function](https://docs.soliditylang.org/en/latest/contracts.html#receive-ether-function). The fallback function always receives data, but in order to also receive Ether it must be marked `payable`.

If the version with parameters is used, `input` will contain the full data sent to the contract (equal to `msg.data`) and can return data in `output`. The returned data will not be ABI-encoded. Instead it will be returned without modifications (not even padding).

In the worst case, if a payable fallback function is also used in place of a receive function, it can only rely on 2300 gas being available (see [receive Ether function](https://docs.soliditylang.org/en/latest/contracts.html#receive-ether-function) for a brief description of the implications of this).

Like any function, the fallback function can execute complex operations as long as there is enough gas passed on to it.

Warning

A `payable` fallback function is also executed for plain Ether transfers, if no [receive Ether function](https://docs.soliditylang.org/en/latest/contracts.html#receive-ether-function) is present. It is recommended to always define a receive Ether function as well, if you define a payable fallback function to distinguish Ether transfers from interface confusions.

Note

If you want to decode the input data, you can check the first four bytes for the function selector and then you can use `abi.decode` together with the array slice syntax to decode ABI-encoded data: `(c, d) = abi.decode(input[4:], (uint256, uint256));` Note that this should only be used as a last resort and proper functions should be used instead.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjIgPDAuOS4wOwoKY29udHJhY3QgVGVzdCB7CiAgICB1aW50IHg7CiAgICAvLyBUaGlzIGZ1bmN0aW9uIGlzIGNhbGxlZCBmb3IgYWxsIG1lc3NhZ2VzIHNlbnQgdG8KICAgIC8vIHRoaXMgY29udHJhY3QgKHRoZXJlIGlzIG5vIG90aGVyIGZ1bmN0aW9uKS4KICAgIC8vIFNlbmRpbmcgRXRoZXIgdG8gdGhpcyBjb250cmFjdCB3aWxsIGNhdXNlIGFuIGV4Y2VwdGlvbiwKICAgIC8vIGJlY2F1c2UgdGhlIGZhbGxiYWNrIGZ1bmN0aW9uIGRvZXMgbm90IGhhdmUgdGhlIGBwYXlhYmxlYAogICAgLy8gbW9kaWZpZXIuCiAgICBmYWxsYmFjaygpIGV4dGVybmFsIHsgeCA9IDE7IH0KfQoKY29udHJhY3QgVGVzdFBheWFibGUgewogICAgdWludCB4OwogICAgdWludCB5OwogICAgLy8gVGhpcyBmdW5jdGlvbiBpcyBjYWxsZWQgZm9yIGFsbCBtZXNzYWdlcyBzZW50IHRvCiAgICAvLyB0aGlzIGNvbnRyYWN0LCBleGNlcHQgcGxhaW4gRXRoZXIgdHJhbnNmZXJzCiAgICAvLyAodGhlcmUgaXMgbm8gb3RoZXIgZnVuY3Rpb24gZXhjZXB0IHRoZSByZWNlaXZlIGZ1bmN0aW9uKS4KICAgIC8vIEFueSBjYWxsIHdpdGggbm9uLWVtcHR5IGNhbGxkYXRhIHRvIHRoaXMgY29udHJhY3Qgd2lsbCBleGVjdXRlCiAgICAvLyB0aGUgZmFsbGJhY2sgZnVuY3Rpb24gKGV2ZW4gaWYgRXRoZXIgaXMgc2VudCBhbG9uZyB3aXRoIHRoZSBjYWxsKS4KICAgIGZhbGxiYWNrKCkgZXh0ZXJuYWwgcGF5YWJsZSB7IHggPSAxOyB5ID0gbXNnLnZhbHVlOyB9CgogICAgLy8gVGhpcyBmdW5jdGlvbiBpcyBjYWxsZWQgZm9yIHBsYWluIEV0aGVyIHRyYW5zZmVycywgaS5lLgogICAgLy8gZm9yIGV2ZXJ5IGNhbGwgd2l0aCBlbXB0eSBjYWxsZGF0YS4KICAgIHJlY2VpdmUoKSBleHRlcm5hbCBwYXlhYmxlIHsgeCA9IDI7IHkgPSBtc2cudmFsdWU7IH0KfQoKY29udHJhY3QgQ2FsbGVyIHsKICAgIGZ1bmN0aW9uIGNhbGxUZXN0KFRlc3QgdGVzdCkgcHVibGljIHJldHVybnMgKGJvb2wpIHsKICAgICAgICAoYm9vbCBzdWNjZXNzLCkgPSBhZGRyZXNzKHRlc3QpLmNhbGwoYWJpLmVuY29kZVdpdGhTaWduYXR1cmUoIm5vbkV4aXN0aW5nRnVuY3Rpb24oKSIpKTsKICAgICAgICByZXF1aXJlKHN1Y2Nlc3MpOwogICAgICAgIC8vIHJlc3VsdHMgaW4gdGVzdC54IGJlY29taW5nID09IDEuCgogICAgICAgIC8vIGFkZHJlc3ModGVzdCkgd2lsbCBub3QgYWxsb3cgdG8gY2FsbCBgYHNlbmRgYCBkaXJlY3RseSwgc2luY2UgYGB0ZXN0YGAgaGFzIG5vIHBheWFibGUKICAgICAgICAvLyBmYWxsYmFjayBmdW5jdGlvbi4KICAgICAgICAvLyBJdCBoYXMgdG8gYmUgY29udmVydGVkIHRvIHRoZSBgYGFkZHJlc3MgcGF5YWJsZWBgIHR5cGUgdG8gZXZlbiBhbGxvdyBjYWxsaW5nIGBgc2VuZGBgIG9uIGl0LgogICAgICAgIGFkZHJlc3MgcGF5YWJsZSB0ZXN0UGF5YWJsZSA9IHBheWFibGUoYWRkcmVzcyh0ZXN0KSk7CgogICAgICAgIC8vIElmIHNvbWVvbmUgc2VuZHMgRXRoZXIgdG8gdGhhdCBjb250cmFjdCwKICAgICAgICAvLyB0aGUgdHJhbnNmZXIgd2lsbCBmYWlsLCBpLmUuIHRoaXMgcmV0dXJucyBmYWxzZSBoZXJlLgogICAgICAgIHJldHVybiB0ZXN0UGF5YWJsZS5zZW5kKDIgZXRoZXIpOwogICAgfQoKICAgIGZ1bmN0aW9uIGNhbGxUZXN0UGF5YWJsZShUZXN0UGF5YWJsZSB0ZXN0KSBwdWJsaWMgcmV0dXJucyAoYm9vbCkgewogICAgICAgIChib29sIHN1Y2Nlc3MsKSA9IGFkZHJlc3ModGVzdCkuY2FsbChhYmkuZW5jb2RlV2l0aFNpZ25hdHVyZSgibm9uRXhpc3RpbmdGdW5jdGlvbigpIikpOwogICAgICAgIHJlcXVpcmUoc3VjY2Vzcyk7CiAgICAgICAgLy8gcmVzdWx0cyBpbiB0ZXN0LnggYmVjb21pbmcgPT0gMSBhbmQgdGVzdC55IGJlY29taW5nIDAuCiAgICAgICAgKHN1Y2Nlc3MsKSA9IGFkZHJlc3ModGVzdCkuY2FsbHt2YWx1ZTogMX0oYWJpLmVuY29kZVdpdGhTaWduYXR1cmUoIm5vbkV4aXN0aW5nRnVuY3Rpb24oKSIpKTsKICAgICAgICByZXF1aXJlKHN1Y2Nlc3MpOwogICAgICAgIC8vIHJlc3VsdHMgaW4gdGVzdC54IGJlY29taW5nID09IDEgYW5kIHRlc3QueSBiZWNvbWluZyAxLgoKICAgICAgICAvLyBJZiBzb21lb25lIHNlbmRzIEV0aGVyIHRvIHRoYXQgY29udHJhY3QsIHRoZSByZWNlaXZlIGZ1bmN0aW9uIGluIFRlc3RQYXlhYmxlIHdpbGwgYmUgY2FsbGVkLgogICAgICAgIC8vIFNpbmNlIHRoYXQgZnVuY3Rpb24gd3JpdGVzIHRvIHN0b3JhZ2UsIGl0IHRha2VzIG1vcmUgZ2FzIHRoYW4gaXMgYXZhaWxhYmxlIHdpdGggYQogICAgICAgIC8vIHNpbXBsZSBgYHNlbmRgYCBvciBgYHRyYW5zZmVyYGAuIEJlY2F1c2Ugb2YgdGhhdCwgd2UgaGF2ZSB0byB1c2UgYSBsb3ctbGV2ZWwgY2FsbC4KICAgICAgICAoc3VjY2VzcywpID0gYWRkcmVzcyh0ZXN0KS5jYWxse3ZhbHVlOiAyIGV0aGVyfSgiIik7CiAgICAgICAgcmVxdWlyZShzdWNjZXNzKTsKICAgICAgICAvLyByZXN1bHRzIGluIHRlc3QueCBiZWNvbWluZyA9PSAyIGFuZCB0ZXN0LnkgYmVjb21pbmcgMiBldGhlci4KCiAgICAgICAgcmV0dXJuIHRydWU7CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.2 <0.9.0;

contract Test {
 uint x;
 // This function is called for all messages sent to
 // this contract (there is no other function).
 // Sending Ether to this contract will cause an exception,
 // because the fallback function does not have the `payable`
 // modifier.
 fallback() external { x = 1; }
}

contract TestPayable {
 uint x;
 uint y;
 // This function is called for all messages sent to
 // this contract, except plain Ether transfers
 // (there is no other function except the receive function).
 // Any call with non-empty calldata to this contract will execute
 // the fallback function (even if Ether is sent along with the call).
 fallback() external payable { x = 1; y = msg.value; }

 // This function is called for plain Ether transfers, i.e.
 // for every call with empty calldata.
 receive() external payable { x = 2; y = msg.value; }
}

contract Caller {
 function callTest(Test test) public returns (bool) {
 (bool success,) = address(test).call(abi.encodeWithSignature("nonExistingFunction()"));
 require(success);
 // results in test.x becoming == 1.

 // address(test) will not allow to call ``send`` directly, since ``test`` has no payable
 // fallback function.
 // It has to be converted to the ``address payable`` type to even allow calling ``send`` on it.
 address payable testPayable = payable(address(test));

 // If someone sends Ether to that contract,
 // the transfer will fail, i.e. this returns false here.
 return testPayable.send(2 ether);
 }

 function callTestPayable(TestPayable test) public returns (bool) {
 (bool success,) = address(test).call(abi.encodeWithSignature("nonExistingFunction()"));
 require(success);
 // results in test.x becoming == 1 and test.y becoming 0.
 (success,) = address(test).call{value: 1}(abi.encodeWithSignature("nonExistingFunction()"));
 require(success);
 // results in test.x becoming == 1 and test.y becoming 1.

 // If someone sends Ether to that contract, the receive function in TestPayable will be called.
 // Since that function writes to storage, it takes more gas than is available with a
 // simple ``send`` or ``transfer``. Because of that, we have to use a low-level call.
 (success,) = address(test).call{value: 2 ether}("");
 require(success);
 // results in test.x becoming == 2 and test.y becoming 2 ether.

 return true;
 }
}

### Function Overloading[](https://docs.soliditylang.org/en/latest/contracts.html#function-overloading "Link to this heading")

A contract can have multiple functions of the same name but with different parameter types. This process is called “overloading” and also applies to inherited functions. The following example shows overloading of the function `f` in the scope of contract `A`.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCmNvbnRyYWN0IEEgewogICAgZnVuY3Rpb24gZih1aW50IHZhbHVlKSBwdWJsaWMgcHVyZSByZXR1cm5zICh1aW50IG91dCkgewogICAgICAgIG91dCA9IHZhbHVlOwogICAgfQoKICAgIGZ1bmN0aW9uIGYodWludCB2YWx1ZSwgYm9vbCByZWFsbHkpIHB1YmxpYyBwdXJlIHJldHVybnMgKHVpbnQgb3V0KSB7CiAgICAgICAgaWYgKHJlYWxseSkKICAgICAgICAgICAgb3V0ID0gdmFsdWU7CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract A {
 function f(uint value) public pure returns (uint out) {
 out = value;
 }

 function f(uint value, bool really) public pure returns (uint out) {
 if (really)
 out = value;
 }
}

Overloaded functions are also present in the external interface. It is an error if two externally visible functions differ by their Solidity types but not by their external types.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCi8vIFRoaXMgd2lsbCBub3QgY29tcGlsZQpjb250cmFjdCBBIHsKICAgIGZ1bmN0aW9uIGYoQiB2YWx1ZSkgcHVibGljIHB1cmUgcmV0dXJucyAoQiBvdXQpIHsKICAgICAgICBvdXQgPSB2YWx1ZTsKICAgIH0KCiAgICBmdW5jdGlvbiBmKGFkZHJlc3MgdmFsdWUpIHB1YmxpYyBwdXJlIHJldHVybnMgKGFkZHJlc3Mgb3V0KSB7CiAgICAgICAgb3V0ID0gdmFsdWU7CiAgICB9Cn0KCmNvbnRyYWN0IEIgewp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

// This will not compile
contract A {
 function f(B value) public pure returns (B out) {
 out = value;
 }

 function f(address value) public pure returns (address out) {
 out = value;
 }
}

contract B {
}

Both `f` function overloads above end up accepting the address type for the ABI although they are considered different inside Solidity.

#### Overload resolution and Argument matching[](https://docs.soliditylang.org/en/latest/contracts.html#overload-resolution-and-argument-matching "Link to this heading")

Overloaded functions are selected by matching the function declarations in the current scope to the arguments supplied in the function call. Functions are selected as overload candidates if all arguments can be implicitly converted to the expected types. If there is not exactly one candidate, resolution fails.

Note

Return parameters are not taken into account for overload resolution.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCmNvbnRyYWN0IEEgewogICAgZnVuY3Rpb24gZih1aW50OCB2YWwpIHB1YmxpYyBwdXJlIHJldHVybnMgKHVpbnQ4IG91dCkgewogICAgICAgIG91dCA9IHZhbDsKICAgIH0KCiAgICBmdW5jdGlvbiBmKHVpbnQyNTYgdmFsKSBwdWJsaWMgcHVyZSByZXR1cm5zICh1aW50MjU2IG91dCkgewogICAgICAgIG91dCA9IHZhbDsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract A {
 function f(uint8 val) public pure returns (uint8 out) {
 out = val;
 }

 function f(uint256 val) public pure returns (uint256 out) {
 out = val;
 }
}

Calling `f(50)` would create a type error since `50` can be implicitly converted both to `uint8` and `uint256` types. On another hand `f(256)` would resolve to `f(uint256)` overload as `256` cannot be implicitly converted to `uint8`.

Events[](https://docs.soliditylang.org/en/latest/contracts.html#events "Link to this heading")
-----------------------------------------------------------------------------------------------

Solidity events give an abstraction on top of the EVM’s logging functionality. Applications can subscribe and listen to these events through the RPC interface of an Ethereum client.

Events can be defined at file level or as inheritable members of contracts (including interfaces and libraries). When you call them, they cause the arguments to be stored in the transaction’s log - a special data structure in the blockchain. These logs are associated with the address of the contract that emitted them, are incorporated into the blockchain, and stay there as long as a block is accessible (forever as of now, but this might change in the future). The Log and its event data are not accessible from within contracts (not even from the contract that created them).

It is possible to request a Merkle proof for logs, so if an external entity supplies a contract with such a proof, it can check that the log actually exists inside the blockchain. You have to supply block headers because the contract can only see the last 256 block hashes.

You can add the attribute `indexed` to up to three parameters which adds them to a special data structure known as [“topics”](https://docs.soliditylang.org/en/latest/abi-spec.html#abi-events) instead of the data part of the log. A topic can only hold a single word (32 bytes) so if you use a [reference type](https://docs.soliditylang.org/en/latest/types.html#reference-types) for an indexed argument, the Keccak-256 hash of the value is stored as a topic instead.

All parameters without the `indexed` attribute are [ABI-encoded](https://docs.soliditylang.org/en/latest/abi-spec.html#abi) into the data part of the log.

Topics allow you to search for events, for example when filtering a sequence of blocks for certain events. You can also filter events by the address of the contract that emitted the event.

For example, the code below uses the web3.js `subscribe("logs")`[method](https://web3js.readthedocs.io/en/1.0/web3-eth-subscribe.html#subscribe-logs) to filter logs that match a topic with a certain address value:

var options = {
 fromBlock: 0,
 address: web3.eth.defaultAccount,
 topics: ["0x0000000000000000000000000000000000000000000000000000000000000000", null, null]
};
web3.eth.subscribe('logs', options, function (error, result) {
 if (!error)
 console.log(result);
})
 .on("data", function (log) {
 console.log(log);
 })
 .on("changed", function (log) {
});

The hash of the signature of the event is one of the topics, except if you declared the event with the `anonymous` specifier. This means that it is not possible to filter for specific anonymous events by name, you can only filter by the contract address. The advantage of anonymous events is that they are cheaper to deploy and call. It also allows you to declare four indexed arguments rather than three.

Note

Since the transaction log only stores the event data and not the type, you have to know the type of the event, including which parameter is indexed and if the event is anonymous in order to correctly interpret the data. In particular, it is possible to “fake” the signature of another event using an anonymous event.

### Members of Events[](https://docs.soliditylang.org/en/latest/contracts.html#members-of-events "Link to this heading")

*   `event.selector`: For non-anonymous events, this is a `bytes32` value containing the `keccak256` hash of the event signature, as used in the default topic.

### Example[](https://docs.soliditylang.org/en/latest/contracts.html#example "Link to this heading")

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjIxIDwwLjkuMDsKCmNvbnRyYWN0IENsaWVudFJlY2VpcHQgewogICAgZXZlbnQgRGVwb3NpdCgKICAgICAgICBhZGRyZXNzIGluZGV4ZWQgZnJvbSwKICAgICAgICBieXRlczMyIGluZGV4ZWQgaWQsCiAgICAgICAgdWludCB2YWx1ZQogICAgKTsKCiAgICBmdW5jdGlvbiBkZXBvc2l0KGJ5dGVzMzIgaWQpIHB1YmxpYyBwYXlhYmxlIHsKICAgICAgICAvLyBFdmVudHMgYXJlIGVtaXR0ZWQgdXNpbmcgYGVtaXRgLCBmb2xsb3dlZCBieQogICAgICAgIC8vIHRoZSBuYW1lIG9mIHRoZSBldmVudCBhbmQgdGhlIGFyZ3VtZW50cwogICAgICAgIC8vIChpZiBhbnkpIGluIHBhcmVudGhlc2VzLiBBbnkgc3VjaCBpbnZvY2F0aW9uCiAgICAgICAgLy8gKGV2ZW4gZGVlcGx5IG5lc3RlZCkgY2FuIGJlIGRldGVjdGVkIGZyb20KICAgICAgICAvLyB0aGUgSmF2YVNjcmlwdCBBUEkgYnkgZmlsdGVyaW5nIGZvciBgRGVwb3NpdGAuCiAgICAgICAgZW1pdCBEZXBvc2l0KG1zZy5zZW5kZXIsIGlkLCBtc2cudmFsdWUpOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.21 <0.9.0;

contract ClientReceipt {
 event Deposit(
 address indexed from,
 bytes32 indexed id,
 uint value
 );

 function deposit(bytes32 id) public payable {
 // Events are emitted using `emit`, followed by
 // the name of the event and the arguments
 // (if any) in parentheses. Any such invocation
 // (even deeply nested) can be detected from
 // the JavaScript API by filtering for `Deposit`.
 emit Deposit(msg.sender, id, msg.value);
 }
}

The use in the JavaScript API is as follows:

var abi = /* abi as generated by the compiler */;
var ClientReceipt = web3.eth.contract(abi);
var clientReceipt = ClientReceipt.at("0x1234...ab67" /* address */);

var depositEvent = clientReceipt.Deposit();

// watch for changes
depositEvent.watch(function(error, result){
 // result contains non-indexed arguments and topics
 // given to the `Deposit` call.
 if (!error)
 console.log(result);
});

// Or pass a callback to start watching immediately
var depositEvent = clientReceipt.Deposit(function(error, result) {
 if (!error)
 console.log(result);
});

The output of the above looks like the following (trimmed):

{
 "returnValues": {
 "from": "0x1111…FFFFCCCC",
 "id": "0x50…sd5adb20",
 "value": "0x420042"
 },
 "raw": {
 "data": "0x7f…91385",
 "topics": ["0xfd4…b4ead7", "0x7f…1a91385"]
 }
}

### Additional Resources for Understanding Events[](https://docs.soliditylang.org/en/latest/contracts.html#additional-resources-for-understanding-events "Link to this heading")

*   [JavaScript documentation](https://github.com/web3/web3.js/blob/1.x/docs/web3-eth-contract.rst#events)

*   [Example usage of events](https://github.com/ethchange/smart-exchange/blob/master/lib/contracts/SmartExchange.sol)

*   [How to access them in js](https://github.com/ethchange/smart-exchange/blob/master/lib/exchange_transactions.js)

Custom Errors[](https://docs.soliditylang.org/en/latest/contracts.html#custom-errors "Link to this heading")
-------------------------------------------------------------------------------------------------------------

Errors in Solidity provide a convenient and gas-efficient way to explain to the user why an operation failed. They can be defined inside and outside of contracts (including interfaces and libraries).

They have to be used together with the [revert statement](https://docs.soliditylang.org/en/latest/control-structures.html#revert-statement) or the [require function](https://docs.soliditylang.org/en/latest/control-structures.html#assert-and-require-statements). In the case of `revert` statements, or `require` calls where the condition is evaluated to be false, all changes in the current call are reverted, and the error data passed back to the caller.

The example below shows custom error usage with the `revert` statement in function `transferWithRevertError`, as well as the newer approach with `require` in function `transferWithRequireError`.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguMjc7CgovLy8gSW5zdWZmaWNpZW50IGJhbGFuY2UgZm9yIHRyYW5zZmVyLiBOZWVkZWQgYHJlcXVpcmVkYCBidXQgb25seQovLy8gYGF2YWlsYWJsZWAgYXZhaWxhYmxlLgovLy8gQHBhcmFtIGF2YWlsYWJsZSBiYWxhbmNlIGF2YWlsYWJsZS4KLy8vIEBwYXJhbSByZXF1aXJlZCByZXF1ZXN0ZWQgYW1vdW50IHRvIHRyYW5zZmVyLgplcnJvciBJbnN1ZmZpY2llbnRCYWxhbmNlKHVpbnQyNTYgYXZhaWxhYmxlLCB1aW50MjU2IHJlcXVpcmVkKTsKCmNvbnRyYWN0IFRlc3RUb2tlbiB7CiAgICBtYXBwaW5nKGFkZHJlc3MgPT4gdWludCkgYmFsYW5jZTsKICAgIGZ1bmN0aW9uIHRyYW5zZmVyV2l0aFJldmVydEVycm9yKGFkZHJlc3MgdG8sIHVpbnQyNTYgYW1vdW50KSBwdWJsaWMgewogICAgICAgIGlmIChhbW91bnQgPiBiYWxhbmNlW21zZy5zZW5kZXJdKQogICAgICAgICAgICByZXZlcnQgSW5zdWZmaWNpZW50QmFsYW5jZSh7CiAgICAgICAgICAgICAgICBhdmFpbGFibGU6IGJhbGFuY2VbbXNnLnNlbmRlcl0sCiAgICAgICAgICAgICAgICByZXF1aXJlZDogYW1vdW50CiAgICAgICAgICAgIH0pOwogICAgICAgIGJhbGFuY2VbbXNnLnNlbmRlcl0gLT0gYW1vdW50OwogICAgICAgIGJhbGFuY2VbdG9dICs9IGFtb3VudDsKICAgIH0KICAgIGZ1bmN0aW9uIHRyYW5zZmVyV2l0aFJlcXVpcmVFcnJvcihhZGRyZXNzIHRvLCB1aW50MjU2IGFtb3VudCkgcHVibGljIHsKICAgICAgICByZXF1aXJlKGFtb3VudCA8PSBiYWxhbmNlW21zZy5zZW5kZXJdLCBJbnN1ZmZpY2llbnRCYWxhbmNlKGJhbGFuY2VbbXNnLnNlbmRlcl0sIGFtb3VudCkpOwogICAgICAgIGJhbGFuY2VbbXNnLnNlbmRlcl0gLT0gYW1vdW50OwogICAgICAgIGJhbGFuY2VbdG9dICs9IGFtb3VudDsKICAgIH0KICAgIC8vIC4uLgp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.27;

/// Insufficient balance for transfer. Needed `required` but only
/// `available` available.
/// @param available balance available.
/// @param required requested amount to transfer.
error InsufficientBalance(uint256 available, uint256 required);

contract TestToken {
 mapping(address => uint) balance;
 function transferWithRevertError(address to, uint256 amount) public {
 if (amount > balance[msg.sender])
 revert InsufficientBalance({
 available: balance[msg.sender],
 required: amount
 });
 balance[msg.sender] -= amount;
 balance[to] += amount;
 }
 function transferWithRequireError(address to, uint256 amount) public {
 require(amount <= balance[msg.sender], InsufficientBalance(balance[msg.sender], amount));
 balance[msg.sender] -= amount;
 balance[to] += amount;
 }
 // ...
}

Another important detail to mention when it comes to using `require` with custom errors, is that memory allocation for the error-based revert reason will only happen in the reverting case, which, along with optimization of constants and string literals makes this about as gas-efficient as the `if (!condition) revert CustomError(args)` pattern.

Errors cannot be overloaded or overridden but are inherited. The same error can be defined in multiple places as long as the scopes are distinct. Instances of errors can only be created using `revert` statements, or as the second argument to `require` functions.

The error creates data that is then passed to the caller with the revert operation to either return to the off-chain component or catch it in a [try/catch statement](https://docs.soliditylang.org/en/latest/control-structures.html#try-catch). Note that an error can only be caught when coming from an external call, reverts happening in internal calls or inside the same function cannot be caught.

If you do not provide any parameters, the error only needs four bytes of data and you can use [NatSpec](https://docs.soliditylang.org/en/latest/natspec-format.html#natspec) as above to further explain the reasons behind the error, which is not stored on chain. This makes this a very cheap and convenient error-reporting feature at the same time.

More specifically, an error instance is ABI-encoded in the same way as a function call to a function of the same name and types would be and then used as the return data in the `revert` opcode. This means that the data consists of a 4-byte selector followed by [ABI-encoded](https://docs.soliditylang.org/en/latest/abi-spec.html#abi) data. The selector consists of the first four bytes of the keccak256-hash of the signature of the error type.

Note

It is possible for a contract to revert with different errors of the same name or even with errors defined in different places that are indistinguishable by the caller. For the outside, i.e. the ABI, only the name of the error is relevant, not the contract or file where it is defined.

The statement `require(condition, "description");` would be equivalent to `if (!condition) revert Error("description")` if you could define `error Error(string)`. Note, however, that `Error` is a built-in type and cannot be defined in user-supplied code.

Similarly, a failing `assert` or similar conditions will revert with an error of the built-in type `Panic(uint256)`.

Note

Error data should only be used to give an indication of failure, but not as a means for control-flow. The reason is that the revert data of inner calls is propagated back through the chain of external calls by default. This means that an inner call can “forge” revert data that looks like it could have come from the contract that called it.

### Members of Errors[](https://docs.soliditylang.org/en/latest/contracts.html#members-of-errors "Link to this heading")

*   `error.selector`: A `bytes4` value containing the error selector.

Inheritance[](https://docs.soliditylang.org/en/latest/contracts.html#inheritance "Link to this heading")
---------------------------------------------------------------------------------------------------------

Solidity supports multiple inheritance including polymorphism.

Polymorphism means that a function call (internal and external) always executes the function of the same name (and parameter types) in the most derived contract in the inheritance hierarchy. This has to be explicitly enabled on each function in the hierarchy using the `virtual` and `override` keywords. See [Function Overriding](https://docs.soliditylang.org/en/latest/contracts.html#function-overriding) for more details.

It is possible to call functions further up in the inheritance hierarchy internally by explicitly specifying the contract using `ContractName.functionName()` or using `super.functionName()` if you want to call the function one level higher up in the flattened inheritance hierarchy (see below).

When a contract inherits from other contracts, only a single contract is created on the blockchain, and the code from all the base contracts is compiled into the created contract. This means that all internal calls to functions of base contracts also just use internal function calls (`super.f(..)` will use JUMP and not a message call).

State variable shadowing is considered as an error. A derived contract can only declare a state variable `x`, if there is no visible state variable with the same name in any of its bases.

The general inheritance system is very similar to [Python’s](https://docs.python.org/3/tutorial/classes.html#inheritance), especially concerning multiple inheritance, but there are also some [differences](https://docs.soliditylang.org/en/latest/contracts.html#multi-inheritance).

Details are given in the following example.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjAgPDAuOS4wOwoKY29udHJhY3QgT3duZWQgewogICAgYWRkcmVzcyBwYXlhYmxlIG93bmVyOwogICAgY29uc3RydWN0b3IoKSB7IG93bmVyID0gcGF5YWJsZShtc2cuc2VuZGVyKTsgfQp9CgovLyBVc2UgYGlzYCB0byBkZXJpdmUgZnJvbSBhbm90aGVyIGNvbnRyYWN0LiBEZXJpdmVkCi8vIGNvbnRyYWN0cyBjYW4gYWNjZXNzIGFsbCBub24tcHJpdmF0ZSBtZW1iZXJzIGluY2x1ZGluZwovLyBpbnRlcm5hbCBmdW5jdGlvbnMgYW5kIHN0YXRlIHZhcmlhYmxlcy4gVGhlc2UgY2Fubm90IGJlCi8vIGFjY2Vzc2VkIGV4dGVybmFsbHkgdmlhIGB0aGlzYCwgdGhvdWdoLgpjb250cmFjdCBFbWl0dGFibGUgaXMgT3duZWQgewogICAgZXZlbnQgRW1pdHRlZCgpOwoKICAgIC8vIFRoZSBrZXl3b3JkIGB2aXJ0dWFsYCBtZWFucyB0aGF0IHRoZSBmdW5jdGlvbiBjYW4gY2hhbmdlCiAgICAvLyBpdHMgYmVoYXZpb3IgaW4gZGVyaXZlZCBjbGFzc2VzICgib3ZlcnJpZGluZyIpLgogICAgZnVuY3Rpb24gZW1pdEV2ZW50KCkgdmlydHVhbCBwdWJsaWMgewogICAgICAgIGlmIChtc2cuc2VuZGVyID09IG93bmVyKQogICAgICAgICAgICBlbWl0IEVtaXR0ZWQoKTsKICAgIH0KfQoKLy8gVGhlc2UgYWJzdHJhY3QgY29udHJhY3RzIGFyZSBvbmx5IHByb3ZpZGVkIHRvIG1ha2UgdGhlCi8vIGludGVyZmFjZSBrbm93biB0byB0aGUgY29tcGlsZXIuIE5vdGUgdGhlIGZ1bmN0aW9uCi8vIHdpdGhvdXQgYm9keS4gSWYgYSBjb250cmFjdCBkb2VzIG5vdCBpbXBsZW1lbnQgYWxsCi8vIGZ1bmN0aW9ucyBpdCBjYW4gb25seSBiZSB1c2VkIGFzIGFuIGludGVyZmFjZS4KYWJzdHJhY3QgY29udHJhY3QgQ29uZmlnIHsKICAgIGZ1bmN0aW9uIGxvb2t1cCh1aW50IGlkKSBwdWJsaWMgdmlydHVhbCByZXR1cm5zIChhZGRyZXNzIGFkcik7Cn0KCmFic3RyYWN0IGNvbnRyYWN0IE5hbWVSZWcgewogICAgZnVuY3Rpb24gcmVnaXN0ZXIoYnl0ZXMzMiBuYW1lKSBwdWJsaWMgdmlydHVhbDsKICAgIGZ1bmN0aW9uIHVucmVnaXN0ZXIoKSBwdWJsaWMgdmlydHVhbDsKfQoKLy8gTXVsdGlwbGUgaW5oZXJpdGFuY2UgaXMgcG9zc2libGUuIE5vdGUgdGhhdCBgT3duZWRgIGlzCi8vIGFsc28gYSBiYXNlIGNsYXNzIG9mIGBFbWl0dGFibGVgLCB5ZXQgdGhlcmUgaXMgb25seSBhIHNpbmdsZQovLyBpbnN0YW5jZSBvZiBgT3duZWRgIChhcyBmb3IgdmlydHVhbCBpbmhlcml0YW5jZSBpbiBDKyspLgpjb250cmFjdCBOYW1lZCBpcyBPd25lZCwgRW1pdHRhYmxlIHsKICAgIGNvbnN0cnVjdG9yKGJ5dGVzMzIgbmFtZSkgewogICAgICAgIENvbmZpZyBjb25maWcgPSBDb25maWcoMHhENWY5RDhEOTQ4ODZFNzBiMDZFNDc0YzNmQjE0RmQ0M0UyZjIzOTcwKTsKICAgICAgICBOYW1lUmVnKGNvbmZpZy5sb29rdXAoMSkpLnJlZ2lzdGVyKG5hbWUpOwogICAgfQoKICAgIC8vIEZ1bmN0aW9ucyBjYW4gYmUgb3ZlcnJpZGRlbiBieSBhbm90aGVyIGZ1bmN0aW9uIHdpdGggdGhlIHNhbWUgbmFtZSBhbmQKICAgIC8vIHRoZSBzYW1lIG51bWJlci90eXBlcyBvZiBpbnB1dHMuIElmIHRoZSBvdmVycmlkaW5nIGZ1bmN0aW9uIGhhcyBkaWZmZXJlbnQKICAgIC8vIHR5cGVzIG9mIG91dHB1dCBwYXJhbWV0ZXJzLCB0aGF0IGNhdXNlcyBhbiBlcnJvci4KICAgIC8vIEJvdGggbG9jYWwgYW5kIG1lc3NhZ2UtYmFzZWQgZnVuY3Rpb24gY2FsbHMgdGFrZSB0aGVzZSBvdmVycmlkZXMKICAgIC8vIGludG8gYWNjb3VudC4KICAgIC8vIElmIHlvdSB3YW50IHRoZSBmdW5jdGlvbiB0byBvdmVycmlkZSwgeW91IG5lZWQgdG8gdXNlIHRoZQogICAgLy8gYG92ZXJyaWRlYCBrZXl3b3JkLiBZb3UgbmVlZCB0byBzcGVjaWZ5IHRoZSBgdmlydHVhbGAga2V5d29yZCBhZ2FpbgogICAgLy8gaWYgeW91IHdhbnQgdGhpcyBmdW5jdGlvbiB0byBiZSBvdmVycmlkZGVuIGFnYWluLgogICAgZnVuY3Rpb24gZW1pdEV2ZW50KCkgcHVibGljIHZpcnR1YWwgb3ZlcnJpZGUgewogICAgICAgIGlmIChtc2cuc2VuZGVyID09IG93bmVyKSB7CiAgICAgICAgICAgIENvbmZpZyBjb25maWcgPSBDb25maWcoMHhENWY5RDhEOTQ4ODZFNzBiMDZFNDc0YzNmQjE0RmQ0M0UyZjIzOTcwKTsKICAgICAgICAgICAgTmFtZVJlZyhjb25maWcubG9va3VwKDEpKS51bnJlZ2lzdGVyKCk7CiAgICAgICAgICAgIC8vIEl0IGlzIHN0aWxsIHBvc3NpYmxlIHRvIGNhbGwgYSBzcGVjaWZpYwogICAgICAgICAgICAvLyBvdmVycmlkZGVuIGZ1bmN0aW9uLgogICAgICAgICAgICBFbWl0dGFibGUuZW1pdEV2ZW50KCk7CiAgICAgICAgfQogICAgfQp9CgoKLy8gSWYgYSBjb25zdHJ1Y3RvciB0YWtlcyBhbiBhcmd1bWVudCwgaXQgbmVlZHMgdG8gYmUKLy8gcHJvdmlkZWQgaW4gdGhlIGhlYWRlciBvciBtb2RpZmllci1pbnZvY2F0aW9uLXN0eWxlIGF0Ci8vIHRoZSBjb25zdHJ1Y3RvciBvZiB0aGUgZGVyaXZlZCBjb250cmFjdCAoc2VlIGJlbG93KS4KY29udHJhY3QgUHJpY2VGZWVkIGlzIE93bmVkLCBFbWl0dGFibGUsIE5hbWVkKCJHb2xkRmVlZCIpIHsKICAgIHVpbnQgaW5mbzsKCiAgICBmdW5jdGlvbiB1cGRhdGVJbmZvKHVpbnQgbmV3SW5mbykgcHVibGljIHsKICAgICAgICBpZiAobXNnLnNlbmRlciA9PSBvd25lcikgaW5mbyA9IG5ld0luZm87CiAgICB9CgogICAgLy8gSGVyZSwgd2Ugb25seSBzcGVjaWZ5IGBvdmVycmlkZWAgYW5kIG5vdCBgdmlydHVhbGAuCiAgICAvLyBUaGlzIG1lYW5zIHRoYXQgY29udHJhY3RzIGRlcml2aW5nIGZyb20gYFByaWNlRmVlZGAKICAgIC8vIGNhbm5vdCBjaGFuZ2UgdGhlIGJlaGF2aW9yIG9mIGBlbWl0RXZlbnRgIGFueW1vcmUuCiAgICBmdW5jdGlvbiBlbWl0RXZlbnQoKSBwdWJsaWMgb3ZlcnJpZGUoRW1pdHRhYmxlLCBOYW1lZCkgeyBOYW1lZC5lbWl0RXZlbnQoKTsgfQogICAgZnVuY3Rpb24gZ2V0KCkgcHVibGljIHZpZXcgcmV0dXJucyh1aW50IHIpIHsgcmV0dXJuIGluZm87IH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Owned {
 address payable owner;
 constructor() { owner = payable(msg.sender); }
}

// Use `is` to derive from another contract. Derived
// contracts can access all non-private members including
// internal functions and state variables. These cannot be
// accessed externally via `this`, though.
contract Emittable is Owned {
 event Emitted();

 // The keyword `virtual` means that the function can change
 // its behavior in derived classes ("overriding").
 function emitEvent() virtual public {
 if (msg.sender == owner)
 emit Emitted();
 }
}

// These abstract contracts are only provided to make the
// interface known to the compiler. Note the function
// without body. If a contract does not implement all
// functions it can only be used as an interface.
abstract contract Config {
 function lookup(uint id) public virtual returns (address adr);
}

abstract contract NameReg {
 function register(bytes32 name) public virtual;
 function unregister() public virtual;
}

// Multiple inheritance is possible. Note that `Owned` is
// also a base class of `Emittable`, yet there is only a single
// instance of `Owned` (as for virtual inheritance in C++).
contract Named is Owned, Emittable {
 constructor(bytes32 name) {
 Config config = Config(0xD5f9D8D94886E70b06E474c3fB14Fd43E2f23970);
 NameReg(config.lookup(1)).register(name);
 }

 // Functions can be overridden by another function with the same name and
 // the same number/types of inputs. If the overriding function has different
 // types of output parameters, that causes an error.
 // Both local and message-based function calls take these overrides
 // into account.
 // If you want the function to override, you need to use the
 // `override` keyword. You need to specify the `virtual` keyword again
 // if you want this function to be overridden again.
 function emitEvent() public virtual override {
 if (msg.sender == owner) {
 Config config = Config(0xD5f9D8D94886E70b06E474c3fB14Fd43E2f23970);
 NameReg(config.lookup(1)).unregister();
 // It is still possible to call a specific
 // overridden function.
 Emittable.emitEvent();
 }
 }
}

// If a constructor takes an argument, it needs to be
// provided in the header or modifier-invocation-style at
// the constructor of the derived contract (see below).
contract PriceFeed is Owned, Emittable, Named("GoldFeed") {
 uint info;

 function updateInfo(uint newInfo) public {
 if (msg.sender == owner) info = newInfo;
 }

 // Here, we only specify `override` and not `virtual`.
 // This means that contracts deriving from `PriceFeed`
 // cannot change the behavior of `emitEvent` anymore.
 function emitEvent() public override(Emittable, Named) { Named.emitEvent(); }
 function get() public view returns(uint r) { return info; }
}

Note that above, we call `Emittable.emitEvent()` to “forward” the emit event request. The way this is done is problematic, as seen in the following example:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjAgPDAuOS4wOwoKY29udHJhY3QgT3duZWQgewogICAgYWRkcmVzcyBwYXlhYmxlIG93bmVyOwogICAgY29uc3RydWN0b3IoKSB7IG93bmVyID0gcGF5YWJsZShtc2cuc2VuZGVyKTsgfQp9Cgpjb250cmFjdCBFbWl0dGFibGUgaXMgT3duZWQgewogICAgZXZlbnQgRW1pdHRlZCgpOwoKICAgIGZ1bmN0aW9uIGVtaXRFdmVudCgpIHZpcnR1YWwgcHVibGljIHsKICAgICAgICBpZiAobXNnLnNlbmRlciA9PSBvd25lcikgewogICAgICAgICAgICBlbWl0IEVtaXR0ZWQoKTsKICAgICAgICB9CiAgICB9Cn0KCmNvbnRyYWN0IEJhc2UxIGlzIEVtaXR0YWJsZSB7CiAgICBldmVudCBCYXNlMUVtaXR0ZWQoKTsKICAgIGZ1bmN0aW9uIGVtaXRFdmVudCgpIHB1YmxpYyB2aXJ0dWFsIG92ZXJyaWRlIHsKICAgICAgICAvKiBIZXJlLCB3ZSBlbWl0IGFuIGV2ZW50IHRvIHNpbXVsYXRlIHNvbWUgQmFzZTEgbG9naWMgKi8KICAgICAgICBlbWl0IEJhc2UxRW1pdHRlZCgpOwogICAgICAgIEVtaXR0YWJsZS5lbWl0RXZlbnQoKTsKICAgIH0KfQoKY29udHJhY3QgQmFzZTIgaXMgRW1pdHRhYmxlIHsKICAgIGV2ZW50IEJhc2UyRW1pdHRlZCgpOwogICAgZnVuY3Rpb24gZW1pdEV2ZW50KCkgcHVibGljIHZpcnR1YWwgb3ZlcnJpZGUgewogICAgICAgIC8qIEhlcmUsIHdlIGVtaXQgYW4gZXZlbnQgdG8gc2ltdWxhdGUgc29tZSBCYXNlMiBsb2dpYyAqLwogICAgICAgIGVtaXQgQmFzZTJFbWl0dGVkKCk7CiAgICAgICAgRW1pdHRhYmxlLmVtaXRFdmVudCgpOwogICAgfQp9Cgpjb250cmFjdCBGaW5hbCBpcyBCYXNlMSwgQmFzZTIgewogICAgZXZlbnQgRmluYWxFbWl0dGVkKCk7CiAgICBmdW5jdGlvbiBlbWl0RXZlbnQoKSBwdWJsaWMgb3ZlcnJpZGUoQmFzZTEsIEJhc2UyKSB7CiAgICAgICAgLyogSGVyZSwgd2UgZW1pdCBhbiBldmVudCB0byBzaW11bGF0ZSBzb21lIEZpbmFsIGxvZ2ljICovCiAgICAgICAgZW1pdCBGaW5hbEVtaXR0ZWQoKTsKICAgICAgICBCYXNlMi5lbWl0RXZlbnQoKTsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Owned {
 address payable owner;
 constructor() { owner = payable(msg.sender); }
}

contract Emittable is Owned {
 event Emitted();

 function emitEvent() virtual public {
 if (msg.sender == owner) {
 emit Emitted();
 }
 }
}

contract Base1 is Emittable {
 event Base1Emitted();
 function emitEvent() public virtual override {
 /* Here, we emit an event to simulate some Base1 logic */
 emit Base1Emitted();
 Emittable.emitEvent();
 }
}

contract Base2 is Emittable {
 event Base2Emitted();
 function emitEvent() public virtual override {
 /* Here, we emit an event to simulate some Base2 logic */
 emit Base2Emitted();
 Emittable.emitEvent();
 }
}

contract Final is Base1, Base2 {
 event FinalEmitted();
 function emitEvent() public override(Base1, Base2) {
 /* Here, we emit an event to simulate some Final logic */
 emit FinalEmitted();
 Base2.emitEvent();
 }
}

A call to `Final.emitEvent()` will call `Base2.emitEvent` because we specify it explicitly in the final override, but this function will bypass `Base1.emitEvent`, resulting in the following sequence of events: `FinalEmitted -> Base2Emitted -> Emitted`, instead of the expected sequence: `FinalEmitted -> Base2Emitted -> Base1Emitted -> Emitted`. The way around this is to use `super`:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjAgPDAuOS4wOwoKY29udHJhY3QgT3duZWQgewogICAgYWRkcmVzcyBwYXlhYmxlIG93bmVyOwogICAgY29uc3RydWN0b3IoKSB7IG93bmVyID0gcGF5YWJsZShtc2cuc2VuZGVyKTsgfQp9Cgpjb250cmFjdCBFbWl0dGFibGUgaXMgT3duZWQgewogICAgZXZlbnQgRW1pdHRlZCgpOwoKICAgIGZ1bmN0aW9uIGVtaXRFdmVudCgpIHZpcnR1YWwgcHVibGljIHsKICAgICAgICBpZiAobXNnLnNlbmRlciA9PSBvd25lcikgewogICAgICAgICAgICBlbWl0IEVtaXR0ZWQoKTsKICAgICAgICB9CiAgICB9Cn0KCmNvbnRyYWN0IEJhc2UxIGlzIEVtaXR0YWJsZSB7CiAgICBldmVudCBCYXNlMUVtaXR0ZWQoKTsKICAgIGZ1bmN0aW9uIGVtaXRFdmVudCgpIHB1YmxpYyB2aXJ0dWFsIG92ZXJyaWRlIHsKICAgICAgICAvKiBIZXJlLCB3ZSBlbWl0IGFuIGV2ZW50IHRvIHNpbXVsYXRlIHNvbWUgQmFzZTEgbG9naWMgKi8KICAgICAgICBlbWl0IEJhc2UxRW1pdHRlZCgpOwogICAgICAgIHN1cGVyLmVtaXRFdmVudCgpOwogICAgfQp9CgoKY29udHJhY3QgQmFzZTIgaXMgRW1pdHRhYmxlIHsKICAgIGV2ZW50IEJhc2UyRW1pdHRlZCgpOwogICAgZnVuY3Rpb24gZW1pdEV2ZW50KCkgcHVibGljIHZpcnR1YWwgb3ZlcnJpZGUgewogICAgICAgIC8qIEhlcmUsIHdlIGVtaXQgYW4gZXZlbnQgdG8gc2ltdWxhdGUgc29tZSBCYXNlMiBsb2dpYyAqLwogICAgICAgIGVtaXQgQmFzZTJFbWl0dGVkKCk7CiAgICAgICAgc3VwZXIuZW1pdEV2ZW50KCk7CiAgICB9Cn0KCmNvbnRyYWN0IEZpbmFsIGlzIEJhc2UxLCBCYXNlMiB7CiAgICBldmVudCBGaW5hbEVtaXR0ZWQoKTsKICAgIGZ1bmN0aW9uIGVtaXRFdmVudCgpIHB1YmxpYyBvdmVycmlkZShCYXNlMSwgQmFzZTIpIHsKICAgICAgICAvKiBIZXJlLCB3ZSBlbWl0IGFuIGV2ZW50IHRvIHNpbXVsYXRlIHNvbWUgRmluYWwgbG9naWMgKi8KICAgICAgICBlbWl0IEZpbmFsRW1pdHRlZCgpOwogICAgICAgIHN1cGVyLmVtaXRFdmVudCgpOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Owned {
 address payable owner;
 constructor() { owner = payable(msg.sender); }
}

contract Emittable is Owned {
 event Emitted();

 function emitEvent() virtual public {
 if (msg.sender == owner) {
 emit Emitted();
 }
 }
}

contract Base1 is Emittable {
 event Base1Emitted();
 function emitEvent() public virtual override {
 /* Here, we emit an event to simulate some Base1 logic */
 emit Base1Emitted();
 super.emitEvent();
 }
}

contract Base2 is Emittable {
 event Base2Emitted();
 function emitEvent() public virtual override {
 /* Here, we emit an event to simulate some Base2 logic */
 emit Base2Emitted();
 super.emitEvent();
 }
}

contract Final is Base1, Base2 {
 event FinalEmitted();
 function emitEvent() public override(Base1, Base2) {
 /* Here, we emit an event to simulate some Final logic */
 emit FinalEmitted();
 super.emitEvent();
 }
}

If `Final` calls a function of `super`, it does not simply call this function on one of its base contracts. Rather, it calls this function on the next base contract in the final inheritance graph, so it will call `Base1.emitEvent()` (note that the final inheritance sequence is – starting with the most derived contract: Final, Base2, Base1, Emittable, Owned). The actual function that is called when using super is not known in the context of the class where it is used, although its type is known. This is similar for ordinary virtual method lookup.

### Function Overriding[](https://docs.soliditylang.org/en/latest/contracts.html#function-overriding "Link to this heading")

Base functions can be overridden by inheriting contracts to change their behavior if they are marked as `virtual`. The overriding function must then use the `override` keyword in the function header. The overriding function may only change the visibility of the overridden function from `external` to `public`. The mutability may be changed to a more strict one following the order: `nonpayable` can be overridden by `view` and `pure`. `view` can be overridden by `pure`. `payable` is an exception and cannot be changed to any other mutability.

The following example demonstrates changing mutability and visibility:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjAgPDAuOS4wOwoKY29udHJhY3QgQmFzZQp7CiAgICBmdW5jdGlvbiBmb28oKSB2aXJ0dWFsIGV4dGVybmFsIHZpZXcge30KfQoKY29udHJhY3QgTWlkZGxlIGlzIEJhc2Uge30KCmNvbnRyYWN0IEluaGVyaXRlZCBpcyBNaWRkbGUKewogICAgZnVuY3Rpb24gZm9vKCkgb3ZlcnJpZGUgcHVibGljIHB1cmUge30KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Base
{
 function foo() virtual external view {}
}

contract Middle is Base {}

contract Inherited is Middle
{
 function foo() override public pure {}
}

For multiple inheritance, the most derived base contracts that define the same function must be specified explicitly after the `override` keyword. In other words, you have to specify all base contracts that define the same function and have not yet been overridden by another base contract (on some path through the inheritance graph). Additionally, if a contract inherits the same function from multiple (unrelated) bases, it has to explicitly override it:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjAgPDAuOS4wOwoKY29udHJhY3QgQmFzZTEKewogICAgZnVuY3Rpb24gZm9vKCkgdmlydHVhbCBwdWJsaWMge30KfQoKY29udHJhY3QgQmFzZTIKewogICAgZnVuY3Rpb24gZm9vKCkgdmlydHVhbCBwdWJsaWMge30KfQoKY29udHJhY3QgSW5oZXJpdGVkIGlzIEJhc2UxLCBCYXNlMgp7CiAgICAvLyBEZXJpdmVzIGZyb20gbXVsdGlwbGUgYmFzZXMgZGVmaW5pbmcgZm9vKCksIHNvIHdlIG11c3QgZXhwbGljaXRseQogICAgLy8gb3ZlcnJpZGUgaXQKICAgIGZ1bmN0aW9uIGZvbygpIHB1YmxpYyBvdmVycmlkZShCYXNlMSwgQmFzZTIpIHt9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

contract Base1
{
 function foo() virtual public {}
}

contract Base2
{
 function foo() virtual public {}
}

contract Inherited is Base1, Base2
{
 // Derives from multiple bases defining foo(), so we must explicitly
 // override it
 function foo() public override(Base1, Base2) {}
}

An explicit override specifier is not required if the function is defined in a common base contract or if there is a unique function in a common base contract that already overrides all other functions.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjAgPDAuOS4wOwoKY29udHJhY3QgQSB7IGZ1bmN0aW9uIGYoKSBwdWJsaWMgcHVyZXt9IH0KY29udHJhY3QgQiBpcyBBIHt9CmNvbnRyYWN0IEMgaXMgQSB7fQovLyBObyBleHBsaWNpdCBvdmVycmlkZSByZXF1aXJlZApjb250cmFjdCBEIGlzIEIsIEMge30=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

contract A { function f() public pure{} }
contract B is A {}
contract C is A {}
// No explicit override required
contract D is B, C {}

More formally, it is not required to override a function (directly or indirectly) inherited from multiple bases if there is a base contract that is part of all override paths for the signature, and (1) that base implements the function and no paths from the current contract to the base mentions a function with that signature or (2) that base does not implement the function and there is at most one mention of the function in all paths from the current contract to that base.

In this sense, an override path for a signature is a path through the inheritance graph that starts at the contract under consideration and ends at a contract mentioning a function with that signature that does not override.

If you do not mark a function that overrides as `virtual`, derived contracts can no longer change the behavior of that function.

Note

Functions with the `private` visibility cannot be `virtual`.

Note

Functions without implementation have to be marked `virtual` outside of interfaces. In interfaces, all functions are automatically considered `virtual`.

Note

Starting from Solidity 0.8.8, the `override` keyword is not required when overriding an interface function, except for the case where the function is defined in multiple bases.

Public state variables can override external functions if the parameter and return types of the function matches the getter function of the variable:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjAgPDAuOS4wOwoKY29udHJhY3QgQQp7CiAgICBmdW5jdGlvbiBmKCkgZXh0ZXJuYWwgdmlldyB2aXJ0dWFsIHJldHVybnModWludCkgeyByZXR1cm4gNTsgfQp9Cgpjb250cmFjdCBCIGlzIEEKewogICAgdWludCBwdWJsaWMgb3ZlcnJpZGUgZjsKfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

contract A
{
 function f() external view virtual returns(uint) { return 5; }
}

contract B is A
{
 uint public override f;
}

Note

While public state variables can override external functions, they themselves cannot be overridden.

### Modifier Overriding[](https://docs.soliditylang.org/en/latest/contracts.html#modifier-overriding "Link to this heading")

Function modifiers can override each other. This works in the same way as [function overriding](https://docs.soliditylang.org/en/latest/contracts.html#function-overriding) (except that there is no overloading for modifiers). The `virtual` keyword must be used on the overridden modifier and the `override` keyword must be used in the overriding modifier:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjAgPDAuOS4wOwoKY29udHJhY3QgQmFzZQp7CiAgICBtb2RpZmllciBmb28oKSB2aXJ0dWFsIHtfO30KfQoKY29udHJhY3QgSW5oZXJpdGVkIGlzIEJhc2UKewogICAgbW9kaWZpZXIgZm9vKCkgb3ZlcnJpZGUge187fQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

contract Base
{
 modifier foo() virtual {_;}
}

contract Inherited is Base
{
 modifier foo() override {_;}
}

In case of multiple inheritance, all direct base contracts must be specified explicitly:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjAgPDAuOS4wOwoKY29udHJhY3QgQmFzZTEKewogICAgbW9kaWZpZXIgZm9vKCkgdmlydHVhbCB7Xzt9Cn0KCmNvbnRyYWN0IEJhc2UyCnsKICAgIG1vZGlmaWVyIGZvbygpIHZpcnR1YWwge187fQp9Cgpjb250cmFjdCBJbmhlcml0ZWQgaXMgQmFzZTEsIEJhc2UyCnsKICAgIG1vZGlmaWVyIGZvbygpIG92ZXJyaWRlKEJhc2UxLCBCYXNlMikge187fQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

contract Base1
{
 modifier foo() virtual {_;}
}

contract Base2
{
 modifier foo() virtual {_;}
}

contract Inherited is Base1, Base2
{
 modifier foo() override(Base1, Base2) {_;}
}

### Constructors[](https://docs.soliditylang.org/en/latest/contracts.html#constructors "Link to this heading")

A constructor is an optional function declared with the `constructor` keyword which is executed upon contract creation, and where you can run contract initialization code.

Before the constructor code is executed, state variables are initialised to their specified value if you initialise them inline, or their [default value](https://docs.soliditylang.org/en/latest/control-structures.html#default-value) if you do not.

After the constructor has run, the final code of the contract is deployed to the blockchain. The deployment of the code costs additional gas linear to the length of the code. This code includes all functions that are part of the public interface and all functions that are reachable from there through function calls. It does not include the constructor code or internal functions that are only called from the constructor.

If there is no constructor, the contract will assume the default constructor, which is equivalent to `constructor() {}`. For example:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjAgPDAuOS4wOwoKYWJzdHJhY3QgY29udHJhY3QgQSB7CiAgICB1aW50IHB1YmxpYyBhOwoKICAgIGNvbnN0cnVjdG9yKHVpbnQgYV8pIHsKICAgICAgICBhID0gYV87CiAgICB9Cn0KCmNvbnRyYWN0IEIgaXMgQSgxKSB7CiAgICBjb25zdHJ1Y3RvcigpIHt9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

abstract contract A {
 uint public a;

 constructor(uint a_) {
 a = a_;
 }
}

contract B is A(1) {
 constructor() {}
}

You can use internal parameters in a constructor (for example storage pointers). In this case, the contract has to be marked [abstract](https://docs.soliditylang.org/en/latest/contracts.html#abstract-contract), because these parameters cannot be assigned valid values from outside but only through the constructors of derived contracts.

Warning

Prior to version 0.4.22, constructors were defined as functions with the same name as the contract. This syntax was deprecated and is not allowed anymore in version 0.5.0.

Warning

Prior to version 0.7.0, you had to specify the visibility of constructors as either `internal` or `public`.

### Arguments for Base Constructors[](https://docs.soliditylang.org/en/latest/contracts.html#arguments-for-base-constructors "Link to this heading")

The constructors of all the base contracts will be called following the linearization rules explained below. If the base constructors have arguments, derived contracts need to specify all of them. This can be done in two ways:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjAgPDAuOS4wOwoKY29udHJhY3QgQmFzZSB7CiAgICB1aW50IHg7CiAgICBjb25zdHJ1Y3Rvcih1aW50IHhfKSB7IHggPSB4XzsgfQp9CgovLyBFaXRoZXIgZGlyZWN0bHkgc3BlY2lmeSBpbiB0aGUgaW5oZXJpdGFuY2UgbGlzdC4uLgpjb250cmFjdCBEZXJpdmVkMSBpcyBCYXNlKDcpIHsKICAgIGNvbnN0cnVjdG9yKCkge30KfQoKLy8gb3IgdGhyb3VnaCBhICJtb2RpZmllciIgb2YgdGhlIGRlcml2ZWQgY29uc3RydWN0b3IuLi4KY29udHJhY3QgRGVyaXZlZDIgaXMgQmFzZSB7CiAgICBjb25zdHJ1Y3Rvcih1aW50IHkpIEJhc2UoeSAqIHkpIHt9Cn0KCi8vIG9yIGRlY2xhcmUgYWJzdHJhY3QuLi4KYWJzdHJhY3QgY29udHJhY3QgRGVyaXZlZDMgaXMgQmFzZSB7Cn0KCi8vIGFuZCBoYXZlIHRoZSBuZXh0IGNvbmNyZXRlIGRlcml2ZWQgY29udHJhY3QgaW5pdGlhbGl6ZSBpdC4KY29udHJhY3QgRGVyaXZlZEZyb21EZXJpdmVkIGlzIERlcml2ZWQzIHsKICAgIGNvbnN0cnVjdG9yKCkgQmFzZSgxMCArIDEwKSB7fQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Base {
 uint x;
 constructor(uint x_) { x = x_; }
}

// Either directly specify in the inheritance list...
contract Derived1 is Base(7) {
 constructor() {}
}

// or through a "modifier" of the derived constructor...
contract Derived2 is Base {
 constructor(uint y) Base(y * y) {}
}

// or declare abstract...
abstract contract Derived3 is Base {
}

// and have the next concrete derived contract initialize it.
contract DerivedFromDerived is Derived3 {
 constructor() Base(10 + 10) {}
}

One way is directly in the inheritance list (`is Base(7)`). The other is in the way a modifier is invoked as part of the derived constructor (`Base(y * y)`). The first way to do it is more convenient if the constructor argument is a constant and defines the behavior of the contract or describes it. The second way has to be used if the constructor arguments of the base depend on those of the derived contract. Arguments have to be given either in the inheritance list or in modifier-style in the derived constructor. Specifying arguments in both places is an error.

If a derived contract does not specify the arguments to all of its base contracts’ constructors, it must be declared abstract. In that case, when another contract derives from it, that other contract’s inheritance list or constructor must provide the necessary parameters for all base classes that haven’t had their parameters specified (otherwise, that other contract must be declared abstract as well). For example, in the above code snippet, see `Derived3` and `DerivedFromDerived`.

### Multiple Inheritance and Linearization[](https://docs.soliditylang.org/en/latest/contracts.html#multiple-inheritance-and-linearization "Link to this heading")

Languages that allow multiple inheritance have to deal with several problems. One is the [Diamond Problem](https://en.wikipedia.org/wiki/Multiple_inheritance#The_diamond_problem). Solidity is similar to Python in that it uses C3 Linearization to force a specific order in the directed acyclic graph (DAG) of base classes. This results in the desirable property of monotonicity but disallows some inheritance graphs. Especially, the order in which the base classes are given in the `is` directive is important: You have to list the direct base contracts in the order from “most base-like” to “most derived”. Note that this order is the reverse of the one used in Python.

Another simplifying way to explain this is that when a function is called that is defined multiple times in different contracts, the given bases are searched from right to left (left to right in Python) in a depth-first manner, stopping at the first match. If a base contract has already been searched, it is skipped.

In the following code, Solidity will give the error “Linearization of inheritance graph impossible”.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjAgPDAuOS4wOwoKY29udHJhY3QgWCB7fQpjb250cmFjdCBBIGlzIFgge30KLy8gVGhpcyB3aWxsIG5vdCBjb21waWxlCmNvbnRyYWN0IEMgaXMgQSwgWCB7fQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.0 <0.9.0;

contract X {}
contract A is X {}
// This will not compile
contract C is A, X {}

The reason for this is that `C` requests `X` to override `A` (by specifying `A, X` in this order), but `A` itself requests to override `X`, which is a contradiction that cannot be resolved.

Due to the fact that you have to explicitly override a function that is inherited from multiple bases without a unique override, C3 linearization is not too important in practice.

One area where inheritance linearization is especially important and perhaps not as clear is when there are multiple constructors in the inheritance hierarchy. The constructors will always be executed in the linearized order, regardless of the order in which their arguments are provided in the inheriting contract’s constructor. For example:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjAgPDAuOS4wOwoKY29udHJhY3QgQmFzZTEgewogICAgY29uc3RydWN0b3IoKSB7fQp9Cgpjb250cmFjdCBCYXNlMiB7CiAgICBjb25zdHJ1Y3RvcigpIHt9Cn0KCi8vIENvbnN0cnVjdG9ycyBhcmUgZXhlY3V0ZWQgaW4gdGhlIGZvbGxvd2luZyBvcmRlcjoKLy8gIDEgLSBCYXNlMQovLyAgMiAtIEJhc2UyCi8vICAzIC0gRGVyaXZlZDEKY29udHJhY3QgRGVyaXZlZDEgaXMgQmFzZTEsIEJhc2UyIHsKICAgIGNvbnN0cnVjdG9yKCkgQmFzZTEoKSBCYXNlMigpIHt9Cn0KCi8vIENvbnN0cnVjdG9ycyBhcmUgZXhlY3V0ZWQgaW4gdGhlIGZvbGxvd2luZyBvcmRlcjoKLy8gIDEgLSBCYXNlMgovLyAgMiAtIEJhc2UxCi8vICAzIC0gRGVyaXZlZDIKY29udHJhY3QgRGVyaXZlZDIgaXMgQmFzZTIsIEJhc2UxIHsKICAgIGNvbnN0cnVjdG9yKCkgQmFzZTIoKSBCYXNlMSgpIHt9Cn0KCi8vIENvbnN0cnVjdG9ycyBhcmUgc3RpbGwgZXhlY3V0ZWQgaW4gdGhlIGZvbGxvd2luZyBvcmRlcjoKLy8gIDEgLSBCYXNlMgovLyAgMiAtIEJhc2UxCi8vICAzIC0gRGVyaXZlZDMKY29udHJhY3QgRGVyaXZlZDMgaXMgQmFzZTIsIEJhc2UxIHsKICAgIGNvbnN0cnVjdG9yKCkgQmFzZTEoKSBCYXNlMigpIHt9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Base1 {
 constructor() {}
}

contract Base2 {
 constructor() {}
}

// Constructors are executed in the following order:
// 1 - Base1
// 2 - Base2
// 3 - Derived1
contract Derived1 is Base1, Base2 {
 constructor() Base1() Base2() {}
}

// Constructors are executed in the following order:
// 1 - Base2
// 2 - Base1
// 3 - Derived2
contract Derived2 is Base2, Base1 {
 constructor() Base2() Base1() {}
}

// Constructors are still executed in the following order:
// 1 - Base2
// 2 - Base1
// 3 - Derived3
contract Derived3 is Base2, Base1 {
 constructor() Base1() Base2() {}
}

### Inheriting Different Kinds of Members of the Same Name[](https://docs.soliditylang.org/en/latest/contracts.html#inheriting-different-kinds-of-members-of-the-same-name "Link to this heading")

The only situations where, due to inheritance, a contract may contain multiple definitions sharing the same name are:

*   Overloading of functions.

*   Overriding of virtual functions.

*   Overriding of external virtual functions by state variable getters.

*   Overriding of virtual modifiers.

*   Overloading of events.

Abstract Contracts[](https://docs.soliditylang.org/en/latest/contracts.html#abstract-contracts "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Contracts must be marked as abstract when at least one of their functions is not implemented or when they do not provide arguments for all of their base contract constructors. Even if this is not the case, a contract may still be marked abstract, such as when you do not intend for the contract to be created directly. Abstract contracts are similar to [Interfaces](https://docs.soliditylang.org/en/latest/contracts.html#interfaces) but an interface is more limited in what it can declare.

An abstract contract is declared using the `abstract` keyword as shown in the following example. Note that this contract needs to be defined as abstract, because the function `utterance()` is declared, but no implementation was provided (no implementation body `{ }` was given).

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjAgPDAuOS4wOwoKYWJzdHJhY3QgY29udHJhY3QgRmVsaW5lIHsKICAgIGZ1bmN0aW9uIHV0dGVyYW5jZSgpIHB1YmxpYyB2aXJ0dWFsIHJldHVybnMgKGJ5dGVzMzIpOwp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

abstract contract Feline {
 function utterance() public virtual returns (bytes32);
}

Such abstract contracts can not be instantiated directly. This is also true, if an abstract contract itself does implement all defined functions. The usage of an abstract contract as a base class is shown in the following example:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjAgPDAuOS4wOwoKYWJzdHJhY3QgY29udHJhY3QgRmVsaW5lIHsKICAgIGZ1bmN0aW9uIHV0dGVyYW5jZSgpIHB1YmxpYyBwdXJlIHZpcnR1YWwgcmV0dXJucyAoYnl0ZXMzMik7Cn0KCmNvbnRyYWN0IENhdCBpcyBGZWxpbmUgewogICAgZnVuY3Rpb24gdXR0ZXJhbmNlKCkgcHVibGljIHB1cmUgb3ZlcnJpZGUgcmV0dXJucyAoYnl0ZXMzMikgeyByZXR1cm4gIm1pYW93IjsgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

abstract contract Feline {
 function utterance() public pure virtual returns (bytes32);
}

contract Cat is Feline {
 function utterance() public pure override returns (bytes32) { return "miaow"; }
}

If a contract inherits from an abstract contract and does not implement all non-implemented functions by overriding, it needs to be marked as abstract as well.

Note that a function without implementation is different from a [Function Type](https://docs.soliditylang.org/en/latest/types.html#function-types) even though their syntax looks very similar.

Example of function without implementation (a function declaration):

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=ZnVuY3Rpb24gZm9vKGFkZHJlc3MpIGV4dGVybmFsIHJldHVybnMgKGFkZHJlc3MpOw==)

function foo(address) external returns (address);

Example of a declaration of a variable whose type is a function type:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=ZnVuY3Rpb24oYWRkcmVzcykgZXh0ZXJuYWwgcmV0dXJucyAoYWRkcmVzcykgZm9vOw==)

function(address) external returns (address) foo;

Abstract contracts decouple the definition of a contract from its implementation providing better extensibility and self-documentation and facilitating patterns like the [Template method](https://en.wikipedia.org/wiki/Template_method_pattern) and removing code duplication. Abstract contracts are useful in the same way that defining methods in an interface is useful. It is a way for the designer of the abstract contract to say “any child of mine must implement this method”.

Note

Abstract contracts cannot override an implemented virtual function with an unimplemented one.

Interfaces[](https://docs.soliditylang.org/en/latest/contracts.html#interfaces "Link to this heading")
-------------------------------------------------------------------------------------------------------

Interfaces are similar to abstract contracts, but they cannot have any functions implemented. There are further restrictions:

*   They cannot inherit from other contracts, but they can inherit from other interfaces.

*   All declared functions must be external in the interface, even if they are public in the contract.

*   They cannot declare a constructor.

*   They cannot declare state variables.

*   They cannot declare modifiers.

Some of these restrictions might be lifted in the future.

Interfaces are basically limited to what the Contract ABI can represent, and the conversion between the ABI and an interface should be possible without any information loss.

Interfaces are denoted by their own keyword:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjIgPDAuOS4wOwoKaW50ZXJmYWNlIFRva2VuIHsKICAgIGVudW0gVG9rZW5UeXBlIHsgRnVuZ2libGUsIE5vbkZ1bmdpYmxlIH0KICAgIHN0cnVjdCBDb2luIHsgc3RyaW5nIG9idmVyc2U7IHN0cmluZyByZXZlcnNlOyB9CiAgICBmdW5jdGlvbiB0cmFuc2ZlcihhZGRyZXNzIHJlY2lwaWVudCwgdWludCBhbW91bnQpIGV4dGVybmFsOwp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.2 <0.9.0;

interface Token {
 enum TokenType { Fungible, NonFungible }
 struct Coin { string obverse; string reverse; }
 function transfer(address recipient, uint amount) external;
}

Contracts can inherit interfaces as they would inherit other contracts.

All functions declared in interfaces are implicitly `virtual` and any functions that override them do not need the `override` keyword. This does not automatically mean that an overriding function can be overridden again - this is only possible if the overriding function is marked `virtual`.

Interfaces can inherit from other interfaces. This has the same rules as normal inheritance.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjIgPDAuOS4wOwoKaW50ZXJmYWNlIFBhcmVudEEgewogICAgZnVuY3Rpb24gdGVzdCgpIGV4dGVybmFsIHJldHVybnMgKHVpbnQyNTYpOwp9CgppbnRlcmZhY2UgUGFyZW50QiB7CiAgICBmdW5jdGlvbiB0ZXN0KCkgZXh0ZXJuYWwgcmV0dXJucyAodWludDI1Nik7Cn0KCmludGVyZmFjZSBTdWJJbnRlcmZhY2UgaXMgUGFyZW50QSwgUGFyZW50QiB7CiAgICAvLyBNdXN0IHJlZGVmaW5lIHRlc3QgaW4gb3JkZXIgdG8gYXNzZXJ0IHRoYXQgdGhlIHBhcmVudAogICAgLy8gbWVhbmluZ3MgYXJlIGNvbXBhdGlibGUuCiAgICBmdW5jdGlvbiB0ZXN0KCkgZXh0ZXJuYWwgb3ZlcnJpZGUoUGFyZW50QSwgUGFyZW50QikgcmV0dXJucyAodWludDI1Nik7Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.2 <0.9.0;

interface ParentA {
 function test() external returns (uint256);
}

interface ParentB {
 function test() external returns (uint256);
}

interface SubInterface is ParentA, ParentB {
 // Must redefine test in order to assert that the parent
 // meanings are compatible.
 function test() external override(ParentA, ParentB) returns (uint256);
}

Types defined inside interfaces and other contract-like structures can be accessed from other contracts: `Token.TokenType` or `Token.Coin`.

Warning

Interfaces have supported `enum` types since [Solidity version 0.5.0](https://docs.soliditylang.org/en/latest/050-breaking-changes.html), make sure the pragma version specifies this version as a minimum.

Libraries[](https://docs.soliditylang.org/en/latest/contracts.html#libraries "Link to this heading")
-----------------------------------------------------------------------------------------------------

Libraries are similar to contracts, but their purpose is that they are deployed only once at a specific address and their code is reused using the `DELEGATECALL` (`CALLCODE` until Homestead) feature of the EVM. This means that if library functions are called, their code is executed in the context of the calling contract, i.e. `this` points to the calling contract, and especially the storage from the calling contract can be accessed. As a library is an isolated piece of source code, it can only access state variables of the calling contract if they are explicitly supplied (it would have no way to name them, otherwise). Library functions can only be called directly (i.e. without the use of `DELEGATECALL`) if they do not modify the state (i.e. if they are `view` or `pure` functions), because libraries are assumed to be stateless. In particular, it is not possible to destroy a library.

Note

Until version 0.4.20, it was possible to destroy libraries by circumventing Solidity’s type system. Starting from that version, libraries contain a [mechanism](https://docs.soliditylang.org/en/latest/contracts.html#call-protection) that disallows state-modifying functions to be called directly (i.e. without `DELEGATECALL`).

Libraries can be seen as implicit base contracts of the contracts that use them. They will not be explicitly visible in the inheritance hierarchy, but calls to library functions look just like calls to functions of explicit base contracts (using qualified access like `L.f()`). Of course, calls to internal functions use the internal calling convention, which means that all internal types can be passed and types [stored in memory](https://docs.soliditylang.org/en/latest/types.html#data-location) will be passed by reference and not copied. To realize this in the EVM, the code of internal library functions that are called from a contract and all functions called from therein will at compile time be included in the calling contract, and a regular `JUMP` call will be used instead of a `DELEGATECALL`.

Note

The inheritance analogy breaks down when it comes to public functions. Calling a public library function with `L.f()` results in an external call (`DELEGATECALL` to be precise). In contrast, `A.f()` is an internal call when `A` is a base contract of the current contract.

The following example illustrates how to use libraries (but using a manual method, be sure to check out [using for](https://docs.soliditylang.org/en/latest/contracts.html#using-for) for a more advanced example to implement a set).

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC42LjAgPDAuOS4wOwoKCi8vIFdlIGRlZmluZSBhIG5ldyBzdHJ1Y3QgZGF0YXR5cGUgdGhhdCB3aWxsIGJlIHVzZWQgdG8KLy8gaG9sZCBpdHMgZGF0YSBpbiB0aGUgY2FsbGluZyBjb250cmFjdC4Kc3RydWN0IERhdGEgewogICAgbWFwcGluZyh1aW50ID0+IGJvb2wpIGZsYWdzOwp9CgpsaWJyYXJ5IFNldCB7CiAgICAvLyBOb3RlIHRoYXQgdGhlIGZpcnN0IHBhcmFtZXRlciBpcyBvZiB0eXBlICJzdG9yYWdlCiAgICAvLyByZWZlcmVuY2UiIGFuZCB0aHVzIG9ubHkgaXRzIHN0b3JhZ2UgYWRkcmVzcyBhbmQgbm90CiAgICAvLyBpdHMgY29udGVudHMgaXMgcGFzc2VkIGFzIHBhcnQgb2YgdGhlIGNhbGwuICBUaGlzIGlzIGEKICAgIC8vIHNwZWNpYWwgZmVhdHVyZSBvZiBsaWJyYXJ5IGZ1bmN0aW9ucy4gIEl0IGlzIGlkaW9tYXRpYwogICAgLy8gdG8gY2FsbCB0aGUgZmlyc3QgcGFyYW1ldGVyIGBzZWxmYCwgaWYgdGhlIGZ1bmN0aW9uIGNhbgogICAgLy8gYmUgc2VlbiBhcyBhIG1ldGhvZCBvZiB0aGF0IG9iamVjdC4KICAgIGZ1bmN0aW9uIGluc2VydChEYXRhIHN0b3JhZ2Ugc2VsZiwgdWludCB2YWx1ZSkKICAgICAgICBwdWJsaWMKICAgICAgICByZXR1cm5zIChib29sKQogICAgewogICAgICAgIGlmIChzZWxmLmZsYWdzW3ZhbHVlXSkKICAgICAgICAgICAgcmV0dXJuIGZhbHNlOyAvLyBhbHJlYWR5IHRoZXJlCiAgICAgICAgc2VsZi5mbGFnc1t2YWx1ZV0gPSB0cnVlOwogICAgICAgIHJldHVybiB0cnVlOwogICAgfQoKICAgIGZ1bmN0aW9uIHJlbW92ZShEYXRhIHN0b3JhZ2Ugc2VsZiwgdWludCB2YWx1ZSkKICAgICAgICBwdWJsaWMKICAgICAgICByZXR1cm5zIChib29sKQogICAgewogICAgICAgIGlmICghc2VsZi5mbGFnc1t2YWx1ZV0pCiAgICAgICAgICAgIHJldHVybiBmYWxzZTsgLy8gbm90IHRoZXJlCiAgICAgICAgc2VsZi5mbGFnc1t2YWx1ZV0gPSBmYWxzZTsKICAgICAgICByZXR1cm4gdHJ1ZTsKICAgIH0KCiAgICBmdW5jdGlvbiBjb250YWlucyhEYXRhIHN0b3JhZ2Ugc2VsZiwgdWludCB2YWx1ZSkKICAgICAgICBwdWJsaWMKICAgICAgICB2aWV3CiAgICAgICAgcmV0dXJucyAoYm9vbCkKICAgIHsKICAgICAgICByZXR1cm4gc2VsZi5mbGFnc1t2YWx1ZV07CiAgICB9Cn0KCgpjb250cmFjdCBDIHsKICAgIERhdGEga25vd25WYWx1ZXM7CgogICAgZnVuY3Rpb24gcmVnaXN0ZXIodWludCB2YWx1ZSkgcHVibGljIHsKICAgICAgICAvLyBUaGUgbGlicmFyeSBmdW5jdGlvbnMgY2FuIGJlIGNhbGxlZCB3aXRob3V0IGEKICAgICAgICAvLyBzcGVjaWZpYyBpbnN0YW5jZSBvZiB0aGUgbGlicmFyeSwgc2luY2UgdGhlCiAgICAgICAgLy8gImluc3RhbmNlIiB3aWxsIGJlIHRoZSBjdXJyZW50IGNvbnRyYWN0LgogICAgICAgIHJlcXVpcmUoU2V0Lmluc2VydChrbm93blZhbHVlcywgdmFsdWUpKTsKICAgIH0KICAgIC8vIEluIHRoaXMgY29udHJhY3QsIHdlIGNhbiBhbHNvIGRpcmVjdGx5IGFjY2VzcyBrbm93blZhbHVlcy5mbGFncywgaWYgd2Ugd2FudC4KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.6.0 <0.9.0;

// We define a new struct datatype that will be used to
// hold its data in the calling contract.
struct Data {
 mapping(uint => bool) flags;
}

library Set {
 // Note that the first parameter is of type "storage
 // reference" and thus only its storage address and not
 // its contents is passed as part of the call. This is a
 // special feature of library functions. It is idiomatic
 // to call the first parameter `self`, if the function can
 // be seen as a method of that object.
 function insert(Data storage self, uint value)
 public
 returns (bool)
 {
 if (self.flags[value])
 return false; // already there
 self.flags[value] = true;
 return true;
 }

 function remove(Data storage self, uint value)
 public
 returns (bool)
 {
 if (!self.flags[value])
 return false; // not there
 self.flags[value] = false;
 return true;
 }

 function contains(Data storage self, uint value)
 public
 view
 returns (bool)
 {
 return self.flags[value];
 }
}

contract C {
 Data knownValues;

 function register(uint value) public {
 // The library functions can be called without a
 // specific instance of the library, since the
 // "instance" will be the current contract.
 require(Set.insert(knownValues, value));
 }
 // In this contract, we can also directly access knownValues.flags, if we want.
}

Of course, you do not have to follow this way to use libraries: they can also be used without defining struct data types. Functions also work without any storage reference parameters, and they can have multiple storage reference parameters and in any position.

The calls to `Set.contains`, `Set.insert` and `Set.remove` are all compiled as calls (`DELEGATECALL`) to an external contract/library. If you use libraries, be aware that an actual external function call is performed. `msg.sender`, `msg.value` and `this` will retain their values in this call, though (prior to Homestead, because of the use of `CALLCODE`, `msg.sender` and `msg.value` changed, though).

The following example shows how to use [types stored in memory](https://docs.soliditylang.org/en/latest/types.html#data-location) and internal functions in libraries in order to implement custom types without the overhead of external function calls:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguMDsKCnN0cnVjdCBiaWdpbnQgewogICAgdWludFtdIGxpbWJzOwp9CgpsaWJyYXJ5IEJpZ0ludCB7CiAgICBmdW5jdGlvbiBmcm9tVWludCh1aW50IHgpIGludGVybmFsIHB1cmUgcmV0dXJucyAoYmlnaW50IG1lbW9yeSByKSB7CiAgICAgICAgci5saW1icyA9IG5ldyB1aW50W10oMSk7CiAgICAgICAgci5saW1ic1swXSA9IHg7CiAgICB9CgogICAgZnVuY3Rpb24gYWRkKGJpZ2ludCBtZW1vcnkgYSwgYmlnaW50IG1lbW9yeSBiKSBpbnRlcm5hbCBwdXJlIHJldHVybnMgKGJpZ2ludCBtZW1vcnkgcikgewogICAgICAgIHIubGltYnMgPSBuZXcgdWludFtdKG1heChhLmxpbWJzLmxlbmd0aCwgYi5saW1icy5sZW5ndGgpKTsKICAgICAgICB1aW50IGNhcnJ5ID0gMDsKICAgICAgICBmb3IgKHVpbnQgaSA9IDA7IGkgPCByLmxpbWJzLmxlbmd0aDsgKytpKSB7CiAgICAgICAgICAgIHVpbnQgbGltYkEgPSBsaW1iKGEsIGkpOwogICAgICAgICAgICB1aW50IGxpbWJCID0gbGltYihiLCBpKTsKICAgICAgICAgICAgdW5jaGVja2VkIHsKICAgICAgICAgICAgICAgIHIubGltYnNbaV0gPSBsaW1iQSArIGxpbWJCICsgY2Fycnk7CgogICAgICAgICAgICAgICAgaWYgKGxpbWJBICsgbGltYkIgPCBsaW1iQSB8fCAobGltYkEgKyBsaW1iQiA9PSB0eXBlKHVpbnQpLm1heCAmJiBjYXJyeSA+IDApKQogICAgICAgICAgICAgICAgICAgIGNhcnJ5ID0gMTsKICAgICAgICAgICAgICAgIGVsc2UKICAgICAgICAgICAgICAgICAgICBjYXJyeSA9IDA7CiAgICAgICAgICAgIH0KICAgICAgICB9CiAgICAgICAgaWYgKGNhcnJ5ID4gMCkgewogICAgICAgICAgICAvLyB0b28gYmFkLCB3ZSBoYXZlIHRvIGFkZCBhIGxpbWIKICAgICAgICAgICAgdWludFtdIG1lbW9yeSBuZXdMaW1icyA9IG5ldyB1aW50W10oci5saW1icy5sZW5ndGggKyAxKTsKICAgICAgICAgICAgdWludCBpOwogICAgICAgICAgICBmb3IgKGkgPSAwOyBpIDwgci5saW1icy5sZW5ndGg7ICsraSkKICAgICAgICAgICAgICAgIG5ld0xpbWJzW2ldID0gci5saW1ic1tpXTsKICAgICAgICAgICAgbmV3TGltYnNbaV0gPSBjYXJyeTsKICAgICAgICAgICAgci5saW1icyA9IG5ld0xpbWJzOwogICAgICAgIH0KICAgIH0KCiAgICBmdW5jdGlvbiBsaW1iKGJpZ2ludCBtZW1vcnkgYSwgdWludCBpbmRleCkgaW50ZXJuYWwgcHVyZSByZXR1cm5zICh1aW50KSB7CiAgICAgICAgcmV0dXJuIGluZGV4IDwgYS5saW1icy5sZW5ndGggPyBhLmxpbWJzW2luZGV4XSA6IDA7CiAgICB9CgogICAgZnVuY3Rpb24gbWF4KHVpbnQgYSwgdWludCBiKSBwcml2YXRlIHB1cmUgcmV0dXJucyAodWludCkgewogICAgICAgIHJldHVybiBhID4gYiA/IGEgOiBiOwogICAgfQp9Cgpjb250cmFjdCBDIHsKICAgIHVzaW5nIEJpZ0ludCBmb3IgYmlnaW50OwoKICAgIGZ1bmN0aW9uIGYoKSBwdWJsaWMgcHVyZSB7CiAgICAgICAgYmlnaW50IG1lbW9yeSB4ID0gQmlnSW50LmZyb21VaW50KDcpOwogICAgICAgIGJpZ2ludCBtZW1vcnkgeSA9IEJpZ0ludC5mcm9tVWludCh0eXBlKHVpbnQpLm1heCk7CiAgICAgICAgYmlnaW50IG1lbW9yeSB6ID0geC5hZGQoeSk7CiAgICAgICAgYXNzZXJ0KHoubGltYigxKSA+IDApOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

struct bigint {
 uint[] limbs;
}

library BigInt {
 function fromUint(uint x) internal pure returns (bigint memory r) {
 r.limbs = new uint[](1);
 r.limbs[0] = x;
 }

 function add(bigint memory a, bigint memory b) internal pure returns (bigint memory r) {
 r.limbs = new uint[](max(a.limbs.length, b.limbs.length));
 uint carry = 0;
 for (uint i = 0; i < r.limbs.length; ++i) {
 uint limbA = limb(a, i);
 uint limbB = limb(b, i);
 unchecked {
 r.limbs[i] = limbA + limbB + carry;

 if (limbA + limbB < limbA || (limbA + limbB == type(uint).max && carry > 0))
 carry = 1;
 else
 carry = 0;
 }
 }
 if (carry > 0) {
 // too bad, we have to add a limb
 uint[] memory newLimbs = new uint[](r.limbs.length + 1);
 uint i;
 for (i = 0; i < r.limbs.length; ++i)
 newLimbs[i] = r.limbs[i];
 newLimbs[i] = carry;
 r.limbs = newLimbs;
 }
 }

 function limb(bigint memory a, uint index) internal pure returns (uint) {
 return index < a.limbs.length ? a.limbs[index] : 0;
 }

 function max(uint a, uint b) private pure returns (uint) {
 return a > b ? a : b;
 }
}

contract C {
 using BigInt for bigint;

 function f() public pure {
 bigint memory x = BigInt.fromUint(7);
 bigint memory y = BigInt.fromUint(type(uint).max);
 bigint memory z = x.add(y);
 assert(z.limb(1) > 0);
 }
}

It is possible to obtain the address of a library by converting the library type to the `address` type, i.e. using `address(LibraryName)`.

As the compiler does not know the address where the library will be deployed, the compiled hex code will contain placeholders of the form `__$30bbc0abd4d6364515865950d3e0d10953$__`[(format was different <v0.5.0)](https://docs.soliditylang.org/en/v0.4.26/contracts.html#libraries). The placeholder is a 34 character prefix of the hex encoding of the keccak256 hash of the fully qualified library name, which would be for example `libraries/bigint.sol:BigInt` if the library was stored in a file called `bigint.sol` in a `libraries/` directory. Such bytecode is incomplete and should not be deployed. Placeholders need to be replaced with actual addresses. You can do that by either passing them to the compiler when the library is being compiled or by using the linker to update an already compiled binary. See [Library Linking](https://docs.soliditylang.org/en/latest/using-the-compiler.html#library-linking) for information on how to use the commandline compiler for linking.

In comparison to contracts, libraries are restricted in the following ways:

*   they cannot have state variables

*   they cannot inherit nor be inherited

*   they cannot receive Ether

*   they cannot be destroyed

(These might be lifted at a later point.)

### Function Signatures and Selectors in Libraries[](https://docs.soliditylang.org/en/latest/contracts.html#function-signatures-and-selectors-in-libraries "Link to this heading")

While external calls to public or external library functions are possible, the calling convention for such calls is considered to be internal to Solidity and not the same as specified for the regular [contract ABI](https://docs.soliditylang.org/en/latest/abi-spec.html#abi). External library functions support more argument types than external contract functions, for example recursive structs and storage pointers. For that reason, the function signatures used to compute the 4-byte selector are computed following an internal naming schema and arguments of types not supported in the contract ABI use an internal encoding.

The following identifiers are used for the types in the signatures:

*   Value types, non-storage `string` and non-storage `bytes` use the same identifiers as in the contract ABI.

*   Non-storage array types follow the same convention as in the contract ABI, i.e. `<type>[]` for dynamic arrays and `<type>[M]` for fixed-size arrays of `M` elements.

*   Non-storage structs are referred to by their fully qualified name, i.e. `C.S` for `contract C { struct S { ... } }`.

*   Storage pointer mappings use `mapping(<keyType> => <valueType>) storage` where `<keyType>` and `<valueType>` are the identifiers for the key and value types of the mapping, respectively.

*   Other storage pointer types use the type identifier of their corresponding non-storage type, but append a single space followed by `storage` to it.

The argument encoding is the same as for the regular contract ABI, except for storage pointers, which are encoded as a `uint256` value referring to the storage slot to which they point.

Similarly to the contract ABI, the selector consists of the first four bytes of the Keccak256-hash of the signature. Its value can be obtained from Solidity using the `.selector` member as follows:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC41LjE0IDwwLjkuMDsKCmxpYnJhcnkgTCB7CiAgICBmdW5jdGlvbiBmKHVpbnQyNTYpIGV4dGVybmFsIHt9Cn0KCmNvbnRyYWN0IEMgewogICAgZnVuY3Rpb24gZygpIHB1YmxpYyBwdXJlIHJldHVybnMgKGJ5dGVzNCkgewogICAgICAgIHJldHVybiBMLmYuc2VsZWN0b3I7CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.5.14 <0.9.0;

library L {
 function f(uint256) external {}
}

contract C {
 function g() public pure returns (bytes4) {
 return L.f.selector;
 }
}

### Call Protection For Libraries[](https://docs.soliditylang.org/en/latest/contracts.html#call-protection-for-libraries "Link to this heading")

As mentioned in the introduction, if a library’s code is executed using a `CALL` instead of a `DELEGATECALL` or `CALLCODE`, it will revert unless a `view` or `pure` function is called.

The EVM does not provide a direct way for a contract to detect whether it was called using `CALL` or not, but a contract can use the `ADDRESS` opcode to find out “where” it is currently running. The generated code compares this address to the address used at construction time to determine the mode of calling.

More specifically, the runtime code of a library always starts with a push instruction, which is a zero of 20 bytes at compilation time. When the deploy code runs, this constant is replaced in memory by the current address and this modified code is stored in the contract. At runtime, this causes the deploy time address to be the first constant to be pushed onto the stack and the dispatcher code compares the current address against this constant for any non-view and non-pure function.

This means that the actual code stored on chain for a library is different from the code reported by the compiler as `deployedBytecode`.

Using For[](https://docs.soliditylang.org/en/latest/contracts.html#using-for "Link to this heading")
-----------------------------------------------------------------------------------------------------

The directive `using A for B` can be used to attach functions (`A`) as operators to user-defined value types or as member functions to any type (`B`). The member functions receive the object they are called on as their first parameter (like the `self` variable in Python). The operator functions receive operands as parameters.

It is valid either at file level or inside a contract, at contract level.

The first part, `A`, can be one of:

*   A list of functions, optionally with an operator name assigned (e.g. `using {f, g as +, h, L.t} for uint`). If no operator is specified, the function can be either a library function or a free function and is attached to the type as a member function. Otherwise it must be a free function and it becomes the definition of that operator on the type.

*   The name of a library (e.g. `using L for uint`) - all non-private functions of the library are attached to the type as member functions

At file level, the second part, `B`, has to be an explicit type (without data location specifier). Inside contracts, you can also use `*` in place of the type (e.g. `using L for *;`), which has the effect that all functions of the library `L` are attached to _all_ types.

If you specify a library, _all_ non-private functions in the library get attached, even those where the type of the first parameter does not match the type of the object. The type is checked at the point the function is called and function overload resolution is performed.

If you use a list of functions (e.g. `using {f, g, h, L.t} for uint`), then the type (`uint`) has to be implicitly convertible to the first parameter of each of these functions. This check is performed even if none of these functions are called. Note that private library functions can only be specified when `using for` is inside a library.

If you define an operator (e.g. `using {f as +} for T`), then the type (`T`) must be a [user-defined value type](https://docs.soliditylang.org/en/latest/types.html#user-defined-value-types) and the definition must be a `pure` function. Operator definitions must be global. The following operators can be defined this way:

| Category | Operator | Possible signatures |
| --- | --- | --- |
| Bitwise | `&` | `function (T, T) pure returns (T)` |
| `|` | `function (T, T) pure returns (T)` |
| `^` | `function (T, T) pure returns (T)` |
| `~` | `function (T) pure returns (T)` |
| Arithmetic | `+` | `function (T, T) pure returns (T)` |
| `-` | `function (T, T) pure returns (T)` |
| `function (T) pure returns (T)` |
| `*` | `function (T, T) pure returns (T)` |
| `/` | `function (T, T) pure returns (T)` |
| `%` | `function (T, T) pure returns (T)` |
| Comparison | `==` | `function (T, T) pure returns (bool)` |
| `!=` | `function (T, T) pure returns (bool)` |
| `<` | `function (T, T) pure returns (bool)` |
| `<=` | `function (T, T) pure returns (bool)` |
| `>` | `function (T, T) pure returns (bool)` |
| `>=` | `function (T, T) pure returns (bool)` |

Note that unary and binary `-` need separate definitions. The compiler will choose the right definition based on how the operator is invoked.

The `using A for B;` directive is active only within the current scope (either the contract or the current module/source unit), including within all of its functions, and has no effect outside of the contract or module in which it is used.

When the directive is used at file level and applied to a user-defined type which was defined at file level in the same file, the word `global` can be added at the end. This will have the effect that the functions and operators are attached to the type everywhere the type is available (including other files), not only in the scope of the using statement.

Let us rewrite the set example from the [Libraries](https://docs.soliditylang.org/en/latest/contracts.html#libraries) section in this way, using file-level functions instead of library functions.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguMTM7CgpzdHJ1Y3QgRGF0YSB7IG1hcHBpbmcodWludCA9PiBib29sKSBmbGFnczsgfQovLyBOb3cgd2UgYXR0YWNoIGZ1bmN0aW9ucyB0byB0aGUgdHlwZS4KLy8gVGhlIGF0dGFjaGVkIGZ1bmN0aW9ucyBjYW4gYmUgdXNlZCB0aHJvdWdob3V0IHRoZSByZXN0IG9mIHRoZSBtb2R1bGUuCi8vIElmIHlvdSBpbXBvcnQgdGhlIG1vZHVsZSwgeW91IGhhdmUgdG8KLy8gcmVwZWF0IHRoZSB1c2luZyBkaXJlY3RpdmUgdGhlcmUsIGZvciBleGFtcGxlIGFzCi8vICAgaW1wb3J0ICJmbGFncy5zb2wiIGFzIEZsYWdzOwovLyAgIHVzaW5nIHtGbGFncy5pbnNlcnQsIEZsYWdzLnJlbW92ZSwgRmxhZ3MuY29udGFpbnN9Ci8vICAgICBmb3IgRmxhZ3MuRGF0YTsKdXNpbmcge2luc2VydCwgcmVtb3ZlLCBjb250YWluc30gZm9yIERhdGE7CgpmdW5jdGlvbiBpbnNlcnQoRGF0YSBzdG9yYWdlIHNlbGYsIHVpbnQgdmFsdWUpCiAgICByZXR1cm5zIChib29sKQp7CiAgICBpZiAoc2VsZi5mbGFnc1t2YWx1ZV0pCiAgICAgICAgcmV0dXJuIGZhbHNlOyAvLyBhbHJlYWR5IHRoZXJlCiAgICBzZWxmLmZsYWdzW3ZhbHVlXSA9IHRydWU7CiAgICByZXR1cm4gdHJ1ZTsKfQoKZnVuY3Rpb24gcmVtb3ZlKERhdGEgc3RvcmFnZSBzZWxmLCB1aW50IHZhbHVlKQogICAgcmV0dXJucyAoYm9vbCkKewogICAgaWYgKCFzZWxmLmZsYWdzW3ZhbHVlXSkKICAgICAgICByZXR1cm4gZmFsc2U7IC8vIG5vdCB0aGVyZQogICAgc2VsZi5mbGFnc1t2YWx1ZV0gPSBmYWxzZTsKICAgIHJldHVybiB0cnVlOwp9CgpmdW5jdGlvbiBjb250YWlucyhEYXRhIHN0b3JhZ2Ugc2VsZiwgdWludCB2YWx1ZSkKICAgIHZpZXcKICAgIHJldHVybnMgKGJvb2wpCnsKICAgIHJldHVybiBzZWxmLmZsYWdzW3ZhbHVlXTsKfQoKCmNvbnRyYWN0IEMgewogICAgRGF0YSBrbm93blZhbHVlczsKCiAgICBmdW5jdGlvbiByZWdpc3Rlcih1aW50IHZhbHVlKSBwdWJsaWMgewogICAgICAgIC8vIEhlcmUsIGFsbCB2YXJpYWJsZXMgb2YgdHlwZSBEYXRhIGhhdmUKICAgICAgICAvLyBjb3JyZXNwb25kaW5nIG1lbWJlciBmdW5jdGlvbnMuCiAgICAgICAgLy8gVGhlIGZvbGxvd2luZyBmdW5jdGlvbiBjYWxsIGlzIGlkZW50aWNhbCB0bwogICAgICAgIC8vIGBTZXQuaW5zZXJ0KGtub3duVmFsdWVzLCB2YWx1ZSlgCiAgICAgICAgcmVxdWlyZShrbm93blZhbHVlcy5pbnNlcnQodmFsdWUpKTsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.13;

struct Data { mapping(uint => bool) flags; }
// Now we attach functions to the type.
// The attached functions can be used throughout the rest of the module.
// If you import the module, you have to
// repeat the using directive there, for example as
// import "flags.sol" as Flags;
// using {Flags.insert, Flags.remove, Flags.contains}
// for Flags.Data;
using {insert, remove, contains} for Data;

function insert(Data storage self, uint value)
 returns (bool)
{
 if (self.flags[value])
 return false; // already there
 self.flags[value] = true;
 return true;
}

function remove(Data storage self, uint value)
 returns (bool)
{
 if (!self.flags[value])
 return false; // not there
 self.flags[value] = false;
 return true;
}

function contains(Data storage self, uint value)
 view
 returns (bool)
{
 return self.flags[value];
}

contract C {
 Data knownValues;

 function register(uint value) public {
 // Here, all variables of type Data have
 // corresponding member functions.
 // The following function call is identical to
 // `Set.insert(knownValues, value)`
 require(knownValues.insert(value));
 }
}

It is also possible to extend built-in types in that way. In this example, we will use a library.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguMTM7CgpsaWJyYXJ5IFNlYXJjaCB7CiAgICBmdW5jdGlvbiBpbmRleE9mKHVpbnRbXSBzdG9yYWdlIHNlbGYsIHVpbnQgdmFsdWUpCiAgICAgICAgcHVibGljCiAgICAgICAgdmlldwogICAgICAgIHJldHVybnMgKHVpbnQpCiAgICB7CiAgICAgICAgZm9yICh1aW50IGkgPSAwOyBpIDwgc2VsZi5sZW5ndGg7IGkrKykKICAgICAgICAgICAgaWYgKHNlbGZbaV0gPT0gdmFsdWUpIHJldHVybiBpOwogICAgICAgIHJldHVybiB0eXBlKHVpbnQpLm1heDsKICAgIH0KfQp1c2luZyBTZWFyY2ggZm9yIHVpbnRbXTsKCmNvbnRyYWN0IEMgewogICAgdWludFtdIGRhdGE7CgogICAgZnVuY3Rpb24gYXBwZW5kKHVpbnQgdmFsdWUpIHB1YmxpYyB7CiAgICAgICAgZGF0YS5wdXNoKHZhbHVlKTsKICAgIH0KCiAgICBmdW5jdGlvbiByZXBsYWNlKHVpbnQgZnJvbSwgdWludCB0bykgcHVibGljIHsKICAgICAgICAvLyBUaGlzIHBlcmZvcm1zIHRoZSBsaWJyYXJ5IGZ1bmN0aW9uIGNhbGwKICAgICAgICB1aW50IGluZGV4ID0gZGF0YS5pbmRleE9mKGZyb20pOwogICAgICAgIGlmIChpbmRleCA9PSB0eXBlKHVpbnQpLm1heCkKICAgICAgICAgICAgZGF0YS5wdXNoKHRvKTsKICAgICAgICBlbHNlCiAgICAgICAgICAgIGRhdGFbaW5kZXhdID0gdG87CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.13;

library Search {
 function indexOf(uint[] storage self, uint value)
 public
 view
 returns (uint)
 {
 for (uint i = 0; i < self.length; i++)
 if (self[i] == value) return i;
 return type(uint).max;
 }
}
using Search for uint[];

contract C {
 uint[] data;

 function append(uint value) public {
 data.push(value);
 }

 function replace(uint from, uint to) public {
 // This performs the library function call
 uint index = data.indexOf(from);
 if (index == type(uint).max)
 data.push(to);
 else
 data[index] = to;
 }
}

Note that all external library calls are actual EVM function calls. This means that if you pass memory or value types, a copy will be performed, even in case of the `self` variable. The only situation where no copy will be performed is when storage reference variables are used or when internal library functions are called.

Another example shows how to define a custom operator for a user-defined type:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguMTk7Cgp0eXBlIFVGaXhlZDE2eDIgaXMgdWludDE2OwoKdXNpbmcgewogICAgYWRkIGFzICssCiAgICBkaXYgYXMgLwp9IGZvciBVRml4ZWQxNngyIGdsb2JhbDsKCnVpbnQzMiBjb25zdGFudCBTQ0FMRSA9IDEwMDsKCmZ1bmN0aW9uIGFkZChVRml4ZWQxNngyIGEsIFVGaXhlZDE2eDIgYikgcHVyZSByZXR1cm5zIChVRml4ZWQxNngyKSB7CiAgICByZXR1cm4gVUZpeGVkMTZ4Mi53cmFwKFVGaXhlZDE2eDIudW53cmFwKGEpICsgVUZpeGVkMTZ4Mi51bndyYXAoYikpOwp9CgpmdW5jdGlvbiBkaXYoVUZpeGVkMTZ4MiBhLCBVRml4ZWQxNngyIGIpIHB1cmUgcmV0dXJucyAoVUZpeGVkMTZ4MikgewogICAgdWludDMyIGEzMiA9IFVGaXhlZDE2eDIudW53cmFwKGEpOwogICAgdWludDMyIGIzMiA9IFVGaXhlZDE2eDIudW53cmFwKGIpOwogICAgdWludDMyIHJlc3VsdDMyID0gYTMyICogU0NBTEUgLyBiMzI7CiAgICByZXF1aXJlKHJlc3VsdDMyIDw9IHR5cGUodWludDE2KS5tYXgsICJEaXZpZGUgb3ZlcmZsb3ciKTsKICAgIHJldHVybiBVRml4ZWQxNngyLndyYXAodWludDE2KGEzMiAqIFNDQUxFIC8gYjMyKSk7Cn0KCmNvbnRyYWN0IE1hdGggewogICAgZnVuY3Rpb24gYXZnKFVGaXhlZDE2eDIgYSwgVUZpeGVkMTZ4MiBiKSBwdWJsaWMgcHVyZSByZXR1cm5zIChVRml4ZWQxNngyKSB7CiAgICAgICAgcmV0dXJuIChhICsgYikgLyBVRml4ZWQxNngyLndyYXAoMjAwKTsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.19;

type UFixed16x2 is uint16;

using {
 add as +,
 div as /
} for UFixed16x2 global;

uint32 constant SCALE = 100;

function add(UFixed16x2 a, UFixed16x2 b) pure returns (UFixed16x2) {
 return UFixed16x2.wrap(UFixed16x2.unwrap(a) + UFixed16x2.unwrap(b));
}

function div(UFixed16x2 a, UFixed16x2 b) pure returns (UFixed16x2) {
 uint32 a32 = UFixed16x2.unwrap(a);
 uint32 b32 = UFixed16x2.unwrap(b);
 uint32 result32 = a32 * SCALE / b32;
 require(result32 <= type(uint16).max, "Divide overflow");
 return UFixed16x2.wrap(uint16(a32 * SCALE / b32));
}

contract Math {
 function avg(UFixed16x2 a, UFixed16x2 b) public pure returns (UFixed16x2) {
 return (a + b) / UFixed16x2.wrap(200);
 }
}
