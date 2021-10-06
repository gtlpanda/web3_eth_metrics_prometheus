
import prometheus_client as prom
import time

from web3 import Web3

w3 = Web3(Web3.HTTPProvider("<INSERT INFURA URL HERE>"))

eth_block_difficulty = prom.Gauge(
    'eth_difficulty', 'Here is the eth difficulty:')


def get_latest_block_diff_eth():
    while True:
        latest_diff_eth = w3.eth.get_block("latest").difficulty
        eth_block_difficulty.set(latest_diff_eth)
        time.sleep(5)


if __name__ == '__main__':
    prom.start_http_server(80)
    # generate_random_numbers()
    get_latest_block_diff_eth()
