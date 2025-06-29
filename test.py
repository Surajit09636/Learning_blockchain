from eth_account import Account

PRIVATE_KEY = "0x4b8c00cC1988131e23c81df9B0D058F31CdC3DdE821c417b26b4a934e0cdaf03"
private_key = "0x4b8c00cC1988131e23c81df9B0D058F31CdC3DdE821c417b26b4a934e0cdaf03"  # from Ganache
derived_address = Account.from_key(private_key).address

print(derived_address)  # must match the 'from' field
