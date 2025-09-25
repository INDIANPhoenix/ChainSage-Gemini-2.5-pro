Title: Inline Assembly — Solidity 0.8.31 documentation

URL Source: https://docs.soliditylang.org/en/latest/assembly.html

Markdown Content:
You can interleave Solidity statements with inline assembly in a language close to the one of the Ethereum Virtual Machine. This gives you more fine-grained control, which is especially useful when you are enhancing the language by writing libraries or optimizing gas usage.

The language used for inline assembly in Solidity is called [Yul](https://docs.soliditylang.org/en/latest/yul.html#yul) and it is documented in its own section. This section will only cover how the inline assembly code can interface with the surrounding Solidity code.

Warning

Inline assembly is a way to access the Ethereum Virtual Machine at a low level. This bypasses several important safety features and checks of Solidity. You should only use it for tasks that need it, and only if you are confident with using it.

An inline assembly block is marked by `assembly { ... }`, where the code inside the curly braces is code in the [Yul](https://docs.soliditylang.org/en/latest/yul.html#yul) language.

The inline assembly code can access local Solidity variables as explained below.

Different inline assembly blocks share no namespace, i.e. it is not possible to call a Yul function or access a Yul variable defined in a different inline assembly block.

Example[](https://docs.soliditylang.org/en/latest/assembly.html#example "Link to this heading")
------------------------------------------------------------------------------------------------

The following example provides library code to access the code of another contract and load it into a `bytes` variable. This is possible with “plain Solidity” too, by using `<address>.code`. But the point here is that reusable assembly libraries can enhance the Solidity language without a compiler change.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCmxpYnJhcnkgR2V0Q29kZSB7CiAgICBmdW5jdGlvbiBhdChhZGRyZXNzIGFkZHIpIHB1YmxpYyB2aWV3IHJldHVybnMgKGJ5dGVzIG1lbW9yeSBjb2RlKSB7CiAgICAgICAgYXNzZW1ibHkgewogICAgICAgICAgICAvLyByZXRyaWV2ZSB0aGUgc2l6ZSBvZiB0aGUgY29kZSwgdGhpcyBuZWVkcyBhc3NlbWJseQogICAgICAgICAgICBsZXQgc2l6ZSA6PSBleHRjb2Rlc2l6ZShhZGRyKQogICAgICAgICAgICAvLyBhbGxvY2F0ZSBvdXRwdXQgYnl0ZSBhcnJheSAtIHRoaXMgY291bGQgYWxzbyBiZSBkb25lIHdpdGhvdXQgYXNzZW1ibHkKICAgICAgICAgICAgLy8gYnkgdXNpbmcgY29kZSA9IG5ldyBieXRlcyhzaXplKQogICAgICAgICAgICBjb2RlIDo9IG1sb2FkKDB4NDApCiAgICAgICAgICAgIC8vIG5ldyAibWVtb3J5IGVuZCIgaW5jbHVkaW5nIHBhZGRpbmcKICAgICAgICAgICAgbXN0b3JlKDB4NDAsIGFkZChjb2RlLCBhbmQoYWRkKGFkZChzaXplLCAweDIwKSwgMHgxZiksIG5vdCgweDFmKSkpKQogICAgICAgICAgICAvLyBzdG9yZSBsZW5ndGggaW4gbWVtb3J5CiAgICAgICAgICAgIG1zdG9yZShjb2RlLCBzaXplKQogICAgICAgICAgICAvLyBhY3R1YWxseSByZXRyaWV2ZSB0aGUgY29kZSwgdGhpcyBuZWVkcyBhc3NlbWJseQogICAgICAgICAgICBleHRjb2RlY29weShhZGRyLCBhZGQoY29kZSwgMHgyMCksIDAsIHNpemUpCiAgICAgICAgfQogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

library GetCode {
 function at(address addr) public view returns (bytes memory code) {
 assembly {
 // retrieve the size of the code, this needs assembly
 let size := extcodesize(addr)
 // allocate output byte array - this could also be done without assembly
 // by using code = new bytes(size)
 code := mload(0x40)
 // new "memory end" including padding
 mstore(0x40, add(code, and(add(add(size, 0x20), 0x1f), not(0x1f))))
 // store length in memory
 mstore(code, size)
 // actually retrieve the code, this needs assembly
 extcodecopy(addr, add(code, 0x20), 0, size)
 }
 }
}

Inline assembly is also beneficial in cases where the optimizer fails to produce efficient code, for example:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC40LjE2IDwwLjkuMDsKCgpsaWJyYXJ5IFZlY3RvclN1bSB7CiAgICAvLyBUaGlzIGZ1bmN0aW9uIGlzIGxlc3MgZWZmaWNpZW50IGJlY2F1c2UgdGhlIG9wdGltaXplciBjdXJyZW50bHkgZmFpbHMgdG8KICAgIC8vIHJlbW92ZSB0aGUgYm91bmRzIGNoZWNrcyBpbiBhcnJheSBhY2Nlc3MuCiAgICBmdW5jdGlvbiBzdW1Tb2xpZGl0eSh1aW50W10gbWVtb3J5IGRhdGEpIHB1YmxpYyBwdXJlIHJldHVybnMgKHVpbnQgc3VtKSB7CiAgICAgICAgZm9yICh1aW50IGkgPSAwOyBpIDwgZGF0YS5sZW5ndGg7ICsraSkKICAgICAgICAgICAgc3VtICs9IGRhdGFbaV07CiAgICB9CgogICAgLy8gV2Uga25vdyB0aGF0IHdlIG9ubHkgYWNjZXNzIHRoZSBhcnJheSBpbiBib3VuZHMsIHNvIHdlIGNhbiBhdm9pZCB0aGUgY2hlY2suCiAgICAvLyAweDIwIG5lZWRzIHRvIGJlIGFkZGVkIHRvIGFuIGFycmF5IGJlY2F1c2UgdGhlIGZpcnN0IHNsb3QgY29udGFpbnMgdGhlCiAgICAvLyBhcnJheSBsZW5ndGguCiAgICBmdW5jdGlvbiBzdW1Bc20odWludFtdIG1lbW9yeSBkYXRhKSBwdWJsaWMgcHVyZSByZXR1cm5zICh1aW50IHN1bSkgewogICAgICAgIGZvciAodWludCBpID0gMDsgaSA8IGRhdGEubGVuZ3RoOyArK2kpIHsKICAgICAgICAgICAgYXNzZW1ibHkgewogICAgICAgICAgICAgICAgc3VtIDo9IGFkZChzdW0sIG1sb2FkKGFkZChhZGQoZGF0YSwgMHgyMCksIG11bChpLCAweDIwKSkpKQogICAgICAgICAgICB9CiAgICAgICAgfQogICAgfQoKICAgIC8vIFNhbWUgYXMgYWJvdmUsIGJ1dCBhY2NvbXBsaXNoIHRoZSBlbnRpcmUgY29kZSB3aXRoaW4gaW5saW5lIGFzc2VtYmx5LgogICAgZnVuY3Rpb24gc3VtUHVyZUFzbSh1aW50W10gbWVtb3J5IGRhdGEpIHB1YmxpYyBwdXJlIHJldHVybnMgKHVpbnQgc3VtKSB7CiAgICAgICAgYXNzZW1ibHkgewogICAgICAgICAgICAvLyBMb2FkIHRoZSBsZW5ndGggKGZpcnN0IDMyIGJ5dGVzKQogICAgICAgICAgICBsZXQgbGVuIDo9IG1sb2FkKGRhdGEpCgogICAgICAgICAgICAvLyBTa2lwIG92ZXIgdGhlIGxlbmd0aCBmaWVsZC4KICAgICAgICAgICAgLy8KICAgICAgICAgICAgLy8gS2VlcCB0ZW1wb3JhcnkgdmFyaWFibGUgc28gaXQgY2FuIGJlIGluY3JlbWVudGVkIGluIHBsYWNlLgogICAgICAgICAgICAvLwogICAgICAgICAgICAvLyBOT1RFOiBpbmNyZW1lbnRpbmcgZGF0YSB3b3VsZCByZXN1bHQgaW4gYW4gdW51c2FibGUKICAgICAgICAgICAgLy8gICAgICAgZGF0YSB2YXJpYWJsZSBhZnRlciB0aGlzIGFzc2VtYmx5IGJsb2NrCiAgICAgICAgICAgIGxldCBkYXRhRWxlbWVudExvY2F0aW9uIDo9IGFkZChkYXRhLCAweDIwKQoKICAgICAgICAgICAgLy8gSXRlcmF0ZSB1bnRpbCB0aGUgYm91bmQgaXMgbm90IG1ldC4KICAgICAgICAgICAgZm9yCiAgICAgICAgICAgICAgICB7IGxldCBlbmQgOj0gYWRkKGRhdGFFbGVtZW50TG9jYXRpb24sIG11bChsZW4sIDB4MjApKSB9CiAgICAgICAgICAgICAgICBsdChkYXRhRWxlbWVudExvY2F0aW9uLCBlbmQpCiAgICAgICAgICAgICAgICB7IGRhdGFFbGVtZW50TG9jYXRpb24gOj0gYWRkKGRhdGFFbGVtZW50TG9jYXRpb24sIDB4MjApIH0KICAgICAgICAgICAgewogICAgICAgICAgICAgICAgc3VtIDo9IGFkZChzdW0sIG1sb2FkKGRhdGFFbGVtZW50TG9jYXRpb24pKQogICAgICAgICAgICB9CiAgICAgICAgfQogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

library VectorSum {
 // This function is less efficient because the optimizer currently fails to
 // remove the bounds checks in array access.
 function sumSolidity(uint[] memory data) public pure returns (uint sum) {
 for (uint i = 0; i < data.length; ++i)
 sum += data[i];
 }

 // We know that we only access the array in bounds, so we can avoid the check.
 // 0x20 needs to be added to an array because the first slot contains the
 // array length.
 function sumAsm(uint[] memory data) public pure returns (uint sum) {
 for (uint i = 0; i < data.length; ++i) {
 assembly {
 sum := add(sum, mload(add(add(data, 0x20), mul(i, 0x20))))
 }
 }
 }

 // Same as above, but accomplish the entire code within inline assembly.
 function sumPureAsm(uint[] memory data) public pure returns (uint sum) {
 assembly {
 // Load the length (first 32 bytes)
 let len := mload(data)

 // Skip over the length field.
 //
 // Keep temporary variable so it can be incremented in place.
 //
 // NOTE: incrementing data would result in an unusable
 // data variable after this assembly block
 let dataElementLocation := add(data, 0x20)

 // Iterate until the bound is not met.
 for
 { let end := add(dataElementLocation, mul(len, 0x20)) }
 lt(dataElementLocation, end)
 { dataElementLocation := add(dataElementLocation, 0x20) }
 {
 sum := add(sum, mload(dataElementLocation))
 }
 }
 }
}

Access to External Variables, Functions and Libraries[](https://docs.soliditylang.org/en/latest/assembly.html#access-to-external-variables-functions-and-libraries "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can access Solidity variables and other identifiers by using their name.

Local variables of value type are directly usable in inline assembly. They can both be read and assigned to.

Local variables that refer to memory evaluate to the address of the variable in memory, not the value itself. Such variables can also be assigned to, but note that an assignment will only change the pointer and not the data and that it is your responsibility to respect Solidity’s memory management. See [Conventions in Solidity](https://docs.soliditylang.org/en/latest/assembly.html#conventions-in-solidity).

Similarly, local variables that refer to statically-sized calldata arrays or calldata structs evaluate to the address of the variable in calldata, not the value itself. The variable can also be assigned a new offset, but note that no validation is performed to ensure that the variable will not point beyond `calldatasize()`.

For external function pointers the address and the function selector can be accessed using `x.address` and `x.selector`. The selector consists of four right-aligned bytes. Both values can be assigned to. For example:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC44LjEwIDwwLjkuMDsKCmNvbnRyYWN0IEMgewogICAgLy8gQXNzaWducyBhIG5ldyBzZWxlY3RvciBhbmQgYWRkcmVzcyB0byB0aGUgcmV0dXJuIHZhcmlhYmxlIEBmdW4KICAgIGZ1bmN0aW9uIGNvbWJpbmVUb0Z1bmN0aW9uUG9pbnRlcihhZGRyZXNzIG5ld0FkZHJlc3MsIHVpbnQgbmV3U2VsZWN0b3IpIHB1YmxpYyBwdXJlIHJldHVybnMgKGZ1bmN0aW9uKCkgZXh0ZXJuYWwgZnVuKSB7CiAgICAgICAgYXNzZW1ibHkgewogICAgICAgICAgICBmdW4uc2VsZWN0b3IgOj0gbmV3U2VsZWN0b3IKICAgICAgICAgICAgZnVuLmFkZHJlc3MgIDo9IG5ld0FkZHJlc3MKICAgICAgICB9CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.10 <0.9.0;

contract C {
 // Assigns a new selector and address to the return variable @fun
 function combineToFunctionPointer(address newAddress, uint newSelector) public pure returns (function() external fun) {
 assembly {
 fun.selector := newSelector
 fun.address := newAddress
 }
 }
}

For dynamic calldata arrays, you can access their calldata offset (in bytes) and length (number of elements) using `x.offset` and `x.length`. Both expressions can also be assigned to, but as for the static case, no validation will be performed to ensure that the resulting data area is within the bounds of `calldatasize()`.

For local storage variables or state variables (including transient storage) a single Yul identifier is not sufficient, since they do not necessarily occupy a single full storage slot. Therefore, their “address” is composed of a slot and a byte-offset inside that slot. To retrieve the slot pointed to by the variable `x`, you use `x.slot`, and to retrieve the byte-offset you use `x.offset`. Using `x` itself will result in an error.

You can also assign to the `.slot` part of a local storage variable pointer. For these (structs, arrays or mappings), the `.offset` part is always zero. It is not possible to assign to the `.slot` or `.offset` part of a state variable, though.

Local Solidity variables are available for assignments, for example:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC44LjI4IDwwLjkuMDsKCi8vIFRoaXMgd2lsbCByZXBvcnQgYSB3YXJuaW5nCmNvbnRyYWN0IEMgewogICAgYm9vbCB0cmFuc2llbnQgYTsKICAgIHVpbnQgYjsKICAgIGZ1bmN0aW9uIGYodWludCB4KSBwdWJsaWMgcmV0dXJucyAodWludCByKSB7CiAgICAgICAgYXNzZW1ibHkgewogICAgICAgICAgICAvLyBXZSBpZ25vcmUgdGhlIHN0b3JhZ2Ugc2xvdCBvZmZzZXQsIHdlIGtub3cgaXQgaXMgemVybwogICAgICAgICAgICAvLyBpbiB0aGlzIHNwZWNpYWwgY2FzZS4KICAgICAgICAgICAgciA6PSBtdWwoeCwgc2xvYWQoYi5zbG90KSkKICAgICAgICAgICAgdHN0b3JlKGEuc2xvdCwgdHJ1ZSkKICAgICAgICB9CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.28 <0.9.0;

// This will report a warning
contract C {
 bool transient a;
 uint b;
 function f(uint x) public returns (uint r) {
 assembly {
 // We ignore the storage slot offset, we know it is zero
 // in this special case.
 r := mul(x, sload(b.slot))
 tstore(a.slot, true)
 }
 }
}

Warning

If you access variables of a type that spans less than 256 bits (for example `uint64`, `address`, or `bytes16`), you cannot make any assumptions about bits not part of the encoding of the type. Especially, do not assume them to be zero. To be safe, always clear the data properly before you use it in a context where this is important: `uint32 x = f(); assembly { x := and(x, 0xffffffff) /* now use x */ }` To clean signed types, you can use the `signextend` opcode: `assembly { signextend(<num_bytes_of_x_minus_one>, x) }`

Since Solidity 0.6.0, the name of an inline assembly variable may not shadow any declaration visible in the scope of the inline assembly block (including variable, contract and function declarations).

Since Solidity 0.7.0, variables and functions declared inside the inline assembly block may not contain `.`, but using `.` is valid to access Solidity variables from outside the inline assembly block. However, it is still valid to use dots if you use Solidity in Yul-only mode.

Things to Avoid[](https://docs.soliditylang.org/en/latest/assembly.html#things-to-avoid "Link to this heading")
----------------------------------------------------------------------------------------------------------------

Inline assembly might have a quite high-level look, but it actually is extremely low-level. Function calls, loops, ifs and switches are converted by simple rewriting rules and after that, the only thing the assembler does for you is re-arranging functional-style opcodes, counting stack height for variable access and removing stack slots for assembly-local variables when the end of their block is reached.

Conventions in Solidity[](https://docs.soliditylang.org/en/latest/assembly.html#conventions-in-solidity "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

### Values of Typed Variables[](https://docs.soliditylang.org/en/latest/assembly.html#values-of-typed-variables "Link to this heading")

In contrast to EVM assembly, Solidity has types which are narrower than 256 bits, e.g. `uint24`. For efficiency, most arithmetic operations ignore the fact that types can be shorter than 256 bits, and the higher-order bits are cleaned when necessary, i.e., shortly before they are written to memory or before comparisons are performed. This means that if you access such a variable from within inline assembly, you might have to manually clean the higher-order bits first.

### Memory Management[](https://docs.soliditylang.org/en/latest/assembly.html#memory-management "Link to this heading")

Solidity manages memory in the following way. There is a “free memory pointer” at position `0x40` in memory. If you want to allocate memory, use the memory starting from where this pointer points at and update it. There is no guarantee that the memory has not been used before and thus you cannot assume that its contents are zero bytes. There is no built-in mechanism to release or free allocated memory. Solidity does not guarantee and does not require that the values in memory are placed at positions aligned to a multiple of any value. Here is an assembly snippet you can use for allocating memory that follows the process outlined above:

[open in Remix](https://remix.ethereum.org/?#language=yul&version=0.8.31&code=ZnVuY3Rpb24gYWxsb2NhdGUobGVuZ3RoKSAtPiBwb3MgewogIHBvcyA6PSBtbG9hZCgweDQwKQogIG1zdG9yZSgweDQwLCBhZGQocG9zLCBsZW5ndGgpKQp9)

function allocate(length) -> pos {
  pos := mload(0x40)
  mstore(0x40, add(pos, length))
}

The first 64 bytes of memory can be used as “scratch space” for short-term allocation. The 32 bytes after the free memory pointer (i.e., starting at `0x60`) are meant to be zero permanently and is used as the initial value for empty dynamic memory arrays. This means that the allocatable memory starts at `0x80`, which is the initial value of the free memory pointer.

Elements in memory arrays in Solidity always occupy multiples of 32 bytes (this is even true for `bytes1[]`, but not for `bytes` and `string`). Multi-dimensional memory arrays are pointers to memory arrays. The length of a dynamic array is stored at the first slot of the array and followed by the array elements.

Warning

Statically-sized memory arrays do not have a length field, but it might be added later to allow better convertibility between statically and dynamically-sized arrays; so, do not rely on this.

### Memory Safety[](https://docs.soliditylang.org/en/latest/assembly.html#memory-safety "Link to this heading")

Without the use of inline assembly, the compiler can rely on memory to remain in a well-defined state at all times. This is especially relevant for [the new code generation pipeline via Yul IR](https://docs.soliditylang.org/en/latest/ir-breaking-changes.html#ir-breaking-changes): this code generation path can move local variables from stack to memory to avoid stack-too-deep errors and perform additional memory optimizations, if it can rely on certain assumptions about memory use.

While we recommend to always respect Solidity’s memory model, inline assembly allows you to use memory in an incompatible way. Therefore, moving stack variables to memory and additional memory optimizations are, by default, globally disabled in the presence of any inline assembly block that contains a memory operation or assigns to Solidity variables in memory.

However, you can specifically annotate an assembly block to indicate that it in fact respects Solidity’s memory model as follows:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=YXNzZW1ibHkgKCJtZW1vcnktc2FmZSIpIHsKICAgIC4uLgp9)

assembly ("memory-safe") {
 ...
}

In particular, a memory-safe assembly block may only access the following memory ranges:

*   Memory allocated by yourself using a mechanism like the `allocate` function described above.

*   Memory allocated by Solidity, e.g. memory within the bounds of a memory array you reference.

*   The scratch space between memory offset 0 and 64 mentioned above.

*   Temporary memory that is located _after_ the value of the free memory pointer at the beginning of the assembly block, i.e. memory that is “allocated” at the free memory pointer without updating the free memory pointer.

Furthermore, if the assembly block assigns to Solidity variables in memory, you need to assure that accesses to the Solidity variables only access these memory ranges.

Since this is mainly about the optimizer, these restrictions still need to be followed, even if the assembly block reverts or terminates. As an example, the following assembly snippet is not memory safe, because the value of `returndatasize()` may exceed the 64 byte scratch space:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=YXNzZW1ibHkgewogIHJldHVybmRhdGFjb3B5KDAsIDAsIHJldHVybmRhdGFzaXplKCkpCiAgcmV2ZXJ0KDAsIHJldHVybmRhdGFzaXplKCkpCn0=)

assembly {
 returndatacopy(0, 0, returndatasize())
 revert(0, returndatasize())
}

On the other hand, the following code _is_ memory safe, because memory beyond the location pointed to by the free memory pointer can safely be used as temporary scratch space:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=YXNzZW1ibHkgKCJtZW1vcnktc2FmZSIpIHsKICBsZXQgcCA6PSBtbG9hZCgweDQwKQogIHJldHVybmRhdGFjb3B5KHAsIDAsIHJldHVybmRhdGFzaXplKCkpCiAgcmV2ZXJ0KHAsIHJldHVybmRhdGFzaXplKCkpCn0=)

assembly ("memory-safe") {
 let p := mload(0x40)
 returndatacopy(p, 0, returndatasize())
 revert(p, returndatasize())
}

Note that you do not need to update the free memory pointer if there is no following allocation, but you can only use memory starting from the current offset given by the free memory pointer.

If the memory operations use a length of zero, it is also fine to just use any offset (not only if it falls into the scratch space):

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=YXNzZW1ibHkgKCJtZW1vcnktc2FmZSIpIHsKICByZXZlcnQoMCwgMCkKfQ==)

assembly ("memory-safe") {
 revert(0, 0)
}

Note that not only memory operations in inline assembly itself can be memory-unsafe, but also assignments to Solidity variables of reference type in memory. For example the following is not memory-safe:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ynl0ZXMgbWVtb3J5IHg7CmFzc2VtYmx5IHsKICB4IDo9IDB4NDAKfQp4WzB4MjBdID0gMHg0Mjs=)

bytes memory x;
assembly {
 x := 0x40
}
x[0x20] = 0x42;

Inline assembly that neither involves any operations that access memory nor assigns to any Solidity variables in memory is automatically considered memory-safe and does not need to be annotated.

Warning

It is your responsibility to make sure that the assembly actually satisfies the memory model. If you annotate an assembly block as memory-safe, but violate one of the memory assumptions, this **will** lead to incorrect and undefined behavior that cannot easily be discovered by testing.

In case you are developing a library that is meant to be compatible across multiple versions of Solidity, you can use a special comment to annotate an assembly block as memory-safe:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8vIEBzb2xpZGl0eSBtZW1vcnktc2FmZS1hc3NlbWJseQphc3NlbWJseSB7CiAgICAuLi4KfQ==)

/// @solidity memory-safe-assembly
assembly {
 ...
}

Note that we will disallow the annotation via comment in a future breaking release; so, if you are not concerned with backward-compatibility with older compiler versions, prefer using the dialect string.

Advanced Safe Use of Memory[](https://docs.soliditylang.org/en/latest/assembly.html#advanced-safe-use-of-memory "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

Beyond the strict definition of memory-safety given above, there are cases in which you may want to use more than 64 bytes of scratch space starting at memory offset `0`. If you are careful, it can be admissible to use memory up to (and not including) offset `0x80` and still safely declare the assembly block as `memory-safe`. This is admissible under either of the following conditions:

*   By the end of the assembly block, the free memory pointer at offset `0x40` is restored to a sane value (i.e. it is either restored to its original value or an increment of it due to a manual memory allocation), and the memory word at offset `0x60` is restored to a value of zero.

*   The assembly block terminates, i.e. execution can never return to high-level Solidity code. This is the case, for example, if your assembly block unconditionally ends in calling the `revert` opcode.

Furthermore, you need to be aware that the default-value of dynamic arrays in Solidity point to memory offset `0x60`, so for the duration of temporarily changing the value at memory offset `0x60`, you can no longer rely on getting accurate length values when reading dynamic arrays, until you restore the zero value at `0x60`. To be more precise, we only guarantee safety when overwriting the zero pointer, if the remainder of the assembly snippet does not interact with the memory of high-level Solidity objects (including by reading from offsets previously stored in variables).
