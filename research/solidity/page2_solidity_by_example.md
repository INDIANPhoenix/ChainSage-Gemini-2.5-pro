Title: Solidity by Example — Solidity 0.8.31 documentation

URL Source: https://docs.soliditylang.org/en/latest/solidity-by-example.html

Published Time: Wed, 07 May 2025 17:06:12 GMT

Markdown Content:
Voting[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#voting "Link to this heading")
---------------------------------------------------------------------------------------------------------

The following contract is quite complex, but showcases a lot of Solidity’s features. It implements a voting contract. Of course, the main problems of electronic voting is how to assign voting rights to the correct persons and how to prevent manipulation. We will not solve all problems here, but at least we will show how delegated voting can be done so that vote counting is **automatic and completely transparent** at the same time.

The idea is to create one contract per ballot, providing a short name for each option. Then the creator of the contract who serves as chairperson will give the right to vote to each address individually.

The persons behind the addresses can then choose to either vote themselves or to delegate their vote to a person they trust.

At the end of the voting time, `winningProposal()` will return the proposal with the largest number of votes.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjAgPDAuOS4wOwovLy8gQHRpdGxlIFZvdGluZyB3aXRoIGRlbGVnYXRpb24uCmNvbnRyYWN0IEJhbGxvdCB7CiAgICAvLyBUaGlzIGRlY2xhcmVzIGEgbmV3IGNvbXBsZXggdHlwZSB3aGljaCB3aWxsCiAgICAvLyBiZSB1c2VkIGZvciB2YXJpYWJsZXMgbGF0ZXIuCiAgICAvLyBJdCB3aWxsIHJlcHJlc2VudCBhIHNpbmdsZSB2b3Rlci4KICAgIHN0cnVjdCBWb3RlciB7CiAgICAgICAgdWludCB3ZWlnaHQ7IC8vIHdlaWdodCBpcyBhY2N1bXVsYXRlZCBieSBkZWxlZ2F0aW9uCiAgICAgICAgYm9vbCB2b3RlZDsgIC8vIGlmIHRydWUsIHRoYXQgcGVyc29uIGFscmVhZHkgdm90ZWQKICAgICAgICBhZGRyZXNzIGRlbGVnYXRlOyAvLyBwZXJzb24gZGVsZWdhdGVkIHRvCiAgICAgICAgdWludCB2b3RlOyAgIC8vIGluZGV4IG9mIHRoZSB2b3RlZCBwcm9wb3NhbAogICAgfQoKICAgIC8vIFRoaXMgaXMgYSB0eXBlIGZvciBhIHNpbmdsZSBwcm9wb3NhbC4KICAgIHN0cnVjdCBQcm9wb3NhbCB7CiAgICAgICAgYnl0ZXMzMiBuYW1lOyAgIC8vIHNob3J0IG5hbWUgKHVwIHRvIDMyIGJ5dGVzKQogICAgICAgIHVpbnQgdm90ZUNvdW50OyAvLyBudW1iZXIgb2YgYWNjdW11bGF0ZWQgdm90ZXMKICAgIH0KCiAgICBhZGRyZXNzIHB1YmxpYyBjaGFpcnBlcnNvbjsKCiAgICAvLyBUaGlzIGRlY2xhcmVzIGEgc3RhdGUgdmFyaWFibGUgdGhhdAogICAgLy8gc3RvcmVzIGEgYFZvdGVyYCBzdHJ1Y3QgZm9yIGVhY2ggcG9zc2libGUgYWRkcmVzcy4KICAgIG1hcHBpbmcoYWRkcmVzcyA9PiBWb3RlcikgcHVibGljIHZvdGVyczsKCiAgICAvLyBBIGR5bmFtaWNhbGx5LXNpemVkIGFycmF5IG9mIGBQcm9wb3NhbGAgc3RydWN0cy4KICAgIFByb3Bvc2FsW10gcHVibGljIHByb3Bvc2FsczsKCiAgICAvLy8gQ3JlYXRlIGEgbmV3IGJhbGxvdCB0byBjaG9vc2Ugb25lIG9mIGBwcm9wb3NhbE5hbWVzYC4KICAgIGNvbnN0cnVjdG9yKGJ5dGVzMzJbXSBtZW1vcnkgcHJvcG9zYWxOYW1lcykgewogICAgICAgIGNoYWlycGVyc29uID0gbXNnLnNlbmRlcjsKICAgICAgICB2b3RlcnNbY2hhaXJwZXJzb25dLndlaWdodCA9IDE7CgogICAgICAgIC8vIEZvciBlYWNoIG9mIHRoZSBwcm92aWRlZCBwcm9wb3NhbCBuYW1lcywKICAgICAgICAvLyBjcmVhdGUgYSBuZXcgcHJvcG9zYWwgb2JqZWN0IGFuZCBhZGQgaXQKICAgICAgICAvLyB0byB0aGUgZW5kIG9mIHRoZSBhcnJheS4KICAgICAgICBmb3IgKHVpbnQgaSA9IDA7IGkgPCBwcm9wb3NhbE5hbWVzLmxlbmd0aDsgaSsrKSB7CiAgICAgICAgICAgIC8vIGBQcm9wb3NhbCh7Li4ufSlgIGNyZWF0ZXMgYSB0ZW1wb3JhcnkKICAgICAgICAgICAgLy8gUHJvcG9zYWwgb2JqZWN0IGFuZCBgcHJvcG9zYWxzLnB1c2goLi4uKWAKICAgICAgICAgICAgLy8gYXBwZW5kcyBpdCB0byB0aGUgZW5kIG9mIGBwcm9wb3NhbHNgLgogICAgICAgICAgICBwcm9wb3NhbHMucHVzaChQcm9wb3NhbCh7CiAgICAgICAgICAgICAgICBuYW1lOiBwcm9wb3NhbE5hbWVzW2ldLAogICAgICAgICAgICAgICAgdm90ZUNvdW50OiAwCiAgICAgICAgICAgIH0pKTsKICAgICAgICB9CiAgICB9CgogICAgLy8gR2l2ZSBgdm90ZXJgIHRoZSByaWdodCB0byB2b3RlIG9uIHRoaXMgYmFsbG90LgogICAgLy8gTWF5IG9ubHkgYmUgY2FsbGVkIGJ5IGBjaGFpcnBlcnNvbmAuCiAgICBmdW5jdGlvbiBnaXZlUmlnaHRUb1ZvdGUoYWRkcmVzcyB2b3RlcikgZXh0ZXJuYWwgewogICAgICAgIC8vIElmIHRoZSBmaXJzdCBhcmd1bWVudCBvZiBgcmVxdWlyZWAgZXZhbHVhdGVzCiAgICAgICAgLy8gdG8gYGZhbHNlYCwgZXhlY3V0aW9uIHRlcm1pbmF0ZXMgYW5kIGFsbAogICAgICAgIC8vIGNoYW5nZXMgdG8gdGhlIHN0YXRlIGFuZCB0byBFdGhlciBiYWxhbmNlcwogICAgICAgIC8vIGFyZSByZXZlcnRlZC4KICAgICAgICAvLyBUaGlzIHVzZWQgdG8gY29uc3VtZSBhbGwgZ2FzIGluIG9sZCBFVk0gdmVyc2lvbnMsIGJ1dAogICAgICAgIC8vIG5vdCBhbnltb3JlLgogICAgICAgIC8vIEl0IGlzIG9mdGVuIGEgZ29vZCBpZGVhIHRvIHVzZSBgcmVxdWlyZWAgdG8gY2hlY2sgaWYKICAgICAgICAvLyBmdW5jdGlvbnMgYXJlIGNhbGxlZCBjb3JyZWN0bHkuCiAgICAgICAgLy8gQXMgYSBzZWNvbmQgYXJndW1lbnQsIHlvdSBjYW4gYWxzbyBwcm92aWRlIGFuCiAgICAgICAgLy8gZXhwbGFuYXRpb24gYWJvdXQgd2hhdCB3ZW50IHdyb25nLgogICAgICAgIHJlcXVpcmUoCiAgICAgICAgICAgIG1zZy5zZW5kZXIgPT0gY2hhaXJwZXJzb24sCiAgICAgICAgICAgICJPbmx5IGNoYWlycGVyc29uIGNhbiBnaXZlIHJpZ2h0IHRvIHZvdGUuIgogICAgICAgICk7CiAgICAgICAgcmVxdWlyZSgKICAgICAgICAgICAgIXZvdGVyc1t2b3Rlcl0udm90ZWQsCiAgICAgICAgICAgICJUaGUgdm90ZXIgYWxyZWFkeSB2b3RlZC4iCiAgICAgICAgKTsKICAgICAgICByZXF1aXJlKHZvdGVyc1t2b3Rlcl0ud2VpZ2h0ID09IDApOwogICAgICAgIHZvdGVyc1t2b3Rlcl0ud2VpZ2h0ID0gMTsKICAgIH0KCiAgICAvLy8gRGVsZWdhdGUgeW91ciB2b3RlIHRvIHRoZSB2b3RlciBgdG9gLgogICAgZnVuY3Rpb24gZGVsZWdhdGUoYWRkcmVzcyB0bykgZXh0ZXJuYWwgewogICAgICAgIC8vIGFzc2lnbnMgcmVmZXJlbmNlCiAgICAgICAgVm90ZXIgc3RvcmFnZSBzZW5kZXIgPSB2b3RlcnNbbXNnLnNlbmRlcl07CiAgICAgICAgcmVxdWlyZShzZW5kZXIud2VpZ2h0ICE9IDAsICJZb3UgaGF2ZSBubyByaWdodCB0byB2b3RlIik7CiAgICAgICAgcmVxdWlyZSghc2VuZGVyLnZvdGVkLCAiWW91IGFscmVhZHkgdm90ZWQuIik7CgogICAgICAgIHJlcXVpcmUodG8gIT0gbXNnLnNlbmRlciwgIlNlbGYtZGVsZWdhdGlvbiBpcyBkaXNhbGxvd2VkLiIpOwoKICAgICAgICAvLyBGb3J3YXJkIHRoZSBkZWxlZ2F0aW9uIGFzIGxvbmcgYXMKICAgICAgICAvLyBgdG9gIGFsc28gZGVsZWdhdGVkLgogICAgICAgIC8vIEluIGdlbmVyYWwsIHN1Y2ggbG9vcHMgYXJlIHZlcnkgZGFuZ2Vyb3VzLAogICAgICAgIC8vIGJlY2F1c2UgaWYgdGhleSBydW4gdG9vIGxvbmcsIHRoZXkgbWlnaHQKICAgICAgICAvLyBuZWVkIG1vcmUgZ2FzIHRoYW4gaXMgYXZhaWxhYmxlIGluIGEgYmxvY2suCiAgICAgICAgLy8gSW4gdGhpcyBjYXNlLCB0aGUgZGVsZWdhdGlvbiB3aWxsIG5vdCBiZSBleGVjdXRlZCwKICAgICAgICAvLyBidXQgaW4gb3RoZXIgc2l0dWF0aW9ucywgc3VjaCBsb29wcyBtaWdodAogICAgICAgIC8vIGNhdXNlIGEgY29udHJhY3QgdG8gZ2V0ICJzdHVjayIgY29tcGxldGVseS4KICAgICAgICB3aGlsZSAodm90ZXJzW3RvXS5kZWxlZ2F0ZSAhPSBhZGRyZXNzKDApKSB7CiAgICAgICAgICAgIHRvID0gdm90ZXJzW3RvXS5kZWxlZ2F0ZTsKCiAgICAgICAgICAgIC8vIFdlIGZvdW5kIGEgbG9vcCBpbiB0aGUgZGVsZWdhdGlvbiwgbm90IGFsbG93ZWQuCiAgICAgICAgICAgIHJlcXVpcmUodG8gIT0gbXNnLnNlbmRlciwgIkZvdW5kIGxvb3AgaW4gZGVsZWdhdGlvbi4iKTsKICAgICAgICB9CgogICAgICAgIFZvdGVyIHN0b3JhZ2UgZGVsZWdhdGVfID0gdm90ZXJzW3RvXTsKCiAgICAgICAgLy8gVm90ZXJzIGNhbm5vdCBkZWxlZ2F0ZSB0byBhY2NvdW50cyB0aGF0IGNhbm5vdCB2b3RlLgogICAgICAgIHJlcXVpcmUoZGVsZWdhdGVfLndlaWdodCA+PSAxKTsKCiAgICAgICAgLy8gU2luY2UgYHNlbmRlcmAgaXMgYSByZWZlcmVuY2UsIHRoaXMKICAgICAgICAvLyBtb2RpZmllcyBgdm90ZXJzW21zZy5zZW5kZXJdYC4KICAgICAgICBzZW5kZXIudm90ZWQgPSB0cnVlOwogICAgICAgIHNlbmRlci5kZWxlZ2F0ZSA9IHRvOwoKICAgICAgICBpZiAoZGVsZWdhdGVfLnZvdGVkKSB7CiAgICAgICAgICAgIC8vIElmIHRoZSBkZWxlZ2F0ZSBhbHJlYWR5IHZvdGVkLAogICAgICAgICAgICAvLyBkaXJlY3RseSBhZGQgdG8gdGhlIG51bWJlciBvZiB2b3RlcwogICAgICAgICAgICBwcm9wb3NhbHNbZGVsZWdhdGVfLnZvdGVdLnZvdGVDb3VudCArPSBzZW5kZXIud2VpZ2h0OwogICAgICAgIH0gZWxzZSB7CiAgICAgICAgICAgIC8vIElmIHRoZSBkZWxlZ2F0ZSBkaWQgbm90IHZvdGUgeWV0LAogICAgICAgICAgICAvLyBhZGQgdG8gaGVyIHdlaWdodC4KICAgICAgICAgICAgZGVsZWdhdGVfLndlaWdodCArPSBzZW5kZXIud2VpZ2h0OwogICAgICAgIH0KICAgIH0KCiAgICAvLy8gR2l2ZSB5b3VyIHZvdGUgKGluY2x1ZGluZyB2b3RlcyBkZWxlZ2F0ZWQgdG8geW91KQogICAgLy8vIHRvIHByb3Bvc2FsIGBwcm9wb3NhbHNbcHJvcG9zYWxdLm5hbWVgLgogICAgZnVuY3Rpb24gdm90ZSh1aW50IHByb3Bvc2FsKSBleHRlcm5hbCB7CiAgICAgICAgVm90ZXIgc3RvcmFnZSBzZW5kZXIgPSB2b3RlcnNbbXNnLnNlbmRlcl07CiAgICAgICAgcmVxdWlyZShzZW5kZXIud2VpZ2h0ICE9IDAsICJIYXMgbm8gcmlnaHQgdG8gdm90ZSIpOwogICAgICAgIHJlcXVpcmUoIXNlbmRlci52b3RlZCwgIkFscmVhZHkgdm90ZWQuIik7CiAgICAgICAgc2VuZGVyLnZvdGVkID0gdHJ1ZTsKICAgICAgICBzZW5kZXIudm90ZSA9IHByb3Bvc2FsOwoKICAgICAgICAvLyBJZiBgcHJvcG9zYWxgIGlzIG91dCBvZiB0aGUgcmFuZ2Ugb2YgdGhlIGFycmF5LAogICAgICAgIC8vIHRoaXMgd2lsbCB0aHJvdyBhdXRvbWF0aWNhbGx5IGFuZCByZXZlcnQgYWxsCiAgICAgICAgLy8gY2hhbmdlcy4KICAgICAgICBwcm9wb3NhbHNbcHJvcG9zYWxdLnZvdGVDb3VudCArPSBzZW5kZXIud2VpZ2h0OwogICAgfQoKICAgIC8vLyBAZGV2IENvbXB1dGVzIHRoZSB3aW5uaW5nIHByb3Bvc2FsIHRha2luZyBhbGwKICAgIC8vLyBwcmV2aW91cyB2b3RlcyBpbnRvIGFjY291bnQuCiAgICBmdW5jdGlvbiB3aW5uaW5nUHJvcG9zYWwoKSBwdWJsaWMgdmlldwogICAgICAgICAgICByZXR1cm5zICh1aW50IHdpbm5pbmdQcm9wb3NhbF8pCiAgICB7CiAgICAgICAgdWludCB3aW5uaW5nVm90ZUNvdW50ID0gMDsKICAgICAgICBmb3IgKHVpbnQgcCA9IDA7IHAgPCBwcm9wb3NhbHMubGVuZ3RoOyBwKyspIHsKICAgICAgICAgICAgaWYgKHByb3Bvc2Fsc1twXS52b3RlQ291bnQgPiB3aW5uaW5nVm90ZUNvdW50KSB7CiAgICAgICAgICAgICAgICB3aW5uaW5nVm90ZUNvdW50ID0gcHJvcG9zYWxzW3BdLnZvdGVDb3VudDsKICAgICAgICAgICAgICAgIHdpbm5pbmdQcm9wb3NhbF8gPSBwOwogICAgICAgICAgICB9CiAgICAgICAgfQogICAgfQoKICAgIC8vIENhbGxzIHdpbm5pbmdQcm9wb3NhbCgpIGZ1bmN0aW9uIHRvIGdldCB0aGUgaW5kZXgKICAgIC8vIG9mIHRoZSB3aW5uZXIgY29udGFpbmVkIGluIHRoZSBwcm9wb3NhbHMgYXJyYXkgYW5kIHRoZW4KICAgIC8vIHJldHVybnMgdGhlIG5hbWUgb2YgdGhlIHdpbm5lcgogICAgZnVuY3Rpb24gd2lubmVyTmFtZSgpIGV4dGVybmFsIHZpZXcKICAgICAgICAgICAgcmV0dXJucyAoYnl0ZXMzMiB3aW5uZXJOYW1lXykKICAgIHsKICAgICAgICB3aW5uZXJOYW1lXyA9IHByb3Bvc2Fsc1t3aW5uaW5nUHJvcG9zYWwoKV0ubmFtZTsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;
/// @title Voting with delegation.
contract Ballot {
 // This declares a new complex type which will
 // be used for variables later.
 // It will represent a single voter.
 struct Voter {
 uint weight; // weight is accumulated by delegation
 bool voted; // if true, that person already voted
 address delegate; // person delegated to
 uint vote; // index of the voted proposal
 }

 // This is a type for a single proposal.
 struct Proposal {
 bytes32 name; // short name (up to 32 bytes)
 uint voteCount; // number of accumulated votes
 }

 address public chairperson;

 // This declares a state variable that
 // stores a `Voter` struct for each possible address.
 mapping(address => Voter) public voters;

 // A dynamically-sized array of `Proposal` structs.
 Proposal[] public proposals;

 /// Create a new ballot to choose one of `proposalNames`.
 constructor(bytes32[] memory proposalNames) {
 chairperson = msg.sender;
 voters[chairperson].weight = 1;

 // For each of the provided proposal names,
 // create a new proposal object and add it
 // to the end of the array.
 for (uint i = 0; i < proposalNames.length; i++) {
 // `Proposal({...})` creates a temporary
 // Proposal object and `proposals.push(...)`
 // appends it to the end of `proposals`.
 proposals.push(Proposal({
 name: proposalNames[i],
 voteCount: 0
 }));
 }
 }

 // Give `voter` the right to vote on this ballot.
 // May only be called by `chairperson`.
 function giveRightToVote(address voter) external {
 // If the first argument of `require` evaluates
 // to `false`, execution terminates and all
 // changes to the state and to Ether balances
 // are reverted.
 // This used to consume all gas in old EVM versions, but
 // not anymore.
 // It is often a good idea to use `require` to check if
 // functions are called correctly.
 // As a second argument, you can also provide an
 // explanation about what went wrong.
 require(
 msg.sender == chairperson,
 "Only chairperson can give right to vote."
 );
 require(
 !voters[voter].voted,
 "The voter already voted."
 );
 require(voters[voter].weight == 0);
 voters[voter].weight = 1;
 }

 /// Delegate your vote to the voter `to`.
 function delegate(address to) external {
 // assigns reference
 Voter storage sender = voters[msg.sender];
 require(sender.weight != 0, "You have no right to vote");
 require(!sender.voted, "You already voted.");

 require(to != msg.sender, "Self-delegation is disallowed.");

 // Forward the delegation as long as
 // `to` also delegated.
 // In general, such loops are very dangerous,
 // because if they run too long, they might
 // need more gas than is available in a block.
 // In this case, the delegation will not be executed,
 // but in other situations, such loops might
 // cause a contract to get "stuck" completely.
 while (voters[to].delegate != address(0)) {
 to = voters[to].delegate;

 // We found a loop in the delegation, not allowed.
 require(to != msg.sender, "Found loop in delegation.");
 }

 Voter storage delegate_ = voters[to];

 // Voters cannot delegate to accounts that cannot vote.
 require(delegate_.weight >= 1);

 // Since `sender` is a reference, this
 // modifies `voters[msg.sender]`.
 sender.voted = true;
 sender.delegate = to;

 if (delegate_.voted) {
 // If the delegate already voted,
 // directly add to the number of votes
 proposals[delegate_.vote].voteCount += sender.weight;
 } else {
 // If the delegate did not vote yet,
 // add to her weight.
 delegate_.weight += sender.weight;
 }
 }

 /// Give your vote (including votes delegated to you)
 /// to proposal `proposals[proposal].name`.
 function vote(uint proposal) external {
 Voter storage sender = voters[msg.sender];
 require(sender.weight != 0, "Has no right to vote");
 require(!sender.voted, "Already voted.");
 sender.voted = true;
 sender.vote = proposal;

 // If `proposal` is out of the range of the array,
 // this will throw automatically and revert all
 // changes.
 proposals[proposal].voteCount += sender.weight;
 }

 /// @dev Computes the winning proposal taking all
 /// previous votes into account.
 function winningProposal() public view
 returns (uint winningProposal_)
 {
 uint winningVoteCount = 0;
 for (uint p = 0; p < proposals.length; p++) {
 if (proposals[p].voteCount > winningVoteCount) {
 winningVoteCount = proposals[p].voteCount;
 winningProposal_ = p;
 }
 }
 }

 // Calls winningProposal() function to get the index
 // of the winner contained in the proposals array and then
 // returns the name of the winner
 function winnerName() external view
 returns (bytes32 winnerName_)
 {
 winnerName_ = proposals[winningProposal()].name;
 }
}

### Possible Improvements[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#possible-improvements "Link to this heading")

Currently, many transactions are needed to assign the rights to vote to all participants. Moreover, if two or more proposals have the same number of votes, `winningProposal()` is not able to register a tie. Can you think of a way to fix these issues?

Blind Auction[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#blind-auction "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

In this section, we will show how easy it is to create a completely blind auction contract on Ethereum. We will start with an open auction where everyone can see the bids that are made and then extend this contract into a blind auction where it is not possible to see the actual bid until the bidding period ends.

### Simple Open Auction[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#simple-open-auction "Link to this heading")

The general idea of the following simple auction contract is that everyone can send their bids during a bidding period. The bids already include sending some compensation, e.g. Ether, in order to bind the bidders to their bid. If the highest bid is raised, the previous highest bidder gets their Ether back. After the end of the bidding period, the contract has to be called manually for the beneficiary to receive their Ether - contracts cannot activate themselves.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguNDsKY29udHJhY3QgU2ltcGxlQXVjdGlvbiB7CiAgICAvLyBQYXJhbWV0ZXJzIG9mIHRoZSBhdWN0aW9uLiBUaW1lcyBhcmUgZWl0aGVyCiAgICAvLyBhYnNvbHV0ZSB1bml4IHRpbWVzdGFtcHMgKHNlY29uZHMgc2luY2UgMTk3MC0wMS0wMSkKICAgIC8vIG9yIHRpbWUgcGVyaW9kcyBpbiBzZWNvbmRzLgogICAgYWRkcmVzcyBwYXlhYmxlIHB1YmxpYyBiZW5lZmljaWFyeTsKICAgIHVpbnQgcHVibGljIGF1Y3Rpb25FbmRUaW1lOwoKICAgIC8vIEN1cnJlbnQgc3RhdGUgb2YgdGhlIGF1Y3Rpb24uCiAgICBhZGRyZXNzIHB1YmxpYyBoaWdoZXN0QmlkZGVyOwogICAgdWludCBwdWJsaWMgaGlnaGVzdEJpZDsKCiAgICAvLyBBbGxvd2VkIHdpdGhkcmF3YWxzIG9mIHByZXZpb3VzIGJpZHMKICAgIG1hcHBpbmcoYWRkcmVzcyA9PiB1aW50KSBwZW5kaW5nUmV0dXJuczsKCiAgICAvLyBTZXQgdG8gdHJ1ZSBhdCB0aGUgZW5kLCBkaXNhbGxvd3MgYW55IGNoYW5nZS4KICAgIC8vIEJ5IGRlZmF1bHQgaW5pdGlhbGl6ZWQgdG8gYGZhbHNlYC4KICAgIGJvb2wgZW5kZWQ7CgogICAgLy8gRXZlbnRzIHRoYXQgd2lsbCBiZSBlbWl0dGVkIG9uIGNoYW5nZXMuCiAgICBldmVudCBIaWdoZXN0QmlkSW5jcmVhc2VkKGFkZHJlc3MgYmlkZGVyLCB1aW50IGFtb3VudCk7CiAgICBldmVudCBBdWN0aW9uRW5kZWQoYWRkcmVzcyB3aW5uZXIsIHVpbnQgYW1vdW50KTsKCiAgICAvLyBFcnJvcnMgdGhhdCBkZXNjcmliZSBmYWlsdXJlcy4KCiAgICAvLyBUaGUgdHJpcGxlLXNsYXNoIGNvbW1lbnRzIGFyZSBzby1jYWxsZWQgbmF0c3BlYwogICAgLy8gY29tbWVudHMuIFRoZXkgd2lsbCBiZSBzaG93biB3aGVuIHRoZSB1c2VyCiAgICAvLyBpcyBhc2tlZCB0byBjb25maXJtIGEgdHJhbnNhY3Rpb24gb3IKICAgIC8vIHdoZW4gYW4gZXJyb3IgaXMgZGlzcGxheWVkLgoKICAgIC8vLyBUaGUgYXVjdGlvbiBoYXMgYWxyZWFkeSBlbmRlZC4KICAgIGVycm9yIEF1Y3Rpb25BbHJlYWR5RW5kZWQoKTsKICAgIC8vLyBUaGVyZSBpcyBhbHJlYWR5IGEgaGlnaGVyIG9yIGVxdWFsIGJpZC4KICAgIGVycm9yIEJpZE5vdEhpZ2hFbm91Z2godWludCBoaWdoZXN0QmlkKTsKICAgIC8vLyBUaGUgYXVjdGlvbiBoYXMgbm90IGVuZGVkIHlldC4KICAgIGVycm9yIEF1Y3Rpb25Ob3RZZXRFbmRlZCgpOwogICAgLy8vIFRoZSBmdW5jdGlvbiBhdWN0aW9uRW5kIGhhcyBhbHJlYWR5IGJlZW4gY2FsbGVkLgogICAgZXJyb3IgQXVjdGlvbkVuZEFscmVhZHlDYWxsZWQoKTsKCiAgICAvLy8gQ3JlYXRlIGEgc2ltcGxlIGF1Y3Rpb24gd2l0aCBgYmlkZGluZ1RpbWVgCiAgICAvLy8gc2Vjb25kcyBiaWRkaW5nIHRpbWUgb24gYmVoYWxmIG9mIHRoZQogICAgLy8vIGJlbmVmaWNpYXJ5IGFkZHJlc3MgYGJlbmVmaWNpYXJ5QWRkcmVzc2AuCiAgICBjb25zdHJ1Y3RvcigKICAgICAgICB1aW50IGJpZGRpbmdUaW1lLAogICAgICAgIGFkZHJlc3MgcGF5YWJsZSBiZW5lZmljaWFyeUFkZHJlc3MKICAgICkgewogICAgICAgIGJlbmVmaWNpYXJ5ID0gYmVuZWZpY2lhcnlBZGRyZXNzOwogICAgICAgIGF1Y3Rpb25FbmRUaW1lID0gYmxvY2sudGltZXN0YW1wICsgYmlkZGluZ1RpbWU7CiAgICB9CgogICAgLy8vIEJpZCBvbiB0aGUgYXVjdGlvbiB3aXRoIHRoZSB2YWx1ZSBzZW50CiAgICAvLy8gdG9nZXRoZXIgd2l0aCB0aGlzIHRyYW5zYWN0aW9uLgogICAgLy8vIFRoZSB2YWx1ZSB3aWxsIG9ubHkgYmUgcmVmdW5kZWQgaWYgdGhlCiAgICAvLy8gYXVjdGlvbiBpcyBub3Qgd29uLgogICAgZnVuY3Rpb24gYmlkKCkgZXh0ZXJuYWwgcGF5YWJsZSB7CiAgICAgICAgLy8gTm8gYXJndW1lbnRzIGFyZSBuZWNlc3NhcnksIGFsbAogICAgICAgIC8vIGluZm9ybWF0aW9uIGlzIGFscmVhZHkgcGFydCBvZgogICAgICAgIC8vIHRoZSB0cmFuc2FjdGlvbi4gVGhlIGtleXdvcmQgcGF5YWJsZQogICAgICAgIC8vIGlzIHJlcXVpcmVkIGZvciB0aGUgZnVuY3Rpb24gdG8KICAgICAgICAvLyBiZSBhYmxlIHRvIHJlY2VpdmUgRXRoZXIuCgogICAgICAgIC8vIFJldmVydCB0aGUgY2FsbCBpZiB0aGUgYmlkZGluZwogICAgICAgIC8vIHBlcmlvZCBpcyBvdmVyLgogICAgICAgIGlmIChibG9jay50aW1lc3RhbXAgPiBhdWN0aW9uRW5kVGltZSkKICAgICAgICAgICAgcmV2ZXJ0IEF1Y3Rpb25BbHJlYWR5RW5kZWQoKTsKCiAgICAgICAgLy8gSWYgdGhlIGJpZCBpcyBub3QgaGlnaGVyLCBzZW5kIHRoZQogICAgICAgIC8vIEV0aGVyIGJhY2sgKHRoZSByZXZlcnQgc3RhdGVtZW50CiAgICAgICAgLy8gd2lsbCByZXZlcnQgYWxsIGNoYW5nZXMgaW4gdGhpcwogICAgICAgIC8vIGZ1bmN0aW9uIGV4ZWN1dGlvbiBpbmNsdWRpbmcKICAgICAgICAvLyBpdCBoYXZpbmcgcmVjZWl2ZWQgdGhlIEV0aGVyKS4KICAgICAgICBpZiAobXNnLnZhbHVlIDw9IGhpZ2hlc3RCaWQpCiAgICAgICAgICAgIHJldmVydCBCaWROb3RIaWdoRW5vdWdoKGhpZ2hlc3RCaWQpOwoKICAgICAgICBpZiAoaGlnaGVzdEJpZCAhPSAwKSB7CiAgICAgICAgICAgIC8vIFNlbmRpbmcgYmFjayB0aGUgRXRoZXIgYnkgc2ltcGx5IHVzaW5nCiAgICAgICAgICAgIC8vIGhpZ2hlc3RCaWRkZXIuc2VuZChoaWdoZXN0QmlkKSBpcyBhIHNlY3VyaXR5IHJpc2sKICAgICAgICAgICAgLy8gYmVjYXVzZSBpdCBjb3VsZCBleGVjdXRlIGFuIHVudHJ1c3RlZCBjb250cmFjdC4KICAgICAgICAgICAgLy8gSXQgaXMgYWx3YXlzIHNhZmVyIHRvIGxldCB0aGUgcmVjaXBpZW50cwogICAgICAgICAgICAvLyB3aXRoZHJhdyB0aGVpciBFdGhlciB0aGVtc2VsdmVzLgogICAgICAgICAgICBwZW5kaW5nUmV0dXJuc1toaWdoZXN0QmlkZGVyXSArPSBoaWdoZXN0QmlkOwogICAgICAgIH0KICAgICAgICBoaWdoZXN0QmlkZGVyID0gbXNnLnNlbmRlcjsKICAgICAgICBoaWdoZXN0QmlkID0gbXNnLnZhbHVlOwogICAgICAgIGVtaXQgSGlnaGVzdEJpZEluY3JlYXNlZChtc2cuc2VuZGVyLCBtc2cudmFsdWUpOwogICAgfQoKICAgIC8vLyBXaXRoZHJhdyBhIGJpZCB0aGF0IHdhcyBvdmVyYmlkLgogICAgZnVuY3Rpb24gd2l0aGRyYXcoKSBleHRlcm5hbCByZXR1cm5zIChib29sKSB7CiAgICAgICAgdWludCBhbW91bnQgPSBwZW5kaW5nUmV0dXJuc1ttc2cuc2VuZGVyXTsKICAgICAgICBpZiAoYW1vdW50ID4gMCkgewogICAgICAgICAgICAvLyBJdCBpcyBpbXBvcnRhbnQgdG8gc2V0IHRoaXMgdG8gemVybyBiZWNhdXNlIHRoZSByZWNpcGllbnQKICAgICAgICAgICAgLy8gY2FuIGNhbGwgdGhpcyBmdW5jdGlvbiBhZ2FpbiBhcyBwYXJ0IG9mIHRoZSByZWNlaXZpbmcgY2FsbAogICAgICAgICAgICAvLyBiZWZvcmUgYHNlbmRgIHJldHVybnMuCiAgICAgICAgICAgIHBlbmRpbmdSZXR1cm5zW21zZy5zZW5kZXJdID0gMDsKCiAgICAgICAgICAgIC8vIG1zZy5zZW5kZXIgaXMgbm90IG9mIHR5cGUgYGFkZHJlc3MgcGF5YWJsZWAgYW5kIG11c3QgYmUKICAgICAgICAgICAgLy8gZXhwbGljaXRseSBjb252ZXJ0ZWQgdXNpbmcgYHBheWFibGUobXNnLnNlbmRlcilgIGluIG9yZGVyCiAgICAgICAgICAgIC8vIHVzZSB0aGUgbWVtYmVyIGZ1bmN0aW9uIGBzZW5kKClgLgogICAgICAgICAgICBpZiAoIXBheWFibGUobXNnLnNlbmRlcikuc2VuZChhbW91bnQpKSB7CiAgICAgICAgICAgICAgICAvLyBObyBuZWVkIHRvIGNhbGwgdGhyb3cgaGVyZSwganVzdCByZXNldCB0aGUgYW1vdW50IG93aW5nCiAgICAgICAgICAgICAgICBwZW5kaW5nUmV0dXJuc1ttc2cuc2VuZGVyXSA9IGFtb3VudDsKICAgICAgICAgICAgICAgIHJldHVybiBmYWxzZTsKICAgICAgICAgICAgfQogICAgICAgIH0KICAgICAgICByZXR1cm4gdHJ1ZTsKICAgIH0KCiAgICAvLy8gRW5kIHRoZSBhdWN0aW9uIGFuZCBzZW5kIHRoZSBoaWdoZXN0IGJpZAogICAgLy8vIHRvIHRoZSBiZW5lZmljaWFyeS4KICAgIGZ1bmN0aW9uIGF1Y3Rpb25FbmQoKSBleHRlcm5hbCB7CiAgICAgICAgLy8gSXQgaXMgYSBnb29kIGd1aWRlbGluZSB0byBzdHJ1Y3R1cmUgZnVuY3Rpb25zIHRoYXQgaW50ZXJhY3QKICAgICAgICAvLyB3aXRoIG90aGVyIGNvbnRyYWN0cyAoaS5lLiB0aGV5IGNhbGwgZnVuY3Rpb25zIG9yIHNlbmQgRXRoZXIpCiAgICAgICAgLy8gaW50byB0aHJlZSBwaGFzZXM6CiAgICAgICAgLy8gMS4gY2hlY2tpbmcgY29uZGl0aW9ucwogICAgICAgIC8vIDIuIHBlcmZvcm1pbmcgYWN0aW9ucyAocG90ZW50aWFsbHkgY2hhbmdpbmcgY29uZGl0aW9ucykKICAgICAgICAvLyAzLiBpbnRlcmFjdGluZyB3aXRoIG90aGVyIGNvbnRyYWN0cwogICAgICAgIC8vIElmIHRoZXNlIHBoYXNlcyBhcmUgbWl4ZWQgdXAsIHRoZSBvdGhlciBjb250cmFjdCBjb3VsZCBjYWxsCiAgICAgICAgLy8gYmFjayBpbnRvIHRoZSBjdXJyZW50IGNvbnRyYWN0IGFuZCBtb2RpZnkgdGhlIHN0YXRlIG9yIGNhdXNlCiAgICAgICAgLy8gZWZmZWN0cyAoZXRoZXIgcGF5b3V0KSB0byBiZSBwZXJmb3JtZWQgbXVsdGlwbGUgdGltZXMuCiAgICAgICAgLy8gSWYgZnVuY3Rpb25zIGNhbGxlZCBpbnRlcm5hbGx5IGluY2x1ZGUgaW50ZXJhY3Rpb24gd2l0aCBleHRlcm5hbAogICAgICAgIC8vIGNvbnRyYWN0cywgdGhleSBhbHNvIGhhdmUgdG8gYmUgY29uc2lkZXJlZCBpbnRlcmFjdGlvbiB3aXRoCiAgICAgICAgLy8gZXh0ZXJuYWwgY29udHJhY3RzLgoKICAgICAgICAvLyAxLiBDb25kaXRpb25zCiAgICAgICAgaWYgKGJsb2NrLnRpbWVzdGFtcCA8IGF1Y3Rpb25FbmRUaW1lKQogICAgICAgICAgICByZXZlcnQgQXVjdGlvbk5vdFlldEVuZGVkKCk7CiAgICAgICAgaWYgKGVuZGVkKQogICAgICAgICAgICByZXZlcnQgQXVjdGlvbkVuZEFscmVhZHlDYWxsZWQoKTsKCiAgICAgICAgLy8gMi4gRWZmZWN0cwogICAgICAgIGVuZGVkID0gdHJ1ZTsKICAgICAgICBlbWl0IEF1Y3Rpb25FbmRlZChoaWdoZXN0QmlkZGVyLCBoaWdoZXN0QmlkKTsKCiAgICAgICAgLy8gMy4gSW50ZXJhY3Rpb24KICAgICAgICBiZW5lZmljaWFyeS50cmFuc2ZlcihoaWdoZXN0QmlkKTsKICAgIH0KfQ==)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;
contract SimpleAuction {
 // Parameters of the auction. Times are either
 // absolute unix timestamps (seconds since 1970-01-01)
 // or time periods in seconds.
 address payable public beneficiary;
 uint public auctionEndTime;

 // Current state of the auction.
 address public highestBidder;
 uint public highestBid;

 // Allowed withdrawals of previous bids
 mapping(address => uint) pendingReturns;

 // Set to true at the end, disallows any change.
 // By default initialized to `false`.
 bool ended;

 // Events that will be emitted on changes.
 event HighestBidIncreased(address bidder, uint amount);
 event AuctionEnded(address winner, uint amount);

 // Errors that describe failures.

 // The triple-slash comments are so-called natspec
 // comments. They will be shown when the user
 // is asked to confirm a transaction or
 // when an error is displayed.

 /// The auction has already ended.
 error AuctionAlreadyEnded();
 /// There is already a higher or equal bid.
 error BidNotHighEnough(uint highestBid);
 /// The auction has not ended yet.
 error AuctionNotYetEnded();
 /// The function auctionEnd has already been called.
 error AuctionEndAlreadyCalled();

 /// Create a simple auction with `biddingTime`
 /// seconds bidding time on behalf of the
 /// beneficiary address `beneficiaryAddress`.
 constructor(
 uint biddingTime,
 address payable beneficiaryAddress
 ) {
 beneficiary = beneficiaryAddress;
 auctionEndTime = block.timestamp + biddingTime;
 }

 /// Bid on the auction with the value sent
 /// together with this transaction.
 /// The value will only be refunded if the
 /// auction is not won.
 function bid() external payable {
 // No arguments are necessary, all
 // information is already part of
 // the transaction. The keyword payable
 // is required for the function to
 // be able to receive Ether.

 // Revert the call if the bidding
 // period is over.
 if (block.timestamp > auctionEndTime)
 revert AuctionAlreadyEnded();

 // If the bid is not higher, send the
 // Ether back (the revert statement
 // will revert all changes in this
 // function execution including
 // it having received the Ether).
 if (msg.value <= highestBid)
 revert BidNotHighEnough(highestBid);

 if (highestBid != 0) {
 // Sending back the Ether by simply using
 // highestBidder.send(highestBid) is a security risk
 // because it could execute an untrusted contract.
 // It is always safer to let the recipients
 // withdraw their Ether themselves.
 pendingReturns[highestBidder] += highestBid;
 }
 highestBidder = msg.sender;
 highestBid = msg.value;
 emit HighestBidIncreased(msg.sender, msg.value);
 }

 /// Withdraw a bid that was overbid.
 function withdraw() external returns (bool) {
 uint amount = pendingReturns[msg.sender];
 if (amount > 0) {
 // It is important to set this to zero because the recipient
 // can call this function again as part of the receiving call
 // before `send` returns.
 pendingReturns[msg.sender] = 0;

 // msg.sender is not of type `address payable` and must be
 // explicitly converted using `payable(msg.sender)` in order
 // use the member function `send()`.
 if (!payable(msg.sender).send(amount)) {
 // No need to call throw here, just reset the amount owing
 pendingReturns[msg.sender] = amount;
 return false;
 }
 }
 return true;
 }

 /// End the auction and send the highest bid
 /// to the beneficiary.
 function auctionEnd() external {
 // It is a good guideline to structure functions that interact
 // with other contracts (i.e. they call functions or send Ether)
 // into three phases:
 // 1. checking conditions
 // 2. performing actions (potentially changing conditions)
 // 3. interacting with other contracts
 // If these phases are mixed up, the other contract could call
 // back into the current contract and modify the state or cause
 // effects (ether payout) to be performed multiple times.
 // If functions called internally include interaction with external
 // contracts, they also have to be considered interaction with
 // external contracts.

 // 1. Conditions
 if (block.timestamp < auctionEndTime)
 revert AuctionNotYetEnded();
 if (ended)
 revert AuctionEndAlreadyCalled();

 // 2. Effects
 ended = true;
 emit AuctionEnded(highestBidder, highestBid);

 // 3. Interaction
 beneficiary.transfer(highestBid);
 }
}

### Blind Auction[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#id2 "Link to this heading")

The previous open auction is extended to a blind auction in the following. The advantage of a blind auction is that there is no time pressure towards the end of the bidding period. Creating a blind auction on a transparent computing platform might sound like a contradiction, but cryptography comes to the rescue.

During the **bidding period**, a bidder does not actually send their bid, but only a hashed version of it. Since it is currently considered practically impossible to find two (sufficiently long) values whose hash values are equal, the bidder commits to the bid by that. After the end of the bidding period, the bidders have to reveal their bids: They send their values unencrypted, and the contract checks that the hash value is the same as the one provided during the bidding period.

Another challenge is how to make the auction **binding and blind** at the same time: The only way to prevent the bidder from just not sending the Ether after they won the auction is to make them send it together with the bid. Since value transfers cannot be blinded in Ethereum, anyone can see the value.

The following contract solves this problem by accepting any value that is larger than the highest bid. Since this can of course only be checked during the reveal phase, some bids might be **invalid**, and this is on purpose (it even provides an explicit flag to place invalid bids with high-value transfers): Bidders can confuse competition by placing several high or low invalid bids.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguNDsKY29udHJhY3QgQmxpbmRBdWN0aW9uIHsKICAgIHN0cnVjdCBCaWQgewogICAgICAgIGJ5dGVzMzIgYmxpbmRlZEJpZDsKICAgICAgICB1aW50IGRlcG9zaXQ7CiAgICB9CgogICAgYWRkcmVzcyBwYXlhYmxlIHB1YmxpYyBiZW5lZmljaWFyeTsKICAgIHVpbnQgcHVibGljIGJpZGRpbmdFbmQ7CiAgICB1aW50IHB1YmxpYyByZXZlYWxFbmQ7CiAgICBib29sIHB1YmxpYyBlbmRlZDsKCiAgICBtYXBwaW5nKGFkZHJlc3MgPT4gQmlkW10pIHB1YmxpYyBiaWRzOwoKICAgIGFkZHJlc3MgcHVibGljIGhpZ2hlc3RCaWRkZXI7CiAgICB1aW50IHB1YmxpYyBoaWdoZXN0QmlkOwoKICAgIC8vIEFsbG93ZWQgd2l0aGRyYXdhbHMgb2YgcHJldmlvdXMgYmlkcwogICAgbWFwcGluZyhhZGRyZXNzID0+IHVpbnQpIHBlbmRpbmdSZXR1cm5zOwoKICAgIGV2ZW50IEF1Y3Rpb25FbmRlZChhZGRyZXNzIHdpbm5lciwgdWludCBoaWdoZXN0QmlkKTsKCiAgICAvLyBFcnJvcnMgdGhhdCBkZXNjcmliZSBmYWlsdXJlcy4KCiAgICAvLy8gVGhlIGZ1bmN0aW9uIGhhcyBiZWVuIGNhbGxlZCB0b28gZWFybHkuCiAgICAvLy8gVHJ5IGFnYWluIGF0IGB0aW1lYC4KICAgIGVycm9yIFRvb0Vhcmx5KHVpbnQgdGltZSk7CiAgICAvLy8gVGhlIGZ1bmN0aW9uIGhhcyBiZWVuIGNhbGxlZCB0b28gbGF0ZS4KICAgIC8vLyBJdCBjYW5ub3QgYmUgY2FsbGVkIGFmdGVyIGB0aW1lYC4KICAgIGVycm9yIFRvb0xhdGUodWludCB0aW1lKTsKICAgIC8vLyBUaGUgZnVuY3Rpb24gYXVjdGlvbkVuZCBoYXMgYWxyZWFkeSBiZWVuIGNhbGxlZC4KICAgIGVycm9yIEF1Y3Rpb25FbmRBbHJlYWR5Q2FsbGVkKCk7CgogICAgLy8gTW9kaWZpZXJzIGFyZSBhIGNvbnZlbmllbnQgd2F5IHRvIHZhbGlkYXRlIGlucHV0cyB0bwogICAgLy8gZnVuY3Rpb25zLiBgb25seUJlZm9yZWAgaXMgYXBwbGllZCB0byBgYmlkYCBiZWxvdzoKICAgIC8vIFRoZSBuZXcgZnVuY3Rpb24gYm9keSBpcyB0aGUgbW9kaWZpZXIncyBib2R5IHdoZXJlCiAgICAvLyBgX2AgaXMgcmVwbGFjZWQgYnkgdGhlIG9sZCBmdW5jdGlvbiBib2R5LgogICAgbW9kaWZpZXIgb25seUJlZm9yZSh1aW50IHRpbWUpIHsKICAgICAgICBpZiAoYmxvY2sudGltZXN0YW1wID49IHRpbWUpIHJldmVydCBUb29MYXRlKHRpbWUpOwogICAgICAgIF87CiAgICB9CiAgICBtb2RpZmllciBvbmx5QWZ0ZXIodWludCB0aW1lKSB7CiAgICAgICAgaWYgKGJsb2NrLnRpbWVzdGFtcCA8PSB0aW1lKSByZXZlcnQgVG9vRWFybHkodGltZSk7CiAgICAgICAgXzsKICAgIH0KCiAgICBjb25zdHJ1Y3RvcigKICAgICAgICB1aW50IGJpZGRpbmdUaW1lLAogICAgICAgIHVpbnQgcmV2ZWFsVGltZSwKICAgICAgICBhZGRyZXNzIHBheWFibGUgYmVuZWZpY2lhcnlBZGRyZXNzCiAgICApIHsKICAgICAgICBiZW5lZmljaWFyeSA9IGJlbmVmaWNpYXJ5QWRkcmVzczsKICAgICAgICBiaWRkaW5nRW5kID0gYmxvY2sudGltZXN0YW1wICsgYmlkZGluZ1RpbWU7CiAgICAgICAgcmV2ZWFsRW5kID0gYmlkZGluZ0VuZCArIHJldmVhbFRpbWU7CiAgICB9CgogICAgLy8vIFBsYWNlIGEgYmxpbmRlZCBiaWQgd2l0aCBgYmxpbmRlZEJpZGAgPQogICAgLy8vIGtlY2NhazI1NihhYmkuZW5jb2RlUGFja2VkKHZhbHVlLCBmYWtlLCBzZWNyZXQpKS4KICAgIC8vLyBUaGUgc2VudCBldGhlciBpcyBvbmx5IHJlZnVuZGVkIGlmIHRoZSBiaWQgaXMgY29ycmVjdGx5CiAgICAvLy8gcmV2ZWFsZWQgaW4gdGhlIHJldmVhbGluZyBwaGFzZS4gVGhlIGJpZCBpcyB2YWxpZCBpZiB0aGUKICAgIC8vLyBldGhlciBzZW50IHRvZ2V0aGVyIHdpdGggdGhlIGJpZCBpcyBhdCBsZWFzdCAidmFsdWUiIGFuZAogICAgLy8vICJmYWtlIiBpcyBub3QgdHJ1ZS4gU2V0dGluZyAiZmFrZSIgdG8gdHJ1ZSBhbmQgc2VuZGluZwogICAgLy8vIG5vdCB0aGUgZXhhY3QgYW1vdW50IGFyZSB3YXlzIHRvIGhpZGUgdGhlIHJlYWwgYmlkIGJ1dAogICAgLy8vIHN0aWxsIG1ha2UgdGhlIHJlcXVpcmVkIGRlcG9zaXQuIFRoZSBzYW1lIGFkZHJlc3MgY2FuCiAgICAvLy8gcGxhY2UgbXVsdGlwbGUgYmlkcy4KICAgIGZ1bmN0aW9uIGJpZChieXRlczMyIGJsaW5kZWRCaWQpCiAgICAgICAgZXh0ZXJuYWwKICAgICAgICBwYXlhYmxlCiAgICAgICAgb25seUJlZm9yZShiaWRkaW5nRW5kKQogICAgewogICAgICAgIGJpZHNbbXNnLnNlbmRlcl0ucHVzaChCaWQoewogICAgICAgICAgICBibGluZGVkQmlkOiBibGluZGVkQmlkLAogICAgICAgICAgICBkZXBvc2l0OiBtc2cudmFsdWUKICAgICAgICB9KSk7CiAgICB9CgogICAgLy8vIFJldmVhbCB5b3VyIGJsaW5kZWQgYmlkcy4gWW91IHdpbGwgZ2V0IGEgcmVmdW5kIGZvciBhbGwKICAgIC8vLyBjb3JyZWN0bHkgYmxpbmRlZCBpbnZhbGlkIGJpZHMgYW5kIGZvciBhbGwgYmlkcyBleGNlcHQgZm9yCiAgICAvLy8gdGhlIHRvdGFsbHkgaGlnaGVzdC4KICAgIGZ1bmN0aW9uIHJldmVhbCgKICAgICAgICB1aW50W10gY2FsbGRhdGEgdmFsdWVzLAogICAgICAgIGJvb2xbXSBjYWxsZGF0YSBmYWtlcywKICAgICAgICBieXRlczMyW10gY2FsbGRhdGEgc2VjcmV0cwogICAgKQogICAgICAgIGV4dGVybmFsCiAgICAgICAgb25seUFmdGVyKGJpZGRpbmdFbmQpCiAgICAgICAgb25seUJlZm9yZShyZXZlYWxFbmQpCiAgICB7CiAgICAgICAgdWludCBsZW5ndGggPSBiaWRzW21zZy5zZW5kZXJdLmxlbmd0aDsKICAgICAgICByZXF1aXJlKHZhbHVlcy5sZW5ndGggPT0gbGVuZ3RoKTsKICAgICAgICByZXF1aXJlKGZha2VzLmxlbmd0aCA9PSBsZW5ndGgpOwogICAgICAgIHJlcXVpcmUoc2VjcmV0cy5sZW5ndGggPT0gbGVuZ3RoKTsKCiAgICAgICAgdWludCByZWZ1bmQ7CiAgICAgICAgZm9yICh1aW50IGkgPSAwOyBpIDwgbGVuZ3RoOyBpKyspIHsKICAgICAgICAgICAgQmlkIHN0b3JhZ2UgYmlkVG9DaGVjayA9IGJpZHNbbXNnLnNlbmRlcl1baV07CiAgICAgICAgICAgICh1aW50IHZhbHVlLCBib29sIGZha2UsIGJ5dGVzMzIgc2VjcmV0KSA9CiAgICAgICAgICAgICAgICAgICAgKHZhbHVlc1tpXSwgZmFrZXNbaV0sIHNlY3JldHNbaV0pOwogICAgICAgICAgICBpZiAoYmlkVG9DaGVjay5ibGluZGVkQmlkICE9IGtlY2NhazI1NihhYmkuZW5jb2RlUGFja2VkKHZhbHVlLCBmYWtlLCBzZWNyZXQpKSkgewogICAgICAgICAgICAgICAgLy8gQmlkIHdhcyBub3QgYWN0dWFsbHkgcmV2ZWFsZWQuCiAgICAgICAgICAgICAgICAvLyBEbyBub3QgcmVmdW5kIGRlcG9zaXQuCiAgICAgICAgICAgICAgICBjb250aW51ZTsKICAgICAgICAgICAgfQogICAgICAgICAgICByZWZ1bmQgKz0gYmlkVG9DaGVjay5kZXBvc2l0OwogICAgICAgICAgICBpZiAoIWZha2UgJiYgYmlkVG9DaGVjay5kZXBvc2l0ID49IHZhbHVlKSB7CiAgICAgICAgICAgICAgICBpZiAocGxhY2VCaWQobXNnLnNlbmRlciwgdmFsdWUpKQogICAgICAgICAgICAgICAgICAgIHJlZnVuZCAtPSB2YWx1ZTsKICAgICAgICAgICAgfQogICAgICAgICAgICAvLyBNYWtlIGl0IGltcG9zc2libGUgZm9yIHRoZSBzZW5kZXIgdG8gcmUtY2xhaW0KICAgICAgICAgICAgLy8gdGhlIHNhbWUgZGVwb3NpdC4KICAgICAgICAgICAgYmlkVG9DaGVjay5ibGluZGVkQmlkID0gYnl0ZXMzMigwKTsKICAgICAgICB9CiAgICAgICAgcGF5YWJsZShtc2cuc2VuZGVyKS50cmFuc2ZlcihyZWZ1bmQpOwogICAgfQoKICAgIC8vLyBXaXRoZHJhdyBhIGJpZCB0aGF0IHdhcyBvdmVyYmlkLgogICAgZnVuY3Rpb24gd2l0aGRyYXcoKSBleHRlcm5hbCB7CiAgICAgICAgdWludCBhbW91bnQgPSBwZW5kaW5nUmV0dXJuc1ttc2cuc2VuZGVyXTsKICAgICAgICBpZiAoYW1vdW50ID4gMCkgewogICAgICAgICAgICAvLyBJdCBpcyBpbXBvcnRhbnQgdG8gc2V0IHRoaXMgdG8gemVybyBiZWNhdXNlIHRoZSByZWNpcGllbnQKICAgICAgICAgICAgLy8gY2FuIGNhbGwgdGhpcyBmdW5jdGlvbiBhZ2FpbiBhcyBwYXJ0IG9mIHRoZSByZWNlaXZpbmcgY2FsbAogICAgICAgICAgICAvLyBiZWZvcmUgYHRyYW5zZmVyYCByZXR1cm5zIChzZWUgdGhlIHJlbWFyayBhYm92ZSBhYm91dAogICAgICAgICAgICAvLyBjb25kaXRpb25zIC0+IGVmZmVjdHMgLT4gaW50ZXJhY3Rpb24pLgogICAgICAgICAgICBwZW5kaW5nUmV0dXJuc1ttc2cuc2VuZGVyXSA9IDA7CgogICAgICAgICAgICBwYXlhYmxlKG1zZy5zZW5kZXIpLnRyYW5zZmVyKGFtb3VudCk7CiAgICAgICAgfQogICAgfQoKICAgIC8vLyBFbmQgdGhlIGF1Y3Rpb24gYW5kIHNlbmQgdGhlIGhpZ2hlc3QgYmlkCiAgICAvLy8gdG8gdGhlIGJlbmVmaWNpYXJ5LgogICAgZnVuY3Rpb24gYXVjdGlvbkVuZCgpCiAgICAgICAgZXh0ZXJuYWwKICAgICAgICBvbmx5QWZ0ZXIocmV2ZWFsRW5kKQogICAgewogICAgICAgIGlmIChlbmRlZCkgcmV2ZXJ0IEF1Y3Rpb25FbmRBbHJlYWR5Q2FsbGVkKCk7CiAgICAgICAgZW1pdCBBdWN0aW9uRW5kZWQoaGlnaGVzdEJpZGRlciwgaGlnaGVzdEJpZCk7CiAgICAgICAgZW5kZWQgPSB0cnVlOwogICAgICAgIGJlbmVmaWNpYXJ5LnRyYW5zZmVyKGhpZ2hlc3RCaWQpOwogICAgfQoKICAgIC8vIFRoaXMgaXMgYW4gImludGVybmFsIiBmdW5jdGlvbiB3aGljaCBtZWFucyB0aGF0IGl0CiAgICAvLyBjYW4gb25seSBiZSBjYWxsZWQgZnJvbSB0aGUgY29udHJhY3QgaXRzZWxmIChvciBmcm9tCiAgICAvLyBkZXJpdmVkIGNvbnRyYWN0cykuCiAgICBmdW5jdGlvbiBwbGFjZUJpZChhZGRyZXNzIGJpZGRlciwgdWludCB2YWx1ZSkgaW50ZXJuYWwKICAgICAgICAgICAgcmV0dXJucyAoYm9vbCBzdWNjZXNzKQogICAgewogICAgICAgIGlmICh2YWx1ZSA8PSBoaWdoZXN0QmlkKSB7CiAgICAgICAgICAgIHJldHVybiBmYWxzZTsKICAgICAgICB9CiAgICAgICAgaWYgKGhpZ2hlc3RCaWRkZXIgIT0gYWRkcmVzcygwKSkgewogICAgICAgICAgICAvLyBSZWZ1bmQgdGhlIHByZXZpb3VzbHkgaGlnaGVzdCBiaWRkZXIuCiAgICAgICAgICAgIHBlbmRpbmdSZXR1cm5zW2hpZ2hlc3RCaWRkZXJdICs9IGhpZ2hlc3RCaWQ7CiAgICAgICAgfQogICAgICAgIGhpZ2hlc3RCaWQgPSB2YWx1ZTsKICAgICAgICBoaWdoZXN0QmlkZGVyID0gYmlkZGVyOwogICAgICAgIHJldHVybiB0cnVlOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;
contract BlindAuction {
 struct Bid {
 bytes32 blindedBid;
 uint deposit;
 }

 address payable public beneficiary;
 uint public biddingEnd;
 uint public revealEnd;
 bool public ended;

 mapping(address => Bid[]) public bids;

 address public highestBidder;
 uint public highestBid;

 // Allowed withdrawals of previous bids
 mapping(address => uint) pendingReturns;

 event AuctionEnded(address winner, uint highestBid);

 // Errors that describe failures.

 /// The function has been called too early.
 /// Try again at `time`.
 error TooEarly(uint time);
 /// The function has been called too late.
 /// It cannot be called after `time`.
 error TooLate(uint time);
 /// The function auctionEnd has already been called.
 error AuctionEndAlreadyCalled();

 // Modifiers are a convenient way to validate inputs to
 // functions. `onlyBefore` is applied to `bid` below:
 // The new function body is the modifier's body where
 // `_` is replaced by the old function body.
 modifier onlyBefore(uint time) {
 if (block.timestamp >= time) revert TooLate(time);
 _;
 }
 modifier onlyAfter(uint time) {
 if (block.timestamp <= time) revert TooEarly(time);
 _;
 }

 constructor(
 uint biddingTime,
 uint revealTime,
 address payable beneficiaryAddress
 ) {
 beneficiary = beneficiaryAddress;
 biddingEnd = block.timestamp + biddingTime;
 revealEnd = biddingEnd + revealTime;
 }

 /// Place a blinded bid with `blindedBid` =
 /// keccak256(abi.encodePacked(value, fake, secret)).
 /// The sent ether is only refunded if the bid is correctly
 /// revealed in the revealing phase. The bid is valid if the
 /// ether sent together with the bid is at least "value" and
 /// "fake" is not true. Setting "fake" to true and sending
 /// not the exact amount are ways to hide the real bid but
 /// still make the required deposit. The same address can
 /// place multiple bids.
 function bid(bytes32 blindedBid)
 external
 payable
 onlyBefore(biddingEnd)
 {
 bids[msg.sender].push(Bid({
 blindedBid: blindedBid,
 deposit: msg.value
 }));
 }

 /// Reveal your blinded bids. You will get a refund for all
 /// correctly blinded invalid bids and for all bids except for
 /// the totally highest.
 function reveal(
 uint[] calldata values,
 bool[] calldata fakes,
 bytes32[] calldata secrets
 )
 external
 onlyAfter(biddingEnd)
 onlyBefore(revealEnd)
 {
 uint length = bids[msg.sender].length;
 require(values.length == length);
 require(fakes.length == length);
 require(secrets.length == length);

 uint refund;
 for (uint i = 0; i < length; i++) {
 Bid storage bidToCheck = bids[msg.sender][i];
 (uint value, bool fake, bytes32 secret) =
 (values[i], fakes[i], secrets[i]);
 if (bidToCheck.blindedBid != keccak256(abi.encodePacked(value, fake, secret))) {
 // Bid was not actually revealed.
 // Do not refund deposit.
 continue;
 }
 refund += bidToCheck.deposit;
 if (!fake && bidToCheck.deposit >= value) {
 if (placeBid(msg.sender, value))
 refund -= value;
 }
 // Make it impossible for the sender to re-claim
 // the same deposit.
 bidToCheck.blindedBid = bytes32(0);
 }
 payable(msg.sender).transfer(refund);
 }

 /// Withdraw a bid that was overbid.
 function withdraw() external {
 uint amount = pendingReturns[msg.sender];
 if (amount > 0) {
 // It is important to set this to zero because the recipient
 // can call this function again as part of the receiving call
 // before `transfer` returns (see the remark above about
 // conditions -> effects -> interaction).
 pendingReturns[msg.sender] = 0;

 payable(msg.sender).transfer(amount);
 }
 }

 /// End the auction and send the highest bid
 /// to the beneficiary.
 function auctionEnd()
 external
 onlyAfter(revealEnd)
 {
 if (ended) revert AuctionEndAlreadyCalled();
 emit AuctionEnded(highestBidder, highestBid);
 ended = true;
 beneficiary.transfer(highestBid);
 }

 // This is an "internal" function which means that it
 // can only be called from the contract itself (or from
 // derived contracts).
 function placeBid(address bidder, uint value) internal
 returns (bool success)
 {
 if (value <= highestBid) {
 return false;
 }
 if (highestBidder != address(0)) {
 // Refund the previously highest bidder.
 pendingReturns[highestBidder] += highestBid;
 }
 highestBid = value;
 highestBidder = bidder;
 return true;
 }
}

Safe Remote Purchase[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#safe-remote-purchase "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

Purchasing goods remotely currently requires multiple parties that need to trust each other. The simplest configuration involves a seller and a buyer. The buyer would like to receive an item from the seller and the seller would like to get some compensation, e.g. Ether, in return. The problematic part is the shipment here: There is no way to determine for sure that the item arrived at the buyer.

There are multiple ways to solve this problem, but all fall short in one or the other way. In the following example, both parties have to put twice the value of the item into the contract as escrow. As soon as this happened, the Ether will stay locked inside the contract until the buyer confirms that they received the item. After that, the buyer is returned the value (half of their deposit) and the seller gets three times the value (their deposit plus the value). The idea behind this is that both parties have an incentive to resolve the situation or otherwise their Ether is locked forever.

This contract of course does not solve the problem, but gives an overview of how you can use state machine-like constructs inside a contract.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5IF4wLjguNDsKY29udHJhY3QgUHVyY2hhc2UgewogICAgdWludCBwdWJsaWMgdmFsdWU7CiAgICBhZGRyZXNzIHBheWFibGUgcHVibGljIHNlbGxlcjsKICAgIGFkZHJlc3MgcGF5YWJsZSBwdWJsaWMgYnV5ZXI7CgogICAgZW51bSBTdGF0ZSB7IENyZWF0ZWQsIExvY2tlZCwgUmVsZWFzZSwgSW5hY3RpdmUgfQogICAgLy8gVGhlIHN0YXRlIHZhcmlhYmxlIGhhcyBhIGRlZmF1bHQgdmFsdWUgb2YgdGhlIGZpcnN0IG1lbWJlciwgYFN0YXRlLmNyZWF0ZWRgCiAgICBTdGF0ZSBwdWJsaWMgc3RhdGU7CgogICAgbW9kaWZpZXIgY29uZGl0aW9uKGJvb2wgY29uZGl0aW9uXykgewogICAgICAgIHJlcXVpcmUoY29uZGl0aW9uXyk7CiAgICAgICAgXzsKICAgIH0KCiAgICAvLy8gT25seSB0aGUgYnV5ZXIgY2FuIGNhbGwgdGhpcyBmdW5jdGlvbi4KICAgIGVycm9yIE9ubHlCdXllcigpOwogICAgLy8vIE9ubHkgdGhlIHNlbGxlciBjYW4gY2FsbCB0aGlzIGZ1bmN0aW9uLgogICAgZXJyb3IgT25seVNlbGxlcigpOwogICAgLy8vIFRoZSBmdW5jdGlvbiBjYW5ub3QgYmUgY2FsbGVkIGF0IHRoZSBjdXJyZW50IHN0YXRlLgogICAgZXJyb3IgSW52YWxpZFN0YXRlKCk7CiAgICAvLy8gVGhlIHByb3ZpZGVkIHZhbHVlIGhhcyB0byBiZSBldmVuLgogICAgZXJyb3IgVmFsdWVOb3RFdmVuKCk7CgogICAgbW9kaWZpZXIgb25seUJ1eWVyKCkgewogICAgICAgIGlmIChtc2cuc2VuZGVyICE9IGJ1eWVyKQogICAgICAgICAgICByZXZlcnQgT25seUJ1eWVyKCk7CiAgICAgICAgXzsKICAgIH0KCiAgICBtb2RpZmllciBvbmx5U2VsbGVyKCkgewogICAgICAgIGlmIChtc2cuc2VuZGVyICE9IHNlbGxlcikKICAgICAgICAgICAgcmV2ZXJ0IE9ubHlTZWxsZXIoKTsKICAgICAgICBfOwogICAgfQoKICAgIG1vZGlmaWVyIGluU3RhdGUoU3RhdGUgc3RhdGVfKSB7CiAgICAgICAgaWYgKHN0YXRlICE9IHN0YXRlXykKICAgICAgICAgICAgcmV2ZXJ0IEludmFsaWRTdGF0ZSgpOwogICAgICAgIF87CiAgICB9CgogICAgZXZlbnQgQWJvcnRlZCgpOwogICAgZXZlbnQgUHVyY2hhc2VDb25maXJtZWQoKTsKICAgIGV2ZW50IEl0ZW1SZWNlaXZlZCgpOwogICAgZXZlbnQgU2VsbGVyUmVmdW5kZWQoKTsKCiAgICAvLyBFbnN1cmUgdGhhdCBgbXNnLnZhbHVlYCBpcyBhbiBldmVuIG51bWJlci4KICAgIC8vIERpdmlzaW9uIHdpbGwgdHJ1bmNhdGUgaWYgaXQgaXMgYW4gb2RkIG51bWJlci4KICAgIC8vIENoZWNrIHZpYSBtdWx0aXBsaWNhdGlvbiB0aGF0IGl0IHdhc24ndCBhbiBvZGQgbnVtYmVyLgogICAgY29uc3RydWN0b3IoKSBwYXlhYmxlIHsKICAgICAgICBzZWxsZXIgPSBwYXlhYmxlKG1zZy5zZW5kZXIpOwogICAgICAgIHZhbHVlID0gbXNnLnZhbHVlIC8gMjsKICAgICAgICBpZiAoKDIgKiB2YWx1ZSkgIT0gbXNnLnZhbHVlKQogICAgICAgICAgICByZXZlcnQgVmFsdWVOb3RFdmVuKCk7CiAgICB9CgogICAgLy8vIEFib3J0IHRoZSBwdXJjaGFzZSBhbmQgcmVjbGFpbSB0aGUgZXRoZXIuCiAgICAvLy8gQ2FuIG9ubHkgYmUgY2FsbGVkIGJ5IHRoZSBzZWxsZXIgYmVmb3JlCiAgICAvLy8gdGhlIGNvbnRyYWN0IGlzIGxvY2tlZC4KICAgIGZ1bmN0aW9uIGFib3J0KCkKICAgICAgICBleHRlcm5hbAogICAgICAgIG9ubHlTZWxsZXIKICAgICAgICBpblN0YXRlKFN0YXRlLkNyZWF0ZWQpCiAgICB7CiAgICAgICAgZW1pdCBBYm9ydGVkKCk7CiAgICAgICAgc3RhdGUgPSBTdGF0ZS5JbmFjdGl2ZTsKICAgICAgICAvLyBXZSB1c2UgdHJhbnNmZXIgaGVyZSBkaXJlY3RseS4gSXQgaXMKICAgICAgICAvLyByZWVudHJhbmN5LXNhZmUsIGJlY2F1c2UgaXQgaXMgdGhlCiAgICAgICAgLy8gbGFzdCBjYWxsIGluIHRoaXMgZnVuY3Rpb24gYW5kIHdlCiAgICAgICAgLy8gYWxyZWFkeSBjaGFuZ2VkIHRoZSBzdGF0ZS4KICAgICAgICBzZWxsZXIudHJhbnNmZXIoYWRkcmVzcyh0aGlzKS5iYWxhbmNlKTsKICAgIH0KCiAgICAvLy8gQ29uZmlybSB0aGUgcHVyY2hhc2UgYXMgYnV5ZXIuCiAgICAvLy8gVHJhbnNhY3Rpb24gaGFzIHRvIGluY2x1ZGUgYDIgKiB2YWx1ZWAgZXRoZXIuCiAgICAvLy8gVGhlIGV0aGVyIHdpbGwgYmUgbG9ja2VkIHVudGlsIGNvbmZpcm1SZWNlaXZlZAogICAgLy8vIGlzIGNhbGxlZC4KICAgIGZ1bmN0aW9uIGNvbmZpcm1QdXJjaGFzZSgpCiAgICAgICAgZXh0ZXJuYWwKICAgICAgICBpblN0YXRlKFN0YXRlLkNyZWF0ZWQpCiAgICAgICAgY29uZGl0aW9uKG1zZy52YWx1ZSA9PSAoMiAqIHZhbHVlKSkKICAgICAgICBwYXlhYmxlCiAgICB7CiAgICAgICAgZW1pdCBQdXJjaGFzZUNvbmZpcm1lZCgpOwogICAgICAgIGJ1eWVyID0gcGF5YWJsZShtc2cuc2VuZGVyKTsKICAgICAgICBzdGF0ZSA9IFN0YXRlLkxvY2tlZDsKICAgIH0KCiAgICAvLy8gQ29uZmlybSB0aGF0IHlvdSAodGhlIGJ1eWVyKSByZWNlaXZlZCB0aGUgaXRlbS4KICAgIC8vLyBUaGlzIHdpbGwgcmVsZWFzZSB0aGUgbG9ja2VkIGV0aGVyLgogICAgZnVuY3Rpb24gY29uZmlybVJlY2VpdmVkKCkKICAgICAgICBleHRlcm5hbAogICAgICAgIG9ubHlCdXllcgogICAgICAgIGluU3RhdGUoU3RhdGUuTG9ja2VkKQogICAgewogICAgICAgIGVtaXQgSXRlbVJlY2VpdmVkKCk7CiAgICAgICAgLy8gSXQgaXMgaW1wb3J0YW50IHRvIGNoYW5nZSB0aGUgc3RhdGUgZmlyc3QgYmVjYXVzZQogICAgICAgIC8vIG90aGVyd2lzZSwgdGhlIGNvbnRyYWN0cyBjYWxsZWQgdXNpbmcgYHNlbmRgIGJlbG93CiAgICAgICAgLy8gY2FuIGNhbGwgaW4gYWdhaW4gaGVyZS4KICAgICAgICBzdGF0ZSA9IFN0YXRlLlJlbGVhc2U7CgogICAgICAgIGJ1eWVyLnRyYW5zZmVyKHZhbHVlKTsKICAgIH0KCiAgICAvLy8gVGhpcyBmdW5jdGlvbiByZWZ1bmRzIHRoZSBzZWxsZXIsIGkuZS4KICAgIC8vLyBwYXlzIGJhY2sgdGhlIGxvY2tlZCBmdW5kcyBvZiB0aGUgc2VsbGVyLgogICAgZnVuY3Rpb24gcmVmdW5kU2VsbGVyKCkKICAgICAgICBleHRlcm5hbAogICAgICAgIG9ubHlTZWxsZXIKICAgICAgICBpblN0YXRlKFN0YXRlLlJlbGVhc2UpCiAgICB7CiAgICAgICAgZW1pdCBTZWxsZXJSZWZ1bmRlZCgpOwogICAgICAgIC8vIEl0IGlzIGltcG9ydGFudCB0byBjaGFuZ2UgdGhlIHN0YXRlIGZpcnN0IGJlY2F1c2UKICAgICAgICAvLyBvdGhlcndpc2UsIHRoZSBjb250cmFjdHMgY2FsbGVkIHVzaW5nIGBzZW5kYCBiZWxvdwogICAgICAgIC8vIGNhbiBjYWxsIGluIGFnYWluIGhlcmUuCiAgICAgICAgc3RhdGUgPSBTdGF0ZS5JbmFjdGl2ZTsKCiAgICAgICAgc2VsbGVyLnRyYW5zZmVyKDMgKiB2YWx1ZSk7CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;
contract Purchase {
 uint public value;
 address payable public seller;
 address payable public buyer;

 enum State { Created, Locked, Release, Inactive }
 // The state variable has a default value of the first member, `State.created`
 State public state;

 modifier condition(bool condition_) {
 require(condition_);
 _;
 }

 /// Only the buyer can call this function.
 error OnlyBuyer();
 /// Only the seller can call this function.
 error OnlySeller();
 /// The function cannot be called at the current state.
 error InvalidState();
 /// The provided value has to be even.
 error ValueNotEven();

 modifier onlyBuyer() {
 if (msg.sender != buyer)
 revert OnlyBuyer();
 _;
 }

 modifier onlySeller() {
 if (msg.sender != seller)
 revert OnlySeller();
 _;
 }

 modifier inState(State state_) {
 if (state != state_)
 revert InvalidState();
 _;
 }

 event Aborted();
 event PurchaseConfirmed();
 event ItemReceived();
 event SellerRefunded();

 // Ensure that `msg.value` is an even number.
 // Division will truncate if it is an odd number.
 // Check via multiplication that it wasn't an odd number.
 constructor() payable {
 seller = payable(msg.sender);
 value = msg.value / 2;
 if ((2 * value) != msg.value)
 revert ValueNotEven();
 }

 /// Abort the purchase and reclaim the ether.
 /// Can only be called by the seller before
 /// the contract is locked.
 function abort()
 external
 onlySeller
 inState(State.Created)
 {
 emit Aborted();
 state = State.Inactive;
 // We use transfer here directly. It is
 // reentrancy-safe, because it is the
 // last call in this function and we
 // already changed the state.
 seller.transfer(address(this).balance);
 }

 /// Confirm the purchase as buyer.
 /// Transaction has to include `2 * value` ether.
 /// The ether will be locked until confirmReceived
 /// is called.
 function confirmPurchase()
 external
 inState(State.Created)
 condition(msg.value == (2 * value))
 payable
 {
 emit PurchaseConfirmed();
 buyer = payable(msg.sender);
 state = State.Locked;
 }

 /// Confirm that you (the buyer) received the item.
 /// This will release the locked ether.
 function confirmReceived()
 external
 onlyBuyer
 inState(State.Locked)
 {
 emit ItemReceived();
 // It is important to change the state first because
 // otherwise, the contracts called using `send` below
 // can call in again here.
 state = State.Release;

 buyer.transfer(value);
 }

 /// This function refunds the seller, i.e.
 /// pays back the locked funds of the seller.
 function refundSeller()
 external
 onlySeller
 inState(State.Release)
 {
 emit SellerRefunded();
 // It is important to change the state first because
 // otherwise, the contracts called using `send` below
 // can call in again here.
 state = State.Inactive;

 seller.transfer(3 * value);
 }
}

Micropayment Channel[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#micropayment-channel "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

In this section, we will learn how to build an example implementation of a payment channel. It uses cryptographic signatures to make repeated transfers of Ether between the same parties secure, instantaneous, and without transaction fees. For the example, we need to understand how to sign and verify signatures, and setup the payment channel.

### Creating and verifying signatures[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#creating-and-verifying-signatures "Link to this heading")

Imagine Alice wants to send some Ether to Bob, i.e. Alice is the sender and Bob is the recipient.

Alice only needs to send cryptographically signed messages off-chain (e.g. via email) to Bob and it is similar to writing checks.

Alice and Bob use signatures to authorize transactions, which is possible with smart contracts on Ethereum. Alice will build a simple smart contract that lets her transmit Ether, but instead of calling a function herself to initiate a payment, she will let Bob do that, and therefore pay the transaction fee.

The contract will work as follows:

> 1.   Alice deploys the `ReceiverPays` contract, attaching enough Ether to cover the payments that will be made.
> 
> 2.   Alice authorizes a payment by signing a message with her private key.
> 
> 3.   Alice sends the cryptographically signed message to Bob. The message does not need to be kept secret (explained later), and the mechanism for sending it does not matter.
> 
> 4.   Bob claims his payment by presenting the signed message to the smart contract, it verifies the authenticity of the message and then releases the funds.

#### Creating the signature[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#creating-the-signature "Link to this heading")

Alice does not need to interact with the Ethereum network to sign the transaction, the process is completely offline. In this tutorial, we will sign messages in the browser using [web3.js](https://github.com/web3/web3.js) and [MetaMask](https://metamask.io/), using the method described in [EIP-712](https://github.com/ethereum/EIPs/pull/712), as it provides a number of other security benefits.

/// Hashing first makes things easier
var hash = web3.utils.sha3("message to sign");
web3.eth.personal.sign(hash, web3.eth.defaultAccount, function () { console.log("Signed"); });

Note

The `web3.eth.personal.sign` prepends the length of the message to the signed data. Since we hash first, the message will always be exactly 32 bytes long, and thus this length prefix is always the same.

#### What to Sign[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#what-to-sign "Link to this heading")

For a contract that fulfills payments, the signed message must include:

> 1.   The recipient’s address.
> 
> 2.   The amount to be transferred.
> 
> 3.   Protection against replay attacks.

A replay attack is when a signed message is reused to claim authorization for a second action. To avoid replay attacks we use the same technique as in Ethereum transactions themselves, a so-called nonce, which is the number of transactions sent by an account. The smart contract checks if a nonce is used multiple times.

Another type of replay attack can occur when the owner deploys a `ReceiverPays` smart contract, makes some payments, and then destroys the contract. Later, they decide to deploy the `RecipientPays` smart contract again, but the new contract does not know the nonces used in the previous deployment, so the attacker can use the old messages again.

Alice can protect against this attack by including the contract’s address in the message, and only messages containing the contract’s address itself will be accepted. You can find an example of this in the first two lines of the `claimPayment()` function of the full contract at the end of this section.

Furthermore, instead of destroying the contract by calling `selfdestruct`, which is currently deprecated, we will disable the contract’s functionalities by freezing it, resulting in the reversion of any call after it being frozen.

#### Packing arguments[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#packing-arguments "Link to this heading")

Now that we have identified what information to include in the signed message, we are ready to put the message together, hash it, and sign it. For simplicity, we concatenate the data. The [ethereumjs-abi](https://github.com/ethereumjs/ethereumjs-abi) library provides a function called `soliditySHA3` that mimics the behavior of Solidity’s `keccak256` function applied to arguments encoded using `abi.encodePacked`. Here is a JavaScript function that creates the proper signature for the `ReceiverPays` example:

// recipient is the address that should be paid.
// amount, in wei, specifies how much ether should be sent.
// nonce can be any unique number to prevent replay attacks
// contractAddress is used to prevent cross-contract replay attacks
function signPayment(recipient, amount, nonce, contractAddress, callback) {
 var hash = "0x" + abi.soliditySHA3(
 ["address", "uint256", "uint256", "address"],
 [recipient, amount, nonce, contractAddress]
 ).toString("hex");

 web3.eth.personal.sign(hash, web3.eth.defaultAccount, callback);
}

#### Recovering the Message Signer in Solidity[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#recovering-the-message-signer-in-solidity "Link to this heading")

In general, ECDSA signatures consist of two parameters, `r` and `s`. Signatures in Ethereum include a third parameter called `v`, that you can use to verify which account’s private key was used to sign the message, and the transaction’s sender. Solidity provides a built-in function [ecrecover](https://docs.soliditylang.org/en/latest/units-and-global-variables.html#mathematical-and-cryptographic-functions) that accepts a message along with the `r`, `s` and `v` parameters and returns the address that was used to sign the message.

#### Computing the Message Hash[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#computing-the-message-hash "Link to this heading")

The smart contract needs to know exactly what parameters were signed, and so it must recreate the message from the parameters and use that for signature verification. The functions `prefixed` and `recoverSigner` do this in the `claimPayment` function.

#### The full contract[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#the-full-contract "Link to this heading")

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjAgPDAuOS4wOwoKY29udHJhY3QgT3duZWQgewogICAgYWRkcmVzcyBwYXlhYmxlIG93bmVyOwogICAgY29uc3RydWN0b3IoKSB7CiAgICAgICAgb3duZXIgPSBwYXlhYmxlKG1zZy5zZW5kZXIpOwogICAgfQp9Cgpjb250cmFjdCBGcmVlemFibGUgaXMgT3duZWQgewogICAgYm9vbCBwcml2YXRlIF9mcm96ZW4gPSBmYWxzZTsKCiAgICBtb2RpZmllciBub3RGcm96ZW4oKSB7CiAgICAgICAgcmVxdWlyZSghX2Zyb3plbiwgIkluYWN0aXZlIENvbnRyYWN0LiIpOwogICAgICAgIF87CiAgICB9CgogICAgZnVuY3Rpb24gZnJlZXplKCkgaW50ZXJuYWwgewogICAgICAgIGlmIChtc2cuc2VuZGVyID09IG93bmVyKQogICAgICAgICAgICBfZnJvemVuID0gdHJ1ZTsKICAgIH0KfQoKY29udHJhY3QgUmVjZWl2ZXJQYXlzIGlzIEZyZWV6YWJsZSB7CiAgICBtYXBwaW5nKHVpbnQyNTYgPT4gYm9vbCkgdXNlZE5vbmNlczsKCiAgICBjb25zdHJ1Y3RvcigpIHBheWFibGUge30KCiAgICBmdW5jdGlvbiBjbGFpbVBheW1lbnQodWludDI1NiBhbW91bnQsIHVpbnQyNTYgbm9uY2UsIGJ5dGVzIG1lbW9yeSBzaWduYXR1cmUpCiAgICAgICAgZXh0ZXJuYWwKICAgICAgICBub3RGcm96ZW4KICAgIHsKICAgICAgICByZXF1aXJlKCF1c2VkTm9uY2VzW25vbmNlXSk7CiAgICAgICAgdXNlZE5vbmNlc1tub25jZV0gPSB0cnVlOwoKICAgICAgICAvLyB0aGlzIHJlY3JlYXRlcyB0aGUgbWVzc2FnZSB0aGF0IHdhcyBzaWduZWQgb24gdGhlIGNsaWVudAogICAgICAgIGJ5dGVzMzIgbWVzc2FnZSA9IHByZWZpeGVkKGtlY2NhazI1NihhYmkuZW5jb2RlUGFja2VkKG1zZy5zZW5kZXIsIGFtb3VudCwgbm9uY2UsIHRoaXMpKSk7CiAgICAgICAgcmVxdWlyZShyZWNvdmVyU2lnbmVyKG1lc3NhZ2UsIHNpZ25hdHVyZSkgPT0gb3duZXIpOwogICAgICAgIHBheWFibGUobXNnLnNlbmRlcikudHJhbnNmZXIoYW1vdW50KTsKICAgIH0KCiAgICAvLy8gZnJlZXplIHRoZSBjb250cmFjdCBhbmQgcmVjbGFpbSB0aGUgbGVmdG92ZXIgZnVuZHMuCiAgICBmdW5jdGlvbiBzaHV0ZG93bigpCiAgICAgICAgZXh0ZXJuYWwKICAgICAgICBub3RGcm96ZW4KICAgIHsKICAgICAgICByZXF1aXJlKG1zZy5zZW5kZXIgPT0gb3duZXIpOwogICAgICAgIGZyZWV6ZSgpOwogICAgICAgIHBheWFibGUobXNnLnNlbmRlcikudHJhbnNmZXIoYWRkcmVzcyh0aGlzKS5iYWxhbmNlKTsKICAgIH0KCiAgICAvLy8gc2lnbmF0dXJlIG1ldGhvZHMuCiAgICBmdW5jdGlvbiBzcGxpdFNpZ25hdHVyZShieXRlcyBtZW1vcnkgc2lnKQogICAgICAgIGludGVybmFsCiAgICAgICAgcHVyZQogICAgICAgIHJldHVybnMgKHVpbnQ4IHYsIGJ5dGVzMzIgciwgYnl0ZXMzMiBzKQogICAgewogICAgICAgIHJlcXVpcmUoc2lnLmxlbmd0aCA9PSA2NSk7CgogICAgICAgIGFzc2VtYmx5IHsKICAgICAgICAgICAgLy8gZmlyc3QgMzIgYnl0ZXMsIGFmdGVyIHRoZSBsZW5ndGggcHJlZml4LgogICAgICAgICAgICByIDo9IG1sb2FkKGFkZChzaWcsIDMyKSkKICAgICAgICAgICAgLy8gc2Vjb25kIDMyIGJ5dGVzLgogICAgICAgICAgICBzIDo9IG1sb2FkKGFkZChzaWcsIDY0KSkKICAgICAgICAgICAgLy8gZmluYWwgYnl0ZSAoZmlyc3QgYnl0ZSBvZiB0aGUgbmV4dCAzMiBieXRlcykuCiAgICAgICAgICAgIHYgOj0gYnl0ZSgwLCBtbG9hZChhZGQoc2lnLCA5NikpKQogICAgICAgIH0KCiAgICAgICAgcmV0dXJuICh2LCByLCBzKTsKICAgIH0KCiAgICBmdW5jdGlvbiByZWNvdmVyU2lnbmVyKGJ5dGVzMzIgbWVzc2FnZSwgYnl0ZXMgbWVtb3J5IHNpZykKICAgICAgICBpbnRlcm5hbAogICAgICAgIHB1cmUKICAgICAgICByZXR1cm5zIChhZGRyZXNzKQogICAgewogICAgICAgICh1aW50OCB2LCBieXRlczMyIHIsIGJ5dGVzMzIgcykgPSBzcGxpdFNpZ25hdHVyZShzaWcpOwogICAgICAgIHJldHVybiBlY3JlY292ZXIobWVzc2FnZSwgdiwgciwgcyk7CiAgICB9CgogICAgLy8vIGJ1aWxkcyBhIHByZWZpeGVkIGhhc2ggdG8gbWltaWMgdGhlIGJlaGF2aW9yIG9mIGV0aF9zaWduLgogICAgZnVuY3Rpb24gcHJlZml4ZWQoYnl0ZXMzMiBoYXNoKSBpbnRlcm5hbCBwdXJlIHJldHVybnMgKGJ5dGVzMzIpIHsKICAgICAgICByZXR1cm4ga2VjY2FrMjU2KGFiaS5lbmNvZGVQYWNrZWQoIlx4MTlFdGhlcmV1bSBTaWduZWQgTWVzc2FnZTpcbjMyIiwgaGFzaCkpOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Owned {
 address payable owner;
 constructor() {
 owner = payable(msg.sender);
 }
}

contract Freezable is Owned {
 bool private _frozen = false;

 modifier notFrozen() {
 require(!_frozen, "Inactive Contract.");
 _;
 }

 function freeze() internal {
 if (msg.sender == owner)
 _frozen = true;
 }
}

contract ReceiverPays is Freezable {
 mapping(uint256 => bool) usedNonces;

 constructor() payable {}

 function claimPayment(uint256 amount, uint256 nonce, bytes memory signature)
 external
 notFrozen
 {
 require(!usedNonces[nonce]);
 usedNonces[nonce] = true;

 // this recreates the message that was signed on the client
 bytes32 message = prefixed(keccak256(abi.encodePacked(msg.sender, amount, nonce, this)));
 require(recoverSigner(message, signature) == owner);
 payable(msg.sender).transfer(amount);
 }

 /// freeze the contract and reclaim the leftover funds.
 function shutdown()
 external
 notFrozen
 {
 require(msg.sender == owner);
 freeze();
 payable(msg.sender).transfer(address(this).balance);
 }

 /// signature methods.
 function splitSignature(bytes memory sig)
 internal
 pure
 returns (uint8 v, bytes32 r, bytes32 s)
 {
 require(sig.length == 65);

 assembly {
 // first 32 bytes, after the length prefix.
 r := mload(add(sig, 32))
 // second 32 bytes.
 s := mload(add(sig, 64))
 // final byte (first byte of the next 32 bytes).
 v := byte(0, mload(add(sig, 96)))
 }

 return (v, r, s);
 }

 function recoverSigner(bytes32 message, bytes memory sig)
 internal
 pure
 returns (address)
 {
 (uint8 v, bytes32 r, bytes32 s) = splitSignature(sig);
 return ecrecover(message, v, r, s);
 }

 /// builds a prefixed hash to mimic the behavior of eth_sign.
 function prefixed(bytes32 hash) internal pure returns (bytes32) {
 return keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", hash));
 }
}

### Writing a Simple Payment Channel[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#writing-a-simple-payment-channel "Link to this heading")

Alice now builds a simple but complete implementation of a payment channel. Payment channels use cryptographic signatures to make repeated transfers of Ether securely, instantaneously, and without transaction fees.

#### What is a Payment Channel?[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#what-is-a-payment-channel "Link to this heading")

Payment channels allow participants to make repeated transfers of Ether without using transactions. This means that you can avoid the delays and fees associated with transactions. We are going to explore a simple unidirectional payment channel between two parties (Alice and Bob). It involves three steps:

> 1.   Alice funds a smart contract with Ether. This “opens” the payment channel.
> 
> 2.   Alice signs messages that specify how much of that Ether is owed to the recipient. This step is repeated for each payment.
> 
> 3.   Bob “closes” the payment channel, withdrawing his portion of the Ether and sending the remainder back to the sender.

Note

Only steps 1 and 3 require Ethereum transactions, step 2 means that the sender transmits a cryptographically signed message to the recipient via off chain methods (e.g. email). This means only two transactions are required to support any number of transfers.

Bob is guaranteed to receive his funds because the smart contract escrows the Ether and honours a valid signed message. The smart contract also enforces a timeout, so Alice is guaranteed to eventually recover her funds even if the recipient refuses to close the channel. It is up to the participants in a payment channel to decide how long to keep it open. For a short-lived transaction, such as paying an internet café for each minute of network access, the payment channel may be kept open for a limited duration. On the other hand, for a recurring payment, such as paying an employee an hourly wage, the payment channel may be kept open for several months or years.

#### Opening the Payment Channel[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#opening-the-payment-channel "Link to this heading")

To open the payment channel, Alice deploys the smart contract, attaching the Ether to be escrowed and specifying the intended recipient and a maximum duration for the channel to exist. This is the `constructor` in the `SimplePaymentChannel` contract, at the end of this section.

#### Making Payments[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#making-payments "Link to this heading")

Alice makes payments by sending signed messages to Bob. This step is performed entirely outside of the Ethereum network. Messages are cryptographically signed by the sender and then transmitted directly to the recipient.

Each message includes the following information:

> *   The smart contract’s address, used to prevent cross-contract replay attacks.
> 
> *   The total amount of Ether that is owed to the recipient so far.

A payment channel is closed just once, at the end of a series of transfers. Because of this, only one of the messages sent is redeemed. This is why each message specifies a cumulative total amount of Ether owed, rather than the amount of the individual micropayment. The recipient will naturally choose to redeem the most recent message because that is the one with the highest total. The nonce per-message is not needed anymore, because the smart contract only honours a single message. The address of the smart contract is still used to prevent a message intended for one payment channel from being used for a different channel.

Here is the modified JavaScript code to cryptographically sign a message from the previous section:

function constructPaymentMessage(contractAddress, amount) {
 return abi.soliditySHA3(
 ["address", "uint256"],
 [contractAddress, amount]
 );
}

function signMessage(message, callback) {
 web3.eth.personal.sign(
 "0x" + message.toString("hex"),
 web3.eth.defaultAccount,
 callback
 );
}

// contractAddress is used to prevent cross-contract replay attacks.
// amount, in wei, specifies how much Ether should be sent.

function signPayment(contractAddress, amount, callback) {
 var message = constructPaymentMessage(contractAddress, amount);
 signMessage(message, callback);
}

#### Closing the Payment Channel[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#closing-the-payment-channel "Link to this heading")

When Bob is ready to receive his funds, it is time to close the payment channel by calling a `close` function on the smart contract. Closing the channel pays the recipient the Ether they are owed and deactivates the contract by freezing it, sending any remaining Ether back to Alice. To close the channel, Bob needs to provide a message signed by Alice.

The smart contract must verify that the message contains a valid signature from the sender. The process for doing this verification is the same as the process the recipient uses. The Solidity functions `isValidSignature` and `recoverSigner` work just like their JavaScript counterparts in the previous section, with the latter function borrowed from the `ReceiverPays` contract.

Only the payment channel recipient can call the `close` function, who naturally passes the most recent payment message because that message carries the highest total owed. If the sender were allowed to call this function, they could provide a message with a lower amount and cheat the recipient out of what they are owed.

The function verifies the signed message matches the given parameters. If everything checks out, the recipient is sent their portion of the Ether, and the sender is sent the remaining funds via a `transfer`. You can see the `close` function in the full contract.

#### Channel Expiration[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#channel-expiration "Link to this heading")

Bob can close the payment channel at any time, but if they fail to do so, Alice needs a way to recover her escrowed funds. An _expiration_ time was set at the time of contract deployment. Once that time is reached, Alice can call `claimTimeout` to recover her funds. You can see the `claimTimeout` function in the full contract.

After this function is called, Bob can no longer receive any Ether, so it is important that Bob closes the channel before the expiration is reached.

#### The full contract[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#id3 "Link to this heading")

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC43LjAgPDAuOS4wOwoKY29udHJhY3QgRnJvemVhYmxlIHsKICAgIGJvb2wgcHJpdmF0ZSBfZnJvemVuID0gZmFsc2U7CgogICAgbW9kaWZpZXIgbm90RnJvemVuKCkgewogICAgICAgIHJlcXVpcmUoIV9mcm96ZW4sICJJbmFjdGl2ZSBDb250cmFjdC4iKTsKICAgICAgICBfOwogICAgfQoKICAgIGZ1bmN0aW9uIGZyZWV6ZSgpIGludGVybmFsIHsKICAgICAgICBfZnJvemVuID0gdHJ1ZTsKICAgIH0KfQoKY29udHJhY3QgU2ltcGxlUGF5bWVudENoYW5uZWwgaXMgRnJvemVhYmxlIHsKICAgIGFkZHJlc3MgcGF5YWJsZSBwdWJsaWMgc2VuZGVyOyAgICAvLyBUaGUgYWNjb3VudCBzZW5kaW5nIHBheW1lbnRzLgogICAgYWRkcmVzcyBwYXlhYmxlIHB1YmxpYyByZWNpcGllbnQ7IC8vIFRoZSBhY2NvdW50IHJlY2VpdmluZyB0aGUgcGF5bWVudHMuCiAgICB1aW50MjU2IHB1YmxpYyBleHBpcmF0aW9uOyAgICAgICAgLy8gVGltZW91dCBpbiBjYXNlIHRoZSByZWNpcGllbnQgbmV2ZXIgY2xvc2VzLgoKICAgIGNvbnN0cnVjdG9yIChhZGRyZXNzIHBheWFibGUgcmVjaXBpZW50QWRkcmVzcywgdWludDI1NiBkdXJhdGlvbikKICAgICAgICBwYXlhYmxlCiAgICB7CiAgICAgICAgc2VuZGVyID0gcGF5YWJsZShtc2cuc2VuZGVyKTsKICAgICAgICByZWNpcGllbnQgPSByZWNpcGllbnRBZGRyZXNzOwogICAgICAgIGV4cGlyYXRpb24gPSBibG9jay50aW1lc3RhbXAgKyBkdXJhdGlvbjsKICAgIH0KCiAgICAvLy8gdGhlIHJlY2lwaWVudCBjYW4gY2xvc2UgdGhlIGNoYW5uZWwgYXQgYW55IHRpbWUgYnkgcHJlc2VudGluZyBhCiAgICAvLy8gc2lnbmVkIGFtb3VudCBmcm9tIHRoZSBzZW5kZXIuIHRoZSByZWNpcGllbnQgd2lsbCBiZSBzZW50IHRoYXQgYW1vdW50LAogICAgLy8vIGFuZCB0aGUgcmVtYWluZGVyIHdpbGwgZ28gYmFjayB0byB0aGUgc2VuZGVyCiAgICBmdW5jdGlvbiBjbG9zZSh1aW50MjU2IGFtb3VudCwgYnl0ZXMgbWVtb3J5IHNpZ25hdHVyZSkKICAgICAgICBleHRlcm5hbAogICAgICAgIG5vdEZyb3plbgogICAgewogICAgICAgIHJlcXVpcmUobXNnLnNlbmRlciA9PSByZWNpcGllbnQpOwogICAgICAgIHJlcXVpcmUoaXNWYWxpZFNpZ25hdHVyZShhbW91bnQsIHNpZ25hdHVyZSkpOwoKICAgICAgICByZWNpcGllbnQudHJhbnNmZXIoYW1vdW50KTsKICAgICAgICBmcmVlemUoKTsKICAgICAgICBzZW5kZXIudHJhbnNmZXIoYWRkcmVzcyh0aGlzKS5iYWxhbmNlKTsKICAgIH0KCiAgICAvLy8gdGhlIHNlbmRlciBjYW4gZXh0ZW5kIHRoZSBleHBpcmF0aW9uIGF0IGFueSB0aW1lCiAgICBmdW5jdGlvbiBleHRlbmQodWludDI1NiBuZXdFeHBpcmF0aW9uKQogICAgICAgIGV4dGVybmFsCiAgICAgICAgbm90RnJvemVuCiAgICB7CiAgICAgICAgcmVxdWlyZShtc2cuc2VuZGVyID09IHNlbmRlcik7CiAgICAgICAgcmVxdWlyZShuZXdFeHBpcmF0aW9uID4gZXhwaXJhdGlvbik7CgogICAgICAgIGV4cGlyYXRpb24gPSBuZXdFeHBpcmF0aW9uOwogICAgfQoKICAgIC8vLyBpZiB0aGUgdGltZW91dCBpcyByZWFjaGVkIHdpdGhvdXQgdGhlIHJlY2lwaWVudCBjbG9zaW5nIHRoZSBjaGFubmVsLAogICAgLy8vIHRoZW4gdGhlIEV0aGVyIGlzIHJlbGVhc2VkIGJhY2sgdG8gdGhlIHNlbmRlci4KICAgIGZ1bmN0aW9uIGNsYWltVGltZW91dCgpCiAgICAgICAgZXh0ZXJuYWwKICAgICAgICBub3RGcm96ZW4KICAgIHsKICAgICAgICByZXF1aXJlKGJsb2NrLnRpbWVzdGFtcCA+PSBleHBpcmF0aW9uKTsKICAgICAgICBmcmVlemUoKTsKICAgICAgICBzZW5kZXIudHJhbnNmZXIoYWRkcmVzcyh0aGlzKS5iYWxhbmNlKTsKICAgIH0KCiAgICBmdW5jdGlvbiBpc1ZhbGlkU2lnbmF0dXJlKHVpbnQyNTYgYW1vdW50LCBieXRlcyBtZW1vcnkgc2lnbmF0dXJlKQogICAgICAgIGludGVybmFsCiAgICAgICAgdmlldwogICAgICAgIHJldHVybnMgKGJvb2wpCiAgICB7CiAgICAgICAgYnl0ZXMzMiBtZXNzYWdlID0gcHJlZml4ZWQoa2VjY2FrMjU2KGFiaS5lbmNvZGVQYWNrZWQodGhpcywgYW1vdW50KSkpOwogICAgICAgIC8vIGNoZWNrIHRoYXQgdGhlIHNpZ25hdHVyZSBpcyBmcm9tIHRoZSBwYXltZW50IHNlbmRlcgogICAgICAgIHJldHVybiByZWNvdmVyU2lnbmVyKG1lc3NhZ2UsIHNpZ25hdHVyZSkgPT0gc2VuZGVyOwogICAgfQoKICAgIC8vLyBBbGwgZnVuY3Rpb25zIGJlbG93IHRoaXMgYXJlIGp1c3QgdGFrZW4gZnJvbSB0aGUgY2hhcHRlcgogICAgLy8vICdjcmVhdGluZyBhbmQgdmVyaWZ5aW5nIHNpZ25hdHVyZXMnIGNoYXB0ZXIuCiAgICBmdW5jdGlvbiBzcGxpdFNpZ25hdHVyZShieXRlcyBtZW1vcnkgc2lnKQogICAgICAgIGludGVybmFsCiAgICAgICAgcHVyZQogICAgICAgIHJldHVybnMgKHVpbnQ4IHYsIGJ5dGVzMzIgciwgYnl0ZXMzMiBzKQogICAgewogICAgICAgIHJlcXVpcmUoc2lnLmxlbmd0aCA9PSA2NSk7CgogICAgICAgIGFzc2VtYmx5IHsKICAgICAgICAgICAgLy8gZmlyc3QgMzIgYnl0ZXMsIGFmdGVyIHRoZSBsZW5ndGggcHJlZml4CiAgICAgICAgICAgIHIgOj0gbWxvYWQoYWRkKHNpZywgMzIpKQogICAgICAgICAgICAvLyBzZWNvbmQgMzIgYnl0ZXMKICAgICAgICAgICAgcyA6PSBtbG9hZChhZGQoc2lnLCA2NCkpCiAgICAgICAgICAgIC8vIGZpbmFsIGJ5dGUgKGZpcnN0IGJ5dGUgb2YgdGhlIG5leHQgMzIgYnl0ZXMpCiAgICAgICAgICAgIHYgOj0gYnl0ZSgwLCBtbG9hZChhZGQoc2lnLCA5NikpKQogICAgICAgIH0KICAgICAgICByZXR1cm4gKHYsIHIsIHMpOwogICAgfQoKICAgIGZ1bmN0aW9uIHJlY292ZXJTaWduZXIoYnl0ZXMzMiBtZXNzYWdlLCBieXRlcyBtZW1vcnkgc2lnKQogICAgICAgIGludGVybmFsCiAgICAgICAgcHVyZQogICAgICAgIHJldHVybnMgKGFkZHJlc3MpCiAgICB7CiAgICAgICAgKHVpbnQ4IHYsIGJ5dGVzMzIgciwgYnl0ZXMzMiBzKSA9IHNwbGl0U2lnbmF0dXJlKHNpZyk7CiAgICAgICAgcmV0dXJuIGVjcmVjb3ZlcihtZXNzYWdlLCB2LCByLCBzKTsKICAgIH0KCiAgICAvLy8gYnVpbGRzIGEgcHJlZml4ZWQgaGFzaCB0byBtaW1pYyB0aGUgYmVoYXZpb3Igb2YgZXRoX3NpZ24uCiAgICBmdW5jdGlvbiBwcmVmaXhlZChieXRlczMyIGhhc2gpIGludGVybmFsIHB1cmUgcmV0dXJucyAoYnl0ZXMzMikgewogICAgICAgIHJldHVybiBrZWNjYWsyNTYoYWJpLmVuY29kZVBhY2tlZCgiXHgxOUV0aGVyZXVtIFNpZ25lZCBNZXNzYWdlOlxuMzIiLCBoYXNoKSk7CiAgICB9Cn0=)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.7.0 <0.9.0;

contract Frozeable {
 bool private _frozen = false;

 modifier notFrozen() {
 require(!_frozen, "Inactive Contract.");
 _;
 }

 function freeze() internal {
 _frozen = true;
 }
}

contract SimplePaymentChannel is Frozeable {
 address payable public sender; // The account sending payments.
 address payable public recipient; // The account receiving the payments.
 uint256 public expiration; // Timeout in case the recipient never closes.

 constructor (address payable recipientAddress, uint256 duration)
 payable
 {
 sender = payable(msg.sender);
 recipient = recipientAddress;
 expiration = block.timestamp + duration;
 }

 /// the recipient can close the channel at any time by presenting a
 /// signed amount from the sender. the recipient will be sent that amount,
 /// and the remainder will go back to the sender
 function close(uint256 amount, bytes memory signature)
 external
 notFrozen
 {
 require(msg.sender == recipient);
 require(isValidSignature(amount, signature));

 recipient.transfer(amount);
 freeze();
 sender.transfer(address(this).balance);
 }

 /// the sender can extend the expiration at any time
 function extend(uint256 newExpiration)
 external
 notFrozen
 {
 require(msg.sender == sender);
 require(newExpiration > expiration);

 expiration = newExpiration;
 }

 /// if the timeout is reached without the recipient closing the channel,
 /// then the Ether is released back to the sender.
 function claimTimeout()
 external
 notFrozen
 {
 require(block.timestamp >= expiration);
 freeze();
 sender.transfer(address(this).balance);
 }

 function isValidSignature(uint256 amount, bytes memory signature)
 internal
 view
 returns (bool)
 {
 bytes32 message = prefixed(keccak256(abi.encodePacked(this, amount)));
 // check that the signature is from the payment sender
 return recoverSigner(message, signature) == sender;
 }

 /// All functions below this are just taken from the chapter
 /// 'creating and verifying signatures' chapter.
 function splitSignature(bytes memory sig)
 internal
 pure
 returns (uint8 v, bytes32 r, bytes32 s)
 {
 require(sig.length == 65);

 assembly {
 // first 32 bytes, after the length prefix
 r := mload(add(sig, 32))
 // second 32 bytes
 s := mload(add(sig, 64))
 // final byte (first byte of the next 32 bytes)
 v := byte(0, mload(add(sig, 96)))
 }
 return (v, r, s);
 }

 function recoverSigner(bytes32 message, bytes memory sig)
 internal
 pure
 returns (address)
 {
 (uint8 v, bytes32 r, bytes32 s) = splitSignature(sig);
 return ecrecover(message, v, r, s);
 }

 /// builds a prefixed hash to mimic the behavior of eth_sign.
 function prefixed(bytes32 hash) internal pure returns (bytes32) {
 return keccak256(abi.encodePacked("\x19Ethereum Signed Message:\n32", hash));
 }
}

Note

The function `splitSignature` does not use all security checks. A real implementation should use a more rigorously tested library, such as openzeppelin’s [version](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/cryptography/ECDSA.sol) of this code.

#### Verifying Payments[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#verifying-payments "Link to this heading")

Unlike in the previous section, messages in a payment channel aren’t redeemed right away. The recipient keeps track of the latest message and redeems it when it’s time to close the payment channel. This means it’s critical that the recipient perform their own verification of each message. Otherwise there is no guarantee that the recipient will be able to get paid in the end.

The recipient should verify each message using the following process:

> 1.   Verify that the contract address in the message matches the payment channel.
> 
> 2.   Verify that the new total is the expected amount.
> 
> 3.   Verify that the new total does not exceed the amount of Ether escrowed.
> 
> 4.   Verify that the signature is valid and comes from the payment channel sender.

We’ll use the [ethereumjs-util](https://github.com/ethereumjs/ethereumjs-util) library to write this verification. The final step can be done a number of ways, and we use JavaScript. The following code borrows the `constructPaymentMessage` function from the signing **JavaScript code** above:

// this mimics the prefixing behavior of the eth_sign JSON-RPC method.
function prefixed(hash) {
 return ethereumjs.ABI.soliditySHA3(
 ["string", "bytes32"],
 ["\x19Ethereum Signed Message:\n32", hash]
 );
}

function recoverSigner(message, signature) {
 var split = ethereumjs.Util.fromRpcSig(signature);
 var publicKey = ethereumjs.Util.ecrecover(message, split.v, split.r, split.s);
 var signer = ethereumjs.Util.pubToAddress(publicKey).toString("hex");
 return signer;
}

function isValidSignature(contractAddress, amount, signature, expectedSigner) {
 var message = prefixed(constructPaymentMessage(contractAddress, amount));
 var signer = recoverSigner(message, signature);
 return signer.toLowerCase() ==
 ethereumjs.Util.stripHexPrefix(expectedSigner).toLowerCase();
}

Modular Contracts[](https://docs.soliditylang.org/en/latest/solidity-by-example.html#modular-contracts "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

A modular approach to building your contracts helps you reduce the complexity and improve the readability which will help to identify bugs and vulnerabilities during development and code review. If you specify and control the behavior of each module in isolation, the interactions you have to consider are only those between the module specifications and not every other moving part of the contract. In the example below, the contract uses the `move` method of the `Balances`[library](https://docs.soliditylang.org/en/latest/contracts.html#libraries) to check that balances sent between addresses match what you expect. In this way, the `Balances` library provides an isolated component that properly tracks balances of accounts. It is easy to verify that the `Balances` library never produces negative balances or overflows and the sum of all balances is an invariant across the lifetime of the contract.

[open in Remix](https://remix.ethereum.org/?#language=solidity&version=0.8.31&code=Ly8gU1BEWC1MaWNlbnNlLUlkZW50aWZpZXI6IEdQTC0zLjAKcHJhZ21hIHNvbGlkaXR5ID49MC41LjAgPDAuOS4wOwoKbGlicmFyeSBCYWxhbmNlcyB7CiAgICBmdW5jdGlvbiBtb3ZlKG1hcHBpbmcoYWRkcmVzcyA9PiB1aW50MjU2KSBzdG9yYWdlIGJhbGFuY2VzLCBhZGRyZXNzIGZyb20sIGFkZHJlc3MgdG8sIHVpbnQgYW1vdW50KSBpbnRlcm5hbCB7CiAgICAgICAgcmVxdWlyZShiYWxhbmNlc1tmcm9tXSA+PSBhbW91bnQpOwogICAgICAgIHJlcXVpcmUoYmFsYW5jZXNbdG9dICsgYW1vdW50ID49IGJhbGFuY2VzW3RvXSk7CiAgICAgICAgYmFsYW5jZXNbZnJvbV0gLT0gYW1vdW50OwogICAgICAgIGJhbGFuY2VzW3RvXSArPSBhbW91bnQ7CiAgICB9Cn0KCmNvbnRyYWN0IFRva2VuIHsKICAgIG1hcHBpbmcoYWRkcmVzcyA9PiB1aW50MjU2KSBiYWxhbmNlczsKICAgIHVzaW5nIEJhbGFuY2VzIGZvciAqOwogICAgbWFwcGluZyhhZGRyZXNzID0+IG1hcHBpbmcoYWRkcmVzcyA9PiB1aW50MjU2KSkgYWxsb3dlZDsKCiAgICBldmVudCBUcmFuc2ZlcihhZGRyZXNzIGZyb20sIGFkZHJlc3MgdG8sIHVpbnQgYW1vdW50KTsKICAgIGV2ZW50IEFwcHJvdmFsKGFkZHJlc3Mgb3duZXIsIGFkZHJlc3Mgc3BlbmRlciwgdWludCBhbW91bnQpOwoKICAgIGZ1bmN0aW9uIHRyYW5zZmVyKGFkZHJlc3MgdG8sIHVpbnQgYW1vdW50KSBleHRlcm5hbCByZXR1cm5zIChib29sIHN1Y2Nlc3MpIHsKICAgICAgICBiYWxhbmNlcy5tb3ZlKG1zZy5zZW5kZXIsIHRvLCBhbW91bnQpOwogICAgICAgIGVtaXQgVHJhbnNmZXIobXNnLnNlbmRlciwgdG8sIGFtb3VudCk7CiAgICAgICAgcmV0dXJuIHRydWU7CgogICAgfQoKICAgIGZ1bmN0aW9uIHRyYW5zZmVyRnJvbShhZGRyZXNzIGZyb20sIGFkZHJlc3MgdG8sIHVpbnQgYW1vdW50KSBleHRlcm5hbCByZXR1cm5zIChib29sIHN1Y2Nlc3MpIHsKICAgICAgICByZXF1aXJlKGFsbG93ZWRbZnJvbV1bbXNnLnNlbmRlcl0gPj0gYW1vdW50KTsKICAgICAgICBhbGxvd2VkW2Zyb21dW21zZy5zZW5kZXJdIC09IGFtb3VudDsKICAgICAgICBiYWxhbmNlcy5tb3ZlKGZyb20sIHRvLCBhbW91bnQpOwogICAgICAgIGVtaXQgVHJhbnNmZXIoZnJvbSwgdG8sIGFtb3VudCk7CiAgICAgICAgcmV0dXJuIHRydWU7CiAgICB9CgogICAgZnVuY3Rpb24gYXBwcm92ZShhZGRyZXNzIHNwZW5kZXIsIHVpbnQgdG9rZW5zKSBleHRlcm5hbCByZXR1cm5zIChib29sIHN1Y2Nlc3MpIHsKICAgICAgICByZXF1aXJlKGFsbG93ZWRbbXNnLnNlbmRlcl1bc3BlbmRlcl0gPT0gMCwgIiIpOwogICAgICAgIGFsbG93ZWRbbXNnLnNlbmRlcl1bc3BlbmRlcl0gPSB0b2tlbnM7CiAgICAgICAgZW1pdCBBcHByb3ZhbChtc2cuc2VuZGVyLCBzcGVuZGVyLCB0b2tlbnMpOwogICAgICAgIHJldHVybiB0cnVlOwogICAgfQoKICAgIGZ1bmN0aW9uIGJhbGFuY2VPZihhZGRyZXNzIHRva2VuT3duZXIpIGV4dGVybmFsIHZpZXcgcmV0dXJucyAodWludCBiYWxhbmNlKSB7CiAgICAgICAgcmV0dXJuIGJhbGFuY2VzW3Rva2VuT3duZXJdOwogICAgfQp9)

// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.5.0 <0.9.0;

library Balances {
 function move(mapping(address => uint256) storage balances, address from, address to, uint amount) internal {
 require(balances[from] >= amount);
 require(balances[to] + amount >= balances[to]);
 balances[from] -= amount;
 balances[to] += amount;
 }
}

contract Token {
 mapping(address => uint256) balances;
 using Balances for *;
 mapping(address => mapping(address => uint256)) allowed;

 event Transfer(address from, address to, uint amount);
 event Approval(address owner, address spender, uint amount);

 function transfer(address to, uint amount) external returns (bool success) {
 balances.move(msg.sender, to, amount);
 emit Transfer(msg.sender, to, amount);
 return true;

 }

 function transferFrom(address from, address to, uint amount) external returns (bool success) {
 require(allowed[from][msg.sender] >= amount);
 allowed[from][msg.sender] -= amount;
 balances.move(from, to, amount);
 emit Transfer(from, to, amount);
 return true;
 }

 function approve(address spender, uint tokens) external returns (bool success) {
 require(allowed[msg.sender][spender] == 0, "");
 allowed[msg.sender][spender] = tokens;
 emit Approval(msg.sender, spender, tokens);
 return true;
 }

 function balanceOf(address tokenOwner) external view returns (uint balance) {
 return balances[tokenOwner];
 }
}
