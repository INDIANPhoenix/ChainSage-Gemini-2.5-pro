Title: Utilities - OpenZeppelin Docs

URL Source: https://docs.openzeppelin.com/contracts/5.x/api/utils

Markdown Content:
Miscellaneous contracts and libraries containing utility functions you can use to improve security, work with new data types, or safely use low-level primitives.

*   [`Math`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math), [`SignedMath`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath): Implementation of various arithmetic functions.

*   [`SafeCast`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast): Checked downcasting functions to avoid silent truncation.

*   [`ReentrancyGuard`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard): A modifier that can prevent reentrancy during certain functions.

*   [`ReentrancyGuardTransient`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient): Variant of [`ReentrancyGuard`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard) that uses transient storage ([EIP-1153](https://eips.ethereum.org/EIPS/eip-1153)).

*   [`Pausable`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable): A common emergency response mechanism that can pause functionality while a remediation is pending.

*   [`Nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces): Utility for tracking and verifying address nonces that only increment.

*   [`NoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed): Alternative to [`Nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces), that support keyed nonces following [ERC-4337 specifications](https://eips.ethereum.org/EIPS/eip-4337#semi-abstracted-nonce-support).

*   [`ERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165), [`ERC165Checker`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker): Utilities for inspecting interfaces supported by contracts.

*   [`BitMaps`](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps): A simple library to manage boolean value mapped to a numerical index in an efficient way.

*   [`EnumerableMap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap): A type like Solidity’s [`mapping`](https://solidity.readthedocs.io/en/latest/types.html#mapping-types), but with key-value _enumeration_: this will let you know how many entries a mapping has, and iterate over them (which is not possible with `mapping`).

*   [`EnumerableSet`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet): Like [`EnumerableMap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap), but for [sets](https://en.wikipedia.org/wiki/Set_(abstract_data_type)). Can be used to store privileged accounts, issued IDs, etc.

*   [`DoubleEndedQueue`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue): An implementation of a [double ended queue](https://en.wikipedia.org/wiki/Double-ended_queue) whose values can be added or removed from both sides. Useful for FIFO and LIFO structures.

*   [`CircularBuffer`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer): A data structure to store the last N values pushed to it.

*   [`Checkpoints`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints): A data structure to store values mapped to a strictly increasing key. Can be used for storing and accessing values over time.

*   [`Heap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap): A library that implements a [binary heap](https://en.wikipedia.org/wiki/Binary_heap) in storage.

*   [`MerkleTree`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree): A library with [Merkle Tree](https://wikipedia.org/wiki/Merkle_Tree) data structures and helper functions.

*   [`Create2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2): Wrapper around the [`CREATE2` EVM opcode](https://blog.openzeppelin.com/getting-the-most-out-of-create2/) for safe use without having to deal with low-level assembly.

*   [`Address`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address): Collection of functions for overloading Solidity’s [`address`](https://docs.soliditylang.org/en/latest/types.html#address) type.

*   [`Arrays`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays): Collection of functions that operate on [`arrays`](https://docs.soliditylang.org/en/latest/types.html#arrays).

*   [`Base64`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64): On-chain base64 and base64URL encoding according to [RFC-4648](https://datatracker.ietf.org/doc/html/rfc4648).

*   [`Bytes`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes): Common operations on bytes objects.

*   [`Calldata`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Calldata): Helpers for manipulating calldata.

*   [`Strings`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings): Common operations for strings formatting.

*   [`ShortStrings`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings): Library to encode (and decode) short strings into (or from) a single bytes32 slot for optimizing costs. Short strings are limited to 31 characters.

*   [`SlotDerivation`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation): Methods for deriving storage slot from ERC-7201 namespaces as well as from constructions such as mapping and arrays.

*   [`StorageSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot): Methods for accessing specific storage slots formatted as common primitive types.

*   [`TransientSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot): Primitives for reading from and writing to transient storage (only value types are currently supported).

*   [`Multicall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall): Abstract contract with a utility to allow batching together multiple calls in a single transaction. Useful for allowing EOAs to perform multiple operations at once.

*   [`Context`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context): A utility for abstracting the sender and calldata in the current execution context.

*   [`Packing`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing): A library for packing and unpacking multiple values into bytes32

*   [`Panic`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic): A library to revert with [Solidity panic codes](https://docs.soliditylang.org/en/v0.8.20/control-structures.html#panic-via-assert-and-error-via-require).

*   [`Comparators`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators): A library that contains comparator functions to use with the [`Heap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap) library.

*   [`CAIP2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2), [`CAIP10`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10): Libraries for formatting and parsing CAIP-2 and CAIP-10 identifiers.

*   [`Blockhash`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Blockhash): A library for accessing historical block hashes beyond the standard 256 block limit utilizing EIP-2935’s historical blockhash functionality.

*   [`Time`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time): A library that provides helpers for manipulating time-related objects, including a `Delay` type.

Because Solidity does not support generic types, [`EnumerableMap`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap) and [`EnumerableSet`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet) are specialized to a limited number of key-value types.

[](https://docs.openzeppelin.com/contracts/5.x/api/utils#math)Math
------------------------------------------------------------------

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math)`Math`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/math/Math.sol)

`import "@openzeppelin/contracts/utils/math/Math.sol";`

Standard math utilities missing in the Solidity language.

Functions

*   [`add512(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-add512-uint256-uint256-)

*   [`mul512(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mul512-uint256-uint256-)

*   [`tryAdd(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryAdd-uint256-uint256-)

*   [`trySub(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-trySub-uint256-uint256-)

*   [`tryMul(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryMul-uint256-uint256-)

*   [`tryDiv(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryDiv-uint256-uint256-)

*   [`tryMod(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryMod-uint256-uint256-)

*   [`saturatingAdd(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingAdd-uint256-uint256-)

*   [`saturatingSub(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingSub-uint256-uint256-)

*   [`saturatingMul(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingMul-uint256-uint256-)

*   [`ternary(condition, a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-ternary-bool-uint256-uint256-)

*   [`max(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-max-uint256-uint256-)

*   [`min(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-min-uint256-uint256-)

*   [`average(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-average-uint256-uint256-)

*   [`ceilDiv(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-ceilDiv-uint256-uint256-)

*   [`mulDiv(x, y, denominator)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulDiv-uint256-uint256-uint256-)

*   [`mulDiv(x, y, denominator, rounding)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulDiv-uint256-uint256-uint256-enum-Math-Rounding-)

*   [`mulShr(x, y, n)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulShr-uint256-uint256-uint8-)

*   [`mulShr(x, y, n, rounding)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulShr-uint256-uint256-uint8-enum-Math-Rounding-)

*   [`invMod(a, n)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invMod-uint256-uint256-)

*   [`invModPrime(a, p)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invModPrime-uint256-uint256-)

*   [`modExp(b, e, m)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-modExp-uint256-uint256-uint256-)

*   [`tryModExp(b, e, m)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryModExp-uint256-uint256-uint256-)

*   [`modExp(b, e, m)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-modExp-bytes-bytes-bytes-)

*   [`tryModExp(b, e, m)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryModExp-bytes-bytes-bytes-)

*   [`sqrt(a)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-sqrt-uint256-)

*   [`sqrt(a, rounding)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-sqrt-uint256-enum-Math-Rounding-)

*   [`log2(x)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log2-uint256-)

*   [`log2(value, rounding)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log2-uint256-enum-Math-Rounding-)

*   [`log10(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log10-uint256-)

*   [`log10(value, rounding)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log10-uint256-enum-Math-Rounding-)

*   [`log256(x)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log256-uint256-)

*   [`log256(value, rounding)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log256-uint256-enum-Math-Rounding-)

*   [`unsignedRoundsUp(rounding)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-unsignedRoundsUp-enum-Math-Rounding-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-add512-uint256-uint256-)`add512(uint256 a, uint256 b) → uint256 high, uint256 low`internal

Return the 512-bit addition of two uint256.

The result is stored in two 256 variables such that sum = high * 2²⁵⁶ + low.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mul512-uint256-uint256-)`mul512(uint256 a, uint256 b) → uint256 high, uint256 low`internal

Return the 512-bit multiplication of two uint256.

The result is stored in two 256 variables such that product = high * 2²⁵⁶ + low.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryAdd-uint256-uint256-)`tryAdd(uint256 a, uint256 b) → bool success, uint256 result`internal

Returns the addition of two unsigned integers, with a success flag (no overflow).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-trySub-uint256-uint256-)`trySub(uint256 a, uint256 b) → bool success, uint256 result`internal

Returns the subtraction of two unsigned integers, with a success flag (no overflow).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryMul-uint256-uint256-)`tryMul(uint256 a, uint256 b) → bool success, uint256 result`internal

Returns the multiplication of two unsigned integers, with a success flag (no overflow).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryDiv-uint256-uint256-)`tryDiv(uint256 a, uint256 b) → bool success, uint256 result`internal

Returns the division of two unsigned integers, with a success flag (no division by zero).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryMod-uint256-uint256-)`tryMod(uint256 a, uint256 b) → bool success, uint256 result`internal

Returns the remainder of dividing two unsigned integers, with a success flag (no division by zero).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingAdd-uint256-uint256-)`saturatingAdd(uint256 a, uint256 b) → uint256`internal

Unsigned saturating addition, bounds to `2²⁵⁶ - 1` instead of overflowing.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingSub-uint256-uint256-)`saturatingSub(uint256 a, uint256 b) → uint256`internal

Unsigned saturating subtraction, bounds to zero instead of overflowing.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-saturatingMul-uint256-uint256-)`saturatingMul(uint256 a, uint256 b) → uint256`internal

Unsigned saturating multiplication, bounds to `2²⁵⁶ - 1` instead of overflowing.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-ternary-bool-uint256-uint256-)`ternary(bool condition, uint256 a, uint256 b) → uint256`internal

Branchless ternary evaluation for `a ? b : c`. Gas costs are constant.

This function may reduce bytecode size and consume less gas when used standalone. However, the compiler may optimize Solidity ternary operations (i.e. `a ? b : c`) to only compute one branch when needed, making this function more expensive.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-max-uint256-uint256-)`max(uint256 a, uint256 b) → uint256`internal

Returns the largest of two numbers.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-min-uint256-uint256-)`min(uint256 a, uint256 b) → uint256`internal

Returns the smallest of two numbers.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-average-uint256-uint256-)`average(uint256 a, uint256 b) → uint256`internal

Returns the average of two numbers. The result is rounded towards zero.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-ceilDiv-uint256-uint256-)`ceilDiv(uint256 a, uint256 b) → uint256`internal

Returns the ceiling of the division of two numbers.

This differs from standard division with `/` in that it rounds towards infinity instead of rounding towards zero.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulDiv-uint256-uint256-uint256-)`mulDiv(uint256 x, uint256 y, uint256 denominator) → uint256 result`internal

Calculates floor(x * y / denominator) with full precision. Throws if result overflows a uint256 or denominator == 0.

Original credit to Remco Bloemen under MIT license ([https://xn—​2-umb.com/21/muldiv](https://xn--xn2-umb-316c.com/21/muldiv)) with further edits by Uniswap Labs also under MIT license.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulDiv-uint256-uint256-uint256-enum-Math-Rounding-)`mulDiv(uint256 x, uint256 y, uint256 denominator, enum Math.Rounding rounding) → uint256`internal

Calculates x * y / denominator with full precision, following the selected rounding direction.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulShr-uint256-uint256-uint8-)`mulShr(uint256 x, uint256 y, uint8 n) → uint256 result`internal

Calculates floor(x * y >> n) with full precision. Throws if result overflows a uint256.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-mulShr-uint256-uint256-uint8-enum-Math-Rounding-)`mulShr(uint256 x, uint256 y, uint8 n, enum Math.Rounding rounding) → uint256`internal

Calculates x * y >> n with full precision, following the selected rounding direction.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invMod-uint256-uint256-)`invMod(uint256 a, uint256 n) → uint256`internal

Calculate the modular multiplicative inverse of a number in Z/nZ.

If n is a prime, then Z/nZ is a field. In that case all elements are inversible, except 0. If n is not a prime, then Z/nZ is not a field, and some elements might not be inversible.

If the input value is not inversible, 0 is returned.

If you know for sure that n is (big) a prime, it may be cheaper to use Fermat’s little theorem and get the inverse using `Math.modExp(a, n - 2, n)`. See [`invModPrime`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invModPrime-uint256-uint256-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invModPrime-uint256-uint256-)`invModPrime(uint256 a, uint256 p) → uint256`internal

Variant of [`invMod`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-invMod-uint256-uint256-). More efficient, but only works if `p` is known to be a prime greater than `2`.

From [Fermat’s little theorem](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem), we know that if p is prime, then `a(p-1) ≡ 1 mod p`. As a consequence, we have `a * a(p-2) ≡ 1 mod p`, which means that `a**(p-2)` is the modular multiplicative inverse of a in Fp.

this function does NOT check that `p` is a prime greater than `2`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-modExp-uint256-uint256-uint256-)`modExp(uint256 b, uint256 e, uint256 m) → uint256`internal

Returns the modular exponentiation of the specified base, exponent and modulus (b ** e % m)

Requirements: - modulus can’t be zero - underlying staticcall to precompile must succeed

The result is only valid if the underlying call succeeds. When using this function, make sure the chain you’re using it on supports the precompiled contract for modular exponentiation at address 0x05 as specified in [EIP-198](https://eips.ethereum.org/EIPS/eip-198). Otherwise, the underlying function will succeed given the lack of a revert, but the result may be incorrectly interpreted as 0.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryModExp-uint256-uint256-uint256-)`tryModExp(uint256 b, uint256 e, uint256 m) → bool success, uint256 result`internal

Returns the modular exponentiation of the specified base, exponent and modulus (b ** e % m). It includes a success flag indicating if the operation succeeded. Operation will be marked as failed if trying to operate modulo 0 or if the underlying precompile reverted.

The result is only valid if the success flag is true. When using this function, make sure the chain you’re using it on supports the precompiled contract for modular exponentiation at address 0x05 as specified in [EIP-198](https://eips.ethereum.org/EIPS/eip-198). Otherwise, the underlying function will succeed given the lack of a revert, but the result may be incorrectly interpreted as 0.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-modExp-bytes-bytes-bytes-)`modExp(bytes b, bytes e, bytes m) → bytes`internal

Variant of [`modExp`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-modExp-bytes-bytes-bytes-) that supports inputs of arbitrary length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryModExp-bytes-bytes-bytes-)`tryModExp(bytes b, bytes e, bytes m) → bool success, bytes result`internal

Variant of [`tryModExp`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-tryModExp-bytes-bytes-bytes-) that supports inputs of arbitrary length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-sqrt-uint256-)`sqrt(uint256 a) → uint256`internal

Returns the square root of a number. If the number is not a perfect square, the value is rounded towards zero.

This method is based on Newton’s method for computing square roots; the algorithm is restricted to only using integer operations.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-sqrt-uint256-enum-Math-Rounding-)`sqrt(uint256 a, enum Math.Rounding rounding) → uint256`internal

Calculates sqrt(a), following the selected rounding direction.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log2-uint256-)`log2(uint256 x) → uint256 r`internal

Return the log in base 2 of a positive value rounded towards zero. Returns 0 if given 0.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log2-uint256-enum-Math-Rounding-)`log2(uint256 value, enum Math.Rounding rounding) → uint256`internal

Return the log in base 2, following the selected rounding direction, of a positive value. Returns 0 if given 0.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log10-uint256-)`log10(uint256 value) → uint256`internal

Return the log in base 10 of a positive value rounded towards zero. Returns 0 if given 0.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log10-uint256-enum-Math-Rounding-)`log10(uint256 value, enum Math.Rounding rounding) → uint256`internal

Return the log in base 10, following the selected rounding direction, of a positive value. Returns 0 if given 0.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log256-uint256-)`log256(uint256 x) → uint256 r`internal

Return the log in base 256 of a positive value rounded towards zero. Returns 0 if given 0.

Adding one to the result gives the number of pairs of hex symbols needed to represent `value` as a hex string.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-log256-uint256-enum-Math-Rounding-)`log256(uint256 value, enum Math.Rounding rounding) → uint256`internal

Return the log in base 256, following the selected rounding direction, of a positive value. Returns 0 if given 0.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Math-unsignedRoundsUp-enum-Math-Rounding-)`unsignedRoundsUp(enum Math.Rounding rounding) → bool`internal

Returns whether a provided rounding mode is considered rounding up for unsigned integers.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath)`SignedMath`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/math/SignedMath.sol)

`import "@openzeppelin/contracts/utils/math/SignedMath.sol";`

Standard signed math utilities missing in the Solidity language.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-ternary-bool-int256-int256-)`ternary(bool condition, int256 a, int256 b) → int256`internal

Branchless ternary evaluation for `a ? b : c`. Gas costs are constant.

This function may reduce bytecode size and consume less gas when used standalone. However, the compiler may optimize Solidity ternary operations (i.e. `a ? b : c`) to only compute one branch when needed, making this function more expensive.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-max-int256-int256-)`max(int256 a, int256 b) → int256`internal

Returns the largest of two signed numbers.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-min-int256-int256-)`min(int256 a, int256 b) → int256`internal

Returns the smallest of two signed numbers.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-average-int256-int256-)`average(int256 a, int256 b) → int256`internal

Returns the average of two signed numbers without overflow. The result is rounded towards zero.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SignedMath-abs-int256-)`abs(int256 n) → uint256`internal

Returns the absolute unsigned value of a signed value.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast)`SafeCast`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/math/SafeCast.sol)

`import "@openzeppelin/contracts/utils/math/SafeCast.sol";`

Wrappers over Solidity’s uintXX/intXX/bool casting operators with added overflow checks.

Downcasting from uint256/int256 in Solidity does not revert on overflow. This can easily result in undesired exploitation or bugs, since developers usually assume that overflows raise errors. `SafeCast` restores this intuition by reverting the transaction when such an operation overflows.

Using this library instead of the unchecked operations eliminates an entire class of bugs, so it’s recommended to use it always.

Functions

*   [`toUint248(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint248-uint256-)

*   [`toUint240(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint240-uint256-)

*   [`toUint232(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint232-uint256-)

*   [`toUint224(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint224-uint256-)

*   [`toUint216(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint216-uint256-)

*   [`toUint208(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint208-uint256-)

*   [`toUint200(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint200-uint256-)

*   [`toUint192(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint192-uint256-)

*   [`toUint184(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint184-uint256-)

*   [`toUint176(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint176-uint256-)

*   [`toUint168(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint168-uint256-)

*   [`toUint160(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint160-uint256-)

*   [`toUint152(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint152-uint256-)

*   [`toUint144(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint144-uint256-)

*   [`toUint136(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint136-uint256-)

*   [`toUint128(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint128-uint256-)

*   [`toUint120(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint120-uint256-)

*   [`toUint112(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint112-uint256-)

*   [`toUint104(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint104-uint256-)

*   [`toUint96(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint96-uint256-)

*   [`toUint88(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint88-uint256-)

*   [`toUint80(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint80-uint256-)

*   [`toUint72(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint72-uint256-)

*   [`toUint64(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint64-uint256-)

*   [`toUint56(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint56-uint256-)

*   [`toUint48(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint48-uint256-)

*   [`toUint40(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint40-uint256-)

*   [`toUint32(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint32-uint256-)

*   [`toUint24(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint24-uint256-)

*   [`toUint16(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint16-uint256-)

*   [`toUint8(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint8-uint256-)

*   [`toUint256(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint256-int256-)

*   [`toInt248(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt248-int256-)

*   [`toInt240(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt240-int256-)

*   [`toInt232(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt232-int256-)

*   [`toInt224(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt224-int256-)

*   [`toInt216(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt216-int256-)

*   [`toInt208(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt208-int256-)

*   [`toInt200(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt200-int256-)

*   [`toInt192(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt192-int256-)

*   [`toInt184(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt184-int256-)

*   [`toInt176(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt176-int256-)

*   [`toInt168(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt168-int256-)

*   [`toInt160(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt160-int256-)

*   [`toInt152(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt152-int256-)

*   [`toInt144(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt144-int256-)

*   [`toInt136(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt136-int256-)

*   [`toInt128(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt128-int256-)

*   [`toInt120(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt120-int256-)

*   [`toInt112(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt112-int256-)

*   [`toInt104(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt104-int256-)

*   [`toInt96(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt96-int256-)

*   [`toInt88(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt88-int256-)

*   [`toInt80(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt80-int256-)

*   [`toInt72(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt72-int256-)

*   [`toInt64(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt64-int256-)

*   [`toInt56(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt56-int256-)

*   [`toInt48(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt48-int256-)

*   [`toInt40(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt40-int256-)

*   [`toInt32(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt32-int256-)

*   [`toInt24(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt24-int256-)

*   [`toInt16(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt16-int256-)

*   [`toInt8(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt8-int256-)

*   [`toInt256(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt256-uint256-)

*   [`toUint(b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint-bool-)

Errors

*   [`SafeCastOverflowedUintDowncast(bits, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedUintDowncast-uint8-uint256-)

*   [`SafeCastOverflowedIntToUint(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedIntToUint-int256-)

*   [`SafeCastOverflowedIntDowncast(bits, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedIntDowncast-uint8-int256-)

*   [`SafeCastOverflowedUintToInt(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedUintToInt-uint256-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint248-uint256-)`toUint248(uint256 value) → uint248`internal

Returns the downcasted uint248 from uint256, reverting on overflow (when the input is greater than largest uint248).

Counterpart to Solidity’s `uint248` operator.

Requirements:

*   input must fit into 248 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint240-uint256-)`toUint240(uint256 value) → uint240`internal

Returns the downcasted uint240 from uint256, reverting on overflow (when the input is greater than largest uint240).

Counterpart to Solidity’s `uint240` operator.

Requirements:

*   input must fit into 240 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint232-uint256-)`toUint232(uint256 value) → uint232`internal

Returns the downcasted uint232 from uint256, reverting on overflow (when the input is greater than largest uint232).

Counterpart to Solidity’s `uint232` operator.

Requirements:

*   input must fit into 232 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint224-uint256-)`toUint224(uint256 value) → uint224`internal

Returns the downcasted uint224 from uint256, reverting on overflow (when the input is greater than largest uint224).

Counterpart to Solidity’s `uint224` operator.

Requirements:

*   input must fit into 224 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint216-uint256-)`toUint216(uint256 value) → uint216`internal

Returns the downcasted uint216 from uint256, reverting on overflow (when the input is greater than largest uint216).

Counterpart to Solidity’s `uint216` operator.

Requirements:

*   input must fit into 216 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint208-uint256-)`toUint208(uint256 value) → uint208`internal

Returns the downcasted uint208 from uint256, reverting on overflow (when the input is greater than largest uint208).

Counterpart to Solidity’s `uint208` operator.

Requirements:

*   input must fit into 208 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint200-uint256-)`toUint200(uint256 value) → uint200`internal

Returns the downcasted uint200 from uint256, reverting on overflow (when the input is greater than largest uint200).

Counterpart to Solidity’s `uint200` operator.

Requirements:

*   input must fit into 200 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint192-uint256-)`toUint192(uint256 value) → uint192`internal

Returns the downcasted uint192 from uint256, reverting on overflow (when the input is greater than largest uint192).

Counterpart to Solidity’s `uint192` operator.

Requirements:

*   input must fit into 192 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint184-uint256-)`toUint184(uint256 value) → uint184`internal

Returns the downcasted uint184 from uint256, reverting on overflow (when the input is greater than largest uint184).

Counterpart to Solidity’s `uint184` operator.

Requirements:

*   input must fit into 184 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint176-uint256-)`toUint176(uint256 value) → uint176`internal

Returns the downcasted uint176 from uint256, reverting on overflow (when the input is greater than largest uint176).

Counterpart to Solidity’s `uint176` operator.

Requirements:

*   input must fit into 176 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint168-uint256-)`toUint168(uint256 value) → uint168`internal

Returns the downcasted uint168 from uint256, reverting on overflow (when the input is greater than largest uint168).

Counterpart to Solidity’s `uint168` operator.

Requirements:

*   input must fit into 168 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint160-uint256-)`toUint160(uint256 value) → uint160`internal

Returns the downcasted uint160 from uint256, reverting on overflow (when the input is greater than largest uint160).

Counterpart to Solidity’s `uint160` operator.

Requirements:

*   input must fit into 160 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint152-uint256-)`toUint152(uint256 value) → uint152`internal

Returns the downcasted uint152 from uint256, reverting on overflow (when the input is greater than largest uint152).

Counterpart to Solidity’s `uint152` operator.

Requirements:

*   input must fit into 152 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint144-uint256-)`toUint144(uint256 value) → uint144`internal

Returns the downcasted uint144 from uint256, reverting on overflow (when the input is greater than largest uint144).

Counterpart to Solidity’s `uint144` operator.

Requirements:

*   input must fit into 144 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint136-uint256-)`toUint136(uint256 value) → uint136`internal

Returns the downcasted uint136 from uint256, reverting on overflow (when the input is greater than largest uint136).

Counterpart to Solidity’s `uint136` operator.

Requirements:

*   input must fit into 136 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint128-uint256-)`toUint128(uint256 value) → uint128`internal

Returns the downcasted uint128 from uint256, reverting on overflow (when the input is greater than largest uint128).

Counterpart to Solidity’s `uint128` operator.

Requirements:

*   input must fit into 128 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint120-uint256-)`toUint120(uint256 value) → uint120`internal

Returns the downcasted uint120 from uint256, reverting on overflow (when the input is greater than largest uint120).

Counterpart to Solidity’s `uint120` operator.

Requirements:

*   input must fit into 120 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint112-uint256-)`toUint112(uint256 value) → uint112`internal

Returns the downcasted uint112 from uint256, reverting on overflow (when the input is greater than largest uint112).

Counterpart to Solidity’s `uint112` operator.

Requirements:

*   input must fit into 112 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint104-uint256-)`toUint104(uint256 value) → uint104`internal

Returns the downcasted uint104 from uint256, reverting on overflow (when the input is greater than largest uint104).

Counterpart to Solidity’s `uint104` operator.

Requirements:

*   input must fit into 104 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint96-uint256-)`toUint96(uint256 value) → uint96`internal

Returns the downcasted uint96 from uint256, reverting on overflow (when the input is greater than largest uint96).

Counterpart to Solidity’s `uint96` operator.

Requirements:

*   input must fit into 96 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint88-uint256-)`toUint88(uint256 value) → uint88`internal

Returns the downcasted uint88 from uint256, reverting on overflow (when the input is greater than largest uint88).

Counterpart to Solidity’s `uint88` operator.

Requirements:

*   input must fit into 88 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint80-uint256-)`toUint80(uint256 value) → uint80`internal

Returns the downcasted uint80 from uint256, reverting on overflow (when the input is greater than largest uint80).

Counterpart to Solidity’s `uint80` operator.

Requirements:

*   input must fit into 80 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint72-uint256-)`toUint72(uint256 value) → uint72`internal

Returns the downcasted uint72 from uint256, reverting on overflow (when the input is greater than largest uint72).

Counterpart to Solidity’s `uint72` operator.

Requirements:

*   input must fit into 72 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint64-uint256-)`toUint64(uint256 value) → uint64`internal

Returns the downcasted uint64 from uint256, reverting on overflow (when the input is greater than largest uint64).

Counterpart to Solidity’s `uint64` operator.

Requirements:

*   input must fit into 64 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint56-uint256-)`toUint56(uint256 value) → uint56`internal

Returns the downcasted uint56 from uint256, reverting on overflow (when the input is greater than largest uint56).

Counterpart to Solidity’s `uint56` operator.

Requirements:

*   input must fit into 56 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint48-uint256-)`toUint48(uint256 value) → uint48`internal

Returns the downcasted uint48 from uint256, reverting on overflow (when the input is greater than largest uint48).

Counterpart to Solidity’s `uint48` operator.

Requirements:

*   input must fit into 48 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint40-uint256-)`toUint40(uint256 value) → uint40`internal

Returns the downcasted uint40 from uint256, reverting on overflow (when the input is greater than largest uint40).

Counterpart to Solidity’s `uint40` operator.

Requirements:

*   input must fit into 40 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint32-uint256-)`toUint32(uint256 value) → uint32`internal

Returns the downcasted uint32 from uint256, reverting on overflow (when the input is greater than largest uint32).

Counterpart to Solidity’s `uint32` operator.

Requirements:

*   input must fit into 32 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint24-uint256-)`toUint24(uint256 value) → uint24`internal

Returns the downcasted uint24 from uint256, reverting on overflow (when the input is greater than largest uint24).

Counterpart to Solidity’s `uint24` operator.

Requirements:

*   input must fit into 24 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint16-uint256-)`toUint16(uint256 value) → uint16`internal

Returns the downcasted uint16 from uint256, reverting on overflow (when the input is greater than largest uint16).

Counterpart to Solidity’s `uint16` operator.

Requirements:

*   input must fit into 16 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint8-uint256-)`toUint8(uint256 value) → uint8`internal

Returns the downcasted uint8 from uint256, reverting on overflow (when the input is greater than largest uint8).

Counterpart to Solidity’s `uint8` operator.

Requirements:

*   input must fit into 8 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint256-int256-)`toUint256(int256 value) → uint256`internal

Converts a signed int256 into an unsigned uint256.

Requirements:

*   input must be greater than or equal to 0.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt248-int256-)`toInt248(int256 value) → int248 downcasted`internal

Returns the downcasted int248 from int256, reverting on overflow (when the input is less than smallest int248 or greater than largest int248).

Counterpart to Solidity’s `int248` operator.

Requirements:

*   input must fit into 248 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt240-int256-)`toInt240(int256 value) → int240 downcasted`internal

Returns the downcasted int240 from int256, reverting on overflow (when the input is less than smallest int240 or greater than largest int240).

Counterpart to Solidity’s `int240` operator.

Requirements:

*   input must fit into 240 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt232-int256-)`toInt232(int256 value) → int232 downcasted`internal

Returns the downcasted int232 from int256, reverting on overflow (when the input is less than smallest int232 or greater than largest int232).

Counterpart to Solidity’s `int232` operator.

Requirements:

*   input must fit into 232 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt224-int256-)`toInt224(int256 value) → int224 downcasted`internal

Returns the downcasted int224 from int256, reverting on overflow (when the input is less than smallest int224 or greater than largest int224).

Counterpart to Solidity’s `int224` operator.

Requirements:

*   input must fit into 224 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt216-int256-)`toInt216(int256 value) → int216 downcasted`internal

Returns the downcasted int216 from int256, reverting on overflow (when the input is less than smallest int216 or greater than largest int216).

Counterpart to Solidity’s `int216` operator.

Requirements:

*   input must fit into 216 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt208-int256-)`toInt208(int256 value) → int208 downcasted`internal

Returns the downcasted int208 from int256, reverting on overflow (when the input is less than smallest int208 or greater than largest int208).

Counterpart to Solidity’s `int208` operator.

Requirements:

*   input must fit into 208 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt200-int256-)`toInt200(int256 value) → int200 downcasted`internal

Returns the downcasted int200 from int256, reverting on overflow (when the input is less than smallest int200 or greater than largest int200).

Counterpart to Solidity’s `int200` operator.

Requirements:

*   input must fit into 200 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt192-int256-)`toInt192(int256 value) → int192 downcasted`internal

Returns the downcasted int192 from int256, reverting on overflow (when the input is less than smallest int192 or greater than largest int192).

Counterpart to Solidity’s `int192` operator.

Requirements:

*   input must fit into 192 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt184-int256-)`toInt184(int256 value) → int184 downcasted`internal

Returns the downcasted int184 from int256, reverting on overflow (when the input is less than smallest int184 or greater than largest int184).

Counterpart to Solidity’s `int184` operator.

Requirements:

*   input must fit into 184 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt176-int256-)`toInt176(int256 value) → int176 downcasted`internal

Returns the downcasted int176 from int256, reverting on overflow (when the input is less than smallest int176 or greater than largest int176).

Counterpart to Solidity’s `int176` operator.

Requirements:

*   input must fit into 176 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt168-int256-)`toInt168(int256 value) → int168 downcasted`internal

Returns the downcasted int168 from int256, reverting on overflow (when the input is less than smallest int168 or greater than largest int168).

Counterpart to Solidity’s `int168` operator.

Requirements:

*   input must fit into 168 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt160-int256-)`toInt160(int256 value) → int160 downcasted`internal

Returns the downcasted int160 from int256, reverting on overflow (when the input is less than smallest int160 or greater than largest int160).

Counterpart to Solidity’s `int160` operator.

Requirements:

*   input must fit into 160 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt152-int256-)`toInt152(int256 value) → int152 downcasted`internal

Returns the downcasted int152 from int256, reverting on overflow (when the input is less than smallest int152 or greater than largest int152).

Counterpart to Solidity’s `int152` operator.

Requirements:

*   input must fit into 152 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt144-int256-)`toInt144(int256 value) → int144 downcasted`internal

Returns the downcasted int144 from int256, reverting on overflow (when the input is less than smallest int144 or greater than largest int144).

Counterpart to Solidity’s `int144` operator.

Requirements:

*   input must fit into 144 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt136-int256-)`toInt136(int256 value) → int136 downcasted`internal

Returns the downcasted int136 from int256, reverting on overflow (when the input is less than smallest int136 or greater than largest int136).

Counterpart to Solidity’s `int136` operator.

Requirements:

*   input must fit into 136 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt128-int256-)`toInt128(int256 value) → int128 downcasted`internal

Returns the downcasted int128 from int256, reverting on overflow (when the input is less than smallest int128 or greater than largest int128).

Counterpart to Solidity’s `int128` operator.

Requirements:

*   input must fit into 128 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt120-int256-)`toInt120(int256 value) → int120 downcasted`internal

Returns the downcasted int120 from int256, reverting on overflow (when the input is less than smallest int120 or greater than largest int120).

Counterpart to Solidity’s `int120` operator.

Requirements:

*   input must fit into 120 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt112-int256-)`toInt112(int256 value) → int112 downcasted`internal

Returns the downcasted int112 from int256, reverting on overflow (when the input is less than smallest int112 or greater than largest int112).

Counterpart to Solidity’s `int112` operator.

Requirements:

*   input must fit into 112 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt104-int256-)`toInt104(int256 value) → int104 downcasted`internal

Returns the downcasted int104 from int256, reverting on overflow (when the input is less than smallest int104 or greater than largest int104).

Counterpart to Solidity’s `int104` operator.

Requirements:

*   input must fit into 104 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt96-int256-)`toInt96(int256 value) → int96 downcasted`internal

Returns the downcasted int96 from int256, reverting on overflow (when the input is less than smallest int96 or greater than largest int96).

Counterpart to Solidity’s `int96` operator.

Requirements:

*   input must fit into 96 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt88-int256-)`toInt88(int256 value) → int88 downcasted`internal

Returns the downcasted int88 from int256, reverting on overflow (when the input is less than smallest int88 or greater than largest int88).

Counterpart to Solidity’s `int88` operator.

Requirements:

*   input must fit into 88 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt80-int256-)`toInt80(int256 value) → int80 downcasted`internal

Returns the downcasted int80 from int256, reverting on overflow (when the input is less than smallest int80 or greater than largest int80).

Counterpart to Solidity’s `int80` operator.

Requirements:

*   input must fit into 80 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt72-int256-)`toInt72(int256 value) → int72 downcasted`internal

Returns the downcasted int72 from int256, reverting on overflow (when the input is less than smallest int72 or greater than largest int72).

Counterpart to Solidity’s `int72` operator.

Requirements:

*   input must fit into 72 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt64-int256-)`toInt64(int256 value) → int64 downcasted`internal

Returns the downcasted int64 from int256, reverting on overflow (when the input is less than smallest int64 or greater than largest int64).

Counterpart to Solidity’s `int64` operator.

Requirements:

*   input must fit into 64 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt56-int256-)`toInt56(int256 value) → int56 downcasted`internal

Returns the downcasted int56 from int256, reverting on overflow (when the input is less than smallest int56 or greater than largest int56).

Counterpart to Solidity’s `int56` operator.

Requirements:

*   input must fit into 56 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt48-int256-)`toInt48(int256 value) → int48 downcasted`internal

Returns the downcasted int48 from int256, reverting on overflow (when the input is less than smallest int48 or greater than largest int48).

Counterpart to Solidity’s `int48` operator.

Requirements:

*   input must fit into 48 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt40-int256-)`toInt40(int256 value) → int40 downcasted`internal

Returns the downcasted int40 from int256, reverting on overflow (when the input is less than smallest int40 or greater than largest int40).

Counterpart to Solidity’s `int40` operator.

Requirements:

*   input must fit into 40 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt32-int256-)`toInt32(int256 value) → int32 downcasted`internal

Returns the downcasted int32 from int256, reverting on overflow (when the input is less than smallest int32 or greater than largest int32).

Counterpart to Solidity’s `int32` operator.

Requirements:

*   input must fit into 32 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt24-int256-)`toInt24(int256 value) → int24 downcasted`internal

Returns the downcasted int24 from int256, reverting on overflow (when the input is less than smallest int24 or greater than largest int24).

Counterpart to Solidity’s `int24` operator.

Requirements:

*   input must fit into 24 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt16-int256-)`toInt16(int256 value) → int16 downcasted`internal

Returns the downcasted int16 from int256, reverting on overflow (when the input is less than smallest int16 or greater than largest int16).

Counterpart to Solidity’s `int16` operator.

Requirements:

*   input must fit into 16 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt8-int256-)`toInt8(int256 value) → int8 downcasted`internal

Returns the downcasted int8 from int256, reverting on overflow (when the input is less than smallest int8 or greater than largest int8).

Counterpart to Solidity’s `int8` operator.

Requirements:

*   input must fit into 8 bits

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toInt256-uint256-)`toInt256(uint256 value) → int256`internal

Converts an unsigned uint256 into a signed int256.

Requirements:

*   input must be less than or equal to maxInt256.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-toUint-bool-)`toUint(bool b) → uint256 u`internal

Cast a boolean (false or true) to a uint256 (0 or 1) with no jump.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedUintDowncast-uint8-uint256-)`SafeCastOverflowedUintDowncast(uint8 bits, uint256 value)`error

Value doesn’t fit in an uint of `bits` size.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedIntToUint-int256-)`SafeCastOverflowedIntToUint(int256 value)`error

An int value doesn’t fit in an uint of `bits` size.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedIntDowncast-uint8-int256-)`SafeCastOverflowedIntDowncast(uint8 bits, int256 value)`error

Value doesn’t fit in an int of `bits` size.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SafeCast-SafeCastOverflowedUintToInt-uint256-)`SafeCastOverflowedUintToInt(uint256 value)`error

An uint value doesn’t fit in an int of `bits` size.

[](https://docs.openzeppelin.com/contracts/5.x/api/utils#security)Security
--------------------------------------------------------------------------

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard)`ReentrancyGuard`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/ReentrancyGuard.sol)

`import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";`

Contract module that helps prevent reentrant calls to a function.

Inheriting from `ReentrancyGuard` will make the [`nonReentrant`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrant--) modifier available, which can be applied to functions to make sure there are no nested (reentrant) calls to them.

Note that because there is a single `nonReentrant` guard, functions marked as `nonReentrant` may not call one another. This can be worked around by making those functions `private`, and then adding `external``nonReentrant` entry points to them.

If EIP-1153 (transient storage) is available on the chain you’re deploying at, consider using [`ReentrancyGuardTransient`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient) instead.

If you would like to learn more about reentrancy and alternative ways to protect against it, check out our blog post [Reentrancy After Istanbul](https://blog.openzeppelin.com/reentrancy-after-istanbul/).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-nonReentrant--)`nonReentrant()`modifier

Prevents a contract from calling itself, directly or indirectly. Calling a `nonReentrant` function from another `nonReentrant` function is not supported. It is possible to prevent this from happening by making the `nonReentrant` function external, and making it call a `private` function that does the actual work.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-constructor--)`constructor()`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-_reentrancyGuardEntered--)`_reentrancyGuardEntered() → bool`internal

Returns true if the reentrancy guard is currently set to "entered", which indicates there is a `nonReentrant` function in the call stack.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard-ReentrancyGuardReentrantCall--)`ReentrancyGuardReentrantCall()`error

Unauthorized reentrant call.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient)`ReentrancyGuardTransient`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/ReentrancyGuardTransient.sol)

`import "@openzeppelin/contracts/utils/ReentrancyGuardTransient.sol";`

Variant of [`ReentrancyGuard`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard) that uses transient storage.

This variant only works on networks where EIP-1153 is available.

_Available since v5.1._

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-nonReentrant--)`nonReentrant()`modifier

Prevents a contract from calling itself, directly or indirectly. Calling a `nonReentrant` function from another `nonReentrant` function is not supported. It is possible to prevent this from happening by making the `nonReentrant` function external, and making it call a `private` function that does the actual work.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-_reentrancyGuardEntered--)`_reentrancyGuardEntered() → bool`internal

Returns true if the reentrancy guard is currently set to "entered", which indicates there is a `nonReentrant` function in the call stack.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuardTransient-ReentrancyGuardReentrantCall--)`ReentrancyGuardReentrantCall()`error

Unauthorized reentrant call.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable)`Pausable`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Pausable.sol)

`import "@openzeppelin/contracts/utils/Pausable.sol";`

Contract module which allows children to implement an emergency stop mechanism that can be triggered by an authorized account.

This module is used through inheritance. It will make available the modifiers `whenNotPaused` and `whenPaused`, which can be applied to the functions of your contract. Note that they will not be pausable by simply including this module, only once the modifiers are put in place.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-whenNotPaused--)`whenNotPaused()`modifier

Modifier to make a function callable only when the contract is not paused.

Requirements:

*   The contract must not be paused.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-whenPaused--)`whenPaused()`modifier

Modifier to make a function callable only when the contract is paused.

Requirements:

*   The contract must be paused.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-paused--)`paused() → bool`public

Returns true if the contract is paused, and false otherwise.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_requireNotPaused--)`_requireNotPaused()`internal

Throws if the contract is paused.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_requirePaused--)`_requirePaused()`internal

Throws if the contract is not paused.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_pause--)`_pause()`internal

Triggers stopped state.

Requirements:

*   The contract must not be paused.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-_unpause--)`_unpause()`internal

Returns to normal state.

Requirements:

*   The contract must be paused.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-Paused-address-)`Paused(address account)`event

Emitted when the pause is triggered by `account`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-Unpaused-address-)`Unpaused(address account)`event

Emitted when the pause is lifted by `account`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-EnforcedPause--)`EnforcedPause()`error

The operation failed because the contract is paused.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Pausable-ExpectedPause--)`ExpectedPause()`error

The operation failed because the contract is not paused.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces)`Nonces`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Nonces.sol)

`import "@openzeppelin/contracts/utils/Nonces.sol";`

Provides tracking nonces for addresses. Nonces will only increment.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-nonces-address-)`nonces(address owner) → uint256`public

Returns the next unused nonce for an address.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useNonce-address-)`_useNonce(address owner) → uint256`internal

Consumes a nonce.

Returns the current value and increments nonce.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useCheckedNonce-address-uint256-)`_useCheckedNonce(address owner, uint256 nonce)`internal

Same as [`_useNonce`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-_useNonce-address-) but checking that `nonce` is the next valid for `owner`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Nonces-InvalidAccountNonce-address-uint256-)`InvalidAccountNonce(address account, uint256 currentNonce)`error

The nonce used for an `account` is not the expected current nonce.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed)`NoncesKeyed`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/NoncesKeyed.sol)

`import "@openzeppelin/contracts/utils/NoncesKeyed.sol";`

Alternative to [`nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-nonces-address-uint192-), that supports key-ed nonces.

This contract inherits from [`nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-nonces-address-uint192-) and reuses its storage for the first nonce key (i.e. `0`). This makes upgrading from [`nonces`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-nonces-address-uint192-) to [`NoncesKeyed`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed) safe when using their upgradeable versions (e.g. `NoncesKeyedUpgradeable`). Doing so will NOT reset the current state of nonces, avoiding replay attacks where a nonce is reused after the upgrade.

Functions

*   [`nonces(owner, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-nonces-address-uint192-)

*   [`_useNonce(owner, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useNonce-address-uint192-)

*   [`_useCheckedNonce(owner, keyNonce)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useCheckedNonce-address-uint256-)

*   [`_useCheckedNonce(owner, key, nonce)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useCheckedNonce-address-uint192-uint64-)

Errors

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-nonces-address-uint192-)`nonces(address owner, uint192 key) → uint256`public

Returns the next unused nonce for an address and key. Result contains the key prefix.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useNonce-address-uint192-)`_useNonce(address owner, uint192 key) → uint256`internal

Consumes the next unused nonce for an address and key.

Returns the current value without the key prefix. Consumed nonce is increased, so calling this function twice with the same arguments will return different (sequential) results.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useCheckedNonce-address-uint256-)`_useCheckedNonce(address owner, uint256 keyNonce)`internal

Same as [`_useNonce`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useNonce-address-uint192-) but checking that `nonce` is the next valid for `owner`.

This version takes the key and the nonce in a single uint256 parameter: - use the first 24 bytes for the key - use the last 8 bytes for the nonce

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useCheckedNonce-address-uint192-uint64-)`_useCheckedNonce(address owner, uint192 key, uint64 nonce)`internal

Same as [`_useNonce`](https://docs.openzeppelin.com/contracts/5.x/api/utils#NoncesKeyed-_useNonce-address-uint192-) but checking that `nonce` is the next valid for `owner`.

This version takes the key and the nonce as two different parameters.

[](https://docs.openzeppelin.com/contracts/5.x/api/utils#introspection)Introspection
------------------------------------------------------------------------------------

This set of interfaces and contracts deal with [type introspection](https://en.wikipedia.org/wiki/Type_introspection) of contracts, that is, examining which functions can be called on them. This is usually referred to as a contract’s _interface_.

Ethereum contracts have no native concept of an interface, so applications must usually simply trust they are not making an incorrect call. For trusted setups this is a non-issue, but often unknown and untrusted third-party addresses need to be interacted with. There may even not be any direct calls to them! (e.g. ERC-20 tokens may be sent to a contract that lacks a way to transfer them out of it, locking them forever). In these cases, a contract _declaring_ its interface can be very helpful in preventing errors.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165)`IERC165`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/introspection/IERC165.sol)

`import "@openzeppelin/contracts/utils/introspection/IERC165.sol";`

Interface of the ERC-165 standard, as defined in the [ERC](https://eips.ethereum.org/EIPS/eip-165).

Implementers can declare support of contract interfaces, which can then be queried by others ([`ERC165Checker`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker)).

For an implementation, see [`ERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165-supportsInterface-bytes4-)`supportsInterface(bytes4 interfaceId) → bool`external

Returns true if this contract implements the interface defined by `interfaceId`. See the corresponding [ERC section](https://eips.ethereum.org/EIPS/eip-165#how-interfaces-are-identified) to learn more about how these ids are created.

This function call must use less than 30 000 gas.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165)`ERC165`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/introspection/ERC165.sol)

`import "@openzeppelin/contracts/utils/introspection/ERC165.sol";`

Implementation of the [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165) interface.

Contracts that want to implement ERC-165 should inherit from this contract and override [`supportsInterface`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165-supportsInterface-bytes4-) to check for the additional interface id that will be supported. For example:

```
function supportsInterface(bytes4 interfaceId) public view virtual override returns (bool) {
    return interfaceId == type(MyInterface).interfaceId || super.supportsInterface(interfaceId);
}
```

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165-supportsInterface-bytes4-)`supportsInterface(bytes4 interfaceId) → bool`public

Returns true if this contract implements the interface defined by `interfaceId`. See the corresponding [ERC section](https://eips.ethereum.org/EIPS/eip-165#how-interfaces-are-identified) to learn more about how these ids are created.

This function call must use less than 30 000 gas.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker)`ERC165Checker`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/introspection/ERC165Checker.sol)

`import "@openzeppelin/contracts/utils/introspection/ERC165Checker.sol";`

Library used to query support of an interface declared via [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165).

Note that these functions return the actual result of the query: they do not `revert` if an interface is not supported. It is up to the caller to decide what to do in these cases.

Functions

*   [`supportsERC165(account)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsERC165-address-)

*   [`supportsInterface(account, interfaceId)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsInterface-address-bytes4-)

*   [`getSupportedInterfaces(account, interfaceIds)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-getSupportedInterfaces-address-bytes4---)

*   [`supportsAllInterfaces(account, interfaceIds)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsAllInterfaces-address-bytes4---)

*   [`supportsERC165InterfaceUnchecked(account, interfaceId)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsERC165InterfaceUnchecked-address-bytes4-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsERC165-address-)`supportsERC165(address account) → bool`internal

Returns true if `account` supports the [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165) interface.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsInterface-address-bytes4-)`supportsInterface(address account, bytes4 interfaceId) → bool`internal

Returns true if `account` supports the interface defined by `interfaceId`. Support for [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165) itself is queried automatically.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-getSupportedInterfaces-address-bytes4---)`getSupportedInterfaces(address account, bytes4[] interfaceIds) → bool[]`internal

Returns a boolean array where each value corresponds to the interfaces passed in and whether they’re supported or not. This allows you to batch check interfaces for a contract where your expectation is that some interfaces may not be supported.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsAllInterfaces-address-bytes4---)`supportsAllInterfaces(address account, bytes4[] interfaceIds) → bool`internal

Returns true if `account` supports all the interfaces defined in `interfaceIds`. Support for [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165) itself is queried automatically.

Batch-querying can lead to gas savings by skipping repeated checks for [`IERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#IERC165) support.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsERC165InterfaceUnchecked-address-bytes4-)`supportsERC165InterfaceUnchecked(address account, bytes4 interfaceId) → bool`internal

Assumes that account contains a contract that supports ERC-165, otherwise the behavior of this method is undefined. This precondition can be checked with [`supportsERC165`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ERC165Checker-supportsERC165-address-).

Some precompiled contracts will falsely indicate support for a given interface, so caution should be exercised when using this function.

Interface identification is specified in ERC-165.

[](https://docs.openzeppelin.com/contracts/5.x/api/utils#data_structures)Data Structures
----------------------------------------------------------------------------------------

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps)`BitMaps`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/structs/BitMaps.sol)

`import "@openzeppelin/contracts/utils/structs/BitMaps.sol";`

Library for managing uint256 to bool mapping in a compact and efficient way, provided the keys are sequential. Largely inspired by Uniswap’s [merkle-distributor](https://github.com/Uniswap/merkle-distributor/blob/master/contracts/MerkleDistributor.sol).

BitMaps pack 256 booleans across each bit of a single 256-bit slot of `uint256` type. Hence booleans corresponding to 256 _sequential_ indices would only consume a single slot, unlike the regular `bool` which would consume an entire slot for a single value.

This results in gas savings in two ways:

*   Setting a zero value to non-zero only once every 256 times

*   Accessing the same warm slot for every 256 _sequential_ indices

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-get-struct-BitMaps-BitMap-uint256-)`get(struct BitMaps.BitMap bitmap, uint256 index) → bool`internal

Returns whether the bit at `index` is set.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-setTo-struct-BitMaps-BitMap-uint256-bool-)`setTo(struct BitMaps.BitMap bitmap, uint256 index, bool value)`internal

Sets the bit at `index` to the boolean `value`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-set-struct-BitMaps-BitMap-uint256-)`set(struct BitMaps.BitMap bitmap, uint256 index)`internal

Sets the bit at `index`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#BitMaps-unset-struct-BitMaps-BitMap-uint256-)`unset(struct BitMaps.BitMap bitmap, uint256 index)`internal

Unsets the bit at `index`.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap)`EnumerableMap`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/structs/EnumerableMap.sol)

`import "@openzeppelin/contracts/utils/structs/EnumerableMap.sol";`

Library for managing an enumerable variant of Solidity’s [`mapping`](https://solidity.readthedocs.io/en/latest/types.html#mapping-types) type.

Maps have the following properties:

*   Entries are added, removed, and checked for existence in constant time (O(1)).

*   Entries are enumerated in O(n). No guarantees are made on the ordering.

*   Map can be cleared (all entries removed) in O(n).

```
contract Example {
    // Add the library methods
    using EnumerableMap for EnumerableMap.UintToAddressMap;

    // Declare a set state variable
    EnumerableMap.UintToAddressMap private myMap;
}
```

The following map types are supported:

*   `uint256 → address` (`UintToAddressMap`) since v3.0.0

*   `address → uint256` (`AddressToUintMap`) since v4.6.0

*   `bytes32 → bytes32` (`Bytes32ToBytes32Map`) since v4.6.0

*   `uint256 → uint256` (`UintToUintMap`) since v4.7.0

*   `bytes32 → uint256` (`Bytes32ToUintMap`) since v4.7.0

*   `uint256 → bytes32` (`UintToBytes32Map`) since v5.1.0

*   `address → address` (`AddressToAddressMap`) since v5.1.0

*   `address → bytes32` (`AddressToBytes32Map`) since v5.1.0

*   `bytes32 → address` (`Bytes32ToAddressMap`) since v5.1.0

*   `bytes → bytes` (`BytesToBytesMap`) since v5.4.0

Trying to delete such a structure from storage will likely result in data corruption, rendering the structure unusable. See [ethereum/solidity#11843](https://github.com/ethereum/solidity/pull/11843) for more info.

In order to clean an EnumerableMap, you can either remove all elements one by one or create a fresh instance using an array of EnumerableMap.

Functions

*   [`set(map, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-bytes32-)

*   [`remove(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)

*   [`clear(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToBytes32Map-)

*   [`contains(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)

*   [`length(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToBytes32Map-)

*   [`at(map, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToBytes32Map-uint256-)

*   [`tryGet(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)

*   [`get(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)

*   [`keys(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToBytes32Map-)

*   [`keys(map, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToBytes32Map-uint256-uint256-)

*   [`set(map, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToUintMap-uint256-uint256-)

*   [`remove(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToUintMap-uint256-)

*   [`clear(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToUintMap-)

*   [`contains(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToUintMap-uint256-)

*   [`length(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToUintMap-)

*   [`at(map, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToUintMap-uint256-)

*   [`tryGet(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToUintMap-uint256-)

*   [`get(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToUintMap-uint256-)

*   [`keys(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToUintMap-)

*   [`keys(map, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToUintMap-uint256-uint256-)

*   [`set(map, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToAddressMap-uint256-address-)

*   [`remove(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToAddressMap-uint256-)

*   [`clear(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToAddressMap-)

*   [`contains(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToAddressMap-uint256-)

*   [`length(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToAddressMap-)

*   [`at(map, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToAddressMap-uint256-)

*   [`tryGet(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToAddressMap-uint256-)

*   [`get(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToAddressMap-uint256-)

*   [`keys(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToAddressMap-)

*   [`keys(map, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToAddressMap-uint256-uint256-)

*   [`set(map, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToBytes32Map-uint256-bytes32-)

*   [`remove(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToBytes32Map-uint256-)

*   [`clear(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToBytes32Map-)

*   [`contains(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToBytes32Map-uint256-)

*   [`length(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToBytes32Map-)

*   [`at(map, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToBytes32Map-uint256-)

*   [`tryGet(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToBytes32Map-uint256-)

*   [`get(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToBytes32Map-uint256-)

*   [`keys(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToBytes32Map-)

*   [`keys(map, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToBytes32Map-uint256-uint256-)

*   [`set(map, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToUintMap-address-uint256-)

*   [`remove(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToUintMap-address-)

*   [`clear(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToUintMap-)

*   [`contains(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToUintMap-address-)

*   [`length(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToUintMap-)

*   [`at(map, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToUintMap-uint256-)

*   [`tryGet(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToUintMap-address-)

*   [`get(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToUintMap-address-)

*   [`keys(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToUintMap-)

*   [`keys(map, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToUintMap-uint256-uint256-)

*   [`set(map, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToAddressMap-address-address-)

*   [`remove(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToAddressMap-address-)

*   [`clear(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToAddressMap-)

*   [`contains(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToAddressMap-address-)

*   [`length(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToAddressMap-)

*   [`at(map, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToAddressMap-uint256-)

*   [`tryGet(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToAddressMap-address-)

*   [`get(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToAddressMap-address-)

*   [`keys(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToAddressMap-)

*   [`keys(map, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToAddressMap-uint256-uint256-)

*   [`set(map, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToBytes32Map-address-bytes32-)

*   [`remove(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToBytes32Map-address-)

*   [`clear(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToBytes32Map-)

*   [`contains(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToBytes32Map-address-)

*   [`length(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToBytes32Map-)

*   [`at(map, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToBytes32Map-uint256-)

*   [`tryGet(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToBytes32Map-address-)

*   [`get(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToBytes32Map-address-)

*   [`keys(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToBytes32Map-)

*   [`keys(map, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToBytes32Map-uint256-uint256-)

*   [`set(map, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToUintMap-bytes32-uint256-)

*   [`remove(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)

*   [`clear(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToUintMap-)

*   [`contains(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)

*   [`length(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToUintMap-)

*   [`at(map, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToUintMap-uint256-)

*   [`tryGet(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)

*   [`get(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)

*   [`keys(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToUintMap-)

*   [`keys(map, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToUintMap-uint256-uint256-)

*   [`set(map, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-address-)

*   [`remove(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)

*   [`clear(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToAddressMap-)

*   [`contains(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)

*   [`length(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToAddressMap-)

*   [`at(map, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToAddressMap-uint256-)

*   [`tryGet(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)

*   [`get(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)

*   [`keys(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToAddressMap-)

*   [`keys(map, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToAddressMap-uint256-uint256-)

*   [`set(map, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-BytesToBytesMap-bytes-bytes-)

*   [`remove(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-BytesToBytesMap-bytes-)

*   [`clear(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-BytesToBytesMap-)

*   [`contains(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-BytesToBytesMap-bytes-)

*   [`length(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-)

*   [`at(map, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-BytesToBytesMap-uint256-)

*   [`tryGet(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-BytesToBytesMap-bytes-)

*   [`get(map, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-BytesToBytesMap-bytes-)

*   [`keys(map)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-BytesToBytesMap-)

*   [`keys(map, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-BytesToBytesMap-uint256-uint256-)

Errors

*   [`EnumerableMapNonexistentKey(key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-EnumerableMapNonexistentKey-bytes32-)

*   [`EnumerableMapNonexistentBytesKey(key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-EnumerableMapNonexistentBytesKey-bytes-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-bytes32-)`set(struct EnumerableMap.Bytes32ToBytes32Map map, bytes32 key, bytes32 value) → bool`internal

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)`remove(struct EnumerableMap.Bytes32ToBytes32Map map, bytes32 key) → bool`internal

Removes a key-value pair from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToBytes32Map-)`clear(struct EnumerableMap.Bytes32ToBytes32Map map)`internal

Removes all the entries from a map. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)`contains(struct EnumerableMap.Bytes32ToBytes32Map map, bytes32 key) → bool`internal

Returns true if the key is in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToBytes32Map-)`length(struct EnumerableMap.Bytes32ToBytes32Map map) → uint256`internal

Returns the number of key-value pairs in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToBytes32Map-uint256-)`at(struct EnumerableMap.Bytes32ToBytes32Map map, uint256 index) → bytes32 key, bytes32 value`internal

Returns the key-value pair stored at position `index` in the map. O(1).

Note that there are no guarantees on the ordering of entries inside the array, and it may change when more entries are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)`tryGet(struct EnumerableMap.Bytes32ToBytes32Map map, bytes32 key) → bool exists, bytes32 value`internal

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToBytes32Map-bytes32-)`get(struct EnumerableMap.Bytes32ToBytes32Map map, bytes32 key) → bytes32`internal

Returns the value associated with `key`. O(1).

Requirements:

*   `key` must be in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToBytes32Map-)`keys(struct EnumerableMap.Bytes32ToBytes32Map map) → bytes32[]`internal

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToBytes32Map-uint256-uint256-)`keys(struct EnumerableMap.Bytes32ToBytes32Map map, uint256 start, uint256 end) → bytes32[]`internal

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToUintMap-uint256-uint256-)`set(struct EnumerableMap.UintToUintMap map, uint256 key, uint256 value) → bool`internal

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToUintMap-uint256-)`remove(struct EnumerableMap.UintToUintMap map, uint256 key) → bool`internal

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToUintMap-)`clear(struct EnumerableMap.UintToUintMap map)`internal

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToUintMap-uint256-)`contains(struct EnumerableMap.UintToUintMap map, uint256 key) → bool`internal

Returns true if the key is in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToUintMap-)`length(struct EnumerableMap.UintToUintMap map) → uint256`internal

Returns the number of elements in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToUintMap-uint256-)`at(struct EnumerableMap.UintToUintMap map, uint256 index) → uint256 key, uint256 value`internal

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToUintMap-uint256-)`tryGet(struct EnumerableMap.UintToUintMap map, uint256 key) → bool exists, uint256 value`internal

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToUintMap-uint256-)`get(struct EnumerableMap.UintToUintMap map, uint256 key) → uint256`internal

Returns the value associated with `key`. O(1).

Requirements:

*   `key` must be in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToUintMap-)`keys(struct EnumerableMap.UintToUintMap map) → uint256[]`internal

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToUintMap-uint256-uint256-)`keys(struct EnumerableMap.UintToUintMap map, uint256 start, uint256 end) → uint256[]`internal

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToAddressMap-uint256-address-)`set(struct EnumerableMap.UintToAddressMap map, uint256 key, address value) → bool`internal

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToAddressMap-uint256-)`remove(struct EnumerableMap.UintToAddressMap map, uint256 key) → bool`internal

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToAddressMap-)`clear(struct EnumerableMap.UintToAddressMap map)`internal

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToAddressMap-uint256-)`contains(struct EnumerableMap.UintToAddressMap map, uint256 key) → bool`internal

Returns true if the key is in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToAddressMap-)`length(struct EnumerableMap.UintToAddressMap map) → uint256`internal

Returns the number of elements in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToAddressMap-uint256-)`at(struct EnumerableMap.UintToAddressMap map, uint256 index) → uint256 key, address value`internal

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToAddressMap-uint256-)`tryGet(struct EnumerableMap.UintToAddressMap map, uint256 key) → bool exists, address value`internal

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToAddressMap-uint256-)`get(struct EnumerableMap.UintToAddressMap map, uint256 key) → address`internal

Returns the value associated with `key`. O(1).

Requirements:

*   `key` must be in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToAddressMap-)`keys(struct EnumerableMap.UintToAddressMap map) → uint256[]`internal

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToAddressMap-uint256-uint256-)`keys(struct EnumerableMap.UintToAddressMap map, uint256 start, uint256 end) → uint256[]`internal

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-UintToBytes32Map-uint256-bytes32-)`set(struct EnumerableMap.UintToBytes32Map map, uint256 key, bytes32 value) → bool`internal

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-UintToBytes32Map-uint256-)`remove(struct EnumerableMap.UintToBytes32Map map, uint256 key) → bool`internal

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-UintToBytes32Map-)`clear(struct EnumerableMap.UintToBytes32Map map)`internal

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-UintToBytes32Map-uint256-)`contains(struct EnumerableMap.UintToBytes32Map map, uint256 key) → bool`internal

Returns true if the key is in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-UintToBytes32Map-)`length(struct EnumerableMap.UintToBytes32Map map) → uint256`internal

Returns the number of elements in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-UintToBytes32Map-uint256-)`at(struct EnumerableMap.UintToBytes32Map map, uint256 index) → uint256 key, bytes32 value`internal

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-UintToBytes32Map-uint256-)`tryGet(struct EnumerableMap.UintToBytes32Map map, uint256 key) → bool exists, bytes32 value`internal

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-UintToBytes32Map-uint256-)`get(struct EnumerableMap.UintToBytes32Map map, uint256 key) → bytes32`internal

Returns the value associated with `key`. O(1).

Requirements:

*   `key` must be in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToBytes32Map-)`keys(struct EnumerableMap.UintToBytes32Map map) → uint256[]`internal

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-UintToBytes32Map-uint256-uint256-)`keys(struct EnumerableMap.UintToBytes32Map map, uint256 start, uint256 end) → uint256[]`internal

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToUintMap-address-uint256-)`set(struct EnumerableMap.AddressToUintMap map, address key, uint256 value) → bool`internal

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToUintMap-address-)`remove(struct EnumerableMap.AddressToUintMap map, address key) → bool`internal

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToUintMap-)`clear(struct EnumerableMap.AddressToUintMap map)`internal

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToUintMap-address-)`contains(struct EnumerableMap.AddressToUintMap map, address key) → bool`internal

Returns true if the key is in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToUintMap-)`length(struct EnumerableMap.AddressToUintMap map) → uint256`internal

Returns the number of elements in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToUintMap-uint256-)`at(struct EnumerableMap.AddressToUintMap map, uint256 index) → address key, uint256 value`internal

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToUintMap-address-)`tryGet(struct EnumerableMap.AddressToUintMap map, address key) → bool exists, uint256 value`internal

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToUintMap-address-)`get(struct EnumerableMap.AddressToUintMap map, address key) → uint256`internal

Returns the value associated with `key`. O(1).

Requirements:

*   `key` must be in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToUintMap-)`keys(struct EnumerableMap.AddressToUintMap map) → address[]`internal

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToUintMap-uint256-uint256-)`keys(struct EnumerableMap.AddressToUintMap map, uint256 start, uint256 end) → address[]`internal

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToAddressMap-address-address-)`set(struct EnumerableMap.AddressToAddressMap map, address key, address value) → bool`internal

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToAddressMap-address-)`remove(struct EnumerableMap.AddressToAddressMap map, address key) → bool`internal

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToAddressMap-)`clear(struct EnumerableMap.AddressToAddressMap map)`internal

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToAddressMap-address-)`contains(struct EnumerableMap.AddressToAddressMap map, address key) → bool`internal

Returns true if the key is in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToAddressMap-)`length(struct EnumerableMap.AddressToAddressMap map) → uint256`internal

Returns the number of elements in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToAddressMap-uint256-)`at(struct EnumerableMap.AddressToAddressMap map, uint256 index) → address key, address value`internal

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToAddressMap-address-)`tryGet(struct EnumerableMap.AddressToAddressMap map, address key) → bool exists, address value`internal

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToAddressMap-address-)`get(struct EnumerableMap.AddressToAddressMap map, address key) → address`internal

Returns the value associated with `key`. O(1).

Requirements:

*   `key` must be in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToAddressMap-)`keys(struct EnumerableMap.AddressToAddressMap map) → address[]`internal

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToAddressMap-uint256-uint256-)`keys(struct EnumerableMap.AddressToAddressMap map, uint256 start, uint256 end) → address[]`internal

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-AddressToBytes32Map-address-bytes32-)`set(struct EnumerableMap.AddressToBytes32Map map, address key, bytes32 value) → bool`internal

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-AddressToBytes32Map-address-)`remove(struct EnumerableMap.AddressToBytes32Map map, address key) → bool`internal

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-AddressToBytes32Map-)`clear(struct EnumerableMap.AddressToBytes32Map map)`internal

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-AddressToBytes32Map-address-)`contains(struct EnumerableMap.AddressToBytes32Map map, address key) → bool`internal

Returns true if the key is in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-AddressToBytes32Map-)`length(struct EnumerableMap.AddressToBytes32Map map) → uint256`internal

Returns the number of elements in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-AddressToBytes32Map-uint256-)`at(struct EnumerableMap.AddressToBytes32Map map, uint256 index) → address key, bytes32 value`internal

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-AddressToBytes32Map-address-)`tryGet(struct EnumerableMap.AddressToBytes32Map map, address key) → bool exists, bytes32 value`internal

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-AddressToBytes32Map-address-)`get(struct EnumerableMap.AddressToBytes32Map map, address key) → bytes32`internal

Returns the value associated with `key`. O(1).

Requirements:

*   `key` must be in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToBytes32Map-)`keys(struct EnumerableMap.AddressToBytes32Map map) → address[]`internal

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-AddressToBytes32Map-uint256-uint256-)`keys(struct EnumerableMap.AddressToBytes32Map map, uint256 start, uint256 end) → address[]`internal

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToUintMap-bytes32-uint256-)`set(struct EnumerableMap.Bytes32ToUintMap map, bytes32 key, uint256 value) → bool`internal

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)`remove(struct EnumerableMap.Bytes32ToUintMap map, bytes32 key) → bool`internal

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToUintMap-)`clear(struct EnumerableMap.Bytes32ToUintMap map)`internal

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)`contains(struct EnumerableMap.Bytes32ToUintMap map, bytes32 key) → bool`internal

Returns true if the key is in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToUintMap-)`length(struct EnumerableMap.Bytes32ToUintMap map) → uint256`internal

Returns the number of elements in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToUintMap-uint256-)`at(struct EnumerableMap.Bytes32ToUintMap map, uint256 index) → bytes32 key, uint256 value`internal

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)`tryGet(struct EnumerableMap.Bytes32ToUintMap map, bytes32 key) → bool exists, uint256 value`internal

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToUintMap-bytes32-)`get(struct EnumerableMap.Bytes32ToUintMap map, bytes32 key) → uint256`internal

Returns the value associated with `key`. O(1).

Requirements:

*   `key` must be in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToUintMap-)`keys(struct EnumerableMap.Bytes32ToUintMap map) → bytes32[]`internal

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToUintMap-uint256-uint256-)`keys(struct EnumerableMap.Bytes32ToUintMap map, uint256 start, uint256 end) → bytes32[]`internal

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-address-)`set(struct EnumerableMap.Bytes32ToAddressMap map, bytes32 key, address value) → bool`internal

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)`remove(struct EnumerableMap.Bytes32ToAddressMap map, bytes32 key) → bool`internal

Removes a value from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-Bytes32ToAddressMap-)`clear(struct EnumerableMap.Bytes32ToAddressMap map)`internal

Removes all the entries from a map. O(n).

This function has an unbounded cost that scales with map size. Developers should keep in mind that using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)`contains(struct EnumerableMap.Bytes32ToAddressMap map, bytes32 key) → bool`internal

Returns true if the key is in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-Bytes32ToAddressMap-)`length(struct EnumerableMap.Bytes32ToAddressMap map) → uint256`internal

Returns the number of elements in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-Bytes32ToAddressMap-uint256-)`at(struct EnumerableMap.Bytes32ToAddressMap map, uint256 index) → bytes32 key, address value`internal

Returns the element stored at position `index` in the map. O(1). Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)`tryGet(struct EnumerableMap.Bytes32ToAddressMap map, bytes32 key) → bool exists, address value`internal

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-Bytes32ToAddressMap-bytes32-)`get(struct EnumerableMap.Bytes32ToAddressMap map, bytes32 key) → address`internal

Returns the value associated with `key`. O(1).

Requirements:

*   `key` must be in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToAddressMap-)`keys(struct EnumerableMap.Bytes32ToAddressMap map) → bytes32[]`internal

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-Bytes32ToAddressMap-uint256-uint256-)`keys(struct EnumerableMap.Bytes32ToAddressMap map, uint256 start, uint256 end) → bytes32[]`internal

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-set-struct-EnumerableMap-BytesToBytesMap-bytes-bytes-)`set(struct EnumerableMap.BytesToBytesMap map, bytes key, bytes value) → bool`internal

Adds a key-value pair to a map, or updates the value for an existing key. O(1).

Returns true if the key was added to the map, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-remove-struct-EnumerableMap-BytesToBytesMap-bytes-)`remove(struct EnumerableMap.BytesToBytesMap map, bytes key) → bool`internal

Removes a key-value pair from a map. O(1).

Returns true if the key was removed from the map, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-clear-struct-EnumerableMap-BytesToBytesMap-)`clear(struct EnumerableMap.BytesToBytesMap map)`internal

Removes all the entries from a map. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the map grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-contains-struct-EnumerableMap-BytesToBytesMap-bytes-)`contains(struct EnumerableMap.BytesToBytesMap map, bytes key) → bool`internal

Returns true if the key is in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-)`length(struct EnumerableMap.BytesToBytesMap map) → uint256`internal

Returns the number of key-value pairs in the map. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-at-struct-EnumerableMap-BytesToBytesMap-uint256-)`at(struct EnumerableMap.BytesToBytesMap map, uint256 index) → bytes key, bytes value`internal

Returns the key-value pair stored at position `index` in the map. O(1).

Note that there are no guarantees on the ordering of entries inside the array, and it may change when more entries are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-length-struct-EnumerableMap-BytesToBytesMap-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-tryGet-struct-EnumerableMap-BytesToBytesMap-bytes-)`tryGet(struct EnumerableMap.BytesToBytesMap map, bytes key) → bool exists, bytes value`internal

Tries to return the value associated with `key`. O(1). Does not revert if `key` is not in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-get-struct-EnumerableMap-BytesToBytesMap-bytes-)`get(struct EnumerableMap.BytesToBytesMap map, bytes key) → bytes value`internal

Returns the value associated with `key`. O(1).

Requirements:

*   `key` must be in the map.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-BytesToBytesMap-)`keys(struct EnumerableMap.BytesToBytesMap map) → bytes[]`internal

Returns an array containing all the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-keys-struct-EnumerableMap-BytesToBytesMap-uint256-uint256-)`keys(struct EnumerableMap.BytesToBytesMap map, uint256 start, uint256 end) → bytes[]`internal

Returns an array containing a slice of the keys

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the map grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-EnumerableMapNonexistentKey-bytes32-)`EnumerableMapNonexistentKey(bytes32 key)`error

Query for a nonexistent map key.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableMap-EnumerableMapNonexistentBytesKey-bytes-)`EnumerableMapNonexistentBytesKey(bytes key)`error

Query for a nonexistent map key.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet)`EnumerableSet`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/structs/EnumerableSet.sol)

`import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";`

Library for managing [sets](https://en.wikipedia.org/wiki/Set_(abstract_data_type)) of primitive types.

Sets have the following properties:

*   Elements are added, removed, and checked for existence in constant time (O(1)).

*   Elements are enumerated in O(n). No guarantees are made on the ordering.

*   Set can be cleared (all elements removed) in O(n).

```
contract Example {
    // Add the library methods
    using EnumerableSet for EnumerableSet.AddressSet;

    // Declare a set state variable
    EnumerableSet.AddressSet private mySet;
}
```

The following types are supported:

*   `bytes32` (`Bytes32Set`) since v3.3.0

*   `address` (`AddressSet`) since v3.3.0

*   `uint256` (`UintSet`) since v3.3.0

*   `string` (`StringSet`) since v5.4.0

*   `bytes` (`BytesSet`) since v5.4.0

Trying to delete such a structure from storage will likely result in data corruption, rendering the structure unusable. See [ethereum/solidity#11843](https://github.com/ethereum/solidity/pull/11843) for more info.

In order to clean an EnumerableSet, you can either remove all elements one by one or create a fresh instance using an array of EnumerableSet.

Functions

*   [`add(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-Bytes32Set-bytes32-)

*   [`remove(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-Bytes32Set-bytes32-)

*   [`clear(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-Bytes32Set-)

*   [`contains(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-Bytes32Set-bytes32-)

*   [`length(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-Bytes32Set-)

*   [`at(set, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-Bytes32Set-uint256-)

*   [`values(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes32Set-)

*   [`values(set, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes32Set-uint256-uint256-)

*   [`add(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-AddressSet-address-)

*   [`remove(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-AddressSet-address-)

*   [`clear(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-AddressSet-)

*   [`contains(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-AddressSet-address-)

*   [`length(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-AddressSet-)

*   [`at(set, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-AddressSet-uint256-)

*   [`values(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-AddressSet-)

*   [`values(set, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-AddressSet-uint256-uint256-)

*   [`add(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-UintSet-uint256-)

*   [`remove(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-UintSet-uint256-)

*   [`clear(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-UintSet-)

*   [`contains(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-UintSet-uint256-)

*   [`length(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-UintSet-)

*   [`at(set, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-UintSet-uint256-)

*   [`values(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-UintSet-)

*   [`values(set, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-UintSet-uint256-uint256-)

*   [`add(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-StringSet-string-)

*   [`remove(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-StringSet-string-)

*   [`clear(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-StringSet-)

*   [`contains(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-StringSet-string-)

*   [`length(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-StringSet-)

*   [`at(set, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-StringSet-uint256-)

*   [`values(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-StringSet-)

*   [`values(set, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-StringSet-uint256-uint256-)

*   [`add(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-BytesSet-bytes-)

*   [`remove(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-BytesSet-bytes-)

*   [`clear(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-BytesSet-)

*   [`contains(set, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-BytesSet-bytes-)

*   [`length(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-BytesSet-)

*   [`at(set, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-BytesSet-uint256-)

*   [`values(set)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-BytesSet-)

*   [`values(set, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-BytesSet-uint256-uint256-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-Bytes32Set-bytes32-)`add(struct EnumerableSet.Bytes32Set set, bytes32 value) → bool`internal

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-Bytes32Set-bytes32-)`remove(struct EnumerableSet.Bytes32Set set, bytes32 value) → bool`internal

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-Bytes32Set-)`clear(struct EnumerableSet.Bytes32Set set)`internal

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-Bytes32Set-bytes32-)`contains(struct EnumerableSet.Bytes32Set set, bytes32 value) → bool`internal

Returns true if the value is in the set. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-Bytes32Set-)`length(struct EnumerableSet.Bytes32Set set) → uint256`internal

Returns the number of values in the set. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-Bytes32Set-uint256-)`at(struct EnumerableSet.Bytes32Set set, uint256 index) → bytes32`internal

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-BytesSet-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes32Set-)`values(struct EnumerableSet.Bytes32Set set) → bytes32[]`internal

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-Bytes32Set-uint256-uint256-)`values(struct EnumerableSet.Bytes32Set set, uint256 start, uint256 end) → bytes32[]`internal

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-AddressSet-address-)`add(struct EnumerableSet.AddressSet set, address value) → bool`internal

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-AddressSet-address-)`remove(struct EnumerableSet.AddressSet set, address value) → bool`internal

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-AddressSet-)`clear(struct EnumerableSet.AddressSet set)`internal

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-AddressSet-address-)`contains(struct EnumerableSet.AddressSet set, address value) → bool`internal

Returns true if the value is in the set. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-AddressSet-)`length(struct EnumerableSet.AddressSet set) → uint256`internal

Returns the number of values in the set. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-AddressSet-uint256-)`at(struct EnumerableSet.AddressSet set, uint256 index) → address`internal

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-BytesSet-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-AddressSet-)`values(struct EnumerableSet.AddressSet set) → address[]`internal

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-AddressSet-uint256-uint256-)`values(struct EnumerableSet.AddressSet set, uint256 start, uint256 end) → address[]`internal

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-UintSet-uint256-)`add(struct EnumerableSet.UintSet set, uint256 value) → bool`internal

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-UintSet-uint256-)`remove(struct EnumerableSet.UintSet set, uint256 value) → bool`internal

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-UintSet-)`clear(struct EnumerableSet.UintSet set)`internal

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-UintSet-uint256-)`contains(struct EnumerableSet.UintSet set, uint256 value) → bool`internal

Returns true if the value is in the set. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-UintSet-)`length(struct EnumerableSet.UintSet set) → uint256`internal

Returns the number of values in the set. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-UintSet-uint256-)`at(struct EnumerableSet.UintSet set, uint256 index) → uint256`internal

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-BytesSet-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-UintSet-)`values(struct EnumerableSet.UintSet set) → uint256[]`internal

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-UintSet-uint256-uint256-)`values(struct EnumerableSet.UintSet set, uint256 start, uint256 end) → uint256[]`internal

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-StringSet-string-)`add(struct EnumerableSet.StringSet set, string value) → bool`internal

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-StringSet-string-)`remove(struct EnumerableSet.StringSet set, string value) → bool`internal

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-StringSet-)`clear(struct EnumerableSet.StringSet set)`internal

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-StringSet-string-)`contains(struct EnumerableSet.StringSet set, string value) → bool`internal

Returns true if the value is in the set. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-StringSet-)`length(struct EnumerableSet.StringSet set) → uint256`internal

Returns the number of values on the set. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-StringSet-uint256-)`at(struct EnumerableSet.StringSet set, uint256 index) → string`internal

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-BytesSet-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-StringSet-)`values(struct EnumerableSet.StringSet set) → string[]`internal

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-StringSet-uint256-uint256-)`values(struct EnumerableSet.StringSet set, uint256 start, uint256 end) → string[]`internal

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-add-struct-EnumerableSet-BytesSet-bytes-)`add(struct EnumerableSet.BytesSet set, bytes value) → bool`internal

Add a value to a set. O(1).

Returns true if the value was added to the set, that is if it was not already present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-remove-struct-EnumerableSet-BytesSet-bytes-)`remove(struct EnumerableSet.BytesSet set, bytes value) → bool`internal

Removes a value from a set. O(1).

Returns true if the value was removed from the set, that is if it was present.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-clear-struct-EnumerableSet-BytesSet-)`clear(struct EnumerableSet.BytesSet set)`internal

Removes all the values from a set. O(n).

Developers should keep in mind that this function has an unbounded cost and using it may render the function uncallable if the set grows to the point where clearing it consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-contains-struct-EnumerableSet-BytesSet-bytes-)`contains(struct EnumerableSet.BytesSet set, bytes value) → bool`internal

Returns true if the value is in the set. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-BytesSet-)`length(struct EnumerableSet.BytesSet set) → uint256`internal

Returns the number of values on the set. O(1).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-at-struct-EnumerableSet-BytesSet-uint256-)`at(struct EnumerableSet.BytesSet set, uint256 index) → bytes`internal

Returns the value stored at position `index` in the set. O(1).

Note that there are no guarantees on the ordering of values inside the array, and it may change when more values are added or removed.

Requirements:

*   `index` must be strictly less than [`length`](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-length-struct-EnumerableSet-BytesSet-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-BytesSet-)`values(struct EnumerableSet.BytesSet set) → bytes[]`internal

Return the entire set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#EnumerableSet-values-struct-EnumerableSet-BytesSet-uint256-uint256-)`values(struct EnumerableSet.BytesSet set, uint256 start, uint256 end) → bytes[]`internal

Return a slice of the set in an array

This operation will copy the entire storage to memory, which can be quite expensive. This is designed to mostly be used by view accessors that are queried without any gas fees. Developers should keep in mind that this function has an unbounded cost, and using it as part of a state-changing function may render the function uncallable if the set grows to a point where copying to memory consumes too much gas to fit in a block.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue)`DoubleEndedQueue`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/structs/DoubleEndedQueue.sol)

`import "@openzeppelin/contracts/utils/structs/DoubleEndedQueue.sol";`

A sequence of items with the ability to efficiently push and pop items (i.e. insert and remove) on both ends of the sequence (called front and back). Among other access patterns, it can be used to implement efficient LIFO and FIFO queues. Storage use is optimized, and all operations are O(1) constant time. This includes [`clear`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-clear-struct-DoubleEndedQueue-Bytes32Deque-), given that the existing queue contents are left in storage.

The struct is called `Bytes32Deque`. Other types can be cast to and from `bytes32`. This data structure can only be used in storage, and not in memory.

`DoubleEndedQueue.Bytes32Deque queue;`

Functions

*   [`pushBack(deque, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-pushBack-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)

*   [`popBack(deque)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-popBack-struct-DoubleEndedQueue-Bytes32Deque-)

*   [`pushFront(deque, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-pushFront-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)

*   [`popFront(deque)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-popFront-struct-DoubleEndedQueue-Bytes32Deque-)

*   [`front(deque)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-front-struct-DoubleEndedQueue-Bytes32Deque-)

*   [`back(deque)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-back-struct-DoubleEndedQueue-Bytes32Deque-)

*   [`at(deque, index)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-at-struct-DoubleEndedQueue-Bytes32Deque-uint256-)

*   [`clear(deque)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-clear-struct-DoubleEndedQueue-Bytes32Deque-)

*   [`length(deque)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-length-struct-DoubleEndedQueue-Bytes32Deque-)

*   [`empty(deque)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-empty-struct-DoubleEndedQueue-Bytes32Deque-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-pushBack-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)`pushBack(struct DoubleEndedQueue.Bytes32Deque deque, bytes32 value)`internal

Inserts an item at the end of the queue.

Reverts with [`Panic.RESOURCE_ERROR`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-RESOURCE_ERROR-uint256) if the queue is full.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-popBack-struct-DoubleEndedQueue-Bytes32Deque-)`popBack(struct DoubleEndedQueue.Bytes32Deque deque) → bytes32 value`internal

Removes the item at the end of the queue and returns it.

Reverts with [`Panic.EMPTY_ARRAY_POP`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-EMPTY_ARRAY_POP-uint256) if the queue is empty.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-pushFront-struct-DoubleEndedQueue-Bytes32Deque-bytes32-)`pushFront(struct DoubleEndedQueue.Bytes32Deque deque, bytes32 value)`internal

Inserts an item at the beginning of the queue.

Reverts with [`Panic.RESOURCE_ERROR`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-RESOURCE_ERROR-uint256) if the queue is full.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-popFront-struct-DoubleEndedQueue-Bytes32Deque-)`popFront(struct DoubleEndedQueue.Bytes32Deque deque) → bytes32 value`internal

Removes the item at the beginning of the queue and returns it.

Reverts with [`Panic.EMPTY_ARRAY_POP`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-EMPTY_ARRAY_POP-uint256) if the queue is empty.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-front-struct-DoubleEndedQueue-Bytes32Deque-)`front(struct DoubleEndedQueue.Bytes32Deque deque) → bytes32 value`internal

Returns the item at the beginning of the queue.

Reverts with [`Panic.ARRAY_OUT_OF_BOUNDS`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ARRAY_OUT_OF_BOUNDS-uint256) if the queue is empty.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-back-struct-DoubleEndedQueue-Bytes32Deque-)`back(struct DoubleEndedQueue.Bytes32Deque deque) → bytes32 value`internal

Returns the item at the end of the queue.

Reverts with [`Panic.ARRAY_OUT_OF_BOUNDS`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ARRAY_OUT_OF_BOUNDS-uint256) if the queue is empty.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-at-struct-DoubleEndedQueue-Bytes32Deque-uint256-)`at(struct DoubleEndedQueue.Bytes32Deque deque, uint256 index) → bytes32 value`internal

Return the item at a position in the queue given by `index`, with the first item at 0 and last item at `length(deque) - 1`.

Reverts with [`Panic.ARRAY_OUT_OF_BOUNDS`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ARRAY_OUT_OF_BOUNDS-uint256) if the index is out of bounds.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-clear-struct-DoubleEndedQueue-Bytes32Deque-)`clear(struct DoubleEndedQueue.Bytes32Deque deque)`internal

Resets the queue back to being empty.

The current items are left behind in storage. This does not affect the functioning of the queue, but misses out on potential gas refunds.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-length-struct-DoubleEndedQueue-Bytes32Deque-)`length(struct DoubleEndedQueue.Bytes32Deque deque) → uint256`internal

Returns the number of items in the queue.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#DoubleEndedQueue-empty-struct-DoubleEndedQueue-Bytes32Deque-)`empty(struct DoubleEndedQueue.Bytes32Deque deque) → bool`internal

Returns true if the queue is empty.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer)`CircularBuffer`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/structs/CircularBuffer.sol)

`import "@openzeppelin/contracts/utils/structs/CircularBuffer.sol";`

A fixed-size buffer for keeping `bytes32` items in storage.

This data structure allows for pushing elements to it, and when its length exceeds the specified fixed size, new items take the place of the oldest element in the buffer, keeping at most `N` elements in the structure.

Elements can’t be removed but the data structure can be cleared. See [`clear`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-clear-struct-CircularBuffer-Bytes32CircularBuffer-).

Complexity: - insertion ([`push`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-push-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)): O(1) - lookup ([`last`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-last-struct-CircularBuffer-Bytes32CircularBuffer-uint256-)): O(1) - inclusion ([`includes`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-includes-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)): O(N) (worst case) - reset ([`clear`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-clear-struct-CircularBuffer-Bytes32CircularBuffer-)): O(1)

*   The struct is called `Bytes32CircularBuffer`. Other types can be cast to and from `bytes32`. This data structure can only be used in storage, and not in memory.

Example usage:

```
contract Example {
    // Add the library methods
    using CircularBuffer for CircularBuffer.Bytes32CircularBuffer;

    // Declare a buffer storage variable
    CircularBuffer.Bytes32CircularBuffer private myBuffer;
}
```

_Available since v5.1._

Functions

*   [`setup(self, size)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-setup-struct-CircularBuffer-Bytes32CircularBuffer-uint256-)

*   [`clear(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-clear-struct-CircularBuffer-Bytes32CircularBuffer-)

*   [`push(self, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-push-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)

*   [`count(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-count-struct-CircularBuffer-Bytes32CircularBuffer-)

*   [`length(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-length-struct-CircularBuffer-Bytes32CircularBuffer-)

*   [`last(self, i)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-last-struct-CircularBuffer-Bytes32CircularBuffer-uint256-)

*   [`includes(self, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-includes-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-setup-struct-CircularBuffer-Bytes32CircularBuffer-uint256-)`setup(struct CircularBuffer.Bytes32CircularBuffer self, uint256 size)`internal

Initialize a new CircularBuffer of a given size.

If the CircularBuffer was already setup and used, calling that function again will reset it to a blank state.

The size of the buffer will affect the execution of [`includes`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-includes-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-) function, as it has a complexity of O(N). Consider a large buffer size may render the function unusable.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-clear-struct-CircularBuffer-Bytes32CircularBuffer-)`clear(struct CircularBuffer.Bytes32CircularBuffer self)`internal

Clear all data in the buffer without resetting memory, keeping the existing size.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-push-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)`push(struct CircularBuffer.Bytes32CircularBuffer self, bytes32 value)`internal

Push a new value to the buffer. If the buffer is already full, the new value replaces the oldest value in the buffer.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-count-struct-CircularBuffer-Bytes32CircularBuffer-)`count(struct CircularBuffer.Bytes32CircularBuffer self) → uint256`internal

Number of values currently in the buffer. This value is 0 for an empty buffer, and cannot exceed the size of the buffer.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-length-struct-CircularBuffer-Bytes32CircularBuffer-)`length(struct CircularBuffer.Bytes32CircularBuffer self) → uint256`internal

Length of the buffer. This is the maximum number of elements kept in the buffer.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-last-struct-CircularBuffer-Bytes32CircularBuffer-uint256-)`last(struct CircularBuffer.Bytes32CircularBuffer self, uint256 i) → bytes32`internal

Getter for the i-th value in the buffer, from the end.

Reverts with [`Panic.ARRAY_OUT_OF_BOUNDS`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ARRAY_OUT_OF_BOUNDS-uint256) if trying to access an element that was not pushed, or that was dropped to make room for newer elements.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-includes-struct-CircularBuffer-Bytes32CircularBuffer-bytes32-)`includes(struct CircularBuffer.Bytes32CircularBuffer self, bytes32 value) → bool`internal

Check if a given value is in the buffer.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CircularBuffer-InvalidBufferSize--)`InvalidBufferSize()`error

Error emitted when trying to setup a buffer with a size of 0.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints)`Checkpoints`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/structs/Checkpoints.sol)

`import "@openzeppelin/contracts/utils/structs/Checkpoints.sol";`

This library defines the `Trace*` struct, for checkpointing values as they change at different points in time, and later looking up past values by block number. See [`Votes`](https://docs.openzeppelin.com/contracts/5.x/api/governance#Votes) as an example.

To create a history of checkpoints define a variable type `Checkpoints.Trace*` in your contract, and store a new checkpoint for the current transaction block using the [`push`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace160-uint96-uint160-) function.

Functions

*   [`push(self, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace224-uint32-uint224-)

*   [`lowerLookup(self, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace224-uint32-)

*   [`upperLookup(self, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace224-uint32-)

*   [`upperLookupRecent(self, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace224-uint32-)

*   [`latest(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace224-)

*   [`latestCheckpoint(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace224-)

*   [`length(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace224-)

*   [`at(self, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace224-uint32-)

*   [`push(self, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace208-uint48-uint208-)

*   [`lowerLookup(self, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace208-uint48-)

*   [`upperLookup(self, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace208-uint48-)

*   [`upperLookupRecent(self, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace208-uint48-)

*   [`latest(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace208-)

*   [`latestCheckpoint(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace208-)

*   [`length(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace208-)

*   [`at(self, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace208-uint32-)

*   [`push(self, key, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace160-uint96-uint160-)

*   [`lowerLookup(self, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace160-uint96-)

*   [`upperLookup(self, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-)

*   [`upperLookupRecent(self, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace160-uint96-)

*   [`latest(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace160-)

*   [`latestCheckpoint(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace160-)

*   [`length(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace160-)

*   [`at(self, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace160-uint32-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace224-uint32-uint224-)`push(struct Checkpoints.Trace224 self, uint32 key, uint224 value) → uint224 oldValue, uint224 newValue`internal

Pushes a (`key`, `value`) pair into a Trace224 so that it is stored as the checkpoint.

Returns previous value and new value.

Never accept `key` as a user input, since an arbitrary `type(uint32).max` key set will disable the library.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace224-uint32-)`lowerLookup(struct Checkpoints.Trace224 self, uint32 key) → uint224`internal

Returns the value in the first (oldest) checkpoint with key greater or equal than the search key, or zero if there is none.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace224-uint32-)`upperLookup(struct Checkpoints.Trace224 self, uint32 key) → uint224`internal

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace224-uint32-)`upperLookupRecent(struct Checkpoints.Trace224 self, uint32 key) → uint224`internal

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

This is a variant of [`upperLookup`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-) that is optimized to find "recent" checkpoint (checkpoints with high keys).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace224-)`latest(struct Checkpoints.Trace224 self) → uint224`internal

Returns the value in the most recent checkpoint, or zero if there are no checkpoints.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace224-)`latestCheckpoint(struct Checkpoints.Trace224 self) → bool exists, uint32 _key, uint224 _value`internal

Returns whether there is a checkpoint in the structure (i.e. it is not empty), and if so the key and value in the most recent checkpoint.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace224-)`length(struct Checkpoints.Trace224 self) → uint256`internal

Returns the number of checkpoints.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace224-uint32-)`at(struct Checkpoints.Trace224 self, uint32 pos) → struct Checkpoints.Checkpoint224`internal

Returns checkpoint at given position.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace208-uint48-uint208-)`push(struct Checkpoints.Trace208 self, uint48 key, uint208 value) → uint208 oldValue, uint208 newValue`internal

Pushes a (`key`, `value`) pair into a Trace208 so that it is stored as the checkpoint.

Returns previous value and new value.

Never accept `key` as a user input, since an arbitrary `type(uint48).max` key set will disable the library.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace208-uint48-)`lowerLookup(struct Checkpoints.Trace208 self, uint48 key) → uint208`internal

Returns the value in the first (oldest) checkpoint with key greater or equal than the search key, or zero if there is none.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace208-uint48-)`upperLookup(struct Checkpoints.Trace208 self, uint48 key) → uint208`internal

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace208-uint48-)`upperLookupRecent(struct Checkpoints.Trace208 self, uint48 key) → uint208`internal

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

This is a variant of [`upperLookup`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-) that is optimized to find "recent" checkpoint (checkpoints with high keys).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace208-)`latest(struct Checkpoints.Trace208 self) → uint208`internal

Returns the value in the most recent checkpoint, or zero if there are no checkpoints.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace208-)`latestCheckpoint(struct Checkpoints.Trace208 self) → bool exists, uint48 _key, uint208 _value`internal

Returns whether there is a checkpoint in the structure (i.e. it is not empty), and if so the key and value in the most recent checkpoint.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace208-)`length(struct Checkpoints.Trace208 self) → uint256`internal

Returns the number of checkpoints.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace208-uint32-)`at(struct Checkpoints.Trace208 self, uint32 pos) → struct Checkpoints.Checkpoint208`internal

Returns checkpoint at given position.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-push-struct-Checkpoints-Trace160-uint96-uint160-)`push(struct Checkpoints.Trace160 self, uint96 key, uint160 value) → uint160 oldValue, uint160 newValue`internal

Pushes a (`key`, `value`) pair into a Trace160 so that it is stored as the checkpoint.

Returns previous value and new value.

Never accept `key` as a user input, since an arbitrary `type(uint96).max` key set will disable the library.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-lowerLookup-struct-Checkpoints-Trace160-uint96-)`lowerLookup(struct Checkpoints.Trace160 self, uint96 key) → uint160`internal

Returns the value in the first (oldest) checkpoint with key greater or equal than the search key, or zero if there is none.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-)`upperLookup(struct Checkpoints.Trace160 self, uint96 key) → uint160`internal

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookupRecent-struct-Checkpoints-Trace160-uint96-)`upperLookupRecent(struct Checkpoints.Trace160 self, uint96 key) → uint160`internal

Returns the value in the last (most recent) checkpoint with key lower or equal than the search key, or zero if there is none.

This is a variant of [`upperLookup`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-upperLookup-struct-Checkpoints-Trace160-uint96-) that is optimized to find "recent" checkpoint (checkpoints with high keys).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latest-struct-Checkpoints-Trace160-)`latest(struct Checkpoints.Trace160 self) → uint160`internal

Returns the value in the most recent checkpoint, or zero if there are no checkpoints.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-latestCheckpoint-struct-Checkpoints-Trace160-)`latestCheckpoint(struct Checkpoints.Trace160 self) → bool exists, uint96 _key, uint160 _value`internal

Returns whether there is a checkpoint in the structure (i.e. it is not empty), and if so the key and value in the most recent checkpoint.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-length-struct-Checkpoints-Trace160-)`length(struct Checkpoints.Trace160 self) → uint256`internal

Returns the number of checkpoints.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-at-struct-Checkpoints-Trace160-uint32-)`at(struct Checkpoints.Trace160 self, uint32 pos) → struct Checkpoints.Checkpoint160`internal

Returns checkpoint at given position.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Checkpoints-CheckpointUnorderedInsertion--)`CheckpointUnorderedInsertion()`error

A value was attempted to be inserted on a past checkpoint.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap)`Heap`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/structs/Heap.sol)

`import "@openzeppelin/contracts/utils/structs/Heap.sol";`

Heaps are represented as a tree of values where the first element (index 0) is the root, and where the node at index i is the child of the node at index (i-1)/2 and the parent of nodes at index 2*i+1 and 2*i+2. Each node stores an element of the heap.

The structure is ordered so that each node is bigger than its parent. An immediate consequence is that the highest priority value is the one at the root. This value can be looked up in constant time (O(1)) at `heap.tree[0]`

The structure is designed to perform the following operations with the corresponding complexities:

*   peek (get the highest priority value): O(1)

*   insert (insert a value): O(log(n))

*   pop (remove the highest priority value): O(log(n))

*   replace (replace the highest priority value with a new value): O(log(n))

*   length (get the number of elements): O(1)

*   clear (remove all elements): O(1)

This library allows for the use of custom comparator functions. Given that manipulating memory can lead to unexpected behavior. Consider verifying that the comparator does not manipulate the Heap’s state directly and that it follows the Solidity memory safety rules.

_Available since v5.1._

Functions

*   [`peek(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-peek-struct-Heap-Uint256Heap-)

*   [`pop(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-)

*   [`pop(self, comp)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-function%E2%80%94%E2%80%8Buint256-uint256%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbool--)

*   [`insert(self, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-)

*   [`insert(self, value, comp)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-function%E2%80%94%E2%80%8Buint256-uint256%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbool--)

*   [`replace(self, newValue)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-replace-struct-Heap-Uint256Heap-uint256-)

*   [`replace(self, newValue, comp)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-replace-struct-Heap-Uint256Heap-uint256-function%E2%80%94%E2%80%8Buint256-uint256%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbool--)

*   [`length(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-length-struct-Heap-Uint256Heap-)

*   [`clear(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-clear-struct-Heap-Uint256Heap-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-peek-struct-Heap-Uint256Heap-)`peek(struct Heap.Uint256Heap self) → uint256`internal

Lookup the root element of the heap.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-)`pop(struct Heap.Uint256Heap self) → uint256`internal

Remove (and return) the root element for the heap using the default comparator.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-function--uint256-uint256--view-returns--bool--)`pop(struct Heap.Uint256Heap self, function (uint256,uint256) view returns (bool) comp) → uint256`internal

Remove (and return) the root element for the heap using the provided comparator.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-)`insert(struct Heap.Uint256Heap self, uint256 value)`internal

Insert a new element in the heap using the default comparator.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-function--uint256-uint256--view-returns--bool--)`insert(struct Heap.Uint256Heap self, uint256 value, function (uint256,uint256) view returns (bool) comp)`internal

Insert a new element in the heap using the provided comparator.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-replace-struct-Heap-Uint256Heap-uint256-)`replace(struct Heap.Uint256Heap self, uint256 newValue) → uint256`internal

Return the root element for the heap, and replace it with a new value, using the default comparator. This is equivalent to using [`pop`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-function%E2%80%94%E2%80%8Buint256-uint256%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbool--) and [`insert`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-function%E2%80%94%E2%80%8Buint256-uint256%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbool--), but requires only one rebalancing operation.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-replace-struct-Heap-Uint256Heap-uint256-function--uint256-uint256--view-returns--bool--)`replace(struct Heap.Uint256Heap self, uint256 newValue, function (uint256,uint256) view returns (bool) comp) → uint256`internal

Return the root element for the heap, and replace it with a new value, using the provided comparator. This is equivalent to using [`pop`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-pop-struct-Heap-Uint256Heap-function%E2%80%94%E2%80%8Buint256-uint256%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbool--) and [`insert`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-insert-struct-Heap-Uint256Heap-uint256-function%E2%80%94%E2%80%8Buint256-uint256%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbool--), but requires only one rebalancing operation.

All inserting and removal from a heap should always be done using the same comparator. Mixing comparator during the lifecycle of a heap will result in undefined behavior.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-length-struct-Heap-Uint256Heap-)`length(struct Heap.Uint256Heap self) → uint256`internal

Returns the number of elements in the heap.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Heap-clear-struct-Heap-Uint256Heap-)`clear(struct Heap.Uint256Heap self)`internal

Removes all elements in the heap.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree)`MerkleTree`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/structs/MerkleTree.sol)

`import "@openzeppelin/contracts/utils/structs/MerkleTree.sol";`

Library for managing [Merkle Tree](https://wikipedia.org/wiki/Merkle_Tree) data structures.

Each tree is a complete binary tree with the ability to sequentially insert leaves, changing them from a zero to a non-zero value and updating its root. This structure allows inserting commitments (or other entries) that are not stored, but can be proven to be part of the tree at a later time if the root is kept. See [`MerkleProof`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#MerkleProof).

A tree is defined by the following parameters:

*   Depth: The number of levels in the tree, it also defines the maximum number of leaves as 2**depth.

*   Zero value: The value that represents an empty leaf. Used to avoid regular zero values to be part of the tree.

*   Hashing function: A cryptographic hash function used to produce internal nodes. Defaults to [`Hashes.commutativeKeccak256`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#Hashes-commutativeKeccak256-bytes32-bytes32-).

Building trees using non-commutative hashing functions (i.e. `H(a, b) != H(b, a)`) is supported. However, proving the inclusion of a leaf in such trees is not possible with the [`MerkleProof`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#MerkleProof) library since it only supports _commutative_ hashing functions.

_Available since v5.1._

Functions

*   [`setup(self, treeDepth, zero)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-)

*   [`setup(self, treeDepth, zero, fnHash)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-function%E2%80%94%E2%80%8Bbytes32-bytes32%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbytes32--)

*   [`push(self, leaf)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-)

*   [`push(self, leaf, fnHash)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-function%E2%80%94%E2%80%8Bbytes32-bytes32%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbytes32--)

*   [`update(self, index, oldValue, newValue, proof)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---)

*   [`update(self, index, oldValue, newValue, proof, fnHash)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---function%E2%80%94%E2%80%8Bbytes32-bytes32%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbytes32--)

*   [`depth(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-depth-struct-MerkleTree-Bytes32PushTree-)

Errors

*   [`MerkleTreeUpdateInvalidIndex(index, length)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-MerkleTreeUpdateInvalidIndex-uint256-uint256-)

*   [`MerkleTreeUpdateInvalidProof()`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-MerkleTreeUpdateInvalidProof--)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-)`setup(struct MerkleTree.Bytes32PushTree self, uint8 treeDepth, bytes32 zero) → bytes32 initialRoot`internal

Initialize a [`Bytes32PushTree`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-Bytes32PushTree) using [`Hashes.commutativeKeccak256`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#Hashes-commutativeKeccak256-bytes32-bytes32-) to hash internal nodes. The capacity of the tree (i.e. number of leaves) is set to `2**treeDepth`.

Calling this function on MerkleTree that was already setup and used will reset it to a blank state.

Once a tree is setup, any push to it must use the same hashing function. This means that values should be pushed to it using the default [push](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-) function.

The zero value should be carefully chosen since it will be stored in the tree representing empty leaves. It should be a value that is not expected to be part of the tree.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-function--bytes32-bytes32--view-returns--bytes32--)`setup(struct MerkleTree.Bytes32PushTree self, uint8 treeDepth, bytes32 zero, function (bytes32,bytes32) view returns (bytes32) fnHash) → bytes32 initialRoot`internal

Same as [setup](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-), but allows to specify a custom hashing function.

Once a tree is setup, any push to it must use the same hashing function. This means that values should be pushed to it using the custom push function, which should be the same one as used during the setup.

Providing a custom hashing function is a security-sensitive operation since it may compromise the soundness of the tree.

Consider verifying that the hashing function does not manipulate the memory state directly and that it follows the Solidity memory safety rules. Otherwise, it may lead to unexpected behavior.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-)`push(struct MerkleTree.Bytes32PushTree self, bytes32 leaf) → uint256 index, bytes32 newRoot`internal

Insert a new leaf in the tree, and compute the new root. Returns the position of the inserted leaf in the tree, and the resulting root.

Hashing the leaf before calling this function is recommended as a protection against second pre-image attacks.

This variant uses [`Hashes.commutativeKeccak256`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#Hashes-commutativeKeccak256-bytes32-bytes32-) to hash internal nodes. It should only be used on merkle trees that were setup using the same (default) hashing function (i.e. by calling [the default setup](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-) function).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-function--bytes32-bytes32--view-returns--bytes32--)`push(struct MerkleTree.Bytes32PushTree self, bytes32 leaf, function (bytes32,bytes32) view returns (bytes32) fnHash) → uint256 index, bytes32 newRoot`internal

Insert a new leaf in the tree, and compute the new root. Returns the position of the inserted leaf in the tree, and the resulting root.

Hashing the leaf before calling this function is recommended as a protection against second pre-image attacks.

This variant uses a custom hashing function to hash internal nodes. It should only be called with the same function as the one used during the initial setup of the merkle tree.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---)`update(struct MerkleTree.Bytes32PushTree self, uint256 index, bytes32 oldValue, bytes32 newValue, bytes32[] proof) → bytes32 oldRoot, bytes32 newRoot`internal

Change the value of the leaf at position `index` from `oldValue` to `newValue`. Returns the recomputed "old" root (before the update) and "new" root (after the update). The caller must verify that the reconstructed old root is the last known one.

The `proof` must be an up-to-date inclusion proof for the leaf being updated. This means that this function is vulnerable to front-running. Any [`push`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-function%E2%80%94%E2%80%8Bbytes32-bytes32%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbytes32--) or [`update`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---function%E2%80%94%E2%80%8Bbytes32-bytes32%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbytes32--) operation (that changes the root of the tree) would render all "in flight" updates invalid.

This variant uses [`Hashes.commutativeKeccak256`](https://docs.openzeppelin.com/contracts/5.x/api/utils/cryptography#Hashes-commutativeKeccak256-bytes32-bytes32-) to hash internal nodes. It should only be used on merkle trees that were setup using the same (default) hashing function (i.e. by calling [the default setup](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-setup-struct-MerkleTree-Bytes32PushTree-uint8-bytes32-) function).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---function--bytes32-bytes32--view-returns--bytes32--)`update(struct MerkleTree.Bytes32PushTree self, uint256 index, bytes32 oldValue, bytes32 newValue, bytes32[] proof, function (bytes32,bytes32) view returns (bytes32) fnHash) → bytes32 oldRoot, bytes32 newRoot`internal

Change the value of the leaf at position `index` from `oldValue` to `newValue`. Returns the recomputed "old" root (before the update) and "new" root (after the update). The caller must verify that the reconstructed old root is the last known one.

The `proof` must be an up-to-date inclusion proof for the leaf being update. This means that this function is vulnerable to front-running. Any [`push`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-push-struct-MerkleTree-Bytes32PushTree-bytes32-function%E2%80%94%E2%80%8Bbytes32-bytes32%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbytes32--) or [`update`](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-update-struct-MerkleTree-Bytes32PushTree-uint256-bytes32-bytes32-bytes32---function%E2%80%94%E2%80%8Bbytes32-bytes32%E2%80%94%E2%80%8Bview-returns%E2%80%94%E2%80%8Bbytes32--) operation (that changes the root of the tree) would render all "in flight" updates invalid.

This variant uses a custom hashing function to hash internal nodes. It should only be called with the same function as the one used during the initial setup of the merkle tree.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-depth-struct-MerkleTree-Bytes32PushTree-)`depth(struct MerkleTree.Bytes32PushTree self) → uint256`internal

Tree’s depth (set at initialization)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-MerkleTreeUpdateInvalidIndex-uint256-uint256-)`MerkleTreeUpdateInvalidIndex(uint256 index, uint256 length)`error

Error emitted when trying to update a leaf that was not previously pushed.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#MerkleTree-MerkleTreeUpdateInvalidProof--)`MerkleTreeUpdateInvalidProof()`error

Error emitted when the proof used during an update is invalid (could not reproduce the side).

[](https://docs.openzeppelin.com/contracts/5.x/api/utils#libraries)Libraries
----------------------------------------------------------------------------

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2)`Create2`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Create2.sol)

`import "@openzeppelin/contracts/utils/Create2.sol";`

Helper to make usage of the `CREATE2` EVM opcode easier and safer. `CREATE2` can be used to compute in advance the address where a smart contract will be deployed, which allows for interesting new mechanisms known as 'counterfactual interactions'.

See the [EIP](https://eips.ethereum.org/EIPS/eip-1014#motivation) for more information.

Functions

*   [`deploy(amount, salt, bytecode)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-deploy-uint256-bytes32-bytes-)

*   [`computeAddress(salt, bytecodeHash)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-)

*   [`computeAddress(salt, bytecodeHash, deployer)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-address-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-deploy-uint256-bytes32-bytes-)`deploy(uint256 amount, bytes32 salt, bytes bytecode) → address addr`internal

Deploys a contract using `CREATE2`. The address where the contract will be deployed can be known in advance via [`computeAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-address-).

The bytecode for a contract can be obtained from Solidity with `type(contractName).creationCode`.

Requirements:

*   `bytecode` must not be empty.

*   `salt` must have not been used for `bytecode` already.

*   the factory must have a balance of at least `amount`.

*   if `amount` is non-zero, `bytecode` must have a `payable` constructor.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-)`computeAddress(bytes32 salt, bytes32 bytecodeHash) → address`internal

Returns the address where a contract will be stored if deployed via [`deploy`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-deploy-uint256-bytes32-bytes-). Any change in the `bytecodeHash` or `salt` will result in a new destination address.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-address-)`computeAddress(bytes32 salt, bytes32 bytecodeHash, address deployer) → address addr`internal

Returns the address where a contract will be stored if deployed via [`deploy`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-deploy-uint256-bytes32-bytes-) from a contract located at `deployer`. If `deployer` is this contract’s address, returns the same value as [`computeAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-computeAddress-bytes32-bytes32-address-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Create2-Create2EmptyBytecode--)`Create2EmptyBytecode()`error

There’s no code to deploy.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address)`Address`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Address.sol)

`import "@openzeppelin/contracts/utils/Address.sol";`

Collection of functions related to the address type

Functions

*   [`sendValue(recipient, amount)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-sendValue-address-payable-uint256-)

*   [`functionCall(target, data)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCall-address-bytes-)

*   [`functionCallWithValue(target, data, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCallWithValue-address-bytes-uint256-)

*   [`functionStaticCall(target, data)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionStaticCall-address-bytes-)

*   [`functionDelegateCall(target, data)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionDelegateCall-address-bytes-)

*   [`verifyCallResultFromTarget(target, success, returndata)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-verifyCallResultFromTarget-address-bool-bytes-)

*   [`verifyCallResult(success, returndata)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-verifyCallResult-bool-bytes-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-sendValue-address-payable-uint256-)`sendValue(address payable recipient, uint256 amount)`internal

Replacement for Solidity’s `transfer`: sends `amount` wei to `recipient`, forwarding all available gas and reverting on errors.

[EIP1884](https://eips.ethereum.org/EIPS/eip-1884) increases the gas cost of certain opcodes, possibly making contracts go over the 2300 gas limit imposed by `transfer`, making them unable to receive funds via `transfer`. [`sendValue`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-sendValue-address-payable-uint256-) removes this limitation.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCall-address-bytes-)`functionCall(address target, bytes data) → bytes`internal

Performs a Solidity function call using a low level `call`. A plain `call` is an unsafe replacement for a function call: use this function instead.

If `target` reverts with a revert reason or custom error, it is bubbled up by this function (like regular Solidity function calls). However, if the call reverted with no returned reason, this function reverts with a {Errors.FailedCall} error.

Returns the raw returned data. To convert to the expected return value, use [`abi.decode`](https://solidity.readthedocs.io/en/latest/units-and-global-variables.html?highlight=abi.decode#abi-encoding-and-decoding-functions).

Requirements:

*   `target` must be a contract.

*   calling `target` with `data` must not revert.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCallWithValue-address-bytes-uint256-)`functionCallWithValue(address target, bytes data, uint256 value) → bytes`internal

Same as [`functionCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCall-address-bytes-), but also transferring `value` wei to `target`.

Requirements:

*   the calling contract must have an ETH balance of at least `value`.

*   the called Solidity function must be `payable`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionStaticCall-address-bytes-)`functionStaticCall(address target, bytes data) → bytes`internal

Same as [`functionCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCall-address-bytes-), but performing a static call.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionDelegateCall-address-bytes-)`functionDelegateCall(address target, bytes data) → bytes`internal

Same as [`functionCall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-functionCall-address-bytes-), but performing a delegate call.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-verifyCallResultFromTarget-address-bool-bytes-)`verifyCallResultFromTarget(address target, bool success, bytes returndata) → bytes`internal

Tool to verify that a low level call to smart-contract was successful, and reverts if the target was not a contract or bubbling up the revert reason (falling back to {Errors.FailedCall}) in case of an unsuccessful call.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-verifyCallResult-bool-bytes-)`verifyCallResult(bool success, bytes returndata) → bytes`internal

Tool to verify that a low level call was successful, and reverts if it wasn’t, either by bubbling the revert reason or with a default {Errors.FailedCall} error.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Address-AddressEmptyCode-address-)`AddressEmptyCode(address target)`error

There’s no code at `target` (it is not a contract).

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays)`Arrays`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Arrays.sol)

`import "@openzeppelin/contracts/utils/Arrays.sol";`

Collection of functions related to array types.

Functions

*   [`sort(array, comp)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-uint256---function%E2%80%94%E2%80%8Buint256-uint256%E2%80%94%E2%80%8Bpure-returns%E2%80%94%E2%80%8Bbool--)

*   [`sort(array)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-uint256---)

*   [`sort(array, comp)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-address---function%E2%80%94%E2%80%8Baddress-address%E2%80%94%E2%80%8Bpure-returns%E2%80%94%E2%80%8Bbool--)

*   [`sort(array)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-address---)

*   [`sort(array, comp)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---function%E2%80%94%E2%80%8Bbytes32-bytes32%E2%80%94%E2%80%8Bpure-returns%E2%80%94%E2%80%8Bbool--)

*   [`sort(array)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---)

*   [`findUpperBound(array, element)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-findUpperBound-uint256---uint256-)

*   [`lowerBound(array, element)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBound-uint256---uint256-)

*   [`upperBound(array, element)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-upperBound-uint256---uint256-)

*   [`lowerBoundMemory(array, element)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBoundMemory-uint256---uint256-)

*   [`upperBoundMemory(array, element)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-upperBoundMemory-uint256---uint256-)

*   [`unsafeAccess(arr, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-address---uint256-)

*   [`unsafeAccess(arr, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-bytes32---uint256-)

*   [`unsafeAccess(arr, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-uint256---uint256-)

*   [`unsafeAccess(arr, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-bytes---uint256-)

*   [`unsafeAccess(arr, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-string---uint256-)

*   [`unsafeMemoryAccess(arr, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-address---uint256-)

*   [`unsafeMemoryAccess(arr, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-bytes32---uint256-)

*   [`unsafeMemoryAccess(arr, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-uint256---uint256-)

*   [`unsafeMemoryAccess(arr, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-bytes---uint256-)

*   [`unsafeMemoryAccess(arr, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-string---uint256-)

*   [`unsafeSetLength(array, len)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-address---uint256-)

*   [`unsafeSetLength(array, len)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-bytes32---uint256-)

*   [`unsafeSetLength(array, len)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-uint256---uint256-)

*   [`unsafeSetLength(array, len)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-bytes---uint256-)

*   [`unsafeSetLength(array, len)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-string---uint256-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-uint256---function--uint256-uint256--pure-returns--bool--)`sort(uint256[] array, function (uint256,uint256) pure returns (bool) comp) → uint256[]`internal

Sort an array of uint256 (in memory) following the provided comparator function.

This function does the sorting "in place", meaning that it overrides the input. The object is returned for convenience, but that returned value can be discarded safely if the caller has a memory pointer to the array.

this function’s cost is `O(n · log(n))` in average and `O(n²)` in the worst case, with n the length of the array. Using it in view functions that are executed through `eth_call` is safe, but one should be very careful when executing this as part of a transaction. If the array being sorted is too large, the sort operation may consume more gas than is available in a block, leading to potential DoS.

Consider memory side-effects when using custom comparator functions that access memory in an unsafe way.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-uint256---)`sort(uint256[] array) → uint256[]`internal

Variant of [`sort`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---) that sorts an array of uint256 in increasing order.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-address---function--address-address--pure-returns--bool--)`sort(address[] array, function (address,address) pure returns (bool) comp) → address[]`internal

Sort an array of address (in memory) following the provided comparator function.

This function does the sorting "in place", meaning that it overrides the input. The object is returned for convenience, but that returned value can be discarded safely if the caller has a memory pointer to the array.

this function’s cost is `O(n · log(n))` in average and `O(n²)` in the worst case, with n the length of the array. Using it in view functions that are executed through `eth_call` is safe, but one should be very careful when executing this as part of a transaction. If the array being sorted is too large, the sort operation may consume more gas than is available in a block, leading to potential DoS.

Consider memory side-effects when using custom comparator functions that access memory in an unsafe way.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-address---)`sort(address[] array) → address[]`internal

Variant of [`sort`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---) that sorts an array of address in increasing order.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---function--bytes32-bytes32--pure-returns--bool--)`sort(bytes32[] array, function (bytes32,bytes32) pure returns (bool) comp) → bytes32[]`internal

Sort an array of bytes32 (in memory) following the provided comparator function.

This function does the sorting "in place", meaning that it overrides the input. The object is returned for convenience, but that returned value can be discarded safely if the caller has a memory pointer to the array.

this function’s cost is `O(n · log(n))` in average and `O(n²)` in the worst case, with n the length of the array. Using it in view functions that are executed through `eth_call` is safe, but one should be very careful when executing this as part of a transaction. If the array being sorted is too large, the sort operation may consume more gas than is available in a block, leading to potential DoS.

Consider memory side-effects when using custom comparator functions that access memory in an unsafe way.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---)`sort(bytes32[] array) → bytes32[]`internal

Variant of [`sort`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-sort-bytes32---) that sorts an array of bytes32 in increasing order.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-findUpperBound-uint256---uint256-)`findUpperBound(uint256[] array, uint256 element) → uint256`internal

Searches a sorted `array` and returns the first index that contains a value greater or equal to `element`. If no such index exists (i.e. all values in the array are strictly less than `element`), the array length is returned. Time complexity O(log n).

The `array` is expected to be sorted in ascending order, and to contain no repeated elements.

Deprecated. This implementation behaves as [`lowerBound`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBound-uint256---uint256-) but lacks support for repeated elements in the array. The [`lowerBound`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBound-uint256---uint256-) function should be used instead.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBound-uint256---uint256-)`lowerBound(uint256[] array, uint256 element) → uint256`internal

Searches an `array` sorted in ascending order and returns the first index that contains a value greater or equal than `element`. If no such index exists (i.e. all values in the array are strictly less than `element`), the array length is returned. Time complexity O(log n).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-upperBound-uint256---uint256-)`upperBound(uint256[] array, uint256 element) → uint256`internal

Searches an `array` sorted in ascending order and returns the first index that contains a value strictly greater than `element`. If no such index exists (i.e. all values in the array are strictly less than `element`), the array length is returned. Time complexity O(log n).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBoundMemory-uint256---uint256-)`lowerBoundMemory(uint256[] array, uint256 element) → uint256`internal

Same as [`lowerBound`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-lowerBound-uint256---uint256-), but with an array in memory.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-upperBoundMemory-uint256---uint256-)`upperBoundMemory(uint256[] array, uint256 element) → uint256`internal

Same as [`upperBound`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-upperBound-uint256---uint256-), but with an array in memory.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-address---uint256-)`unsafeAccess(address[] arr, uint256 pos) → struct StorageSlot.AddressSlot`internal

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-bytes32---uint256-)`unsafeAccess(bytes32[] arr, uint256 pos) → struct StorageSlot.Bytes32Slot`internal

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-uint256---uint256-)`unsafeAccess(uint256[] arr, uint256 pos) → struct StorageSlot.Uint256Slot`internal

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-bytes---uint256-)`unsafeAccess(bytes[] arr, uint256 pos) → struct StorageSlot.BytesSlot`internal

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeAccess-string---uint256-)`unsafeAccess(string[] arr, uint256 pos) → struct StorageSlot.StringSlot`internal

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-address---uint256-)`unsafeMemoryAccess(address[] arr, uint256 pos) → address res`internal

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-bytes32---uint256-)`unsafeMemoryAccess(bytes32[] arr, uint256 pos) → bytes32 res`internal

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-uint256---uint256-)`unsafeMemoryAccess(uint256[] arr, uint256 pos) → uint256 res`internal

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-bytes---uint256-)`unsafeMemoryAccess(bytes[] arr, uint256 pos) → bytes res`internal

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeMemoryAccess-string---uint256-)`unsafeMemoryAccess(string[] arr, uint256 pos) → string res`internal

Access an array in an "unsafe" way. Skips solidity "index-out-of-range" check.

Only use if you are certain `pos` is lower than the array length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-address---uint256-)`unsafeSetLength(address[] array, uint256 len)`internal

Helper to set the length of a dynamic array. Directly writing to `.length` is forbidden.

this does not clear elements if length is reduced, of initialize elements if length is increased.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-bytes32---uint256-)`unsafeSetLength(bytes32[] array, uint256 len)`internal

Helper to set the length of a dynamic array. Directly writing to `.length` is forbidden.

this does not clear elements if length is reduced, of initialize elements if length is increased.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-uint256---uint256-)`unsafeSetLength(uint256[] array, uint256 len)`internal

Helper to set the length of a dynamic array. Directly writing to `.length` is forbidden.

this does not clear elements if length is reduced, of initialize elements if length is increased.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-bytes---uint256-)`unsafeSetLength(bytes[] array, uint256 len)`internal

Helper to set the length of a dynamic array. Directly writing to `.length` is forbidden.

this does not clear elements if length is reduced, of initialize elements if length is increased.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Arrays-unsafeSetLength-string---uint256-)`unsafeSetLength(string[] array, uint256 len)`internal

Helper to set the length of a dynamic array. Directly writing to `.length` is forbidden.

this does not clear elements if length is reduced, of initialize elements if length is increased.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64)`Base64`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Base64.sol)

`import "@openzeppelin/contracts/utils/Base64.sol";`

Provides a set of functions to operate with Base64 strings.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-encode-bytes-)`encode(bytes data) → string`internal

Converts a `bytes` to its Bytes64 `string` representation.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-encodeURL-bytes-)`encodeURL(bytes data) → string`internal

Converts a `bytes` to its Bytes64Url `string` representation. Output is not padded with `=` as specified in [rfc4648](https://www.rfc-editor.org/rfc/rfc4648).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-_TABLE-string)`string _TABLE`internal constant

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Base64-_TABLE_URL-string)`string _TABLE_URL`internal constant

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes)`Bytes`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Bytes.sol)

`import "@openzeppelin/contracts/utils/Bytes.sol";`

Bytes operations.

Functions

*   [`indexOf(buffer, s)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-indexOf-bytes-bytes1-)

*   [`indexOf(buffer, s, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-indexOf-bytes-bytes1-uint256-)

*   [`lastIndexOf(buffer, s)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-lastIndexOf-bytes-bytes1-)

*   [`lastIndexOf(buffer, s, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-lastIndexOf-bytes-bytes1-uint256-)

*   [`slice(buffer, start)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-slice-bytes-uint256-)

*   [`slice(buffer, start, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-slice-bytes-uint256-uint256-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-indexOf-bytes-bytes1-)`indexOf(bytes buffer, bytes1 s) → uint256`internal

Forward search for `s` in `buffer` * If `s` is present in the buffer, returns the index of the first instance * If `s` is not present in the buffer, returns type(uint256).max

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-indexOf-bytes-bytes1-uint256-)`indexOf(bytes buffer, bytes1 s, uint256 pos) → uint256`internal

Forward search for `s` in `buffer` starting at position `pos` * If `s` is present in the buffer (at or after `pos`), returns the index of the next instance * If `s` is not present in the buffer (at or after `pos`), returns type(uint256).max

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-lastIndexOf-bytes-bytes1-)`lastIndexOf(bytes buffer, bytes1 s) → uint256`internal

Backward search for `s` in `buffer` * If `s` is present in the buffer, returns the index of the last instance * If `s` is not present in the buffer, returns type(uint256).max

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-lastIndexOf-bytes-bytes1-uint256-)`lastIndexOf(bytes buffer, bytes1 s, uint256 pos) → uint256`internal

Backward search for `s` in `buffer` starting at position `pos` * If `s` is present in the buffer (at or before `pos`), returns the index of the previous instance * If `s` is not present in the buffer (at or before `pos`), returns type(uint256).max

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-slice-bytes-uint256-)`slice(bytes buffer, uint256 start) → bytes`internal

Copies the content of `buffer`, from `start` (included) to the end of `buffer` into a new bytes object in memory.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Bytes-slice-bytes-uint256-uint256-)`slice(bytes buffer, uint256 start, uint256 end) → bytes`internal

Copies the content of `buffer`, from `start` (included) to `end` (excluded) into a new bytes object in memory.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Calldata)`Calldata`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Calldata.sol)

`import "@openzeppelin/contracts/utils/Calldata.sol";`

Helper library for manipulating objects in calldata.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Calldata-emptyBytes--)`emptyBytes() → bytes result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Calldata-emptyString--)`emptyString() → string result`internal

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings)`Strings`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Strings.sol)

`import "@openzeppelin/contracts/utils/Strings.sol";`

String operations.

Functions

*   [`toString(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toString-uint256-)

*   [`toStringSigned(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toStringSigned-int256-)

*   [`toHexString(value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-uint256-)

*   [`toHexString(value, length)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-uint256-uint256-)

*   [`toHexString(addr)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-address-)

*   [`toChecksumHexString(addr)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toChecksumHexString-address-)

*   [`equal(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-equal-string-string-)

*   [`parseUint(input)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-)

*   [`parseUint(input, begin, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-uint256-uint256-)

*   [`tryParseUint(input)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseUint-string-)

*   [`tryParseUint(input, begin, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseUint-string-uint256-uint256-)

*   [`parseInt(input)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-)

*   [`parseInt(input, begin, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-uint256-uint256-)

*   [`tryParseInt(input)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseInt-string-)

*   [`tryParseInt(input, begin, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseInt-string-uint256-uint256-)

*   [`parseHexUint(input)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-)

*   [`parseHexUint(input, begin, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-uint256-uint256-)

*   [`tryParseHexUint(input)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseHexUint-string-)

*   [`tryParseHexUint(input, begin, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseHexUint-string-uint256-uint256-)

*   [`parseAddress(input)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-)

*   [`parseAddress(input, begin, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-uint256-uint256-)

*   [`tryParseAddress(input)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseAddress-string-)

*   [`tryParseAddress(input, begin, end)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseAddress-string-uint256-uint256-)

*   [`escapeJSON(input)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-escapeJSON-string-)

Errors

*   [`StringsInsufficientHexLength(value, length)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInsufficientHexLength-uint256-uint256-)

*   [`StringsInvalidChar()`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInvalidChar--)

*   [`StringsInvalidAddressFormat()`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInvalidAddressFormat--)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toString-uint256-)`toString(uint256 value) → string`internal

Converts a `uint256` to its ASCII `string` decimal representation.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toStringSigned-int256-)`toStringSigned(int256 value) → string`internal

Converts a `int256` to its ASCII `string` decimal representation.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-uint256-)`toHexString(uint256 value) → string`internal

Converts a `uint256` to its ASCII `string` hexadecimal representation.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-uint256-uint256-)`toHexString(uint256 value, uint256 length) → string`internal

Converts a `uint256` to its ASCII `string` hexadecimal representation with fixed length.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toHexString-address-)`toHexString(address addr) → string`internal

Converts an `address` with fixed length of 20 bytes to its not checksummed ASCII `string` hexadecimal representation.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toChecksumHexString-address-)`toChecksumHexString(address addr) → string`internal

Converts an `address` with fixed length of 20 bytes to its checksummed ASCII `string` hexadecimal representation, according to EIP-55.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-equal-string-string-)`equal(string a, string b) → bool`internal

Returns true if the two strings are equal.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-)`parseUint(string input) → uint256`internal

Parse a decimal string and returns the value as a `uint256`.

Requirements: - The string must be formatted as `[0-9]*` - The result must fit into an `uint256` type

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-uint256-uint256-)`parseUint(string input, uint256 begin, uint256 end) → uint256`internal

Variant of [`parseUint`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-) that parses a substring of `input` located between position `begin` (included) and `end` (excluded).

Requirements: - The substring must be formatted as `[0-9]*` - The result must fit into an `uint256` type

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseUint-string-)`tryParseUint(string input) → bool success, uint256 value`internal

Variant of [`parseUint`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-) that returns false if the parsing fails because of an invalid character.

This function will revert if the result does not fit in a `uint256`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseUint-string-uint256-uint256-)`tryParseUint(string input, uint256 begin, uint256 end) → bool success, uint256 value`internal

Variant of [`parseUint`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseUint-string-uint256-uint256-) that returns false if the parsing fails because of an invalid character.

This function will revert if the result does not fit in a `uint256`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-)`parseInt(string input) → int256`internal

Parse a decimal string and returns the value as a `int256`.

Requirements: - The string must be formatted as `[-+]?[0-9]*` - The result must fit in an `int256` type.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-uint256-uint256-)`parseInt(string input, uint256 begin, uint256 end) → int256`internal

Variant of [`parseInt`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-) that parses a substring of `input` located between position `begin` (included) and `end` (excluded).

Requirements: - The substring must be formatted as `[-+]?[0-9]*` - The result must fit in an `int256` type.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseInt-string-)`tryParseInt(string input) → bool success, int256 value`internal

Variant of [`parseInt`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-) that returns false if the parsing fails because of an invalid character or if the result does not fit in a `int256`.

This function will revert if the absolute value of the result does not fit in a `uint256`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseInt-string-uint256-uint256-)`tryParseInt(string input, uint256 begin, uint256 end) → bool success, int256 value`internal

Variant of [`parseInt`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseInt-string-uint256-uint256-) that returns false if the parsing fails because of an invalid character or if the result does not fit in a `int256`.

This function will revert if the absolute value of the result does not fit in a `uint256`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-)`parseHexUint(string input) → uint256`internal

Parse a hexadecimal string (with or without "0x" prefix), and returns the value as a `uint256`.

Requirements: - The string must be formatted as `(0x)?[0-9a-fA-F]*` - The result must fit in an `uint256` type.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-uint256-uint256-)`parseHexUint(string input, uint256 begin, uint256 end) → uint256`internal

Variant of [`parseHexUint`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-) that parses a substring of `input` located between position `begin` (included) and `end` (excluded).

Requirements: - The substring must be formatted as `(0x)?[0-9a-fA-F]*` - The result must fit in an `uint256` type.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseHexUint-string-)`tryParseHexUint(string input) → bool success, uint256 value`internal

Variant of [`parseHexUint`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-) that returns false if the parsing fails because of an invalid character.

This function will revert if the result does not fit in a `uint256`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseHexUint-string-uint256-uint256-)`tryParseHexUint(string input, uint256 begin, uint256 end) → bool success, uint256 value`internal

Variant of [`parseHexUint`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseHexUint-string-uint256-uint256-) that returns false if the parsing fails because of an invalid character.

This function will revert if the result does not fit in a `uint256`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-)`parseAddress(string input) → address`internal

Parse a hexadecimal string (with or without "0x" prefix), and returns the value as an `address`.

Requirements: - The string must be formatted as `(0x)?[0-9a-fA-F]{40}`

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-uint256-uint256-)`parseAddress(string input, uint256 begin, uint256 end) → address`internal

Variant of [`parseAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-) that parses a substring of `input` located between position `begin` (included) and `end` (excluded).

Requirements: - The substring must be formatted as `(0x)?[0-9a-fA-F]{40}`

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseAddress-string-)`tryParseAddress(string input) → bool success, address value`internal

Variant of [`parseAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-) that returns false if the parsing fails because the input is not a properly formatted address. See [`parseAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-) requirements.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-tryParseAddress-string-uint256-uint256-)`tryParseAddress(string input, uint256 begin, uint256 end) → bool success, address value`internal

Variant of [`parseAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-uint256-uint256-) that returns false if the parsing fails because input is not a properly formatted address. See [`parseAddress`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-parseAddress-string-uint256-uint256-) requirements.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-escapeJSON-string-)`escapeJSON(string input) → string`internal

Escape special characters in JSON strings. This can be useful to prevent JSON injection in NFT metadata.

This function should only be used in double quoted JSON strings. Single quotes are not escaped.

This function escapes all unicode characters, and not just the ones in ranges defined in section 2.5 of RFC-4627 (U+0000 to U+001F, U+0022 and U+005C). ECMAScript’s `JSON.parse` does recover escaped unicode characters that are not in this range, but other tooling may provide different results.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInsufficientHexLength-uint256-uint256-)`StringsInsufficientHexLength(uint256 value, uint256 length)`error

The `value` string doesn’t fit in the specified `length`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInvalidChar--)`StringsInvalidChar()`error

The string being parsed contains characters that are not in scope of the given base.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-StringsInvalidAddressFormat--)`StringsInvalidAddressFormat()`error

The string being parsed is not a properly formatted address.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings)`ShortStrings`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/ShortStrings.sol)

`import "@openzeppelin/contracts/utils/ShortStrings.sol";`

This library provides functions to convert short memory strings into a `ShortString` type that can be used as an immutable variable.

Strings of arbitrary length can be optimized using this library if they are short enough (up to 31 bytes) by packing them with their length (1 byte) in a single EVM word (32 bytes). Additionally, a fallback mechanism can be used for every other case.

Usage example:

```
contract Named {
    using ShortStrings for *;

    ShortString private immutable _name;
    string private _nameFallback;

    constructor(string memory contractName) {
        _name = contractName.toShortStringWithFallback(_nameFallback);
    }

    function name() external view returns (string memory) {
        return _name.toStringWithFallback(_nameFallback);
    }
}
```

Functions

*   [`toShortString(str)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortString-string-)

*   [`toString(sstr)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toString-ShortString-)

*   [`byteLength(sstr)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-byteLength-ShortString-)

*   [`toShortStringWithFallback(value, store)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortStringWithFallback-string-string-)

*   [`toStringWithFallback(value, store)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toStringWithFallback-ShortString-string-)

*   [`byteLengthWithFallback(value, store)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-byteLengthWithFallback-ShortString-string-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortString-string-)`toShortString(string str) → ShortString`internal

Encode a string of at most 31 chars into a `ShortString`.

This will trigger a `StringTooLong` error is the input string is too long.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toString-ShortString-)`toString(ShortString sstr) → string`internal

Decode a `ShortString` back to a "normal" string.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-byteLength-ShortString-)`byteLength(ShortString sstr) → uint256`internal

Return the length of a `ShortString`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortStringWithFallback-string-string-)`toShortStringWithFallback(string value, string store) → ShortString`internal

Encode a string into a `ShortString`, or write it to storage if it is too long.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toStringWithFallback-ShortString-string-)`toStringWithFallback(ShortString value, string store) → string`internal

Decode a string that was encoded to `ShortString` or written to storage using [`toShortStringWithFallback`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortStringWithFallback-string-string-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-byteLengthWithFallback-ShortString-string-)`byteLengthWithFallback(ShortString value, string store) → uint256`internal

Return the length of a string that was encoded to `ShortString` or written to storage using [`toShortStringWithFallback`](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-toShortStringWithFallback-string-string-).

This will return the "byte length" of the string. This may not reflect the actual length in terms of actual characters as the UTF-8 encoding of a single character can span over multiple bytes.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-StringTooLong-string-)`StringTooLong(string str)`error

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#ShortStrings-InvalidShortString--)`InvalidShortString()`error

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation)`SlotDerivation`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/SlotDerivation.sol)

`import "@openzeppelin/contracts/utils/SlotDerivation.sol";`

Library for computing storage (and transient storage) locations from namespaces and deriving slots corresponding to standard patterns. The derivation method for array and mapping matches the storage layout used by the solidity language / compiler.

Example usage:

```
contract Example {
    // Add the library methods
    using StorageSlot for bytes32;
    using SlotDerivation for bytes32;

    // Declare a namespace
    string private constant _NAMESPACE = "<namespace>"; // eg. OpenZeppelin.Slot

    function setValueInNamespace(uint256 key, address newValue) internal {
        _NAMESPACE.erc7201Slot().deriveMapping(key).getAddressSlot().value = newValue;
    }

    function getValueInNamespace(uint256 key) internal view returns (address) {
        return _NAMESPACE.erc7201Slot().deriveMapping(key).getAddressSlot().value;
    }
}
```

Consider using this library along with [`StorageSlot`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot).

This library provides a way to manipulate storage locations in a non-standard way. Tooling for checking upgrade safety will ignore the slots accessed through this library.

_Available since v5.1._

Functions

*   [`erc7201Slot(namespace)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-erc7201Slot-string-)

*   [`offset(slot, pos)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-offset-bytes32-uint256-)

*   [`deriveArray(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveArray-bytes32-)

*   [`deriveMapping(slot, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-address-)

*   [`deriveMapping(slot, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bool-)

*   [`deriveMapping(slot, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bytes32-)

*   [`deriveMapping(slot, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-uint256-)

*   [`deriveMapping(slot, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-int256-)

*   [`deriveMapping(slot, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-string-)

*   [`deriveMapping(slot, key)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bytes-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-erc7201Slot-string-)`erc7201Slot(string namespace) → bytes32 slot`internal

Derive an ERC-7201 slot from a string (namespace).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-offset-bytes32-uint256-)`offset(bytes32 slot, uint256 pos) → bytes32 result`internal

Add an offset to a slot to get the n-th element of a structure or an array.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveArray-bytes32-)`deriveArray(bytes32 slot) → bytes32 result`internal

Derive the location of the first element in an array from the slot where the length is stored.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-address-)`deriveMapping(bytes32 slot, address key) → bytes32 result`internal

Derive the location of a mapping element from the key.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bool-)`deriveMapping(bytes32 slot, bool key) → bytes32 result`internal

Derive the location of a mapping element from the key.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bytes32-)`deriveMapping(bytes32 slot, bytes32 key) → bytes32 result`internal

Derive the location of a mapping element from the key.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-uint256-)`deriveMapping(bytes32 slot, uint256 key) → bytes32 result`internal

Derive the location of a mapping element from the key.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-int256-)`deriveMapping(bytes32 slot, int256 key) → bytes32 result`internal

Derive the location of a mapping element from the key.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-string-)`deriveMapping(bytes32 slot, string key) → bytes32 result`internal

Derive the location of a mapping element from the key.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation-deriveMapping-bytes32-bytes-)`deriveMapping(bytes32 slot, bytes key) → bytes32 result`internal

Derive the location of a mapping element from the key.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot)`StorageSlot`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/StorageSlot.sol)

`import "@openzeppelin/contracts/utils/StorageSlot.sol";`

Library for reading and writing primitive types to specific storage slots.

Storage slots are often used to avoid storage conflict when dealing with upgradeable contracts. This library helps with reading and writing to such slots without the need for inline assembly.

The functions in this library return Slot structs that contain a `value` member that can be used to read or write.

Example usage to set ERC-1967 implementation slot:

```
contract ERC1967 {
    // Define the slot. Alternatively, use the SlotDerivation library to derive the slot.
    bytes32 internal constant _IMPLEMENTATION_SLOT = 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc;

    function _getImplementation() internal view returns (address) {
        return StorageSlot.getAddressSlot(_IMPLEMENTATION_SLOT).value;
    }

    function _setImplementation(address newImplementation) internal {
        require(newImplementation.code.length > 0);
        StorageSlot.getAddressSlot(_IMPLEMENTATION_SLOT).value = newImplementation;
    }
}
```

Consider using this library along with [`SlotDerivation`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation).

Functions

*   [`getAddressSlot(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getAddressSlot-bytes32-)

*   [`getBooleanSlot(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBooleanSlot-bytes32-)

*   [`getBytes32Slot(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytes32Slot-bytes32-)

*   [`getUint256Slot(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getUint256Slot-bytes32-)

*   [`getInt256Slot(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getInt256Slot-bytes32-)

*   [`getStringSlot(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getStringSlot-bytes32-)

*   [`getStringSlot(store)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getStringSlot-string-)

*   [`getBytesSlot(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytesSlot-bytes32-)

*   [`getBytesSlot(store)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytesSlot-bytes-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getAddressSlot-bytes32-)`getAddressSlot(bytes32 slot) → struct StorageSlot.AddressSlot r`internal

Returns an `AddressSlot` with member `value` located at `slot`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBooleanSlot-bytes32-)`getBooleanSlot(bytes32 slot) → struct StorageSlot.BooleanSlot r`internal

Returns a `BooleanSlot` with member `value` located at `slot`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytes32Slot-bytes32-)`getBytes32Slot(bytes32 slot) → struct StorageSlot.Bytes32Slot r`internal

Returns a `Bytes32Slot` with member `value` located at `slot`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getUint256Slot-bytes32-)`getUint256Slot(bytes32 slot) → struct StorageSlot.Uint256Slot r`internal

Returns a `Uint256Slot` with member `value` located at `slot`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getInt256Slot-bytes32-)`getInt256Slot(bytes32 slot) → struct StorageSlot.Int256Slot r`internal

Returns a `Int256Slot` with member `value` located at `slot`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getStringSlot-bytes32-)`getStringSlot(bytes32 slot) → struct StorageSlot.StringSlot r`internal

Returns a `StringSlot` with member `value` located at `slot`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getStringSlot-string-)`getStringSlot(string store) → struct StorageSlot.StringSlot r`internal

Returns an `StringSlot` representation of the string storage pointer `store`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytesSlot-bytes32-)`getBytesSlot(bytes32 slot) → struct StorageSlot.BytesSlot r`internal

Returns a `BytesSlot` with member `value` located at `slot`.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#StorageSlot-getBytesSlot-bytes-)`getBytesSlot(bytes store) → struct StorageSlot.BytesSlot r`internal

Returns an `BytesSlot` representation of the bytes storage pointer `store`.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot)`TransientSlot`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/TransientSlot.sol)

`import "@openzeppelin/contracts/utils/TransientSlot.sol";`

Library for reading and writing value-types to specific transient storage slots.

Transient slots are often used to store temporary values that are removed after the current transaction. This library helps with reading and writing to such slots without the need for inline assembly.

*   Example reading and writing values using transient storage:

```
contract Lock {
    using TransientSlot for *;

    // Define the slot. Alternatively, use the SlotDerivation library to derive the slot.
    bytes32 internal constant _LOCK_SLOT = 0xf4678858b2b588224636b8522b729e7722d32fc491da849ed75b3fdf3c84f542;

    modifier locked() {
        require(!_LOCK_SLOT.asBoolean().tload());

        _LOCK_SLOT.asBoolean().tstore(true);
        _;
        _LOCK_SLOT.asBoolean().tstore(false);
    }
}
```

Consider using this library along with [`SlotDerivation`](https://docs.openzeppelin.com/contracts/5.x/api/utils#SlotDerivation).

Functions

*   [`asAddress(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asAddress-bytes32-)

*   [`asBoolean(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asBoolean-bytes32-)

*   [`asBytes32(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asBytes32-bytes32-)

*   [`asUint256(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asUint256-bytes32-)

*   [`asInt256(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asInt256-bytes32-)

*   [`tload(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-AddressSlot-)

*   [`tstore(slot, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-AddressSlot-address-)

*   [`tload(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-BooleanSlot-)

*   [`tstore(slot, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-BooleanSlot-bool-)

*   [`tload(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Bytes32Slot-)

*   [`tstore(slot, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Bytes32Slot-bytes32-)

*   [`tload(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Uint256Slot-)

*   [`tstore(slot, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Uint256Slot-uint256-)

*   [`tload(slot)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Int256Slot-)

*   [`tstore(slot, value)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Int256Slot-int256-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asAddress-bytes32-)`asAddress(bytes32 slot) → TransientSlot.AddressSlot`internal

Cast an arbitrary slot to a AddressSlot.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asBoolean-bytes32-)`asBoolean(bytes32 slot) → TransientSlot.BooleanSlot`internal

Cast an arbitrary slot to a BooleanSlot.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asBytes32-bytes32-)`asBytes32(bytes32 slot) → TransientSlot.Bytes32Slot`internal

Cast an arbitrary slot to a Bytes32Slot.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asUint256-bytes32-)`asUint256(bytes32 slot) → TransientSlot.Uint256Slot`internal

Cast an arbitrary slot to a Uint256Slot.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-asInt256-bytes32-)`asInt256(bytes32 slot) → TransientSlot.Int256Slot`internal

Cast an arbitrary slot to a Int256Slot.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-AddressSlot-)`tload(TransientSlot.AddressSlot slot) → address value`internal

Load the value held at location `slot` in transient storage.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-AddressSlot-address-)`tstore(TransientSlot.AddressSlot slot, address value)`internal

Store `value` at location `slot` in transient storage.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-BooleanSlot-)`tload(TransientSlot.BooleanSlot slot) → bool value`internal

Load the value held at location `slot` in transient storage.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-BooleanSlot-bool-)`tstore(TransientSlot.BooleanSlot slot, bool value)`internal

Store `value` at location `slot` in transient storage.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Bytes32Slot-)`tload(TransientSlot.Bytes32Slot slot) → bytes32 value`internal

Load the value held at location `slot` in transient storage.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Bytes32Slot-bytes32-)`tstore(TransientSlot.Bytes32Slot slot, bytes32 value)`internal

Store `value` at location `slot` in transient storage.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Uint256Slot-)`tload(TransientSlot.Uint256Slot slot) → uint256 value`internal

Load the value held at location `slot` in transient storage.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Uint256Slot-uint256-)`tstore(TransientSlot.Uint256Slot slot, uint256 value)`internal

Store `value` at location `slot` in transient storage.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tload-TransientSlot-Int256Slot-)`tload(TransientSlot.Int256Slot slot) → int256 value`internal

Load the value held at location `slot` in transient storage.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#TransientSlot-tstore-TransientSlot-Int256Slot-int256-)`tstore(TransientSlot.Int256Slot slot, int256 value)`internal

Store `value` at location `slot` in transient storage.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall)`Multicall`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Multicall.sol)

`import "@openzeppelin/contracts/utils/Multicall.sol";`

Provides a function to batch together multiple calls in a single external call.

Consider any assumption about calldata validation performed by the sender may be violated if it’s not especially careful about sending transactions invoking [`multicall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall-multicall-bytes---). For example, a relay address that filters function selectors won’t filter calls nested within a [`multicall`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall-multicall-bytes---) operation.

Since 5.0.1 and 4.9.4, this contract identifies non-canonical contexts (i.e. `msg.sender` is not [`Context._msgSender`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_msgSender--)). If a non-canonical context is identified, the following self `delegatecall` appends the last bytes of `msg.data` to the subcall. This makes it safe to use with [`ERC2771Context`](https://docs.openzeppelin.com/contracts/5.x/api/metatx#ERC2771Context). Contexts that don’t affect the resolution of [`Context._msgSender`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_msgSender--) are not propagated to subcalls.

Functions

*   [`multicall(data)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall-multicall-bytes---)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Multicall-multicall-bytes---)`multicall(bytes[] data) → bytes[] results`external

Receives and executes a batch of function calls on this contract.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context)`Context`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Context.sol)

`import "@openzeppelin/contracts/utils/Context.sol";`

Provides information about the current execution context, including the sender of the transaction and its data. While these are generally available via msg.sender and msg.data, they should not be accessed in such a direct manner, since when dealing with meta-transactions the account sending and paying for execution may not be the actual sender (as far as an application is concerned).

This contract is only required for intermediate, library-like contracts.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_msgSender--)`_msgSender() → address`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_msgData--)`_msgData() → bytes`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Context-_contextSuffixLength--)`_contextSuffixLength() → uint256`internal

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing)`Packing`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Packing.sol)

`import "@openzeppelin/contracts/utils/Packing.sol";`

Helper library packing and unpacking multiple values into bytesXX.

Example usage:

```
library MyPacker {
    type MyType is bytes32;

    function _pack(address account, bytes4 selector, uint64 period) external pure returns (MyType) {
        bytes12 subpack = Packing.pack_4_8(selector, bytes8(period));
        bytes32 pack = Packing.pack_20_12(bytes20(account), subpack);
        return MyType.wrap(pack);
    }

    function _unpack(MyType self) external pure returns (address, bytes4, uint64) {
        bytes32 pack = MyType.unwrap(self);
        return (
            address(Packing.extract_32_20(pack, 0)),
            Packing.extract_32_4(pack, 20),
            uint64(Packing.extract_32_8(pack, 24))
        );
    }
}
```

_Available since v5.1._

Functions

*   [`pack_1_1(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_1_1-bytes1-bytes1-)

*   [`pack_2_2(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_2-bytes2-bytes2-)

*   [`pack_2_4(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_4-bytes2-bytes4-)

*   [`pack_2_6(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_6-bytes2-bytes6-)

*   [`pack_2_8(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_8-bytes2-bytes8-)

*   [`pack_2_10(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_10-bytes2-bytes10-)

*   [`pack_2_20(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_20-bytes2-bytes20-)

*   [`pack_2_22(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_22-bytes2-bytes22-)

*   [`pack_4_2(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_2-bytes4-bytes2-)

*   [`pack_4_4(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_4-bytes4-bytes4-)

*   [`pack_4_6(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_6-bytes4-bytes6-)

*   [`pack_4_8(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_8-bytes4-bytes8-)

*   [`pack_4_12(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_12-bytes4-bytes12-)

*   [`pack_4_16(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_16-bytes4-bytes16-)

*   [`pack_4_20(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_20-bytes4-bytes20-)

*   [`pack_4_24(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_24-bytes4-bytes24-)

*   [`pack_4_28(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_28-bytes4-bytes28-)

*   [`pack_6_2(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_2-bytes6-bytes2-)

*   [`pack_6_4(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_4-bytes6-bytes4-)

*   [`pack_6_6(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_6-bytes6-bytes6-)

*   [`pack_6_10(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_10-bytes6-bytes10-)

*   [`pack_6_16(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_16-bytes6-bytes16-)

*   [`pack_6_22(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_22-bytes6-bytes22-)

*   [`pack_8_2(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_2-bytes8-bytes2-)

*   [`pack_8_4(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_4-bytes8-bytes4-)

*   [`pack_8_8(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_8-bytes8-bytes8-)

*   [`pack_8_12(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_12-bytes8-bytes12-)

*   [`pack_8_16(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_16-bytes8-bytes16-)

*   [`pack_8_20(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_20-bytes8-bytes20-)

*   [`pack_8_24(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_24-bytes8-bytes24-)

*   [`pack_10_2(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_2-bytes10-bytes2-)

*   [`pack_10_6(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_6-bytes10-bytes6-)

*   [`pack_10_10(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_10-bytes10-bytes10-)

*   [`pack_10_12(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_12-bytes10-bytes12-)

*   [`pack_10_22(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_22-bytes10-bytes22-)

*   [`pack_12_4(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_4-bytes12-bytes4-)

*   [`pack_12_8(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_8-bytes12-bytes8-)

*   [`pack_12_10(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_10-bytes12-bytes10-)

*   [`pack_12_12(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_12-bytes12-bytes12-)

*   [`pack_12_16(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_16-bytes12-bytes16-)

*   [`pack_12_20(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_20-bytes12-bytes20-)

*   [`pack_16_4(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_4-bytes16-bytes4-)

*   [`pack_16_6(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_6-bytes16-bytes6-)

*   [`pack_16_8(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_8-bytes16-bytes8-)

*   [`pack_16_12(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_12-bytes16-bytes12-)

*   [`pack_16_16(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_16-bytes16-bytes16-)

*   [`pack_20_2(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_2-bytes20-bytes2-)

*   [`pack_20_4(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_4-bytes20-bytes4-)

*   [`pack_20_8(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_8-bytes20-bytes8-)

*   [`pack_20_12(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_12-bytes20-bytes12-)

*   [`pack_22_2(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_2-bytes22-bytes2-)

*   [`pack_22_6(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_6-bytes22-bytes6-)

*   [`pack_22_10(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_10-bytes22-bytes10-)

*   [`pack_24_4(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_24_4-bytes24-bytes4-)

*   [`pack_24_8(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_24_8-bytes24-bytes8-)

*   [`pack_28_4(left, right)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_28_4-bytes28-bytes4-)

*   [`extract_2_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_2_1-bytes2-uint8-)

*   [`replace_2_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_2_1-bytes2-bytes1-uint8-)

*   [`extract_4_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_4_1-bytes4-uint8-)

*   [`replace_4_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_4_1-bytes4-bytes1-uint8-)

*   [`extract_4_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_4_2-bytes4-uint8-)

*   [`replace_4_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_4_2-bytes4-bytes2-uint8-)

*   [`extract_6_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_6_1-bytes6-uint8-)

*   [`replace_6_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_1-bytes6-bytes1-uint8-)

*   [`extract_6_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_6_2-bytes6-uint8-)

*   [`replace_6_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_2-bytes6-bytes2-uint8-)

*   [`extract_6_4(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_6_4-bytes6-uint8-)

*   [`replace_6_4(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_4-bytes6-bytes4-uint8-)

*   [`extract_8_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_1-bytes8-uint8-)

*   [`replace_8_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_1-bytes8-bytes1-uint8-)

*   [`extract_8_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_2-bytes8-uint8-)

*   [`replace_8_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_2-bytes8-bytes2-uint8-)

*   [`extract_8_4(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_4-bytes8-uint8-)

*   [`replace_8_4(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_4-bytes8-bytes4-uint8-)

*   [`extract_8_6(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_8_6-bytes8-uint8-)

*   [`replace_8_6(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_6-bytes8-bytes6-uint8-)

*   [`extract_10_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_1-bytes10-uint8-)

*   [`replace_10_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_1-bytes10-bytes1-uint8-)

*   [`extract_10_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_2-bytes10-uint8-)

*   [`replace_10_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_2-bytes10-bytes2-uint8-)

*   [`extract_10_4(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_4-bytes10-uint8-)

*   [`replace_10_4(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_4-bytes10-bytes4-uint8-)

*   [`extract_10_6(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_6-bytes10-uint8-)

*   [`replace_10_6(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_6-bytes10-bytes6-uint8-)

*   [`extract_10_8(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_10_8-bytes10-uint8-)

*   [`replace_10_8(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_8-bytes10-bytes8-uint8-)

*   [`extract_12_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_1-bytes12-uint8-)

*   [`replace_12_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_1-bytes12-bytes1-uint8-)

*   [`extract_12_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_2-bytes12-uint8-)

*   [`replace_12_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_2-bytes12-bytes2-uint8-)

*   [`extract_12_4(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_4-bytes12-uint8-)

*   [`replace_12_4(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_4-bytes12-bytes4-uint8-)

*   [`extract_12_6(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_6-bytes12-uint8-)

*   [`replace_12_6(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_6-bytes12-bytes6-uint8-)

*   [`extract_12_8(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_8-bytes12-uint8-)

*   [`replace_12_8(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_8-bytes12-bytes8-uint8-)

*   [`extract_12_10(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_12_10-bytes12-uint8-)

*   [`replace_12_10(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_10-bytes12-bytes10-uint8-)

*   [`extract_16_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_1-bytes16-uint8-)

*   [`replace_16_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_1-bytes16-bytes1-uint8-)

*   [`extract_16_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_2-bytes16-uint8-)

*   [`replace_16_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_2-bytes16-bytes2-uint8-)

*   [`extract_16_4(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_4-bytes16-uint8-)

*   [`replace_16_4(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_4-bytes16-bytes4-uint8-)

*   [`extract_16_6(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_6-bytes16-uint8-)

*   [`replace_16_6(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_6-bytes16-bytes6-uint8-)

*   [`extract_16_8(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_8-bytes16-uint8-)

*   [`replace_16_8(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_8-bytes16-bytes8-uint8-)

*   [`extract_16_10(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_10-bytes16-uint8-)

*   [`replace_16_10(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_10-bytes16-bytes10-uint8-)

*   [`extract_16_12(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_16_12-bytes16-uint8-)

*   [`replace_16_12(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_12-bytes16-bytes12-uint8-)

*   [`extract_20_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_1-bytes20-uint8-)

*   [`replace_20_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_1-bytes20-bytes1-uint8-)

*   [`extract_20_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_2-bytes20-uint8-)

*   [`replace_20_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_2-bytes20-bytes2-uint8-)

*   [`extract_20_4(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_4-bytes20-uint8-)

*   [`replace_20_4(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_4-bytes20-bytes4-uint8-)

*   [`extract_20_6(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_6-bytes20-uint8-)

*   [`replace_20_6(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_6-bytes20-bytes6-uint8-)

*   [`extract_20_8(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_8-bytes20-uint8-)

*   [`replace_20_8(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_8-bytes20-bytes8-uint8-)

*   [`extract_20_10(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_10-bytes20-uint8-)

*   [`replace_20_10(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_10-bytes20-bytes10-uint8-)

*   [`extract_20_12(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_12-bytes20-uint8-)

*   [`replace_20_12(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_12-bytes20-bytes12-uint8-)

*   [`extract_20_16(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_20_16-bytes20-uint8-)

*   [`replace_20_16(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_16-bytes20-bytes16-uint8-)

*   [`extract_22_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_1-bytes22-uint8-)

*   [`replace_22_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_1-bytes22-bytes1-uint8-)

*   [`extract_22_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_2-bytes22-uint8-)

*   [`replace_22_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_2-bytes22-bytes2-uint8-)

*   [`extract_22_4(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_4-bytes22-uint8-)

*   [`replace_22_4(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_4-bytes22-bytes4-uint8-)

*   [`extract_22_6(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_6-bytes22-uint8-)

*   [`replace_22_6(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_6-bytes22-bytes6-uint8-)

*   [`extract_22_8(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_8-bytes22-uint8-)

*   [`replace_22_8(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_8-bytes22-bytes8-uint8-)

*   [`extract_22_10(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_10-bytes22-uint8-)

*   [`replace_22_10(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_10-bytes22-bytes10-uint8-)

*   [`extract_22_12(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_12-bytes22-uint8-)

*   [`replace_22_12(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_12-bytes22-bytes12-uint8-)

*   [`extract_22_16(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_16-bytes22-uint8-)

*   [`replace_22_16(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_16-bytes22-bytes16-uint8-)

*   [`extract_22_20(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_22_20-bytes22-uint8-)

*   [`replace_22_20(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_20-bytes22-bytes20-uint8-)

*   [`extract_24_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_1-bytes24-uint8-)

*   [`replace_24_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_1-bytes24-bytes1-uint8-)

*   [`extract_24_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_2-bytes24-uint8-)

*   [`replace_24_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_2-bytes24-bytes2-uint8-)

*   [`extract_24_4(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_4-bytes24-uint8-)

*   [`replace_24_4(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_4-bytes24-bytes4-uint8-)

*   [`extract_24_6(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_6-bytes24-uint8-)

*   [`replace_24_6(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_6-bytes24-bytes6-uint8-)

*   [`extract_24_8(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_8-bytes24-uint8-)

*   [`replace_24_8(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_8-bytes24-bytes8-uint8-)

*   [`extract_24_10(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_10-bytes24-uint8-)

*   [`replace_24_10(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_10-bytes24-bytes10-uint8-)

*   [`extract_24_12(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_12-bytes24-uint8-)

*   [`replace_24_12(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_12-bytes24-bytes12-uint8-)

*   [`extract_24_16(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_16-bytes24-uint8-)

*   [`replace_24_16(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_16-bytes24-bytes16-uint8-)

*   [`extract_24_20(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_20-bytes24-uint8-)

*   [`replace_24_20(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_20-bytes24-bytes20-uint8-)

*   [`extract_24_22(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_24_22-bytes24-uint8-)

*   [`replace_24_22(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_22-bytes24-bytes22-uint8-)

*   [`extract_28_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_1-bytes28-uint8-)

*   [`replace_28_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_1-bytes28-bytes1-uint8-)

*   [`extract_28_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_2-bytes28-uint8-)

*   [`replace_28_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_2-bytes28-bytes2-uint8-)

*   [`extract_28_4(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_4-bytes28-uint8-)

*   [`replace_28_4(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_4-bytes28-bytes4-uint8-)

*   [`extract_28_6(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_6-bytes28-uint8-)

*   [`replace_28_6(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_6-bytes28-bytes6-uint8-)

*   [`extract_28_8(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_8-bytes28-uint8-)

*   [`replace_28_8(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_8-bytes28-bytes8-uint8-)

*   [`extract_28_10(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_10-bytes28-uint8-)

*   [`replace_28_10(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_10-bytes28-bytes10-uint8-)

*   [`extract_28_12(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_12-bytes28-uint8-)

*   [`replace_28_12(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_12-bytes28-bytes12-uint8-)

*   [`extract_28_16(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_16-bytes28-uint8-)

*   [`replace_28_16(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_16-bytes28-bytes16-uint8-)

*   [`extract_28_20(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_20-bytes28-uint8-)

*   [`replace_28_20(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_20-bytes28-bytes20-uint8-)

*   [`extract_28_22(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_22-bytes28-uint8-)

*   [`replace_28_22(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_22-bytes28-bytes22-uint8-)

*   [`extract_28_24(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_28_24-bytes28-uint8-)

*   [`replace_28_24(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_24-bytes28-bytes24-uint8-)

*   [`extract_32_1(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_1-bytes32-uint8-)

*   [`replace_32_1(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_1-bytes32-bytes1-uint8-)

*   [`extract_32_2(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_2-bytes32-uint8-)

*   [`replace_32_2(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_2-bytes32-bytes2-uint8-)

*   [`extract_32_4(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_4-bytes32-uint8-)

*   [`replace_32_4(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_4-bytes32-bytes4-uint8-)

*   [`extract_32_6(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_6-bytes32-uint8-)

*   [`replace_32_6(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_6-bytes32-bytes6-uint8-)

*   [`extract_32_8(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_8-bytes32-uint8-)

*   [`replace_32_8(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_8-bytes32-bytes8-uint8-)

*   [`extract_32_10(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_10-bytes32-uint8-)

*   [`replace_32_10(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_10-bytes32-bytes10-uint8-)

*   [`extract_32_12(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_12-bytes32-uint8-)

*   [`replace_32_12(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_12-bytes32-bytes12-uint8-)

*   [`extract_32_16(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_16-bytes32-uint8-)

*   [`replace_32_16(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_16-bytes32-bytes16-uint8-)

*   [`extract_32_20(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_20-bytes32-uint8-)

*   [`replace_32_20(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_20-bytes32-bytes20-uint8-)

*   [`extract_32_22(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_22-bytes32-uint8-)

*   [`replace_32_22(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_22-bytes32-bytes22-uint8-)

*   [`extract_32_24(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_24-bytes32-uint8-)

*   [`replace_32_24(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_24-bytes32-bytes24-uint8-)

*   [`extract_32_28(self, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-extract_32_28-bytes32-uint8-)

*   [`replace_32_28(self, value, offset)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_28-bytes32-bytes28-uint8-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_1_1-bytes1-bytes1-)`pack_1_1(bytes1 left, bytes1 right) → bytes2 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_2-bytes2-bytes2-)`pack_2_2(bytes2 left, bytes2 right) → bytes4 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_4-bytes2-bytes4-)`pack_2_4(bytes2 left, bytes4 right) → bytes6 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_6-bytes2-bytes6-)`pack_2_6(bytes2 left, bytes6 right) → bytes8 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_8-bytes2-bytes8-)`pack_2_8(bytes2 left, bytes8 right) → bytes10 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_10-bytes2-bytes10-)`pack_2_10(bytes2 left, bytes10 right) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_20-bytes2-bytes20-)`pack_2_20(bytes2 left, bytes20 right) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_2_22-bytes2-bytes22-)`pack_2_22(bytes2 left, bytes22 right) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_2-bytes4-bytes2-)`pack_4_2(bytes4 left, bytes2 right) → bytes6 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_4-bytes4-bytes4-)`pack_4_4(bytes4 left, bytes4 right) → bytes8 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_6-bytes4-bytes6-)`pack_4_6(bytes4 left, bytes6 right) → bytes10 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_8-bytes4-bytes8-)`pack_4_8(bytes4 left, bytes8 right) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_12-bytes4-bytes12-)`pack_4_12(bytes4 left, bytes12 right) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_16-bytes4-bytes16-)`pack_4_16(bytes4 left, bytes16 right) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_20-bytes4-bytes20-)`pack_4_20(bytes4 left, bytes20 right) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_24-bytes4-bytes24-)`pack_4_24(bytes4 left, bytes24 right) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_4_28-bytes4-bytes28-)`pack_4_28(bytes4 left, bytes28 right) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_2-bytes6-bytes2-)`pack_6_2(bytes6 left, bytes2 right) → bytes8 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_4-bytes6-bytes4-)`pack_6_4(bytes6 left, bytes4 right) → bytes10 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_6-bytes6-bytes6-)`pack_6_6(bytes6 left, bytes6 right) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_10-bytes6-bytes10-)`pack_6_10(bytes6 left, bytes10 right) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_16-bytes6-bytes16-)`pack_6_16(bytes6 left, bytes16 right) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_6_22-bytes6-bytes22-)`pack_6_22(bytes6 left, bytes22 right) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_2-bytes8-bytes2-)`pack_8_2(bytes8 left, bytes2 right) → bytes10 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_4-bytes8-bytes4-)`pack_8_4(bytes8 left, bytes4 right) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_8-bytes8-bytes8-)`pack_8_8(bytes8 left, bytes8 right) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_12-bytes8-bytes12-)`pack_8_12(bytes8 left, bytes12 right) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_16-bytes8-bytes16-)`pack_8_16(bytes8 left, bytes16 right) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_20-bytes8-bytes20-)`pack_8_20(bytes8 left, bytes20 right) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_8_24-bytes8-bytes24-)`pack_8_24(bytes8 left, bytes24 right) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_2-bytes10-bytes2-)`pack_10_2(bytes10 left, bytes2 right) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_6-bytes10-bytes6-)`pack_10_6(bytes10 left, bytes6 right) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_10-bytes10-bytes10-)`pack_10_10(bytes10 left, bytes10 right) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_12-bytes10-bytes12-)`pack_10_12(bytes10 left, bytes12 right) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_10_22-bytes10-bytes22-)`pack_10_22(bytes10 left, bytes22 right) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_4-bytes12-bytes4-)`pack_12_4(bytes12 left, bytes4 right) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_8-bytes12-bytes8-)`pack_12_8(bytes12 left, bytes8 right) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_10-bytes12-bytes10-)`pack_12_10(bytes12 left, bytes10 right) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_12-bytes12-bytes12-)`pack_12_12(bytes12 left, bytes12 right) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_16-bytes12-bytes16-)`pack_12_16(bytes12 left, bytes16 right) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_12_20-bytes12-bytes20-)`pack_12_20(bytes12 left, bytes20 right) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_4-bytes16-bytes4-)`pack_16_4(bytes16 left, bytes4 right) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_6-bytes16-bytes6-)`pack_16_6(bytes16 left, bytes6 right) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_8-bytes16-bytes8-)`pack_16_8(bytes16 left, bytes8 right) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_12-bytes16-bytes12-)`pack_16_12(bytes16 left, bytes12 right) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_16_16-bytes16-bytes16-)`pack_16_16(bytes16 left, bytes16 right) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_2-bytes20-bytes2-)`pack_20_2(bytes20 left, bytes2 right) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_4-bytes20-bytes4-)`pack_20_4(bytes20 left, bytes4 right) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_8-bytes20-bytes8-)`pack_20_8(bytes20 left, bytes8 right) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_20_12-bytes20-bytes12-)`pack_20_12(bytes20 left, bytes12 right) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_2-bytes22-bytes2-)`pack_22_2(bytes22 left, bytes2 right) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_6-bytes22-bytes6-)`pack_22_6(bytes22 left, bytes6 right) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_22_10-bytes22-bytes10-)`pack_22_10(bytes22 left, bytes10 right) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_24_4-bytes24-bytes4-)`pack_24_4(bytes24 left, bytes4 right) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_24_8-bytes24-bytes8-)`pack_24_8(bytes24 left, bytes8 right) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-pack_28_4-bytes28-bytes4-)`pack_28_4(bytes28 left, bytes4 right) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_2_1-bytes2-bytes1-uint8-)`replace_2_1(bytes2 self, bytes1 value, uint8 offset) → bytes2 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_4_1-bytes4-bytes1-uint8-)`replace_4_1(bytes4 self, bytes1 value, uint8 offset) → bytes4 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_4_2-bytes4-bytes2-uint8-)`replace_4_2(bytes4 self, bytes2 value, uint8 offset) → bytes4 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_1-bytes6-bytes1-uint8-)`replace_6_1(bytes6 self, bytes1 value, uint8 offset) → bytes6 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_2-bytes6-bytes2-uint8-)`replace_6_2(bytes6 self, bytes2 value, uint8 offset) → bytes6 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_6_4-bytes6-bytes4-uint8-)`replace_6_4(bytes6 self, bytes4 value, uint8 offset) → bytes6 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_1-bytes8-bytes1-uint8-)`replace_8_1(bytes8 self, bytes1 value, uint8 offset) → bytes8 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_2-bytes8-bytes2-uint8-)`replace_8_2(bytes8 self, bytes2 value, uint8 offset) → bytes8 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_4-bytes8-bytes4-uint8-)`replace_8_4(bytes8 self, bytes4 value, uint8 offset) → bytes8 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_8_6-bytes8-bytes6-uint8-)`replace_8_6(bytes8 self, bytes6 value, uint8 offset) → bytes8 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_1-bytes10-bytes1-uint8-)`replace_10_1(bytes10 self, bytes1 value, uint8 offset) → bytes10 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_2-bytes10-bytes2-uint8-)`replace_10_2(bytes10 self, bytes2 value, uint8 offset) → bytes10 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_4-bytes10-bytes4-uint8-)`replace_10_4(bytes10 self, bytes4 value, uint8 offset) → bytes10 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_6-bytes10-bytes6-uint8-)`replace_10_6(bytes10 self, bytes6 value, uint8 offset) → bytes10 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_10_8-bytes10-bytes8-uint8-)`replace_10_8(bytes10 self, bytes8 value, uint8 offset) → bytes10 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_1-bytes12-bytes1-uint8-)`replace_12_1(bytes12 self, bytes1 value, uint8 offset) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_2-bytes12-bytes2-uint8-)`replace_12_2(bytes12 self, bytes2 value, uint8 offset) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_4-bytes12-bytes4-uint8-)`replace_12_4(bytes12 self, bytes4 value, uint8 offset) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_6-bytes12-bytes6-uint8-)`replace_12_6(bytes12 self, bytes6 value, uint8 offset) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_8-bytes12-bytes8-uint8-)`replace_12_8(bytes12 self, bytes8 value, uint8 offset) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_12_10-bytes12-bytes10-uint8-)`replace_12_10(bytes12 self, bytes10 value, uint8 offset) → bytes12 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_1-bytes16-bytes1-uint8-)`replace_16_1(bytes16 self, bytes1 value, uint8 offset) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_2-bytes16-bytes2-uint8-)`replace_16_2(bytes16 self, bytes2 value, uint8 offset) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_4-bytes16-bytes4-uint8-)`replace_16_4(bytes16 self, bytes4 value, uint8 offset) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_6-bytes16-bytes6-uint8-)`replace_16_6(bytes16 self, bytes6 value, uint8 offset) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_8-bytes16-bytes8-uint8-)`replace_16_8(bytes16 self, bytes8 value, uint8 offset) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_10-bytes16-bytes10-uint8-)`replace_16_10(bytes16 self, bytes10 value, uint8 offset) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_16_12-bytes16-bytes12-uint8-)`replace_16_12(bytes16 self, bytes12 value, uint8 offset) → bytes16 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_1-bytes20-bytes1-uint8-)`replace_20_1(bytes20 self, bytes1 value, uint8 offset) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_2-bytes20-bytes2-uint8-)`replace_20_2(bytes20 self, bytes2 value, uint8 offset) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_4-bytes20-bytes4-uint8-)`replace_20_4(bytes20 self, bytes4 value, uint8 offset) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_6-bytes20-bytes6-uint8-)`replace_20_6(bytes20 self, bytes6 value, uint8 offset) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_8-bytes20-bytes8-uint8-)`replace_20_8(bytes20 self, bytes8 value, uint8 offset) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_10-bytes20-bytes10-uint8-)`replace_20_10(bytes20 self, bytes10 value, uint8 offset) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_12-bytes20-bytes12-uint8-)`replace_20_12(bytes20 self, bytes12 value, uint8 offset) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_20_16-bytes20-bytes16-uint8-)`replace_20_16(bytes20 self, bytes16 value, uint8 offset) → bytes20 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_1-bytes22-bytes1-uint8-)`replace_22_1(bytes22 self, bytes1 value, uint8 offset) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_2-bytes22-bytes2-uint8-)`replace_22_2(bytes22 self, bytes2 value, uint8 offset) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_4-bytes22-bytes4-uint8-)`replace_22_4(bytes22 self, bytes4 value, uint8 offset) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_6-bytes22-bytes6-uint8-)`replace_22_6(bytes22 self, bytes6 value, uint8 offset) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_8-bytes22-bytes8-uint8-)`replace_22_8(bytes22 self, bytes8 value, uint8 offset) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_10-bytes22-bytes10-uint8-)`replace_22_10(bytes22 self, bytes10 value, uint8 offset) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_12-bytes22-bytes12-uint8-)`replace_22_12(bytes22 self, bytes12 value, uint8 offset) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_16-bytes22-bytes16-uint8-)`replace_22_16(bytes22 self, bytes16 value, uint8 offset) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_22_20-bytes22-bytes20-uint8-)`replace_22_20(bytes22 self, bytes20 value, uint8 offset) → bytes22 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_1-bytes24-bytes1-uint8-)`replace_24_1(bytes24 self, bytes1 value, uint8 offset) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_2-bytes24-bytes2-uint8-)`replace_24_2(bytes24 self, bytes2 value, uint8 offset) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_4-bytes24-bytes4-uint8-)`replace_24_4(bytes24 self, bytes4 value, uint8 offset) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_6-bytes24-bytes6-uint8-)`replace_24_6(bytes24 self, bytes6 value, uint8 offset) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_8-bytes24-bytes8-uint8-)`replace_24_8(bytes24 self, bytes8 value, uint8 offset) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_10-bytes24-bytes10-uint8-)`replace_24_10(bytes24 self, bytes10 value, uint8 offset) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_12-bytes24-bytes12-uint8-)`replace_24_12(bytes24 self, bytes12 value, uint8 offset) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_16-bytes24-bytes16-uint8-)`replace_24_16(bytes24 self, bytes16 value, uint8 offset) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_20-bytes24-bytes20-uint8-)`replace_24_20(bytes24 self, bytes20 value, uint8 offset) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_24_22-bytes24-bytes22-uint8-)`replace_24_22(bytes24 self, bytes22 value, uint8 offset) → bytes24 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_1-bytes28-bytes1-uint8-)`replace_28_1(bytes28 self, bytes1 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_2-bytes28-bytes2-uint8-)`replace_28_2(bytes28 self, bytes2 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_4-bytes28-bytes4-uint8-)`replace_28_4(bytes28 self, bytes4 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_6-bytes28-bytes6-uint8-)`replace_28_6(bytes28 self, bytes6 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_8-bytes28-bytes8-uint8-)`replace_28_8(bytes28 self, bytes8 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_10-bytes28-bytes10-uint8-)`replace_28_10(bytes28 self, bytes10 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_12-bytes28-bytes12-uint8-)`replace_28_12(bytes28 self, bytes12 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_16-bytes28-bytes16-uint8-)`replace_28_16(bytes28 self, bytes16 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_20-bytes28-bytes20-uint8-)`replace_28_20(bytes28 self, bytes20 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_22-bytes28-bytes22-uint8-)`replace_28_22(bytes28 self, bytes22 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_28_24-bytes28-bytes24-uint8-)`replace_28_24(bytes28 self, bytes24 value, uint8 offset) → bytes28 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_1-bytes32-bytes1-uint8-)`replace_32_1(bytes32 self, bytes1 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_2-bytes32-bytes2-uint8-)`replace_32_2(bytes32 self, bytes2 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_4-bytes32-bytes4-uint8-)`replace_32_4(bytes32 self, bytes4 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_6-bytes32-bytes6-uint8-)`replace_32_6(bytes32 self, bytes6 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_8-bytes32-bytes8-uint8-)`replace_32_8(bytes32 self, bytes8 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_10-bytes32-bytes10-uint8-)`replace_32_10(bytes32 self, bytes10 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_12-bytes32-bytes12-uint8-)`replace_32_12(bytes32 self, bytes12 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_16-bytes32-bytes16-uint8-)`replace_32_16(bytes32 self, bytes16 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_20-bytes32-bytes20-uint8-)`replace_32_20(bytes32 self, bytes20 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_22-bytes32-bytes22-uint8-)`replace_32_22(bytes32 self, bytes22 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_24-bytes32-bytes24-uint8-)`replace_32_24(bytes32 self, bytes24 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-replace_32_28-bytes32-bytes28-uint8-)`replace_32_28(bytes32 self, bytes28 value, uint8 offset) → bytes32 result`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Packing-OutOfRangeAccess--)`OutOfRangeAccess()`error

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic)`Panic`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Panic.sol)

`import "@openzeppelin/contracts/utils/Panic.sol";`

Helper library for emitting standardized panic codes.

```
contract Example {
     using Panic for uint256;

     // Use any of the declared internal constants
     function foo() { Panic.GENERIC.panic(); }

     // Alternatively
     function foo() { Panic.panic(Panic.GENERIC); }
}
```

_Available since v5.1._

Internal Variables

*   [`uint256 constant GENERIC`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-GENERIC-uint256)

*   [`uint256 constant ASSERT`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ASSERT-uint256)

*   [`uint256 constant UNDER_OVERFLOW`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-UNDER_OVERFLOW-uint256)

*   [`uint256 constant DIVISION_BY_ZERO`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-DIVISION_BY_ZERO-uint256)

*   [`uint256 constant ENUM_CONVERSION_ERROR`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ENUM_CONVERSION_ERROR-uint256)

*   [`uint256 constant STORAGE_ENCODING_ERROR`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-STORAGE_ENCODING_ERROR-uint256)

*   [`uint256 constant EMPTY_ARRAY_POP`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-EMPTY_ARRAY_POP-uint256)

*   [`uint256 constant ARRAY_OUT_OF_BOUNDS`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ARRAY_OUT_OF_BOUNDS-uint256)

*   [`uint256 constant RESOURCE_ERROR`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-RESOURCE_ERROR-uint256)

*   [`uint256 constant INVALID_INTERNAL_FUNCTION`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-INVALID_INTERNAL_FUNCTION-uint256)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-panic-uint256-)`panic(uint256 code)`internal

Reverts with a panic code. Recommended to use with the internal constants with predefined codes.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-GENERIC-uint256)`uint256 GENERIC`internal constant

generic / unspecified error

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ASSERT-uint256)`uint256 ASSERT`internal constant

used by the assert() builtin

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-UNDER_OVERFLOW-uint256)`uint256 UNDER_OVERFLOW`internal constant

arithmetic underflow or overflow

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-DIVISION_BY_ZERO-uint256)`uint256 DIVISION_BY_ZERO`internal constant

division or modulo by zero

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ENUM_CONVERSION_ERROR-uint256)`uint256 ENUM_CONVERSION_ERROR`internal constant

enum conversion error

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-STORAGE_ENCODING_ERROR-uint256)`uint256 STORAGE_ENCODING_ERROR`internal constant

invalid encoding in storage

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-EMPTY_ARRAY_POP-uint256)`uint256 EMPTY_ARRAY_POP`internal constant

empty array pop

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-ARRAY_OUT_OF_BOUNDS-uint256)`uint256 ARRAY_OUT_OF_BOUNDS`internal constant

array out of bounds access

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-RESOURCE_ERROR-uint256)`uint256 RESOURCE_ERROR`internal constant

resource error (too large allocation or too large array)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Panic-INVALID_INTERNAL_FUNCTION-uint256)`uint256 INVALID_INTERNAL_FUNCTION`internal constant

calling invalid internal function

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators)`Comparators`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Comparators.sol)

`import "@openzeppelin/contracts/utils/Comparators.sol";`

Provides a set of functions to compare values.

_Available since v5.1._

Functions

*   [`lt(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators-lt-uint256-uint256-)

*   [`gt(a, b)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators-gt-uint256-uint256-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators-lt-uint256-uint256-)`lt(uint256 a, uint256 b) → bool`internal

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Comparators-gt-uint256-uint256-)`gt(uint256 a, uint256 b) → bool`internal

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2)`CAIP2`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/CAIP2.sol)

`import "@openzeppelin/contracts/utils/CAIP2.sol";`

Helper library to format and parse CAIP-2 identifiers

[CAIP-2](https://github.com/ChainAgnostic/CAIPs/blob/main/CAIPs/caip-2.md) defines chain identifiers as: chain_id: namespace + ":" + reference namespace: [-a-z0-9]{3,8} reference: [-_a-zA-Z0-9]{1,32}

In some cases, multiple CAIP-2 identifiers may all be valid representation of a single chain. For EVM chains, it is recommended to use `eip155:xxx` as the canonical representation (where `xxx` is the EIP-155 chain id). Consider the possible ambiguity when processing CAIP-2 identifiers or when using them in the context of hashes.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2-local--)`local() → string`internal

Return the CAIP-2 identifier for the current (local) chain.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2-format-string-string-)`format(string namespace, string ref) → string`internal

Return the CAIP-2 identifier for a given namespace and reference.

This function does not verify that the inputs are properly formatted.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2-parse-string-)`parse(string caip2) → string namespace, string ref`internal

Parse a CAIP-2 identifier into its components.

This function does not verify that the CAIP-2 input is properly formatted.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10)`CAIP10`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/CAIP10.sol)

`import "@openzeppelin/contracts/utils/CAIP10.sol";`

Helper library to format and parse CAIP-10 identifiers

[CAIP-10](https://github.com/ChainAgnostic/CAIPs/blob/main/CAIPs/caip-10.md) defines account identifiers as: account_id: chain_id + ":" + account_address chain_id: [-a-z0-9]{3,8}:[-_a-zA-Z0-9]{1,32} (See [`CAIP2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2)) account_address: [-.%a-zA-Z0-9]{1,128}

According to [CAIP-10’s canonicalization section]([https://github.com/ChainAgnostic/CAIPs/blob/main/CAIPs/caip-10.md#canonicalization](https://github.com/ChainAgnostic/CAIPs/blob/main/CAIPs/caip-10.md#canonicalization)), the implementation remains at the developer’s discretion. Please note that case variations may introduce ambiguity. For example, when building hashes to identify accounts or data associated to them, multiple representations of the same account would derive to different hashes. For EVM chains, we recommend using checksummed addresses for the "account_address" part. They can be generated onchain using [`Strings.toChecksumHexString`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Strings-toChecksumHexString-address-).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10-local-address-)`local(address account) → string`internal

Return the CAIP-10 identifier for an account on the current (local) chain.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10-format-string-string-)`format(string caip2, string account) → string`internal

Return the CAIP-10 identifier for a given caip2 chain and account.

This function does not verify that the inputs are properly formatted.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP10-parse-string-)`parse(string caip10) → string caip2, string account`internal

Parse a CAIP-10 identifier into its components.

This function does not verify that the CAIP-10 input is properly formatted. The `caip2` return can be parsed using the [`CAIP2`](https://docs.openzeppelin.com/contracts/5.x/api/utils#CAIP2) library.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Blockhash)`Blockhash`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/Blockhash.sol)

`import "@openzeppelin/contracts/utils/Blockhash.sol";`

Library for accessing historical block hashes beyond the standard 256 block limit. Uses EIP-2935’s history storage contract which maintains a ring buffer of the last 8191 block hashes in state.

For blocks within the last 256 blocks, it uses the native `BLOCKHASH` opcode. For blocks between 257 and 8191 blocks ago, it queries the EIP-2935 history storage. For blocks older than 8191 or future blocks, it returns zero, matching the `BLOCKHASH` behavior.

After EIP-2935 activation, it takes 8191 blocks to completely fill the history. Before that, only block hashes since the fork block will be available.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Blockhash-blockHash-uint256-)`blockHash(uint256 blockNumber) → bytes32`internal

Retrieves the block hash for any historical block within the supported range.

The function gracefully handles future blocks and blocks beyond the history window by returning zero, consistent with the EVM’s native `BLOCKHASH` behavior.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Blockhash-HISTORY_STORAGE_ADDRESS-address)`address HISTORY_STORAGE_ADDRESS`internal constant

Address of the EIP-2935 history storage contract.

### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time)`Time`[](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v5.4.0/contracts/utils/types/Time.sol)

`import "@openzeppelin/contracts/utils/types/Time.sol";`

This library provides helpers for manipulating time-related objects.

It uses the following types: - `uint48` for timepoints - `uint32` for durations

While the library doesn’t provide specific types for timepoints and duration, it does provide: - a `Delay` type to represent duration that can be programmed to change value automatically at a given point - additional helper functions

Functions

*   [`timestamp()`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-timestamp--)

*   [`blockNumber()`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-blockNumber--)

*   [`toDelay(duration)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-toDelay-uint32-)

*   [`getFull(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-getFull-Time-Delay-)

*   [`get(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-get-Time-Delay-)

*   [`withUpdate(self, newValue, minSetback)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-withUpdate-Time-Delay-uint32-uint32-)

*   [`unpack(self)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-unpack-Time-Delay-)

*   [`pack(valueBefore, valueAfter, effect)`](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-pack-uint32-uint32-uint48-)

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-timestamp--)`timestamp() → uint48`internal

Get the block timestamp as a Timepoint.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-blockNumber--)`blockNumber() → uint48`internal

Get the block number as a Timepoint.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-toDelay-uint32-)`toDelay(uint32 duration) → Time.Delay`internal

Wrap a duration into a Delay to add the one-step "update in the future" feature

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-getFull-Time-Delay-)`getFull(Time.Delay self) → uint32 valueBefore, uint32 valueAfter, uint48 effect`internal

Get the current value plus the pending value and effect timepoint if there is a scheduled change. If the effect timepoint is 0, then the pending value should not be considered.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-get-Time-Delay-)`get(Time.Delay self) → uint32`internal

Get the current value.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-withUpdate-Time-Delay-uint32-uint32-)`withUpdate(Time.Delay self, uint32 newValue, uint32 minSetback) → Time.Delay updatedDelay, uint48 effect`internal

Update a Delay object so that it takes a new duration after a timepoint that is automatically computed to enforce the old delay at the moment of the update. Returns the updated Delay object and the timestamp when the new delay becomes effective.

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-unpack-Time-Delay-)`unpack(Time.Delay self) → uint32 valueBefore, uint32 valueAfter, uint48 effect`internal

Split a delay into its components: valueBefore, valueAfter and effect (transition timepoint).

#### [](https://docs.openzeppelin.com/contracts/5.x/api/utils#Time-pack-uint32-uint32-uint48-)`pack(uint32 valueBefore, uint32 valueAfter, uint48 effect) → Time.Delay`internal

pack the components into a Delay object.
