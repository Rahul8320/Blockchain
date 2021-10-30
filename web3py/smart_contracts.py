import json
from eth_utils import address
from web3 import Web3, contract

url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(url))

web3.eth.defaultAccount = web3.eth.accounts[1]

abi = json.loads()
address = web3.toChecksumAddress()

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.greet().call())

tx_hash = contract.functions.setGreeting('Hello, I am Rahul!').transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print('Udated greeting: {}'.format(
    contract.functions.greet().call()
))
