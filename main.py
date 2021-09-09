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
#import matplotlib.pyplot as plt
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
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
day = "22"
days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
year = "2020"
countries_of_interest = ["China"]

#main
while not ((month == "09") and (day == "08") and (year == "2021")):
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
  if (day == "01") and (month in ("01","03","05","07","08","10","12")):
    days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
  elif (day == "01") and (month in ("04","06","09","11")):
    days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
  elif (day == "01") and (month == "02") and (year == "2020"):
    days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29"]
  elif (day == "01") and (month == "02") and (year == "2021"):
    days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28"]
  elif (day == "01"):
    print("something went wrong!")
    print(month + "-" + day + "-" + year)
    break
print(data_set_dictionary["09-02-2021"])