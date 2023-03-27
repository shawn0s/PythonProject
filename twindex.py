import pandas as pd
import numpy as np
from pymongo import MongoClient
from bson.objectid import ObjectId

def get_database(db):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb://127.0.0.1/"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client[db]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    db = get_database("tw_market_dev")
    stocks = db["stocks"]
    df = pd.read_excel("C:/Users/Shawn/Desktop/tw-index.xlsx", skiprows=1, date_parser= [0])

    data = []
    for index, row in df.iterrows():
        twindex = {
            "_id": ObjectId(),
            "stockNo": "TAIEX",
            "stockType": "index",
            "open": row["開盤"],
            "high": row["最高"],
            "low": row["最低"],
            "close": row["收盤"],
            "stockDate": row["時間"].strftime("%Y%m%d"),
            "amount": row["成交額"],
            "date": row["時間"]
        }
        stocks.insert_one(twindex)

        # print(twindex)
    # print(data[1])
    # stocks.insert_many(data)


    # data = df.to_dict('records')


