import pandas as pd
cols = ["month", "year", "cases", "geoId"]
df = pd.read_excel("COVID-19-sample-BDB2021.xlsx", usecols=cols)

ncases = 0
for i, row in df.iterrows():
  id = row["geoId"]
  month = row["month"]
  year = row["year"]
  if (id=="IT") and (month==11) and (year==2020):
    ncases += row["cases"]

print(ncases)
