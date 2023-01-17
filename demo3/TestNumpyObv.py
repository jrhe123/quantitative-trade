import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
from unittest import TestCase

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html
# 0: code
# 1: date
# 2: end price
# 3: start price
# 4: high price
# 5: low price
# 6: volumn
class TestNumpyObv(TestCase):
    def calculate(self):
        date_converter = lambda x: datetime.strptime(x.decode(), "%Y-%m-%d")
        file_name = "./data/data.csv"
        data = np.genfromtxt(
            file_name,
            delimiter=",",
            dtype=[
                ("stock_name", "U25"),
                ("date", "datetime64[s]"),
                ("end_price", "f8"),
                ("start_price", "f8"),
                ("high_price", "f8"),
                ("low_price", "f8"),
                ("volume", "f8"),
            ],
            converters={1: date_converter},
            names=True,
        )
        df = pd.DataFrame(
            {
                "end_price": data["end_price"],
                "volume": data["volume"],
            },
            index=data["date"],
        )
        df["obv"] = np.where(
            df["end_price"] > df["end_price"].shift(1),
            df["volume"],
            np.where(df["end_price"] < df["end_price"].shift(1), -df["volume"], 0),
        ).cumsum()

        print(df["obv"])


def main():
    obj = TestNumpyObv()
    obj.calculate()


if __name__ == "__main__":
    main()
