from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_script import get_account
from web3 import Web3


def deploy_fundme():
    account = get_account()
    #pass the price feed address to our fundMe contract

    #if we are in a persistent network like rinkeby, use the associate address
    #otherwise, deploy mock contract

    if network.show_active() != "development":
        price_feed_address =  config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks....")
        if len(MockV3Aggregator) <= 0:
            print(f"mock V3 aggregator len {len(MockV3Aggregator)}")
            MockV3Aggregator.deploy(18,Web3.toWei(2000,"ether"),{"from":account})
        price_feed_address = MockV3Aggregator[-1].address # recently deployed
      
        print("....Mocks Deployed!")

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from":account}, 
        publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fundme()
