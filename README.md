# Bridge

## Features and Capabilities

- Launches the Bridge (BDG) ERC20 Smart Contract onto the Kovan Testnet (via Brownie and Infura).

## Hierarchy 

- The whole current codebase launches the token transfer system.
- Bridge currently has no frontend, only this functional token transfer system.
- Reference: https://www.youtube.com/watch?v=8rpir_ZSK1g&ab_channel=PatrickCollins

## Running Bridge

- Create your own .env file in order to set private key and set Infura project
  - From your Infura project page, you can set the chain to launch your smart contract
- Set environmental variables to .env (by "source .env" from the terminal)
- Run 'brownie run scripts/deploy_token.py --network kovan' from your terminal to deploy the token onto the Kovan Testnet
