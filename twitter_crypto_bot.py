# Importing all the needed libraries and variables.
import tweepy
from pycoingecko import CoinGeckoAPI
import json
from apscheduler.schedulers.blocking import BlockingScheduler
from Twitter_Info import *

cg = CoinGeckoAPI()

# Setting up our OAuth.
client = tweepy.Client(
    consumer_key= API_KEY,
    consumer_secret= API_KEY_SECRET,
    access_token= ACCESS_TOKEN,
    access_token_secret= ACCESS_TOKEN_SECRET
)
# This function will tweet the updated price of Bitcoin and Ethereum bi-hourly.
def run_every_half_hour():
    btc_24_change = cg.get_price(ids='bitcoin' , vs_currencies='usd' , include_24hr_change = True)
    eth_24_change = cg.get_price(ids='ethereum' , vs_currencies='usd' , include_24hr_change = True)

    btc_24_change_json = json.dumps(btc_24_change)
    eth_24_change_json = json.dumps(eth_24_change)

    btc_price_change = ""
    eth_price_change = ""

    btc_24_change_json = btc_24_change_json.replace('usd_24h_change', '', -1)
    btc_24_change_json = btc_24_change_json.replace('  ', ' ', -1)
    for i in btc_24_change_json:
        if(i.isdigit()):
            btc_price_change =  btc_price_change + i
        elif(i == "."):
            btc_price_change = btc_price_change + i
        elif(i == " "):
            btc_price_change = btc_price_change + i
        elif (i == "-"):
            btc_price_change = btc_price_change + i
        elif (i == "+"):
            btc_price_change = btc_price_change + i

    eth_24_change_json = eth_24_change_json.replace('usd_24h_change', '', -1)
    eth_24_change_json = eth_24_change_json.replace("  ", " ", -1)
    for i in eth_24_change_json:
        if(i.isdigit()):
            eth_price_change =  eth_price_change + i
        elif( i == "."):
            eth_price_change =  eth_price_change + i
        elif(i == " "):
            eth_price_change = eth_price_change + i
        elif (i == "-"):
            eth_price_change = eth_price_change + i
        elif (i == "+"):
            eth_price_change = eth_price_change + i

    btc_price_change = btc_price_change[2 : -1]
    eth_price_change = eth_price_change[2: -1]

    btc_price = ""
    eth_price = ""
    btc_24hr = ""
    eth_24hr = ""


    for i in btc_price_change:
        btc_price = btc_price + i
        if (i == " "):
            break

    for i in eth_price_change:
        eth_price += i
        if (i == " "):
            break

    eth_space_pos = eth_price_change.find(" ") + 1
    btc_space_pos = btc_price_change.find(" ") + 1


    btc_24hr = btc_price_change[btc_space_pos: -1]
    eth_24hr = eth_price_change[eth_space_pos: -1]

    btc_price = float(btc_price)
    eth_price = float(eth_price)

    btc_price = round(btc_price, 2)
    eth_price = round(eth_price, 2)

    btc_price = str(btc_price)
    eth_price = str(eth_price)

    btc_24hr = float(btc_24hr)
    eth_24hr = float(eth_24hr)

    btc_24hr = round(btc_24hr, 2)
    eth_24hr = round(eth_24hr, 2)

    btc_24hr = str(btc_24hr)
    eth_24hr = str(eth_24hr)

    if(float(btc_24hr) >= 0):
        btc_24hr = "+" + btc_24hr

    if(float(eth_24hr) >= 0):
        eth_24hr = "+" + eth_24hr

    btc_24hr = str(btc_24hr)
    eth_24hr = str(eth_24hr)

    btc_price = '{:,}'.format(float(btc_price))
    eth_price = '{:,}'.format(float(eth_price))
# This will post the tweet.
    response = client.create_tweet(text="Bitcoin ( $BTC) is currently worth: $" + btc_price + " (" + btc_24hr + "%)" +" \nEthereum ( $ETH) is currently worth: $" + eth_price + " (" + eth_24hr + "%)" + "\n\n\nPowered by the CoinGecko API.", reply_settings= "mentionedUsers")
    print("Success.")


scheduler = BlockingScheduler()
scheduler.add_job(run_every_half_hour, 'interval', minutes=30)
scheduler.start()