I am studying an Ethereum network interact with it using Python code.

This aims to be a set of basic functionalities ordered kind of neatly as a first exploration of interacting with wallets and smart contracts on an Ethereum network, using Python.

This is a work in progress

# draft plan

## Interacting with deployed contracts
Currently any contract can be deployed, and I would like to build standardized functionalit to interact with the contract.

What I would like to prevent is needing to rewrite lots of functionality needed to interact with each new contract that is created.

1 So let's just start writing some code to interacts with the current contract.
2 Then add another contract (thus a different interface) and deploy it
3 Then write code to interact with the second contract, and abstract away as much of the re-useable functionality as possible.

## Write wrapper for using Web3 object, for common functionalities
- deploying contract
- set_gas_price_strategy

