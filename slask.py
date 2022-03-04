import pandas as pd
import matplotlib as mlt
import datetime

dataslask = pd.read_csv("drivmedelspriser.csv", delimiter=";")
print(dataslask[["Diesel"]].describe())