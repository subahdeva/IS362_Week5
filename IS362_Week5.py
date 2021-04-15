#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd

airport_data = pd.read_csv('https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airports.csv',na_filter=False)

# What is the northernmost airport in the United States?
# Using the latitude column of this raw data, we can determine what is the northernmost
# airport in the U.S.
# The table below Dillant Hopkins Airport is the northernmost part of the U.S.
# however, according to Google maps: 
# https://www.google.com/maps/place/Wiley+Post-Will+Rogers+Memorial+Airport/@70.9704186,-140.4461716,3z/data=!4m5!3m4!1s0x50c327fff620aae7:0x936de8c8fd2d094b!8m2!3d71.284909!4d-156.766362?hl=en
# Wiley Post Will Rogers Memorial is the northernmost part, thus making 

airport_data.sort_values(by=['lat'], ascending=False).head()

# What is the easternmost airport in the United States?
# When looking at the results of the table below in the longitude column, 
# it shows that Eareckson As being the easternmost airport in the U.S.
# however, according to Google maps: 
# https://www.google.com/maps/place/Eastport+Municipal+Airport-EPM/@45.0809204,-67.4577252,9z/data=!4m5!3m4!1s0x4ca8bcbb416bb557:0xe8e7c4805bb5f1e8!8m2!3d44.9099999!4d-67.012779?hl=en
# the Eastport Municipal Airport is the easternmost airport in the U.S.

airport_data.sort_values(by=['lon'], ascending=False).head()

# On February 12th, 2013, which New York area airport had the windiest weather?
weather_data = pd.read_csv('https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/weather.csv')

# According to the data in this table for February 12, 2013
# EWR airport had the windiest weather on this day however looking at this data 

weather_data[(weather_data["month"]==2) & (weather_data["day"]==12) & (weather_data["year"]==2013)].sort_values(by=["wind_speed"], ascending=False).head()


# In[ ]:





# In[ ]:




