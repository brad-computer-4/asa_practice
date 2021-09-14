'''
    first part to create an account
'''

# from algosdk import account
# from algosdk import mnemonic

# private_key, public_address = account.generate_account()
# print("Base64 Private Key: {}\nPublic Algorand Address: {}\n".format(private_key, public_address))
# print(mnemonic.from_private_key(private_key))

'''
    some script from the docs
'''

# import json
# from algosdk import account, mnemonic

# acct = account.generate_account()
# address1 = acct[1]
# print("Account 1")
# print(address1)
# mnemonic1 = mnemonic.from_private_key(acct[0])

# print("Account 2")
# acct = account.generate_account()
# address2 = acct[1]
# print(address2)
# mnemonic2 = mnemonic.from_private_key(acct[0])

# print("Account 3")
# acct = account.generate_account()
# address3 = acct[1]
# print(address3)
# mnemonic3 = mnemonic.from_private_key(acct[0])
# print ("")
# print("Copy off accounts above and add TestNet Algo funds using the TestNet Dispenser at https://bank.testnet.algorand.network/")
# print("copy off the following mnemonic code for use later")
# print("")
# print("mnemonic1 = \"{}\"".format(mnemonic1))
# print("mnemonic2 = \"{}\"".format(mnemonic2))
# print("mnemonic3 = \"{}\"".format(mnemonic3))



'''
    checking the balance
'''

from algosdk.v2client import algod
from config import account_one, mnemonic_one, token
import json
ip_address = 'https://testnet.algoexplorerapi.io'
client = algod.AlgodClient(token, ip_address, headers={'User-Agent': 'hey'})
account_info = client.account_info(account_one)
print(json.dumps(account_info, indent=4))

account_balance = account_info.get('amount')


print('Account balance: {} microAlgos'.format(account_balance))




