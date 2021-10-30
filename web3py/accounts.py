from web3 import Web3 

url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(url))

print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0x34437841A5ec76828949AD14243Ab79B23ccd7F9")

print(web3.fromWei(balance, "ether"))