from brownie import network,accounts,config,MockV3Aggregator
from web3 import Web3
LOCAL_DEVELOPMENT_ENVIRONMENTS = ["development","my-ganache","my-ganache1"]
FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]

def getAccount():
    if (network.show_active() in LOCAL_DEVELOPMENT_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        if(len(accounts)==0):
            accounts.add()
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

DECIMALS = 8
# This is 2,000
INITIAL_VALUE = 200000000000
def deploy_mocks():
    if(len(MockV3Aggregator)<=0):
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks...")
        #account = getAccount()
        MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": getAccount()})
        print("Mocks Deployed!")