from web3 import Web3 

url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(url))

print(web3.isConnected())

account_1 = "0x34437841A5ec76828949AD14243Ab79B23ccd7F9"
account_2 = "0x36aBE9aBfaF148304e8cc98C706A308B61E94FE0"

private_key = "070729e568b3b359f2d4fbffc4022845e8b32eedf66f78e2aae44e4db465ac47"

nonce = web3.eth.getTransactionCount(account_1)

tx = {
    'nonce' : nonce,
    'to' : account_2,
    'value' : web3.toWei(1,'ether'),
    'gas' : 2000000,
    'gasPrice' : web3.toWei('50','gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(web3.toHex(tx_hash))