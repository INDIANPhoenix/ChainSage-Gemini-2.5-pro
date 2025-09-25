Title: Backwards Compatibility - OpenZeppelin Docs

URL Source: https://docs.openzeppelin.com/contracts/5.x/backwards-compatibility

Markdown Content:
In backwards compatible releases, all changes should be either additions or modifications to internal implementation details. Most code should continue to compile and behave as expected. The exceptions to this rule are listed below.

### [](https://docs.openzeppelin.com/contracts/5.x/backwards-compatibility#security)Security

Infrequently a patch or minor update will remove or change an API in a breaking way, but only if the previous API is considered insecure. These breaking changes will be noted in the changelog and release notes, and published along with a security advisory.

### [](https://docs.openzeppelin.com/contracts/5.x/backwards-compatibility#draft_or_pre_final_ercs)Draft or Pre-Final ERCs

ERCs that are not Final can change in incompatible ways. For this reason, we avoid shipping implementations of ERCs before they are Final. Some exceptions are made for ERCs that have been published for a long time and seem unlikely to change. Implementations for ERCs that may have breaking changes are published in files named `draft-*.sol` to make that condition explicit. There is no backwards compatibility guarantee for content in files prefixed with `draft`.

Standards that have achieved widespread adoption with strong backwards compatibility expectations from the community may be treated as de-facto finalized and published without the `draft-` prefix, as extensive ecosystem reliance makes breaking changes highly unlikely.

### [](https://docs.openzeppelin.com/contracts/5.x/backwards-compatibility#virtual_overrides)Virtual & Overrides

Almost all functions in this library are virtual with some exceptions, but this does not mean that overrides are encouraged. There is a subset of functions that are designed to be overridden. By defining overrides outside of this subset you are potentially relying on internal implementation details. We make efforts to preserve backwards compatibility even in these cases but it is extremely difficult and easy to accidentally break. Caution is advised.

Additionally, some minor updates may result in new compilation errors of the kind "two or more base classes define function with same name and parameter types" or "need to specify overridden contract", due to what Solidity considers ambiguity in inherited functions. This should be resolved by adding an override that invokes the function via `super`.

### [](https://docs.openzeppelin.com/contracts/5.x/backwards-compatibility#structs)Structs

Struct members with an underscore prefix should be considered "private" and may break in minor versions. Struct data should only be accessed and modified through library functions.

### [](https://docs.openzeppelin.com/contracts/5.x/backwards-compatibility#errors)Errors

The specific error format and data that is included with reverts should not be assumed stable unless otherwise specified.

### [](https://docs.openzeppelin.com/contracts/5.x/backwards-compatibility#major_releases)Major Releases

Major releases should be assumed incompatible. Nevertheless, the external interfaces of contracts will remain compatible if they are standardized, or if the maintainers judge that changing them would cause significant strain on the ecosystem.

An important aspect that major releases may break is "upgrade compatibility", in particular storage layout compatibility. It will never be safe for a live contract to upgrade from one major release to another.
