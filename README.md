# Twitter Price bot
This program pulls the price and 24-hour price changes of specified cryptocurrencies(in this case Bitcoin and Ethereum) from Coingecko, via their API. Then, it formats the price data, and tweets it using the tweepy api. Additionally, this program utilizes the apscheduler library to run the script every set interval(in this case bi-hourly).

**Requirements to run this program:**
1. You must have valid Twitter Authentication. You can learn more [here.](https://developer.twitter.com/en/docs/authentication/overview)
2. You must have the required libraries installed on your machine, you can install them using the command:
```
 pip install requiredlibs.txt
```
**License:**
MIT License

Copyright (c) 2022 Mustafa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
