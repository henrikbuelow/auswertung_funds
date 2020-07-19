from tkinter import *
import pandas as pd


def showData ():

    data = pd.read_csv("Funds_sheet_Data.csv")
    print(data[:1])
    return data

#showData()