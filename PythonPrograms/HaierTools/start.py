
import pandas as pd
import numpy as np


class Test():

    def __init__(self):
        data = pd.read_excel("./Views/waterheater.xlsx")
        print(data)

if __name__ == '__main__':
    t = Test()