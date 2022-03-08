import pandas as pd
import matplotlib as mlt
import datetime

#https://github.com/pandas-dev/pandas/blob/main/doc/cheatsheet/Pandas_Cheat_Sheet.pdf

#https://www.w3schools.com/python/matplotlib_grid.asp

dataslask = pd.read_csv("drivmedelspriser.csv", delimiter=";")
#Visar datan som den är inläst
print("Showing imported data")
#print("Removeing null data : ",dataslask.dropna(inplace=True))
print(dataslask.head())
print(dataslask.dtypes)
print(dataslask.describe())
print("Corolation: ",dataslask.corr())
print("Duplicated: ",dataslask.duplicated())

print("\nStarting Data Cleaning\n")

#ersätter "," med "."

def format_str(x):
    if type(x)==str:
        return x.replace(",",".")
    return x

dataslask["BF95"]=dataslask["BF95"].apply(format_str)
dataslask["Diesel"]=dataslask["Diesel"].apply(format_str)

#format_dataframe(dataslask["BF95"],",",".")
#format_dataframe(dataslask["Diesel"],",",".")

# def format_dataframe(dataframe:pd.DataFrame,rep_oldstr:str,rep_newstr:str):
#     for index in range(len(dataframe)):
#         if(type(dataframe[index])==str):
#             dataframe[index]=dataframe[index].replace(rep_oldstr,rep_newstr)
#         else:
#             print(f"Not a string value, at [{index}] , type = {type(dataframe[index])}")

#Konverterar värderna till rätt typ
dataslask["BF95"]=dataslask["BF95"].astype(float)
dataslask["Diesel"]=dataslask["Diesel"].astype(float)
dataslask["DateTime"]=pd.to_datetime(dataslask["DateTime"])
#Visar data
print(dataslask)
print(dataslask.dtypes)
print(dataslask.describe())
print(dataslask.corr())

#Lite plots

import matplotlib.pyplot as plt


plt.plot(dataslask["DateTime"],dataslask["Diesel"],color="red")
plt.plot(dataslask["DateTime"],dataslask["BF95"],color="blue")
plt.grid() # visar ett runät
plt.title("Plot över Datan")
plt.xlabel("DateTime")
plt.ylabel("Pris kr/liter")
leg=["Diesel","BF95"]
plt.legend(leg)
plt.show()


    
    