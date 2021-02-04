from yahoo_fin import stock_info as si
from time import time
from datetime import datetime

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

# AAPL AMZN TSLA gme AMC SPY MSFT SBUX FB

tags = input("").split(" ")

t = time()
while 1:
    # print(time() - t)
    if (time() - t) > 5:
        for tick in tags:
            print(f"{tick.upper()}\t\t{si.get_live_price(tick)}")
        t = time()
        print(datetime.now().strftime("%H:%M:%S"))

