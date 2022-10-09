# Twitter Price bot
This program pulls the price and 24-hour price changes of specified cryptocurrencies(in this case Bitcoin and Ethereum) from Coingecko, via their API. Then, it formats the price data, and tweets it using the tweepy api. Additionally, this program utilizes the apscheduler library to run the script every set interval(in this case bi-hourly).

**Requirements to run this program:**
1. You must have valid Twitter Authentication -> You can learn more here: 
2. You must have the required libraries installed on your machine, you can install them using the command -> pip install requirements.txt

License:
