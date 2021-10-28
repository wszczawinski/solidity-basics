
from brownie import (
    MockV3Aggregator,
    network,
)
from scripts.helpful_scripts import (
    get_account,
)

DECIMALS = 8
INITIAL_VALUE = 200000000000


def deploy_mocks():
    """
    Mock for testnet deployment
    """
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    account = get_account()
    MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": account})
    print("Mocks Deployed!")


def main():
    deploy_mocks()
