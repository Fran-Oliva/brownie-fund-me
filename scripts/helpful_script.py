from brownie import network, config, accounts
def get_account():
    # diferentes formas de settear accounts
    #1
    #account =accounts[0]
    #2
    #account = accounts.load("metamask_fran")
    #3
    #account = accounts.add(os.getenv("PRIVATE_KEY"))
    #4
    #account = accounts.add(config["wallets"]["from_key"])    
    #print(account)

    if(network.show_active()=="development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"]) 