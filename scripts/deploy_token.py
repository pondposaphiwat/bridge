from brownie import accounts, config, EasyToken

initial_supply = 1000000000000000
token_name = "BRIDGE"
token_symbol = "BRG"

def main():
    account = accounts.add(config["wallets"]["from_key"])
    erc20 = EasyToken.deploy(
        initial_supply, {"from": account}
    )