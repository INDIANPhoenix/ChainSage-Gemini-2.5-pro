Title: slither/docs/src/tools/Contract-Flattening.md at master · crytic/slither

URL Source: https://github.com/crytic/slither/blob/master/docs/src/tools/Contract-Flattening.md

Markdown Content:
[Skip to content](https://github.com/crytic/slither/blob/master/docs/src/tools/Contract-Flattening.md#start-of-content)

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

39 lines (25 loc) · 1.33 KB

· [](https://github.com/crytic/slither/blob/master/CODEOWNERS#L1)

`slither-flat` produces a flattened version of the codebase.

Features
--------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Contract-Flattening.md#features)
*   Code flattening
*   Support multiple [strategies](https://github.com/crytic/slither/blob/master/docs/src/tools/Contract-Flattening.md#strategies)
*   Support circular dependency
*   Support all the compilation platforms (Truffle, embark, buidler, etherlime, ...).

Usage
-----

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Contract-Flattening.md#usage)
`slither-flat target`

*   `--contract ContractName`: flatten only one contract (standalone file)

### Strategies

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Contract-Flattening.md#strategies)
`slither-flat` contains three strategies that can be specified with the `--strategy` flag:

*   `MostDerived`: Export all the most derived contracts (every file is standalone)
*   `OneFile`: Export all the contracts in one standalone file
*   `LocalImport`: Export every contract in one separate file, and include import ".." in their preludes

Default: `MostDerived`

### Patching

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Contract-Flattening.md#patching)
`slither-flat` can transform the codebase to help some usage (eg. [Echidna](https://github.com/crytic/echidna))

*   `--convert-external`: convert `external` function to `public`. This is meant to facilitate [Echidna](https://github.com/crytic/echidna) usage.
*   `--contract name`: To flatten only a target contract
*   `--remove-assert`: Remove call to assert().

### Export option

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Contract-Flattening.md#export-option)
*   `--dir DirName`: output directory
*   `--json file.json`: export the results to a json file (`--json -` output to the standard output
*   `--zip file.zip`: export to a ZIP file
*   `--zip-type type`: ZIP compression type (default lzma))
