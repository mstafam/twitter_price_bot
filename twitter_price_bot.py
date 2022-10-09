import tweepy
from pycoingecko import CoinGeckoAPI
import json
from apscheduler.schedulers.blocking import BlockingScheduler
from Twitter_Info import *

cg = CoinGeckoAPI()

client = tweepy.Client(
    consumer_key= API_KEY,
    consumer_secret= API_KEY_SECRET,
    access_token= ACCESS_TOKEN,
    access_token_secret= ACCESS_TOKEN_SECRET
)

def get_price(crypto):
        price_change = cg.get_price(ids=crypto , vs_currencies='usd' , include_24hr_change = True)
        price_change = json.dumps(price_change)
        price_change = price_change.replace('usd_24h_change', '', -1)
        valid_list = [".", " ", "-", "+"]
        new_price_change = ''
        for i in price_change:
            if(i.isdigit() or i in valid_list):
                new_price_change = new_price_change + i
        price_change = new_price_change
        price_change = price_change.replace('  ', ' ', -1)
        price_change = price_change[1:]
        price = price_change.split(" ")[0]
        change = price_change.split(" ")[1]
        def roundVal(val):
            val = float(val)
            val = "{:.2f}".format(val)
            val = str(val)
            return val
        price = roundVal(price)
        change = roundVal(change)
        if(float(change) >= 0):
            change = "+" + change
            change = str(change)
            price = '{:,}'.format(float(price))
        return price, change

def main():
    btc_price, btc_change = get_price("Bitcoin")
    eth_price, eth_change = get_price("Ethereum")
    client.create_tweet(text="Bitcoin ( $BTC) is currently worth: $" + btc_price + " (" + btc_change + "%)" +" \nEthereum ( $ETH) is currently worth: $" + eth_price + " (" + eth_change + "%)" + "\n\n\nPowered by the CoinGecko API.", reply_settings= "mentionedUsers")
    print("Success.")

scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', minutes=30)
scheduler.start()