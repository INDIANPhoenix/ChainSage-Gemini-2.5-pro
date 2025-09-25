Title: slither/docs/src/tools/README.md at master · crytic/slither

URL Source: https://github.com/crytic/slither/blob/master/docs/src/tools/README.md

Markdown Content:
[Skip to content](https://github.com/crytic/slither/blob/master/docs/src/tools/README.md#start-of-content)

Navigation Menu
---------------

*   
    *   [GitHub Copilot Write better code with AI](https://github.com/features/copilot)
    *   [GitHub Spark New Build and deploy intelligent apps](https://github.com/features/spark)
    *   [GitHub Models New Manage and compare prompts](https://github.com/features/models)
    *   [GitHub Advanced Security Find and fix vulnerabilities](https://github.com/security/advanced-security)
    *   [Actions Automate any workflow](https://github.com/features/actions)

    *   [Codespaces Instant dev environments](https://github.com/features/codespaces)
    *   [Issues Plan and track work](https://github.com/features/issues)
    *   [Code Review Manage code changes](https://github.com/features/code-review)
    *   [Discussions Collaborate outside of code](https://github.com/features/discussions)
    *   [Code Search Find more, search less](https://github.com/features/code-search)

[View all features](https://github.com/features)

*   
Explore

    *   [Learning Pathways](https://resources.github.com/learn/pathways)
    *   [Events & Webinars](https://github.com/resources/events)
    *   [Ebooks & Whitepapers](https://github.com/resources/whitepapers)
    *   [Customer Stories](https://github.com/customer-stories)
    *   [Partners](https://partner.github.com/)
    *   [Executive Insights](https://github.com/solutions/executive-insights)

*   
    *   [GitHub Sponsors Fund open source developers](https://github.com/sponsors)

    *   [The ReadME Project GitHub community articles](https://github.com/readme)

*   
    *   [Enterprise platform AI-powered developer platform](https://github.com/enterprise)

*   [Pricing](https://github.com/pricing)

Provide feedback
----------------

Saved searches
--------------

Use saved searches to filter your results more quickly
------------------------------------------------------

[Sign up](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Fblob%2Fshow&source=header-repo&source_repo=crytic%2Fslither)

*   [Notifications](https://github.com/login?return_to=%2Fcrytic%2Fslither)You must be signed in to change notification settings
*   [Fork 1.1k](https://github.com/login?return_to=%2Fcrytic%2Fslither)
*   [Star 5.9k](https://github.com/login?return_to=%2Fcrytic%2Fslither)

Files
-----

*   .github 
*   docs/src 
    *   api 
    *   detectors 
    *   printers 
    *   tools 
        *   Adding-a-new-utility.md 
        *   Code-Similarity-Detector.md 
        *   Contract-Flattening.md 
        *   Doctor.md 
        *   Documentation.md 
        *   ERC-Conformance.md 
        *   Interface.md 
        *   Mutator.md 
        *   Path-Finding-Utility.md 
        *   Property-generation.md 
        *   README.md 
        *   ReadStorage.md 
        *   Slither-format.md 
        *   Upgradeability-Checks.md 

    *   tutorials 
    *   README.md 
    *   SUMMARY.md 
    *   Usage.md 

*   examples 
*   plugin_example 
*   scripts 
*   slither 
*   tests 
*   .coderabbit.yaml 
*   .dockerignore 
*   .gitattributes 
*   .gitignore 
*   .pre-commit-hooks.yaml 
*   CITATION.cff 
*   CODEOWNERS 
*   CONTRIBUTING.md 
*   Dockerfile 
*   LICENSE 
*   Makefile 
*   README.md 
*   funding.json 
*   logo.png 
*   pyproject.toml 
*   setup.py 
*   trophies.md 

Latest commit
-------------

Mar 7, 2025

File metadata and controls
--------------------------

16 lines (15 loc) · 3.57 KB

· [](https://github.com/crytic/slither/blob/master/CODEOWNERS#L1)

Slither comes with inbuilt tools

| Name | Command-Line | What it Does |
| --- | --- | --- |
| [Code Similarity](https://github.com/crytic/slither/blob/master/docs/src/tools/Code-Similarity-Detector.md) | `slither-simil` | Detects similar Solidity functions/contracts using code similarity analysis. Useful for finding duplicated code, similar vulnerabilities, or analyzing large codebases. |
| [Contract Flattening](https://github.com/crytic/slither/blob/master/docs/src/tools/Contract-Flattening.md) | `slither-flat` | Flattens a Solidity codebase by inlining all imports into a single file. Useful for contract verification on Etherscan or debugging. |
| [Documentation](https://github.com/crytic/slither/blob/master/docs/src/tools/Documentation.md) | `slither-doc` | Automatically generates documentation for Solidity contracts, including inheritance information, functions, modifiers, and more. |
| [Doctor](https://github.com/crytic/slither/blob/master/docs/src/tools/Doctor.md) | `slither-doctor` | Helps diagnose and fix common issues in your environment that might prevent Slither from working correctly. |
| [ERC Conformance](https://github.com/crytic/slither/blob/master/docs/src/tools/ERC-Conformance.md) | `slither-check-erc` | Validates whether a contract correctly implements various ERC standards (ERC20, ERC721, etc.) by checking required functions and their signatures. |
| [Interface](https://github.com/crytic/slither/blob/master/docs/src/tools/Interface.md) | `slither-interface` | Generates Solidity interfaces from contract implementations, useful for creating minimal interfaces for contract interactions. |
| [Mutator](https://github.com/crytic/slither/blob/master/docs/src/tools/Mutator.md) | `slither-mutate` | Performs mutation testing on Solidity contracts by automatically generating variants with small modifications to test suite effectiveness. |
| [Path Finding](https://github.com/crytic/slither/blob/master/docs/src/tools/Path-Finding-Utility.md) | `slither-prop` | Analyzes call paths between functions in smart contracts to understand control and data flow. |
| [Property Generation](https://github.com/crytic/slither/blob/master/docs/src/tools/Property-generation.md) | `slither-prop` | Automatically generates security properties and unit tests for smart contracts based on their behavior. |
| [Read Storage](https://github.com/crytic/slither/blob/master/docs/src/tools/ReadStorage.md) | `slither-read-storage` | Reads contract storage values directly from the blockchain, helping debug deployed contracts. |
| [Format](https://github.com/crytic/slither/blob/master/docs/src/tools/Slither-format.md) | `slither-format` | Automatically patch bugs. |
| [Upgradeability Checks](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md) | `slither-check-upgradeability` | Analyzes upgradeable contracts for common issues and vulnerabilities in proxy patterns. |
