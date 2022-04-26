from brownie import accounts, config, TokenERC20

initial_supply = 1000000
token_name = "BRIDGE"
token_symbol = "BRG"

def main():
    account = accounts[0]
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}
    )