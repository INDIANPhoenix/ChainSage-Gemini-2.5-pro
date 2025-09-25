Title: Language Influences — Solidity 0.8.31 documentation

URL Source: https://docs.soliditylang.org/en/latest/language-influences.html

Markdown Content:
Language Influences — Solidity 0.8.31 documentation

===============

[![Image 1: Solidity logo](https://docs.soliditylang.org/en/latest/_static/img/logo.svg)](https://soliditylang.org/)[{skip to content}](https://docs.soliditylang.org/en/latest/language-influences.html#content)[Blog](https://soliditylang.org/blog)[Documentation](https://docs.soliditylang.org/)[Use cases](https://soliditylang.org/use-cases)[Contribute](https://docs.soliditylang.org/en/latest/contributing.html)[About](https://soliditylang.org/about)[Forum](https://forum.soliditylang.org/)

![Image 2: Color mode toggle icon](https://docs.soliditylang.org/en/latest/_static/img/moon.svg)![Image 3: Toggle menu](https://docs.soliditylang.org/en/latest/_static/img/hamburger-light.svg)

 0.8.31 

Basics

*   [Introduction to Smart Contracts](https://docs.soliditylang.org/en/latest/introduction-to-smart-contracts.html)
*   [Solidity by Example](https://docs.soliditylang.org/en/latest/solidity-by-example.html)
*   [Installing the Solidity Compiler](https://docs.soliditylang.org/en/latest/installing-solidity.html)

Language Description

*   [Layout of a Solidity Source File](https://docs.soliditylang.org/en/latest/layout-of-source-files.html)
*   [Structure of a Contract](https://docs.soliditylang.org/en/latest/structure-of-a-contract.html)
*   [Types](https://docs.soliditylang.org/en/latest/types.html)
*   [Units and Globally Available Variables](https://docs.soliditylang.org/en/latest/units-and-global-variables.html)
*   [Expressions and Control Structures](https://docs.soliditylang.org/en/latest/control-structures.html)
*   [Contracts](https://docs.soliditylang.org/en/latest/contracts.html)
*   [Inline Assembly](https://docs.soliditylang.org/en/latest/assembly.html)
*   [Cheatsheet](https://docs.soliditylang.org/en/latest/cheatsheet.html)
*   [Language Grammar](https://docs.soliditylang.org/en/latest/grammar.html)

Compiler

*   [Using the Compiler](https://docs.soliditylang.org/en/latest/using-the-compiler.html)
*   [Analysing the Compiler Output](https://docs.soliditylang.org/en/latest/analysing-compilation-output.html)
*   [Solidity IR-based Codegen Changes](https://docs.soliditylang.org/en/latest/ir-breaking-changes.html)

Internals

*   [Layout of State Variables in Storage and Transient Storage](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html)
*   [Layout in Memory](https://docs.soliditylang.org/en/latest/internals/layout_in_memory.html)
*   [Layout of Call Data](https://docs.soliditylang.org/en/latest/internals/layout_in_calldata.html)
*   [Cleaning Up Variables](https://docs.soliditylang.org/en/latest/internals/variable_cleanup.html)
*   [Source Mappings](https://docs.soliditylang.org/en/latest/internals/source_mappings.html)
*   [The Optimizer](https://docs.soliditylang.org/en/latest/internals/optimizer.html)
*   [Contract Metadata](https://docs.soliditylang.org/en/latest/metadata.html)
*   [Contract ABI Specification](https://docs.soliditylang.org/en/latest/abi-spec.html)

Advisory content

*   [Security Considerations](https://docs.soliditylang.org/en/latest/security-considerations.html)
*   [List of Known Bugs](https://docs.soliditylang.org/en/latest/bugs.html)
*   [Solidity v0.5.0 Breaking Changes](https://docs.soliditylang.org/en/latest/050-breaking-changes.html)
*   [Solidity v0.6.0 Breaking Changes](https://docs.soliditylang.org/en/latest/060-breaking-changes.html)
*   [Solidity v0.7.0 Breaking Changes](https://docs.soliditylang.org/en/latest/070-breaking-changes.html)
*   [Solidity v0.8.0 Breaking Changes](https://docs.soliditylang.org/en/latest/080-breaking-changes.html)

Additional Material

*   [NatSpec Format](https://docs.soliditylang.org/en/latest/natspec-format.html)
*   [SMTChecker and Formal Verification](https://docs.soliditylang.org/en/latest/smtchecker.html)
*   [Yul](https://docs.soliditylang.org/en/latest/yul.html)
*   [Import Path Resolution](https://docs.soliditylang.org/en/latest/path-resolution.html)

Resources

*   [Style Guide](https://docs.soliditylang.org/en/latest/style-guide.html)
*   [Common Patterns](https://docs.soliditylang.org/en/latest/common-patterns.html)
*   [Resources](https://docs.soliditylang.org/en/latest/resources.html)
*   [Contributing](https://docs.soliditylang.org/en/latest/contributing.html)
*   [Language Influences](https://docs.soliditylang.org/en/latest/language-influences.html#)
*   [Solidity Brand Guide](https://docs.soliditylang.org/en/latest/brand-guide.html)

*   [Keyword Index](https://docs.soliditylang.org/en/latest/genindex.html)

*   [](https://docs.soliditylang.org/en/latest/index.html)
*   Language Influences
*   [Edit on GitHub](https://github.com/ethereum/solidity/blob/develop/docs/language-influences.rst)

* * *

Language Influences[](https://docs.soliditylang.org/en/latest/language-influences.html#language-influences "Link to this heading")
===================================================================================================================================

Solidity is a [curly-bracket language](https://en.wikipedia.org/wiki/List_of_programming_languages_by_type#Curly_bracket_languages) that has been influenced and inspired by several well-known programming languages.

Solidity is most profoundly influenced by C++, but also borrowed concepts from languages like Python, JavaScript, and others.

The influence from C++ can be seen in the syntax for variable declarations, for loops, the concept of overloading functions, implicit and explicit type conversions and many other details.

In the early days of the language, Solidity used to be partly influenced by JavaScript. This was due to function-level scoping of variables and the use of the keyword `var`. The JavaScript influence was reduced starting from version 0.4.0. Now, the main remaining similarity to JavaScript is that functions are defined using the keyword `function`. Solidity also supports import syntax and semantics that are similar to those available in JavaScript. Besides those points, Solidity looks like most other curly-bracket languages and has no major JavaScript influence anymore.

Another influence to Solidity was Python. Solidity’s modifiers were added trying to model Python’s decorators with a much more restricted functionality. Furthermore, multiple inheritance, C3 linearization, and the `super` keyword are taken from Python as well as the general assignment and copy semantics of value and reference types.

[Previous](https://docs.soliditylang.org/en/latest/contributing.html "Contributing")[Next](https://docs.soliditylang.org/en/latest/brand-guide.html "Solidity Brand Guide")

* * *

© Copyright 2016-2025, The Solidity Authors.

Customized with ❤️ by the [ethereum.org](https://ethereum.org/) team.

[Credits and attribution](https://docs.soliditylang.org/en/latest/credits-and-attribution.html).
