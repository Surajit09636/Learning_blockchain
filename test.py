from eth_account import Account

PRIVATE_KEY = "0x821e16615e9a0928E03e14761D30cB61066a92605ed2db9cb1cd261e820242b5"
private_key = "0x821e16615e9a0928E03e14761D30cB61066a92605ed2db9cb1cd261e820242b5"  # from Ganache
derived_address = Account.from_key(private_key).address

print(derived_address)  # must match the 'from' field
