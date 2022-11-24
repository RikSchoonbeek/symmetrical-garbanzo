I am studying the Ethereum network interact with it using Python code.

This aims to be a set of basic functionalities ordered kind of neatly as a first exploration of interacting with wallets and smart contracts on an Ethereum network, using Python. Examples of such interactions are:
- deploying of contracts
- sending transactions to public functions on deployed contracts
- sending transactions between accounts on the network

The current plan is to have two components:
1 Ethereum smart contract management
2 Interface for interacting with Ethereumnet works (main and test)

# Components explained
## 1 Ethereum smart contract management
- Storage of smart contract related data:
  - contract solidity files
  - compiled contract abi and bytecode
- This component will provide use cases for other components to use:
  - compile a contract's solidity into the data we need to interact with the Ethereum network
  - retrieve a compiled contract's abi and bytecode

# To do (definitive)

## Interacting with deployed contracts
Currently any contract can be deployed, and I would like to build standardized functionalit to interact with the contract.

What I would like to prevent is needing to rewrite lots of functionality needed to interact with each new contract that is created. But I expect that each non standardized contract will need it's own use case handling function as each (non standard) contract has a unique interface.

Let's see if I can
- create one or two use cases for non standard contracts
- create one use case for an ERC20 and an ERC721 token, which are both standardized contracts.

1 So let's just start writing some code to interacts with the current contract.
2 Then add another contract (thus a different interface) and deploy it
3 Then write code to interact with the second contract, and abstract away as much of the re-useable functionality as possible.

4 then have contracts for an ERC20 and ERC721 token
5 then write a use case for each, and make sure these use cases can work with any ERC20 and ERC721 token respectively

- Probably switch to another form of storage? Maybe ask what the requirements are of my storage.
  At least make the storage solution a detail using the repository pattern.

# To do (potential)

## For each deployed contract have the address, abi, bytecode and solidity code in persistent storage
Reason: what happens if the solidity is changed, recompiled, overwriting the abi and bytecode. Therefore each deployment of a contract should be seen as a separate entity, potentially unique, and therefore storing the solidity code, bytecode and abi. This should be enough to know what the contract does and how to work with it, to understand it's functionality and interface.
- it could also be usefull to have types available that can be used to send data to and work with data that is returned from the contract, see an example of this in 
