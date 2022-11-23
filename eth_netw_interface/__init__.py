"""
TODO keep updated in accordance with evolving changes
I expect this package to basically export a single class that acts as a wrapper/interface
for any interaction I want to have with Ethereum networks.

I envision this class to wrap the functionalities like the ones offered by the web3.py package,
and that either a single instance of this class is instantiated to be able to do anything, or
potentially multiple of these instances of that is more logical.

But this class should be seen as a high level interface, a starting point for the different use
cases I have/want for Ethereum networks (the main net, or test nets)

Potentially I can, besides this main class, give access to types that represent different entities
and value objects that are used while interacting with an Ethereum network. But I am not sure if
this is the best location for that.
"""
from .eth_netw_interface import *
