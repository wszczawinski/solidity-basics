# FundMe smart contract

Creates contract on testnet which enables to send funds to the address od contract creator.

## Install and Launch Project 🚀

```bash
pip install -r requirements.txt
npm install

touch .env
cat >> .env 
export PRIVATE_KEY=<testnet_private_key>

brownie compile
brownie run scripts/deploy.py
```
