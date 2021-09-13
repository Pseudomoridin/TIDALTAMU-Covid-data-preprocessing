"""
STEPS TO SUCCESS
1. Obtain and import covid data set
2. Clean it and get rid of everything unimportant
?. Data that makes sense and proves/shows something
"""

"""ALL DATES WILL BE WRITTEN AS MM-DD-YYYY"""
#imports
import pandas as pd
pd.set_option("display.max_columns", None, "display.max_rows", 5)
from nasty import REFERENCE
import matplotlib.pyplot as plt
#import numpy as np

#method definition
def parse_raw_to_list(raw):
  new_dict = {}
  keys = raw.keys().tolist()
  for key in keys:
    if "Country" in key:
      country_index_string = key
    if "Confirmed" in key:
      confirmed_index_string = key
  for x in range(len(raw)):
    if raw.iloc[x][country_index_string] in new_dict:
      if pd.isnull(raw.iloc[x][confirmed_index_string]):
        new_dict[raw.iloc[x][country_index_string]] += 0.0
      else:
        new_dict[raw.iloc[x][country_index_string]] += raw.iloc[x][confirmed_index_string]
    else:
      if pd.isnull(raw.iloc[x][confirmed_index_string]):
        new_dict[raw.iloc[x][country_index_string]] = 0.0
      else:
        new_dict[raw.iloc[x][country_index_string]] = raw.iloc[x][confirmed_index_string]

  return new_dict

def raw_csv(_date):
  raw = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + _date + '.csv')
  return raw

#variable declaration and initialization
data_set_dictionary = {}
month = "01"
months = REFERENCE.months
day = "22"
days = REFERENCE.thirty_one
year = "2020"
labels = [0]
countries_iterated = []

#Countries of interest




#main
while not ((month == "09") and (day == "08") and (year == "2021")):
  labels.append(month + "-" + day)
  raw_file = raw_csv(month + "-" + day + "-" + year)
  data_set_dictionary[month + "-" + day + "-" + year] = parse_raw_to_list(raw_file)
  print("Data set for",month + "-" + day + "-" + year,"parsed.")
  try:
    day = days[days.index(day) + 1]
  except IndexError:
    try:
      month = months[months.index(month) + 1]
      day = days[0]
    except IndexError:
      year = "2021"
      month = months[0]
      day = days[0]
  if (day == "01") and (month in REFERENCE.thirty_one_months):
    days = REFERENCE.thirty_one
  elif (day == "01") and (month in REFERENCE.thirty_months):
    days = REFERENCE.thirty
  elif (day == "01") and (month == "02") and (year == "2020"):
    days = REFERENCE.twenty_nine
  elif (day == "01") and (month == "02") and (year == "2021"):
    days = REFERENCE.twenty_eight
  elif (day == "01"):
    raise Exception("Something went wrong at",month + "-" + day + "-" + year)

#"""
#variable redefining
month = "01"
day = "22"
days = REFERENCE.thirty_one
year = "2020"

#translating cases per country by day to cases per day by country
for x in range(len(data_set_dictionary)):
  #break
  for country in REFERENCE.countries:
    #break
    for key in data_set_dictionary[month + "-" + day + "-" + year].keys():
      #break
      if country["name"] in key:
        country[1].append(int(data_set_dictionary[month + "-" + day + "-" + year][key]))
        countries_iterated.append(country["name"])
        #print(country[1])
        break
    if country["name"] not in countries_iterated:
      country[1].append(0)
  try:
    day = days[days.index(day) + 1]
  except IndexError:
    try:
      month = months[months.index(month) + 1]
      day = days[0]
    except IndexError:
      year = "2021"
      month = months[0]
      day = days[0]
  if (day == "01") and (month in REFERENCE.thirty_one_months):
    days = REFERENCE.thirty_one
  elif (day == "01") and (month in ("04","06","09","11")):
    days = REFERENCE.thirty
  elif (day == "01") and (month == "02") and (year == "2020"):
    days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29"]
  elif (day == "01") and (month == "02") and (year == "2021"):
    days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
  elif (day == "01"):
    raise Exception("Something went wrong at",month + "-" + day + "-" + year)
"""
#print(countries)
for country in REFERENCE.countries:
  print(country)
  print("\n\n\n")
#"""

"""
for item in labels:
  item = ""#"""
fig, ax = plt.subplots()
width = 1
for country in REFERENCE.countries:
  ax.plot(labels[0:len(country[1])], country[1], width, label=country["name"])

ax.set_ylabel('COVID19 cases')
ax.set_title('COVID19 worldwide cases by country')
ax.legend()

plt.show()