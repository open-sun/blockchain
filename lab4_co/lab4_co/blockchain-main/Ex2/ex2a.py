from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


cust1_private_key = CBitcoinSecret(
    'cTKkodPzkCsr8ZArAarBJynova92PxYXr1penRP4LtdFRuDyRt3h')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret(
    'cRpXhfvFxvhdWRjpa8C1ZAv6XsydxsS2FtydF5EJE4EgS8xuxxqV')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret(
    'cNrRqR1HmnDecK8U1qneToR2fu1kVb1uHa7W1vsa3yktGEqrRQrS')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2
my_private_key = CBitcoinSecret('cUaHgy7dvDm3b3shFPU6vBXd6Jv6q176FHBP1u2sXWA1dePpQ9p3')
my_public_key = my_private_key.pub
# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.

ex2a_txout_scriptPubKey = CScript([
    2,  
    my_public_key,
    cust1_public_key,
    cust2_public_key,
    cust3_public_key,
    4,  
    OP_CHECKMULTISIG
])
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0001
    txid_to_spend = (
        '9ad7b3bafb860ccfaa5348f09d22e5e9ceabdef4e601852f8b6b81f35eedf3f3')
    utxo_index = 1
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
