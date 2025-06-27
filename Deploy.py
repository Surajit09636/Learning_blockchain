
from solcx import compile_standard

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

print(compiled_sol)