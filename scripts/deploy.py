from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_script import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS



def deploy_fundme():
    account = get_account()
    #pass the price feed address to our fundMe contract

    #if we are in a persistent network like rinkeby, use the associate address
    #otherwise, deploy mock contract

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address =  config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address # recently deployed

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from":account}, 
        publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fundme()
