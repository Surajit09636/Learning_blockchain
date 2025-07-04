import json
from solcx import compile_standard
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()

with open("./MyContract.sol", "r") as f:
    contract_source_code = f.read()
    
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"MyContract.sol": {"content": contract_source_code}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": [
                        "abi", "metadata", "evm.bytecode", "evm.sourceMap"
                    ]
                }
            }
        }
    },
    solc_version="0.8.0"
)

# with open("compiled_contract.json", "w") as f:
#     json.dump(compiled_sol, f)
    
# Getting bytecode
bytecode = compiled_sol["contracts"]["MyContract.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# Getting ABI
abi = compiled_sol["contracts"]["MyContract.sol"]["SimpleStorage"]["abi"]

# for connecting to gannache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_ID = 1337
My_address = "0xbBaA1cCFAD466BfD0F94209E5C402277E9171F0d"
private_key = os.getenv("PRIVATE_KEY")

# Create the contract in python 
MyContract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Get the latest transaction
nonce = w3.eth.get_transaction_count(My_address)
print(nonce)

# Build a transaction
# Sign a transaction
# send a transaction
transaction = MyContract.constructor().build_transaction({
    "chainId": chain_ID,
    "from": My_address,
    "nonce": nonce
})
signed_tnx = w3.eth.account.sign_transaction(transaction, private_key = private_key)

tx_hash = w3.eth.send_raw_transaction(signed_tnx.rawTransaction)
tx_reciept = w3.eth.wait_for_transaction_receipt(tx_hash)

# working with contract
# Contract ABI
#Contract Address
my_contract = w3.eth.contract(address=tx_reciept.contractAddress, abi=abi)
print(my_contract.functions.retrive().call())

store_transaction = my_contract.functions.store(15).build_transaction(
    {"chainId": chain_ID, "from": My_address, "nonce": nonce + 1}
)

signed_store_transaction = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)

send_store_tnx = w3.eth.send_raw_transaction(signed_store_transaction.rawTransaction)
tx_reciept = w3.eth.wait_for_transaction_receipt(send_store_tnx)