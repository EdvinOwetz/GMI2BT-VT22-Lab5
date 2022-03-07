import pandas as pd
import matplotlib as mlt
import datetime

#https://github.com/pandas-dev/pandas/blob/main/doc/cheatsheet/Pandas_Cheat_Sheet.pdf

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
def format_dataframe(dataframe:pd.DataFrame,rep_oldstr:str,rep_newstr:str):
    for index in range(len(dataframe)):
        if(type(dataframe[index])==str):
            dataframe[index]=dataframe[index].replace(rep_oldstr,rep_newstr)
        else:
            print(f"Not a string value, at [{index}] , type = {type(dataframe[index])}")

format_dataframe(dataslask["BF95"],",",".")
format_dataframe(dataslask["Diesel"],",",".")
#Konverterar värderna till rätt typ
dataslask[["BF95"]]=dataslask[["BF95"]].astype(float)
dataslask[["Diesel"]]=dataslask[["Diesel"]].astype(float)
dataslask["DateTime"]=pd.to_datetime(dataslask["DateTime"])
#Visar data
print(dataslask)
print(dataslask.dtypes)
print(dataslask.describe())
print(dataslask.corr())




    
    