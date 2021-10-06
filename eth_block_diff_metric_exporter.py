
import prometheus_client as prom
from random import randrange
import time

from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/8c300834a4484968b3b8556dbbb38ece"))

# RANDOM_NUMBER_GAUGE = prom.Gauge('rendom_number_gauge', 'Random number between 1 - 100')

RANDOM_NUMBER_GAUGE = prom.Gauge('eth_difficulty', 'Here is the eth difficulty:')


# def generate_random_numbers():
#     while True:
#         random_number = randrange(10)
#         RANDOM_NUMBER_GAUGE.set(random_number)
#         time.sleep(5)

def get_latest_block_diff_eth():
    while True:
        latest_diff_eth = w3.eth.get_block("latest").difficulty
        RANDOM_NUMBER_GAUGE.set(latest_diff_eth)
        time.sleep(5)



if __name__ == '__main__':
    prom.start_http_server(80)
    # generate_random_numbers()
    get_latest_block_diff_eth()