import pandas as pd
import matplotlib as mlt
import datetime

data=pd.read_csv("IMDB-Movie-Data.csv")
#date1=datetime.date

#data[["Year"]] = data[["Year"]].astype(float)


print(data.head())
#print(data.dtypes)

#apply(pd.to_numeric)

#data[["Year"]] = pd.to_datetime(data[["Year"]],format="y")

datum=datetime.date(2002,1,1)
print(datum.year)

print(data.dtypes)