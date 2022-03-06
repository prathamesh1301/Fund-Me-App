from unittest.mock import Mock
from brownie import network,accounts,config,FundMe,MockV3Aggregator
from scripts.helper_scripts import getAccount,deploy_mocks,LOCAL_DEVELOPMENT_ENVIRONMENTS



def fund_me_deploy():
    account = getAccount()
    if(network.show_active() not in LOCAL_DEVELOPMENT_ENVIRONMENTS):
        priceFeed = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        priceFeed = MockV3Aggregator[-1].address
        

    fund_me = FundMe.deploy(priceFeed,{"from":account},publish_source = config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    fund_me_deploy()