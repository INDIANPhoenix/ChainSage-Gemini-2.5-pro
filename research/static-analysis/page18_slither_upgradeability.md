Title: slither/docs/src/tools/Upgradeability-Checks.md at master · crytic/slither

URL Source: https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md

Markdown Content:
`slither-check-upgradeability` helps review contracts that use the [delegatecall proxy pattern](https://blog.trailofbits.com/2018/09/05/contract-upgrade-anti-patterns/).

Checks
------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#checks)
| Num | Check | What it Detects | Impact | Proxy | Contract V2 |
| --- | --- | --- | --- | --- | --- |
| 1 | `became-constant` | [Variables that should not be constant](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#variables-that-should-not-be-constant) | High |  | X |
| 2 | `function-id-collision` | [Functions IDs collision](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#functions-ids-collisions) | High | X |  |
| 3 | `function-shadowing` | [Functions shadowing](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#functions-shadowing) | High | X |  |
| 4 | `missing-calls` | [Missing calls to init functions](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initialize-functions-are-not-called) | High |  |  |
| 5 | `missing-init-modifier` | [initializer() is not called](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initializer-is-not-called) | High |  |  |
| 6 | `multiple-calls` | [Init functions called multiple times](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initialize-functions-are-called-multiple-times) | High |  |  |
| 7 | `order-vars-contracts` | [Incorrect vars order with the v2](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#incorrect-variables-with-the-v2) | High |  | X |
| 8 | `order-vars-proxy` | [Incorrect vars order with the proxy](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#incorrect-variables-with-the-proxy) | High | X |  |
| 9 | `variables-initialized` | [State variables with an initial value](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#state-variable-initialized) | High |  |  |
| 10 | `were-constant` | [Variables that should be constant](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#variables-that-should-be-constant) | High |  | X |
| 11 | `extra-vars-proxy` | [Extra vars in the proxy](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#extra-variables-in-the-proxy) | Medium | X |  |
| 12 | `missing-variables` | [Variable missing in the v2](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#missing-variables) | Medium |  | X |
| 13 | `extra-vars-v2` | [Extra vars in the v2](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#extra-variables-in-the-v2) | Informational |  | X |
| 14 | `init-inherited` | [Initializable is not inherited](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initializable-is-not-inherited) | Informational |  |  |
| 15 | `init-missing` | [Initializable is missing](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initializable-is-missing) | Informational |  |  |
| 16 | `initialize-target` | [Initialize function that must be called](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initialize-function) | Informational |  |  |
| 17 | `initializer-missing` | [initializer() is missing](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initializer-is-missing) | Informational |  |  |

Usage
-----

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#usage)

```
slither-check-upgradeability project ContractName
```

*   `project` can be a Solidity file, or a platform (truffle/embark/..) directory

### Contract V2

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#contract-v2)
If you want to check the contract and its update, use:

*   `--new-contract-name ContractName`
*   `--new-contract-filename contract_project`

`--new-contract-filename` is not needed if the new contract is in the same codebase than the original one.

### Proxy

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#proxy)
If you want to check also the proxy, use:

*   `--proxy-name ProxyName`
*   `--proxy-filename proxy_project`

`--proxy-filename` is not needed if the proxy is in the same codebase than the targeted contract.

#### ZOS

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#zos)
If you use zos, you will have the proxy and the contract in different directories.

Likely, you will use one of the proxy from [https://github.com/zeppelinos/zos](https://github.com/zeppelinos/zos). Clone the `zos`, and install the dependencies:

```
git clone https://github.com/zeppelinos/zos
cd zos/packages/lib
npm install
rm contracts/mocks/WithConstructorImplementation.sol
```

Note: `contracts/mocks/WithConstructorImplementation.sol` must be removed as it contains a [name clash collision](https://github.com/crytic/slither/wiki#keyerror-or-nonetype-error) with `contracts/mocks/Invalid.sol`

Then from your project directory:

```
slither-check-upgradeability . ContractName --proxy-filename /path/to/zos/packages/lib/ --proxy-name UpgradeabilityProxy
```

According to your setup, you might choose another proxy name than `UpgradeabilityProxy`.

Checks Description
------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#checks-description)
Variables that should not be constant
-------------------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#variables-that-should-not-be-constant)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration)
*   Check: `became-constant`
*   Severity: `High`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description)
Detect state variables that should not be `constant̀`.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario)

contract Contract{
    uint variable1;
    uint variable2;
    uint variable3;
}

contract ContractV2{
    uint variable1;
    uint constant variable2;
    uint variable3;
}

Because `variable2` is now a `constant`, the storage location of `variable3` will be different. As a result, `ContractV2` will have a corrupted storage layout.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation)
Do not make an existing state variable `constant`.

Functions IDs collisions
------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#functions-ids-collisions)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-1)
*   Check: `function-id-collision`
*   Severity: `High`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-1)
Detect function ID collision between the contract and the proxy.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-1)

contract Contract{
    function gsf() public {
        // ...
    }
}

contract Proxy{
    function tgeo() public {
        // ...
    }
}

`Proxy.tgeo()` and `Contract.gsf()` have the same function ID (0x67e43e43). As a result, `Proxy.tgeo()` will shadow Contract.gsf()`.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-1)
Rename the function. Avoid public functions in the proxy.

Functions shadowing
-------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#functions-shadowing)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-2)
*   Check: `function-shadowing`
*   Severity: `High`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-2)
Detect function shadowing between the contract and the proxy.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-2)

contract Contract{
    function get() public {
        // ...
    }
}

contract Proxy{
    function get() public {
        // ...
    }
}

`Proxy.get` will shadow any call to `get()`. As a result `get()` is never executed in the logic contract and cannot be updated.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-2)
Rename the function. Avoid public functions in the proxy.

Initialize functions are not called
-----------------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initialize-functions-are-not-called)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-3)
*   Check: `missing-calls`
*   Severity: `High`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-3)
Detect missing calls to initialize functions.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-3)

contract Base{
    function initialize() public{
        ///
    }
}
contract Derived is Base{
    function initialize() public{
        ///
    }
}

`Derived.initialize` does not call `Base.initialize` leading the contract to not be correctly initialized.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-3)
Ensure all the initialize functions are reached by the most derived initialize function.

initializer() is not called
---------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initializer-is-not-called)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-4)
*   Check: `missing-init-modifier`
*   Severity: `High`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-4)
Detect if `Initializable.initializer()` is called.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-4)

contract Contract{
    function initialize() public{
        ///
    }
}

`initialize` should have the `initializer` modifier to prevent someone from initializing the contract multiple times.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-4)
Use `Initializable.initializer()`.

Initialize functions are called multiple times
----------------------------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initialize-functions-are-called-multiple-times)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-5)
*   Check: `multiple-calls`
*   Severity: `High`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-5)
Detect multiple calls to a initialize function.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-5)

contract Base{
    function initialize(uint) public{
        ///
    }
}
contract Derived is Base{
    function initialize(uint a, uint b) public{
        initialize(a);
    }
}

contract DerivedDerived is Derived{
    function initialize() public{
        initialize(0);
        initialize(0, 1 );
    }
}

`Base.initialize(uint)` is called two times in `DerivedDerived.initialize` execution, leading to a potential corruption.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-5)
Call only one time every initialize function.

Incorrect variables with the v2
-------------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#incorrect-variables-with-the-v2)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-6)
*   Check: `order-vars-contracts`
*   Severity: `High`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-6)
Detect variables that are different between the original contract and the updated one.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-6)

contract Contract{
    uint variable1;
}

contract ContractV2{
    address variable1;
}

`Contract` and `ContractV2` do not have the same storage layout. As a result the storage of both contracts can be corrupted.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-6)
Respect the variable order of the original contract in the updated contract.

Incorrect variables with the proxy
----------------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#incorrect-variables-with-the-proxy)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-7)
*   Check: `order-vars-proxy`
*   Severity: `High`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-7)
Detect variables that are different between the contract and the proxy.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-7)

contract Contract{
    uint variable1;
}

contract Proxy{
    address variable1;
}

`Contract` and `Proxy` do not have the same storage layout. As a result the storage of both contracts can be corrupted.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-7)
Avoid variables in the proxy. If a variable is in the proxy, ensure it has the same layout than in the contract.

State variable initialized
--------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#state-variable-initialized)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-8)
*   Check: `variables-initialized`
*   Severity: `High`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-8)
Detect state variables that are initialized.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-8)

contract Contract{
    uint variable = 10;
}

Using `Contract` will the delegatecall proxy pattern will lead `variable` to be 0 when called through the proxy.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-8)
Using initialize functions to write initial values in state variables.

Variables that should be constant
---------------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#variables-that-should-be-constant)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-9)
*   Check: `were-constant`
*   Severity: `High`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-9)
Detect state variables that should be `constant̀`.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-9)

contract Contract{
    uint variable1;
    uint constant variable2;
    uint variable3;
}

contract ContractV2{
    uint variable1;
    uint variable2;
    uint variable3;
}

Because `variable2` is not anymore a `constant`, the storage location of `variable3` will be different. As a result, `ContractV2` will have a corrupted storage layout.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-9)
Do not remove `constant` from a state variables during an update.

Extra variables in the proxy
----------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#extra-variables-in-the-proxy)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-10)
*   Check: `extra-vars-proxy`
*   Severity: `Medium`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-10)
Detect variables that are in the proxy and not in the contract.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-10)

contract Contract{
    uint variable1;
}

contract Proxy{
    uint variable1;
    uint variable2;
}

`Proxy` contains additional variables. A future update of `Contract` is likely to corrupt the proxy.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-10)
Avoid variables in the proxy. If a variable is in the proxy, ensure it has the same layout than in the contract.

Missing variables
-----------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#missing-variables)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-11)
*   Check: `missing-variables`
*   Severity: `Medium`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-11)
Detect variables that were present in the original contracts but are not in the updated one.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-11)

contract V1{
    uint variable1;
    uint variable2;
}

contract V2{
    uint variable1;
}

The new version, `V2` does not contain `variable1`. If a new variable is added in an update of `V2`, this variable will hold the latest value of `variable2` and will be corrupted.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-11)
Do not change the order of the state variables in the updated contract.

Extra variables in the v2
-------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#extra-variables-in-the-v2)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-12)
*   Check: `extra-vars-v2`
*   Severity: `Informational`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-12)
Show new variables in the updated contract.

This finding does not have an immediate security impact and is informative.

### Exploit Scenario:

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#exploit-scenario-12)

contract Contract{
    uint variable1;
}

contract Proxy{
    uint variable1;
    uint variable2;
}

`Proxy` contains additional variables. A future update of `Contract` is likely to corrupt the proxy.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-12)
Ensure that all the new variables are expected.

Initializable is not inherited
------------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initializable-is-not-inherited)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-13)
*   Check: `init-inherited`
*   Severity: `Informational`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-13)
Detect if `Initializable` is inherited.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-13)
Review manually the contract's initialization. Consider inheriting `Initializable`.

Initializable is missing
------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initializable-is-missing)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-14)
*   Check: `init-missing`
*   Severity: `Informational`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-14)
Detect if a contract `Initializable` is present.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-14)
Review manually the contract's initialization.. Consider using a `Initializable` contract to follow [standard practice](https://docs.openzeppelin.com/upgrades/2.7/writing-upgradeable).

Initialize function
-------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initialize-function)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-15)
*   Check: `initialize-target`
*   Severity: `Informational`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-15)
Show the function that must be called at deployment.

This finding does not have an immediate security impact and is informative.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-15)
Ensure that the function is called at deployment.

initializer() is missing
------------------------

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#initializer-is-missing)
### Configuration

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#configuration-16)
*   Check: `initializer-missing`
*   Severity: `Informational`

### Description

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#description-16)
Detect the lack of `Initializable.initializer()` modifier.

### Recommendation

[](https://github.com/crytic/slither/blob/master/docs/src/tools/Upgradeability-Checks.md#recommendation-16)
Review manually the contract's initialization. Consider inheriting a `Initializable.initializer()` modifier.
