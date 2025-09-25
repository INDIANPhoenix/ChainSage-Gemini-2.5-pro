Title: How to set up on-chain governance - OpenZeppelin Docs

URL Source: https://docs.openzeppelin.com/contracts/5.x/governance

Markdown Content:
In this guide we will learn how OpenZeppelin’s Governor contract works, how to set it up, and how to use it to create proposals, vote for them, and execute them, using tools provided by Ethers.js and Tally.

[](https://docs.openzeppelin.com/contracts/5.x/governance#introduction)Introduction
-----------------------------------------------------------------------------------

Decentralized protocols are in constant evolution from the moment they are publicly released. Often, the initial team retains control of this evolution in the first stages, but eventually delegates it to a community of stakeholders. The process by which this community makes decisions is called on-chain governance, and it has become a central component of decentralized protocols, fueling varied decisions such as parameter tweaking, smart contract upgrades, integrations with other protocols, treasury management, grants, etc.

This governance protocol is generally implemented in a special-purpose contract called “Governor”. The GovernorAlpha and GovernorBravo contracts designed by Compound have been very successful and popular so far, with the downside that projects with different requirements have had to fork the code to customize it for their needs, which can pose a high risk of introducing security issues. For OpenZeppelin Contracts, we set out to build a modular system of Governor contracts so that forking is not needed, and different requirements can be accommodated by writing small modules using Solidity inheritance. You will find the most common requirements out of the box in OpenZeppelin Contracts, but writing additional ones is simple, and we will be adding new features as requested by the community in future releases. Additionally, the design of OpenZeppelin Governor requires minimal use of storage and results in more gas efficient operation.

[](https://docs.openzeppelin.com/contracts/5.x/governance#compatibility)Compatibility
-------------------------------------------------------------------------------------

OpenZeppelin’s Governor system was designed with a concern for compatibility with existing systems that were based on Compound’s GovernorAlpha and GovernorBravo. Because of this, you will find that many modules are presented in two variants, one of which is built for compatibility with those systems.

### [](https://docs.openzeppelin.com/contracts/5.x/governance#erc20votes_erc20votescomp)ERC20Votes & ERC20VotesComp

The ERC-20 extension to keep track of votes and vote delegation is one such case. The shorter one is the more generic version because it can support token supplies greater than 2^96, while the “Comp” variant is limited in that regard, but exactly fits the interface of the COMP token that is used by GovernorAlpha and Bravo. Both contract variants share the same events, so they are fully compatible when looking at events only.

### [](https://docs.openzeppelin.com/contracts/5.x/governance#governor_governorstorage)Governor & GovernorStorage

An OpenZeppelin Governor contract is not interface-compatible with Compound’s GovernorAlpha or Bravo. Even though events are fully compatible, proposal lifecycle functions (creation, execution, etc.) have different signatures that are meant to optimize storage use. Other functions from GovernorAlpha and Bravo are likewise not available. It’s possible to opt in some Bravo-like behavior by inheriting from the GovernorStorage module. This module provides proposal enumerability and alternate versions of the `queue`, `execute` and `cancel` function that only take the proposal id. This module reduces the calldata needed by some operations in exchange for an increased storage footprint. This might be a good trade-off for some L2 chains. It also provides primitives for indexer-free frontends.

Note that even with the use of this module, one important difference with Compound’s GovernorBravo is the way that `proposalId`s are calculated. Governor uses the hash of the proposal parameters with the purpose of keeping its data off-chain by event indexing, while the original Bravo implementation uses sequential `proposalId`s.

### [](https://docs.openzeppelin.com/contracts/5.x/governance#governortimelockcontrol_governortimelockcompound)GovernorTimelockControl & GovernorTimelockCompound

When using a timelock with your Governor contract, you can use either OpenZeppelin’s TimelockController or Compound’s Timelock. Based on the choice of timelock, you should choose the corresponding Governor module: GovernorTimelockControl or GovernorTimelockCompound respectively. This allows you to migrate an existing GovernorAlpha instance to an OpenZeppelin-based Governor without changing the timelock in use.

### [](https://docs.openzeppelin.com/contracts/5.x/governance#tally)Tally

[Tally](https://www.tally.xyz/) is a full-fledged application for user owned on-chain governance. It comprises a voting dashboard, proposal creation wizard, real time research and analysis, and educational content.

For all of these options, the Governor will be compatible with Tally: users will be able to create proposals, see voting periods and delays following [IERC6372](https://docs.openzeppelin.com/contracts/5.x/api/interfaces#IERC6372), visualize voting power and advocates, navigate proposals, and cast votes. For proposal creation in particular, projects can also use [Defender Transaction Proposals](https://docs.openzeppelin.com/defender/module/actions#transaction-proposals-reference) as an alternative interface.

In the rest of this guide, we will focus on a fresh deploy of the vanilla OpenZeppelin Governor features without concern for compatibility with GovernorAlpha or Bravo.

[](https://docs.openzeppelin.com/contracts/5.x/governance#setup)Setup
---------------------------------------------------------------------

### [](https://docs.openzeppelin.com/contracts/5.x/governance#token)Token

The voting power of each account in our governance setup will be determined by an ERC-20 token. The token has to implement the ERC20Votes extension. This extension will keep track of historical balances so that voting power is retrieved from past snapshots rather than current balance, which is an important protection that prevents double voting.

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {ERC20Permit} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";
import {ERC20Votes} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import {Nonces} from "@openzeppelin/contracts/utils/Nonces.sol";

contract MyToken is ERC20, ERC20Permit, ERC20Votes {
    constructor() ERC20("MyToken", "MTK") ERC20Permit("MyToken") {}

    // The functions below are overrides required by Solidity.

    function _update(address from, address to, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._update(from, to, amount);
    }

    function nonces(address owner) public view virtual override(ERC20Permit, Nonces) returns (uint256) {
        return super.nonces(owner);
    }
}
```

If your project already has a live token that does not include ERC20Votes and is not upgradeable, you can wrap it in a governance token by using ERC20Wrapper. This will allow token holders to participate in governance by wrapping their tokens 1-to-1.

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {IERC20, ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {ERC20Permit} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";
import {ERC20Votes} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import {ERC20Wrapper} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Wrapper.sol";
import {Nonces} from "@openzeppelin/contracts/utils/Nonces.sol";

contract MyTokenWrapped is ERC20, ERC20Permit, ERC20Votes, ERC20Wrapper {
    constructor(
        IERC20 wrappedToken
    ) ERC20("MyTokenWrapped", "MTK") ERC20Permit("MyTokenWrapped") ERC20Wrapper(wrappedToken) {}

    // The functions below are overrides required by Solidity.

    function decimals() public view override(ERC20, ERC20Wrapper) returns (uint8) {
        return super.decimals();
    }

    function _update(address from, address to, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._update(from, to, amount);
    }

    function nonces(address owner) public view virtual override(ERC20Permit, Nonces) returns (uint256) {
        return super.nonces(owner);
    }
}
```

The only other source of voting power available in OpenZeppelin Contracts currently is [`ERC721Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#ERC721Votes). ERC-721 tokens that don’t provide this functionality can be wrapped into a voting tokens using a combination of [`ERC721Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#ERC721Votes) and [`ERC721Wrapper`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#ERC721Wrapper).

The internal clock used by the token to store voting balances will dictate the operating mode of the Governor contract attached to it. By default, block numbers are used. Since v4.9, developers can override the [IERC6372](https://docs.openzeppelin.com/contracts/5.x/api/interfaces#IERC6372) clock to use timestamps instead of block numbers.

### [](https://docs.openzeppelin.com/contracts/5.x/governance#governor)Governor

Initially, we will build a Governor without a timelock. The core logic is given by the Governor contract, but we still need to choose: 1) how voting power is determined, 2) how many votes are needed for quorum, 3) what options people have when casting a vote and how those votes are counted, and 4) what type of token should be used to vote. Each of these aspects is customizable by writing your own module, or more easily choosing one from OpenZeppelin Contracts.

For 1) we will use the GovernorVotes module, which hooks to an IVotes instance to determine the voting power of an account based on the token balance they hold when a proposal becomes active. This module requires as a constructor parameter the address of the token. This module also discovers the clock mode (ERC-6372) used by the token and applies it to the Governor.

For 2) we will use GovernorVotesQuorumFraction which works together with ERC20Votes to define quorum as a percentage of the total supply at the block a proposal’s voting power is retrieved. This requires a constructor parameter to set the percentage. Most Governors nowadays use 4%, so we will initialize the module with parameter 4 (this indicates the percentage, resulting in 4%).

For 3) we will use GovernorCountingSimple, a module that offers 3 options to voters: For, Against, and Abstain, and where only For and Abstain votes are counted towards quorum.

Besides these modules, Governor itself has some parameters we must set.

votingDelay: How long after a proposal is created should voting power be fixed. A large voting delay gives users time to unstake tokens if necessary.

votingPeriod: How long does a proposal remain open to votes.

These parameters are specified in the unit defined in the token’s clock. Assuming the token uses block numbers, and assuming block time of around 12 seconds, we will have set votingDelay = 1 day = 7200 blocks, and votingPeriod = 1 week = 50400 blocks.

We can optionally set a proposal threshold as well. This restricts proposal creation to accounts that have enough voting power.

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import {Governor} from "@openzeppelin/contracts/governance/Governor.sol";
import {GovernorCountingSimple} from "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";
import {GovernorVotes} from "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";
import {GovernorVotesQuorumFraction} from "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";
import {GovernorTimelockControl} from "@openzeppelin/contracts/governance/extensions/GovernorTimelockControl.sol";
import {TimelockController} from "@openzeppelin/contracts/governance/TimelockController.sol";
import {IVotes} from "@openzeppelin/contracts/governance/utils/IVotes.sol";

contract MyGovernor is
    Governor,
    GovernorCountingSimple,
    GovernorVotes,
    GovernorVotesQuorumFraction,
    GovernorTimelockControl
{
    constructor(
        IVotes _token,
        TimelockController _timelock
    ) Governor("MyGovernor") GovernorVotes(_token) GovernorVotesQuorumFraction(4) GovernorTimelockControl(_timelock) {}

    function votingDelay() public pure override returns (uint256) {
        return 7200; // 1 day
    }

    function votingPeriod() public pure override returns (uint256) {
        return 50400; // 1 week
    }

    function proposalThreshold() public pure override returns (uint256) {
        return 0;
    }

    // The functions below are overrides required by Solidity.

    function state(uint256 proposalId) public view override(Governor, GovernorTimelockControl) returns (ProposalState) {
        return super.state(proposalId);
    }

    function proposalNeedsQueuing(
        uint256 proposalId
    ) public view virtual override(Governor, GovernorTimelockControl) returns (bool) {
        return super.proposalNeedsQueuing(proposalId);
    }

    function _queueOperations(
        uint256 proposalId,
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) internal override(Governor, GovernorTimelockControl) returns (uint48) {
        return super._queueOperations(proposalId, targets, values, calldatas, descriptionHash);
    }

    function _executeOperations(
        uint256 proposalId,
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) internal override(Governor, GovernorTimelockControl) {
        super._executeOperations(proposalId, targets, values, calldatas, descriptionHash);
    }

    function _cancel(
        address[] memory targets,
        uint256[] memory values,
        bytes[] memory calldatas,
        bytes32 descriptionHash
    ) internal override(Governor, GovernorTimelockControl) returns (uint256) {
        return super._cancel(targets, values, calldatas, descriptionHash);
    }

    function _executor() internal view override(Governor, GovernorTimelockControl) returns (address) {
        return super._executor();
    }
}
```

### [](https://docs.openzeppelin.com/contracts/5.x/governance#timelock)Timelock

It is good practice to add a timelock to governance decisions. This allows users to exit the system if they disagree with a decision before it is executed. We will use OpenZeppelin’s TimelockController in combination with the GovernorTimelockControl module.

When using a timelock, it is the timelock that will execute proposals and thus the timelock that should hold any funds, ownership, and access control roles. Before version 4.5 there was no way to recover funds in the Governor contract when using a timelock! Before version 4.3, when using the Compound Timelock, ETH in the timelock was not easily accessible.

TimelockController uses an AccessControl setup that we need to understand in order to set up roles.

*   The Proposer role is in charge of queueing operations: this is the role the Governor instance should be granted, and it should likely be the only proposer in the system.

*   The Executor role is in charge of executing already available operations: we can assign this role to the special zero address to allow anyone to execute (if operations can be particularly time sensitive, the Governor should be made Executor instead).

*   Lastly, there is the Admin role, which can grant and revoke the two previous roles: this is a very sensitive role that will be granted automatically to the timelock itself, and optionally to a second account, which can be used for ease of setup but should promptly renounce the role.

[](https://docs.openzeppelin.com/contracts/5.x/governance#proposal_lifecycle)Proposal Lifecycle
-----------------------------------------------------------------------------------------------

Let’s walk through how to create and execute a proposal on our newly deployed Governor.

A proposal is a sequence of actions that the Governor contract will perform if it passes. Each action consists of a target address, calldata encoding a function call, and an amount of ETH to include. Additionally, a proposal includes a human-readable description.

### [](https://docs.openzeppelin.com/contracts/5.x/governance#create_a_proposal)Create a Proposal

Let’s say we want to create a proposal to give a team a grant, in the form of ERC-20 tokens from the governance treasury. This proposal will consist of a single action where the target is the ERC-20 token, calldata is the encoded function call `transfer(<team wallet>, <grant amount>)`, and with 0 ETH attached.

Generally a proposal will be created with the help of an interface such as Tally or [Defender Proposals](https://docs.openzeppelin.com/defender/module/actions#transaction-proposals-reference). Here we will show how to create the proposal using Ethers.js.

First we get all the parameters necessary for the proposal action.

```
const tokenAddress = ...;
const token = await ethers.getContractAt(‘ERC20’, tokenAddress);

const teamAddress = ...;
const grantAmount = ...;
const transferCalldata = token.interface.encodeFunctionData(‘transfer’, [teamAddress, grantAmount]);
```

Now we are ready to call the propose function of the Governor. Note that we don’t pass in one array of actions, but instead three arrays corresponding to the list of targets, the list of values, and the list of calldatas. In this case it’s a single action, so it’s simple:

```
await governor.propose(
  [tokenAddress],
  [0],
  [transferCalldata],
  “Proposal #1: Give grant to team”,
);
```

This will create a new proposal, with a proposal id that is obtained by hashing together the proposal data, and which will also be found in an event in the logs of the transaction.

### [](https://docs.openzeppelin.com/contracts/5.x/governance#cast_a_vote)Cast a Vote

Once a proposal is active, delegates can cast their vote. Note that it is delegates who carry voting power: if a token holder wants to participate, they can set a trusted representative as their delegate, or they can become a delegate themselves by self-delegating their voting power.

Votes are cast by interacting with the Governor contract through the `castVote` family of functions. Voters would generally invoke this from a governance UI such as Tally.

![Image 1: Voting in Tally](https://docs.openzeppelin.com/contracts/5.x/_images/tally-vote.png)

### [](https://docs.openzeppelin.com/contracts/5.x/governance#execute_the_proposal)Execute the Proposal

Once the voting period is over, if quorum was reached (enough voting power participated) and the majority voted in favor, the proposal is considered successful and can proceed to be executed. Once a proposal passes, it can be queued and executed from the same place you voted.

![Image 2: Administration Panel in Tally](https://docs.openzeppelin.com/contracts/5.x/_images/tally-exec.png)

We will see now how to do this manually using Ethers.js.

If a timelock was set up, the first step to execution is queueing. You will notice that both the queue and execute functions require passing in the entire proposal parameters, as opposed to just the proposal id. This is necessary because this data is not stored on chain, as a measure to save gas. Note that these parameters can always be found in the events emitted by the contract. The only parameter that is not sent in its entirety is the description, since this is only needed in its hashed form to compute the proposal id.

To queue, we call the queue function:

```
const descriptionHash = ethers.utils.id(“Proposal #1: Give grant to team”);

await governor.queue(
  [tokenAddress],
  [0],
  [transferCalldata],
  descriptionHash,
);
```

This will cause the Governor to interact with the timelock contract and queue the actions for execution after the required delay.

After enough time has passed (according to the timelock parameters), the proposal can be executed. If there was no timelock to begin with, this step can be ran immediately after the proposal succeeds.

```
await governor.execute(
  [tokenAddress],
  [0],
  [transferCalldata],
  descriptionHash,
);
```

Executing the proposal will transfer the ERC-20 tokens to the chosen recipient. To wrap up: we set up a system where a treasury is controlled by the collective decision of the token holders of a project, and all actions are executed via proposals enforced by on-chain votes.

[](https://docs.openzeppelin.com/contracts/5.x/governance#timestamp_based_governance)Timestamp based governance
---------------------------------------------------------------------------------------------------------------

### [](https://docs.openzeppelin.com/contracts/5.x/governance#motivation)Motivation

It is sometimes difficult to deal with durations expressed in number of blocks because of inconsistent or unpredictable time between blocks. This is particularly true of some L2 networks where blocks are produced based on blockchain usage. Using number of blocks can also lead to the governance rules being affected by network upgrades that modify the expected time between blocks.

The difficulty of replacing block numbers with timestamps is that the Governor and the token must both use the same format when querying past votes. If a token is designed around block numbers, it is not possible for a Governor to reliably do timestamp based lookups.

Therefore, designing a timestamp based voting system starts with the token.

### [](https://docs.openzeppelin.com/contracts/5.x/governance#token_2)Token

Since v4.9, all voting contracts (including [`ERC20Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC20#ERC20Votes) and [`ERC721Votes`](https://docs.openzeppelin.com/contracts/5.x/api/token/ERC721#ERC721Votes)) rely on [IERC6372](https://docs.openzeppelin.com/contracts/5.x/api/interfaces#IERC6372) for clock management. In order to change from operating with block numbers to operating with timestamps, all that is required is to override the `clock()` and `CLOCK_MODE()` functions.

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import {ERC20Permit} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Permit.sol";
import {ERC20Votes} from "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol";
import {Nonces} from "@openzeppelin/contracts/utils/Nonces.sol";

contract MyTokenTimestampBased is ERC20, ERC20Permit, ERC20Votes {
    constructor() ERC20("MyTokenTimestampBased", "MTK") ERC20Permit("MyTokenTimestampBased") {}

    // Overrides IERC6372 functions to make the token & governor timestamp-based

    function clock() public view override returns (uint48) {
        return uint48(block.timestamp);
    }

    // solhint-disable-next-line func-name-mixedcase
    function CLOCK_MODE() public pure override returns (string memory) {
        return "mode=timestamp";
    }

    // The functions below are overrides required by Solidity.

    function _update(address from, address to, uint256 amount) internal override(ERC20, ERC20Votes) {
        super._update(from, to, amount);
    }

    function nonces(address owner) public view virtual override(ERC20Permit, Nonces) returns (uint256) {
        return super.nonces(owner);
    }
}
```

### [](https://docs.openzeppelin.com/contracts/5.x/governance#governor_2)Governor

The Governor will automatically detect the clock mode used by the token and adapt to it. There is no need to override anything in the Governor contract. However, the clock mode does affect how some values are interpreted. It is therefore necessary to set the `votingDelay()` and `votingPeriod()` accordingly.

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import {Governor} from "@openzeppelin/contracts/governance/Governor.sol";
import {GovernorCountingSimple} from "@openzeppelin/contracts/governance/compatibility/GovernorCountingSimple.sol";
import {GovernorVotes} from "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";
import {GovernorVotesQuorumFraction} from "@openzeppelin/contracts/governance/extensions/GovernorVotesQuorumFraction.sol";
import {GovernorTimelockControl} from "@openzeppelin/contracts/governance/extensions/GovernorTimelockControl.sol";
import {TimelockController} from "@openzeppelin/contracts/governance/TimelockController.sol";
import {IVotes} from "@openzeppelin/contracts/governance/utils/IVotes.sol";

contract MyGovernor is Governor, GovernorCountingSimple, GovernorVotes, GovernorVotesQuorumFraction, GovernorTimelockControl {
    constructor(IVotes _token, TimelockController _timelock)
        Governor("MyGovernor")
        GovernorVotes(_token)
        GovernorVotesQuorumFraction(4)
        GovernorTimelockControl(_timelock)
    {}

    function votingDelay() public pure virtual override returns (uint256) {
        return 1 days;
    }

    function votingPeriod() public pure virtual override returns (uint256) {
        return 1 weeks;
    }

    function proposalThreshold() public pure virtual override returns (uint256) {
        return 0;
    }

    // ...
}
```

### [](https://docs.openzeppelin.com/contracts/5.x/governance#disclaimer)Disclaimer

Timestamp based voting is a recent feature that was formalized in ERC-6372 and ERC-5805, and introduced in v4.9. At the time this feature is released, some governance tooling may not support it yet. Users can expect invalid reporting of deadlines & durations if the tool is not able to interpret the ERC6372 clock. This invalid reporting by offchain tools does not affect the onchain security and functionality of the governance contract.

Governors with timestamp support (v4.9 and above) are compatible with old tokens (before v4.9) and will operate in "block number" mode (which is the mode all old tokens operate on). On the other hand, old Governor instances (before v4.9) are not compatible with new tokens operating using timestamps. If you update your token code to use timestamps, make sure to also update your Governor code.
