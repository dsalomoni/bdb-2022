import pandas as pd
cols = ["month", "year", "cases", "geoId"]
df = pd.read_csv("COVID-19-sample-BDB2021.csv", usecols=cols)

ncases = 0
for i, row in df.iterrows():
  id = row["geoId"]
  month = row["month"]
  year = row["year"]
  if (id=="IT") and (month==7) and (year==2020):
    ncases += row["cases"]

print(ncases)
