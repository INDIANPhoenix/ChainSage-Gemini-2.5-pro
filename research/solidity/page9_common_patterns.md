Title: Common Patterns — Solidity 0.8.31 documentation

URL Source: https://docs.soliditylang.org/en/latest/common-patterns.html

Markdown Content:
Withdrawal from Contracts[](https://docs.soliditylang.org/en/latest/common-patterns.html#withdrawal-from-contracts "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------

The recommended method of sending funds after an effect is using the withdrawal pattern. Although the most intuitive method of sending Ether, as a result of an effect, is a direct `transfer` call, this is not recommended as it introduces a potential security risk. You may read more about this on the [Security Considerations](https://docs.soliditylang.org/en/latest/security-considerations.html#security-considerations) page.

The following is an example of the withdrawal pattern in practice in a contract where the goal is to send the most of some compensation, e.g. Ether, to the contract in order to become the “richest”, inspired by [King of the Ether](https://www.kingoftheether.com/).

In the following contract, if you are no longer the richest, you receive the funds of the person who is now the richest.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguNDsKCmNvbnRyYWN0IFdpdGhkcmF3YWxDb250cmFjdCB7CiAgICBhZGRyZXNzIHB1YmxpYyByaWNoZXN0OwogICAgdWludCBwdWJsaWMgbW9zdFNlbnQ7CgogICAgbWFwcGluZyhhZGRyZXNzID0+IHVpbnQpIHBlbmRpbmdXaXRoZHJhd2FsczsKCiAgICAvLy8gVGhlIGFtb3VudCBvZiBFdGhlciBzZW50IHdhcyBub3QgaGlnaGVyIHRoYW4KICAgIC8vLyB0aGUgY3VycmVudGx5IGhpZ2hlc3QgYW1vdW50LgogICAgZXJyb3IgTm90RW5vdWdoRXRoZXIoKTsKCiAgICBjb25zdHJ1Y3RvcigpIHBheWFibGUgewogICAgICAgIHJpY2hlc3QgPSBtc2cuc2VuZGVyOwogICAgICAgIG1vc3RTZW50ID0gbXNnLnZhbHVlOwogICAgfQoKICAgIGZ1bmN0aW9uIGJlY29tZVJpY2hlc3QoKSBwdWJsaWMgcGF5YWJsZSB7CiAgICAgICAgaWYgKG1zZy52YWx1ZSA8PSBtb3N0U2VudCkgcmV2ZXJ0IE5vdEVub3VnaEV0aGVyKCk7CiAgICAgICAgcGVuZGluZ1dpdGhkcmF3YWxzW3JpY2hlc3RdICs9IG1zZy52YWx1ZTsKICAgICAgICByaWNoZXN0ID0gbXNnLnNlbmRlcjsKICAgICAgICBtb3N0U2VudCA9IG1zZy52YWx1ZTsKICAgIH0KCiAgICBmdW5jdGlvbiB3aXRoZHJhdygpIHB1YmxpYyB7CiAgICAgICAgdWludCBhbW91bnQgPSBwZW5kaW5nV2l0aGRyYXdhbHNbbXNnLnNlbmRlcl07CiAgICAgICAgLy8gUmVtZW1iZXIgdG8gemVybyB0aGUgcGVuZGluZyByZWZ1bmQgYmVmb3JlCiAgICAgICAgLy8gc2VuZGluZyB0byBwcmV2ZW50IHJlZW50cmFuY3kgYXR0YWNrcwogICAgICAgIHBlbmRpbmdXaXRoZHJhd2Fsc1ttc2cuc2VuZGVyXSA9IDA7CiAgICAgICAgcGF5YWJsZShtc2cuc2VuZGVyKS50cmFuc2ZlcihhbW91bnQpOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

contract WithdrawalContract {
 address public richest;
 uint public mostSent;

 mapping(address => uint) pendingWithdrawals;

 /// The amount of Ether sent was not higher than
 /// the currently highest amount.
 error NotEnoughEther();

 constructor() payable {
 richest = msg.sender;
 mostSent = msg.value;
 }

 function becomeRichest() public payable {
 if (msg.value <= mostSent) revert NotEnoughEther();
 pendingWithdrawals[richest] += msg.value;
 richest = msg.sender;
 mostSent = msg.value;
 }

 function withdraw() public {
 uint amount = pendingWithdrawals[msg.sender];
 // Remember to zero the pending refund before
 // sending to prevent reentrancy attacks
 pendingWithdrawals[msg.sender] = 0;
 payable(msg.sender).transfer(amount);
 }
}

This is as opposed to the more intuitive sending pattern:

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguNDsKCmNvbnRyYWN0IFNlbmRDb250cmFjdCB7CiAgICBhZGRyZXNzIHBheWFibGUgcHVibGljIHJpY2hlc3Q7CiAgICB1aW50IHB1YmxpYyBtb3N0U2VudDsKCiAgICAvLy8gVGhlIGFtb3VudCBvZiBFdGhlciBzZW50IHdhcyBub3QgaGlnaGVyIHRoYW4KICAgIC8vLyB0aGUgY3VycmVudGx5IGhpZ2hlc3QgYW1vdW50LgogICAgZXJyb3IgTm90RW5vdWdoRXRoZXIoKTsKCiAgICBjb25zdHJ1Y3RvcigpIHBheWFibGUgewogICAgICAgIHJpY2hlc3QgPSBwYXlhYmxlKG1zZy5zZW5kZXIpOwogICAgICAgIG1vc3RTZW50ID0gbXNnLnZhbHVlOwogICAgfQoKICAgIGZ1bmN0aW9uIGJlY29tZVJpY2hlc3QoKSBwdWJsaWMgcGF5YWJsZSB7CiAgICAgICAgaWYgKG1zZy52YWx1ZSA8PSBtb3N0U2VudCkgcmV2ZXJ0IE5vdEVub3VnaEV0aGVyKCk7CiAgICAgICAgLy8gVGhpcyBsaW5lIGNhbiBjYXVzZSBwcm9ibGVtcyAoZXhwbGFpbmVkIGJlbG93KS4KICAgICAgICByaWNoZXN0LnRyYW5zZmVyKG1zZy52YWx1ZSk7CiAgICAgICAgcmljaGVzdCA9IHBheWFibGUobXNnLnNlbmRlcik7CiAgICAgICAgbW9zdFNlbnQgPSBtc2cudmFsdWU7CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

contract SendContract {
 address payable public richest;
 uint public mostSent;

 /// The amount of Ether sent was not higher than
 /// the currently highest amount.
 error NotEnoughEther();

 constructor() payable {
 richest = payable(msg.sender);
 mostSent = msg.value;
 }

 function becomeRichest() public payable {
 if (msg.value <= mostSent) revert NotEnoughEther();
 // This line can cause problems (explained below).
 richest.transfer(msg.value);
 richest = payable(msg.sender);
 mostSent = msg.value;
 }
}

Notice that, in this example, an attacker could trap the contract into an unusable state by causing `richest` to be the address of a contract that has a receive or fallback function which fails (e.g. by using `revert()` or by just consuming more than the 2300 gas stipend transferred to them). That way, whenever `transfer` is called to deliver funds to the “poisoned” contract, it will fail and thus also `becomeRichest` will fail, with the contract being stuck forever.

In contrast, if you use the “withdraw” pattern from the first example, the attacker can only cause his or her own withdraw to fail and not the rest of the contract’s workings.

Restricting Access[](https://docs.soliditylang.org/en/latest/common-patterns.html#restricting-access "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

Restricting access is a common pattern for contracts. Note that you can never restrict any human or computer from reading the content of your transactions or your contract’s state. You can make it a bit harder by using encryption, but if your contract is supposed to read the data, so will everyone else.

You can restrict read access to your contract’s state by **other contracts**. That is actually the default unless you declare your state variables `public`.

Furthermore, you can restrict who can make modifications to your contract’s state or call your contract’s functions and this is what this section is about.

The use of **function modifiers** makes these restrictions highly readable.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguNDsKCmNvbnRyYWN0IEFjY2Vzc1Jlc3RyaWN0aW9uIHsKICAgIC8vIFRoZXNlIHdpbGwgYmUgYXNzaWduZWQgYXQgdGhlIGNvbnN0cnVjdGlvbgogICAgLy8gcGhhc2UsIHdoZXJlIGBtc2cuc2VuZGVyYCBpcyB0aGUgYWNjb3VudAogICAgLy8gY3JlYXRpbmcgdGhpcyBjb250cmFjdC4KICAgIGFkZHJlc3MgcHVibGljIG93bmVyID0gbXNnLnNlbmRlcjsKICAgIHVpbnQgcHVibGljIGNyZWF0aW9uVGltZSA9IGJsb2NrLnRpbWVzdGFtcDsKCiAgICAvLyBOb3cgZm9sbG93cyBhIGxpc3Qgb2YgZXJyb3JzIHRoYXQKICAgIC8vIHRoaXMgY29udHJhY3QgY2FuIGdlbmVyYXRlIHRvZ2V0aGVyCiAgICAvLyB3aXRoIGEgdGV4dHVhbCBleHBsYW5hdGlvbiBpbiBzcGVjaWFsCiAgICAvLyBjb21tZW50cy4KCiAgICAvLy8gU2VuZGVyIG5vdCBhdXRob3JpemVkIGZvciB0aGlzCiAgICAvLy8gb3BlcmF0aW9uLgogICAgZXJyb3IgVW5hdXRob3JpemVkKCk7CgogICAgLy8vIEZ1bmN0aW9uIGNhbGxlZCB0b28gZWFybHkuCiAgICBlcnJvciBUb29FYXJseSgpOwoKICAgIC8vLyBOb3QgZW5vdWdoIEV0aGVyIHNlbnQgd2l0aCBmdW5jdGlvbiBjYWxsLgogICAgZXJyb3IgTm90RW5vdWdoRXRoZXIoKTsKCiAgICAvLyBNb2RpZmllcnMgY2FuIGJlIHVzZWQgdG8gY2hhbmdlCiAgICAvLyB0aGUgYm9keSBvZiBhIGZ1bmN0aW9uLgogICAgLy8gSWYgdGhpcyBtb2RpZmllciBpcyB1c2VkLCBpdCB3aWxsCiAgICAvLyBwcmVwZW5kIGEgY2hlY2sgdGhhdCBvbmx5IHBhc3NlcwogICAgLy8gaWYgdGhlIGZ1bmN0aW9uIGlzIGNhbGxlZCBmcm9tCiAgICAvLyBhIGNlcnRhaW4gYWRkcmVzcy4KICAgIG1vZGlmaWVyIG9ubHlCeShhZGRyZXNzIGFjY291bnQpCiAgICB7CiAgICAgICAgaWYgKG1zZy5zZW5kZXIgIT0gYWNjb3VudCkKICAgICAgICAgICAgcmV2ZXJ0IFVuYXV0aG9yaXplZCgpOwogICAgICAgIC8vIERvIG5vdCBmb3JnZXQgdGhlICJfOyIhIEl0IHdpbGwKICAgICAgICAvLyBiZSByZXBsYWNlZCBieSB0aGUgYWN0dWFsIGZ1bmN0aW9uCiAgICAgICAgLy8gYm9keSB3aGVuIHRoZSBtb2RpZmllciBpcyB1c2VkLgogICAgICAgIF87CiAgICB9CgogICAgLy8vIE1ha2UgYG5ld093bmVyYCB0aGUgbmV3IG93bmVyIG9mIHRoaXMKICAgIC8vLyBjb250cmFjdC4KICAgIGZ1bmN0aW9uIGNoYW5nZU93bmVyKGFkZHJlc3MgbmV3T3duZXIpCiAgICAgICAgcHVibGljCiAgICAgICAgb25seUJ5KG93bmVyKQogICAgewogICAgICAgIG93bmVyID0gbmV3T3duZXI7CiAgICB9CgogICAgbW9kaWZpZXIgb25seUFmdGVyKHVpbnQgdGltZSkgewogICAgICAgIGlmIChibG9jay50aW1lc3RhbXAgPCB0aW1lKQogICAgICAgICAgICByZXZlcnQgVG9vRWFybHkoKTsKICAgICAgICBfOwogICAgfQoKICAgIC8vLyBFcmFzZSBvd25lcnNoaXAgaW5mb3JtYXRpb24uCiAgICAvLy8gTWF5IG9ubHkgYmUgY2FsbGVkIDYgd2Vla3MgYWZ0ZXIKICAgIC8vLyB0aGUgY29udHJhY3QgaGFzIGJlZW4gY3JlYXRlZC4KICAgIGZ1bmN0aW9uIGRpc293bigpCiAgICAgICAgcHVibGljCiAgICAgICAgb25seUJ5KG93bmVyKQogICAgICAgIG9ubHlBZnRlcihjcmVhdGlvblRpbWUgKyA2IHdlZWtzKQogICAgewogICAgICAgIGRlbGV0ZSBvd25lcjsKICAgIH0KCiAgICAvLyBUaGlzIG1vZGlmaWVyIHJlcXVpcmVzIGEgY2VydGFpbgogICAgLy8gZmVlIGJlaW5nIGFzc29jaWF0ZWQgd2l0aCBhIGZ1bmN0aW9uIGNhbGwuCiAgICAvLyBJZiB0aGUgY2FsbGVyIHNlbnQgdG9vIG11Y2gsIGhlIG9yIHNoZSBpcwogICAgLy8gcmVmdW5kZWQsIGJ1dCBvbmx5IGFmdGVyIHRoZSBmdW5jdGlvbiBib2R5LgogICAgLy8gVGhpcyB3YXMgZGFuZ2Vyb3VzIGJlZm9yZSBTb2xpZGl0eSB2ZXJzaW9uIDAuNC4wLAogICAgLy8gd2hlcmUgaXQgd2FzIHBvc3NpYmxlIHRvIHNraXAgdGhlIHBhcnQgYWZ0ZXIgYF87YC4KICAgIG1vZGlmaWVyIGNvc3RzKHVpbnQgYW1vdW50KSB7CiAgICAgICAgaWYgKG1zZy52YWx1ZSA8IGFtb3VudCkKICAgICAgICAgICAgcmV2ZXJ0IE5vdEVub3VnaEV0aGVyKCk7CgogICAgICAgIF87CiAgICAgICAgaWYgKG1zZy52YWx1ZSA+IGFtb3VudCkKICAgICAgICAgICAgcGF5YWJsZShtc2cuc2VuZGVyKS50cmFuc2Zlcihtc2cudmFsdWUgLSBhbW91bnQpOwogICAgfQoKICAgIGZ1bmN0aW9uIGZvcmNlT3duZXJDaGFuZ2UoYWRkcmVzcyBuZXdPd25lcikKICAgICAgICBwdWJsaWMKICAgICAgICBwYXlhYmxlCiAgICAgICAgY29zdHMoMjAwIGV0aGVyKQogICAgewogICAgICAgIG93bmVyID0gbmV3T3duZXI7CiAgICAgICAgLy8ganVzdCBzb21lIGV4YW1wbGUgY29uZGl0aW9uCiAgICAgICAgaWYgKHVpbnQxNjAob3duZXIpICYgMCA9PSAxKQogICAgICAgICAgICAvLyBUaGlzIGRpZCBub3QgcmVmdW5kIGZvciBTb2xpZGl0eQogICAgICAgICAgICAvLyBiZWZvcmUgdmVyc2lvbiAwLjQuMC4KICAgICAgICAgICAgcmV0dXJuOwogICAgICAgIC8vIHJlZnVuZCBvdmVycGFpZCBmZWVzCiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

contract AccessRestriction {
 // These will be assigned at the construction
 // phase, where `msg.sender` is the account
 // creating this contract.
 address public owner = msg.sender;
 uint public creationTime = block.timestamp;

 // Now follows a list of errors that
 // this contract can generate together
 // with a textual explanation in special
 // comments.

 /// Sender not authorized for this
 /// operation.
 error Unauthorized();

 /// Function called too early.
 error TooEarly();

 /// Not enough Ether sent with function call.
 error NotEnoughEther();

 // Modifiers can be used to change
 // the body of a function.
 // If this modifier is used, it will
 // prepend a check that only passes
 // if the function is called from
 // a certain address.
 modifier onlyBy(address account)
 {
 if (msg.sender != account)
 revert Unauthorized();
 // Do not forget the "_;"! It will
 // be replaced by the actual function
 // body when the modifier is used.
 _;
 }

 /// Make `newOwner` the new owner of this
 /// contract.
 function changeOwner(address newOwner)
 public
 onlyBy(owner)
 {
 owner = newOwner;
 }

 modifier onlyAfter(uint time) {
 if (block.timestamp < time)
 revert TooEarly();
 _;
 }

 /// Erase ownership information.
 /// May only be called 6 weeks after
 /// the contract has been created.
 function disown()
 public
 onlyBy(owner)
 onlyAfter(creationTime + 6 weeks)
 {
 delete owner;
 }

 // This modifier requires a certain
 // fee being associated with a function call.
 // If the caller sent too much, he or she is
 // refunded, but only after the function body.
 // This was dangerous before Solidity version 0.4.0,
 // where it was possible to skip the part after `_;`.
 modifier costs(uint amount) {
 if (msg.value < amount)
 revert NotEnoughEther();

 _;
 if (msg.value > amount)
 payable(msg.sender).transfer(msg.value - amount);
 }

 function forceOwnerChange(address newOwner)
 public
 payable
 costs(200 ether)
 {
 owner = newOwner;
 // just some example condition
 if (uint160(owner) & 0 == 1)
 // This did not refund for Solidity
 // before version 0.4.0.
 return;
 // refund overpaid fees
 }
}

A more specialised way in which access to function calls can be restricted will be discussed in the next example.

State Machine[](https://docs.soliditylang.org/en/latest/common-patterns.html#state-machine "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

Contracts often act as a state machine, which means that they have certain **stages** in which they behave differently or in which different functions can be called. A function call often ends a stage and transitions the contract into the next stage (especially if the contract models **interaction**). It is also common that some stages are automatically reached at a certain point in **time**.

An example for this is a blind auction contract which starts in the stage “accepting blinded bids”, then transitions to “revealing bids” which is ended by “determine auction outcome”.

Function modifiers can be used in this situation to model the states and guard against incorrect usage of the contract.

### Example[](https://docs.soliditylang.org/en/latest/common-patterns.html#example "Link to this heading")

In the following example, the modifier `atStage` ensures that the function can only be called at a certain stage.

Automatic timed transitions are handled by the modifier `timedTransitions`, which should be used for all functions.

Note

**Modifier Order Matters**. If atStage is combined with timedTransitions, make sure that you mention it after the latter, so that the new stage is taken into account.

Finally, the modifier `transitionNext` can be used to automatically go to the next stage when the function finishes.

Note

**Modifier May be Skipped**. This only applies to Solidity before version 0.4.0: Since modifiers are applied by simply replacing code and not by using a function call, the code in the transitionNext modifier can be skipped if the function itself uses return. If you want to do that, make sure to call nextStage manually from those functions. Starting with version 0.4.0, modifier code will run even if the function explicitly returns.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguNDsKCmNvbnRyYWN0IFN0YXRlTWFjaGluZSB7CiAgICBlbnVtIFN0YWdlcyB7CiAgICAgICAgQWNjZXB0aW5nQmxpbmRlZEJpZHMsCiAgICAgICAgUmV2ZWFsQmlkcywKICAgICAgICBBbm90aGVyU3RhZ2UsCiAgICAgICAgQXJlV2VEb25lWWV0LAogICAgICAgIEZpbmlzaGVkCiAgICB9CiAgICAvLy8gRnVuY3Rpb24gY2Fubm90IGJlIGNhbGxlZCBhdCB0aGlzIHRpbWUuCiAgICBlcnJvciBGdW5jdGlvbkludmFsaWRBdFRoaXNTdGFnZSgpOwoKICAgIC8vIFRoaXMgaXMgdGhlIGN1cnJlbnQgc3RhZ2UuCiAgICBTdGFnZXMgcHVibGljIHN0YWdlID0gU3RhZ2VzLkFjY2VwdGluZ0JsaW5kZWRCaWRzOwoKICAgIHVpbnQgcHVibGljIGNyZWF0aW9uVGltZSA9IGJsb2NrLnRpbWVzdGFtcDsKCiAgICBtb2RpZmllciBhdFN0YWdlKFN0YWdlcyBzdGFnZV8pIHsKICAgICAgICBpZiAoc3RhZ2UgIT0gc3RhZ2VfKQogICAgICAgICAgICByZXZlcnQgRnVuY3Rpb25JbnZhbGlkQXRUaGlzU3RhZ2UoKTsKICAgICAgICBfOwogICAgfQoKICAgIGZ1bmN0aW9uIG5leHRTdGFnZSgpIGludGVybmFsIHsKICAgICAgICBzdGFnZSA9IFN0YWdlcyh1aW50KHN0YWdlKSArIDEpOwogICAgfQoKICAgIC8vIFBlcmZvcm0gdGltZWQgdHJhbnNpdGlvbnMuIEJlIHN1cmUgdG8gbWVudGlvbgogICAgLy8gdGhpcyBtb2RpZmllciBmaXJzdCwgb3RoZXJ3aXNlIHRoZSBndWFyZHMKICAgIC8vIHdpbGwgbm90IHRha2UgdGhlIG5ldyBzdGFnZSBpbnRvIGFjY291bnQuCiAgICBtb2RpZmllciB0aW1lZFRyYW5zaXRpb25zKCkgewogICAgICAgIGlmIChzdGFnZSA9PSBTdGFnZXMuQWNjZXB0aW5nQmxpbmRlZEJpZHMgJiYKICAgICAgICAgICAgICAgICAgICBibG9jay50aW1lc3RhbXAgPj0gY3JlYXRpb25UaW1lICsgMTAgZGF5cykKICAgICAgICAgICAgbmV4dFN0YWdlKCk7CiAgICAgICAgaWYgKHN0YWdlID09IFN0YWdlcy5SZXZlYWxCaWRzICYmCiAgICAgICAgICAgICAgICBibG9jay50aW1lc3RhbXAgPj0gY3JlYXRpb25UaW1lICsgMTIgZGF5cykKICAgICAgICAgICAgbmV4dFN0YWdlKCk7CiAgICAgICAgLy8gVGhlIG90aGVyIHN0YWdlcyB0cmFuc2l0aW9uIGJ5IHRyYW5zYWN0aW9uCiAgICAgICAgXzsKICAgIH0KCiAgICAvLyBPcmRlciBvZiB0aGUgbW9kaWZpZXJzIG1hdHRlcnMgaGVyZSEKICAgIGZ1bmN0aW9uIGJpZCgpCiAgICAgICAgcHVibGljCiAgICAgICAgcGF5YWJsZQogICAgICAgIHRpbWVkVHJhbnNpdGlvbnMKICAgICAgICBhdFN0YWdlKFN0YWdlcy5BY2NlcHRpbmdCbGluZGVkQmlkcykKICAgIHsKICAgICAgICAvLyBXZSB3aWxsIG5vdCBpbXBsZW1lbnQgdGhhdCBoZXJlCiAgICB9CgogICAgZnVuY3Rpb24gcmV2ZWFsKCkKICAgICAgICBwdWJsaWMKICAgICAgICB0aW1lZFRyYW5zaXRpb25zCiAgICAgICAgYXRTdGFnZShTdGFnZXMuUmV2ZWFsQmlkcykKICAgIHsKICAgIH0KCiAgICAvLyBUaGlzIG1vZGlmaWVyIGdvZXMgdG8gdGhlIG5leHQgc3RhZ2UKICAgIC8vIGFmdGVyIHRoZSBmdW5jdGlvbiBpcyBkb25lLgogICAgbW9kaWZpZXIgdHJhbnNpdGlvbk5leHQoKQogICAgewogICAgICAgIF87CiAgICAgICAgbmV4dFN0YWdlKCk7CiAgICB9CgogICAgZnVuY3Rpb24gZygpCiAgICAgICAgcHVibGljCiAgICAgICAgdGltZWRUcmFuc2l0aW9ucwogICAgICAgIGF0U3RhZ2UoU3RhZ2VzLkFub3RoZXJTdGFnZSkKICAgICAgICB0cmFuc2l0aW9uTmV4dAogICAgewogICAgfQoKICAgIGZ1bmN0aW9uIGgoKQogICAgICAgIHB1YmxpYwogICAgICAgIHRpbWVkVHJhbnNpdGlvbnMKICAgICAgICBhdFN0YWdlKFN0YWdlcy5BcmVXZURvbmVZZXQpCiAgICAgICAgdHJhbnNpdGlvbk5leHQKICAgIHsKICAgIH0KCiAgICBmdW5jdGlvbiBpKCkKICAgICAgICBwdWJsaWMKICAgICAgICB0aW1lZFRyYW5zaXRpb25zCiAgICAgICAgYXRTdGFnZShTdGFnZXMuRmluaXNoZWQpCiAgICB7CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

contract StateMachine {
 enum Stages {
 AcceptingBlindedBids,
 RevealBids,
 AnotherStage,
 AreWeDoneYet,
 Finished
 }
 /// Function cannot be called at this time.
 error FunctionInvalidAtThisStage();

 // This is the current stage.
 Stages public stage = Stages.AcceptingBlindedBids;

 uint public creationTime = block.timestamp;

 modifier atStage(Stages stage_) {
 if (stage != stage_)
 revert FunctionInvalidAtThisStage();
 _;
 }

 function nextStage() internal {
 stage = Stages(uint(stage) + 1);
 }

 // Perform timed transitions. Be sure to mention
 // this modifier first, otherwise the guards
 // will not take the new stage into account.
 modifier timedTransitions() {
 if (stage == Stages.AcceptingBlindedBids &&
 block.timestamp >= creationTime + 10 days)
 nextStage();
 if (stage == Stages.RevealBids &&
 block.timestamp >= creationTime + 12 days)
 nextStage();
 // The other stages transition by transaction
 _;
 }

 // Order of the modifiers matters here!
 function bid()
 public
 payable
 timedTransitions
 atStage(Stages.AcceptingBlindedBids)
 {
 // We will not implement that here
 }

 function reveal()
 public
 timedTransitions
 atStage(Stages.RevealBids)
 {
 }

 // This modifier goes to the next stage
 // after the function is done.
 modifier transitionNext()
 {
 _;
 nextStage();
 }

 function g()
 public
 timedTransitions
 atStage(Stages.AnotherStage)
 transitionNext
 {
 }

 function h()
 public
 timedTransitions
 atStage(Stages.AreWeDoneYet)
 transitionNext
 {
 }

 function i()
 public
 timedTransitions
 atStage(Stages.Finished)
 {
 }
}
