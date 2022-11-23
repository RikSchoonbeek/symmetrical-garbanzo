I am studying an Ethereum network interact with it using Python code.

This aims to be a set of basic functionalities ordered kind of neatly as a first exploration of interacting with wallets and smart contracts on an Ethereum network, using Python.

This is a work in progress

# How to use
A `.env` file is required in the root of the project, containing private data to be set as environment variables. This is asked to contain a private_key, so be sure that you know how to keep this private.

## Adding and compiling contracts
Solidity contracts can be added to the contracts directory. The name of the contract file, without extension, will be used to interact with it later from the code.

The contracts can then be compiled by using the functionality within `compile_use_cases.py` with the result of the compilation being saved to a `<contract name>.json` file within `contracts/compiled/`.

## Deploying a contract
Functionality for this is in the `main_use_cases.py` file, and is currently called from `test_use_case_calls.py`.


# draft plan

## Interacting with deployed contracts
Currently any contract can be deployed, and I would like to build standardized functionalit to interact with the contract.

What I would like to prevent is needing to rewrite lots of functionality needed to interact with each new contract that is created.

1 So let's just start writing some code to interacts with the current contract.
2 Then add another contract (thus a different interface) and deploy it
3 Then write code to interact with the second contract, and abstract away as much of the re-useable functionality as possible.