from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 3
ex3a_txout_scriptPubKey = [
OP_2DUP,          
OP_ADD,           #计算 x + y
2212 ,
OP_EQUALVERIFY,  # 检查 x + y 是否等于 2212
OP_SUB,           # 计算 x - y
422,
OP_EQUAL     # 检查 x - y
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.0000202
    txid_to_spend =(
        'f8dd43d1074becc1ff6f387a34efd6f0a5e204f1931e425582da5c918e1844f3')
    utxo_index = 0
    ##################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex3a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
