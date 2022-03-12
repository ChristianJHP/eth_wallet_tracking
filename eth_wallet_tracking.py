from ast import Lambda
from tokenize import Double
from requests import get
from matplotlib import pyplot as plt
from datetime import datetime

API_KEY = "13WGMDIGIV5PMSIUXH6EAH63XBQKXAZDAP"
BASE_URL = "https://api.etherscan.io/api"
ETHER_VALUE = 10 ** 18

'''https://api.etherscan.io/api
   ?module=account
   &action=balance
   &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
   &tag=latest
   &apikey=YourApiKeyToken'''


def make_api_url(module, action, address, **kwargs):
    url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

    for key, value in kwargs.items():
        url += f"&{key}={value}"

    return url

def get_account_balance(address): 
    get_balance_url = make_api_url("account", "balance", address, tag = "latest")
    response = get(get_balance_url)
    data = response.json()
    
    value = int(data["result"]) / ETHER_VALUE
    return value

def get_transactions(address):
    get_transactions_url = make_api_url("account", "txlist", address, startblock = 0, endblock =99999999, page =1, offset = 10000, sort = "asc")
    response = get(get_transactions_url)
    data = response.json()["result"]

    internal_tx_url = make_api_url("account", "txlistinternal", address, startblock = 0, endblock =99999999, page =1, offset = 10000, sort = "asc")
    response2 = get(internal_tx_url)
    data2 = response2.json()["result"]

    data.extend(data2)
    data.sort(key=Lambda x: x["timeStamp"])
    
    current_balance = 0
    times = []
    balances = []

    for tx in data:
        to = tx["to"]
        from_addr = tx["from"]
        value = int(tx["value"]) / ETHER_VALUE
        if
        gas = int(tx["gasUsed"]) 
        time = datetime.fromtimestamp(int(tx['timeStamp']))
        money_in = to.lower() == address.lower()

        if money_in:
            current_balance += value
        else:
            current_balance -= value + gas

        balances.append(current_balance)
        times.append(time)

address = "0x9879305247f69adce8f89fbe809dd11ab807532b"
get_transactions(address)



