import os
from pydoc import describe
from statistics import mean
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
covid_data = pd.read_csv("full_data.csv")
covid_data.head(5)
covid_data.info()
print(covid_data.describe())
# choose the domain of the data
covid_data.iloc[0, 1]
covid_data.iloc[2, 0:5]
covid_data.iloc[0:2, :]
covid_data.iloc[0:10:2, 0:5]
covid_data.iloc[10:21, 0:3:2]
covid_data.iloc[0:3, [0, 1, 3]]
# True if the column is chosen
my_columns = [True, True, False, True, False, False]
covid_data.iloc[0:3, my_columns]
covid_data.loc[2:4, "date"]
covid_data.loc[0:81, "total_cases"]
my_columns = [False, False, False, False, True, False]
print(covid_data.loc[0:81, my_columns])
a = []
for location in covid_data.loc[:, "location"]:
    a.append(location == "Afghanistan")
print(covid_data.loc[a, "total_cases"])
b = []
for location in covid_data.loc[:, "location"]:
    b.append(location == "China")
c = covid_data.iloc[b, [0, 2, 3]]
d = np.mean(c.loc[:, "new_cases"])
print(d)
e = np.mean(c.loc[:, "new_deaths"])
print(e)
print(e/d)  # the proportion of new cases that kill the infected person
case = c.loc[:, "new_cases"]
death = c.loc[:, "new_deaths"]
date = c.loc[:, "date"]
plt.boxplot((case, death), labels=("new cases", "new deaths"))
plt.title("new cases and new deaths in China")
plt.show()
plt.plot(date, case, "go")  # decide the colour and shape of splashes
plt.plot(date, death, "y+")
plt.xlabel("date")
plt.ylabel("cases/deaths")
plt.title("number of cases and deaths in China over time")
plt.xticks(date.iloc[0:len(date):4], rotation=-90)
plt.show()
m = []
for location in covid_data.loc[:, "location"]:
    m.append(location == "France")
n = covid_data.iloc[m, [0, 2, 3]]
cases = n.loc[:, "new_cases"]
deaths = n.loc[:, "new_deaths"]
dates = n.loc[:, "date"]
plt.plot(dates, cases, "bo")
plt.plot(dates, deaths, "r+")
plt.xlabel("date")
plt.ylabel("cases/deaths")
plt.title("number of cases and deaths in France over time")
plt.xticks(dates.iloc[0:len(dates):4], rotation=-90)
plt.show()
