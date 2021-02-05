from yahoo_fin import stock_info as si
from time import time
from datetime import datetime
from decimal import Decimal

import os;

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# TEST TICKETS
# AAPL AMZN TSLA gme AMC SPY MSFT SBUX FB

tags = input("").split(" ")

t = time()
clear = lambda: os.system('cls')

prices = []

def print_watching():
    clear()
    temp = []
    global prices
    for i in range(len(tags)):
        tick = tags[i]
        x = si.get_live_price(tick)
        print(f"{tick.upper()}\t\t{x}", end="")
        if prices:
            change = "="
            if(x > prices[i]): change = "▲"
            if(x < prices[i]): change = "▼"
            print(f"({change}{round(abs(x - prices[i]), 2)})")
        else: print()
        temp.append(round(x, 2))
    prices = temp[:]
    print(datetime.now().strftime("%H:%M:%S"))

print_watching()


CONST_INTERVAL = 5

while True:
    # print(time() - t)
    if (time() - t) > CONST_INTERVAL:
        print_watching()
        t = time()

