# This is a sample Python script.
from pymongo import MongoClient
from pandas import DataFrame
import numpy as np


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_database(db):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://127.0.0.1/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client[db]


def moving_average(a, n):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Get the database
    dbname = get_database('tw_market')
    collection_stocks = dbname["stocks"]
    item_details = collection_stocks.find({"stockNo": "2330"}).sort("date")
    # for i in range(item_count):
    data = list(item_details)
    close_array = []
    for idx in range(len(data)):
        stock = data[idx]
        open = stock.get("open")
        high = stock.get("high")
        low = stock.get("low")
        close = stock.get("close")
        # This does not give a very readable output
        close_array.append(close)

    ma5 = moving_average(close_array, 5)
    ma10 = moving_average(close_array, 10)
    ma5 = np.concatenate(([None, None, None, None], ma5))
    ma10 = np.concatenate(([None, None, None, None, None, None, None, None, None], ma10))
    for idx in range(len(data)):
        if ma5[idx] is None or ma10[idx] is None:
            continue
        stock = data[idx]
        open_price = stock.get("open")
        high_price = stock.get("high")
        low_price = stock.get("low")
        close_price = stock.get("close")

        ma5e = ma5[idx]
        ma10e = ma10[idx]
        if close_price > open_price and ma5e > ma10e:
            if low_price <= ma10e < close_price:
                print(stock.get("stockDate") + " 買進" + stock.get("stockNo") + "價格 " + str(stock.get("close"))+" ma5 " + str(ma5e) + " ma10 " + str(ma10e))

    # print(close_array)
    # print(len(close_array))
    # print(len(ma5))
    # print(len(ma10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
