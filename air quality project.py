#!/usr/bin/env python
# coding: utf-8

# # AIR QUALITY OF INDIAN CITIES
# 

# # ABOUT THE PROJECT
# Through this project I am trying to analyse, using the data of air quality in major Indian cities, the condition of air polution in our country. We will know in the end if the condition has improved or worsened and check the progress of major cities with regards to air pollution.

# # DATSET
# The dataset used here has been downloaded from Kaggle. The link to which is as follows. 
# https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india?resource=download. 
#     It consists of air quality data of major cities from 2015 to 2020.

# In[7]:


datset_url='https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india?resource=download'


# installing open datasets packages

# In[9]:


get_ipython().system('pip install opendatasets')
get_ipython().system('pip install pandas')


# importing the dataset
# 

# In[12]:


import opendatasets as od
od.download(datset_url)


# In[13]:


import os 
os.listdir('.')


# In[14]:


data_dir = "./air-quality-data-in-india"


# In[15]:


os.listdir(data_dir)


# In[16]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[17]:


air_quality_df = pd.read_csv('./air-quality-data-in-india/city_day.csv')
air_quality_df


# # cleaning the dataset
# In this step the problems like missing dataset, invalid data will be handled.

# Deleting the rows which have no data except city name
# and also deleting the AQI_Bucket column

# In[18]:


air_df=air_quality_df.dropna(thresh=14).reset_index(drop=True)
air_df


# In[20]:


air_df=air_df.drop(['AQI_Bucket'],axis=1)
air_df


# # Replacing NaN values
# We have to handle the NaN values. So wherever in the dataframe, we find NaN values. It's to be replaced with 0 except for the AQI column. It will be replaced with mean.
# 
# 

# In[21]:


#Replacing NaN values in AQI with mean of AQI
air_df['AQI']=air_df['AQI'].fillna(air_df.mean(numeric_only=True))


# In[22]:


#Replacing all other NaN values with zeroes
air_df.fillna(0)


# # Finding List of different cities

# In[25]:


cities=pd.unique(air_df['City'])
print(cities)
print('There are total {} cities in dataframe'.format(len(cities)))


# # Sorting the cities in order of average AQI

# In[26]:


avg_aqi=air_df.groupby('City')['AQI'].mean()
avg_aqi.sort_values()


# Covert the date into datetime type from object type

# In[29]:


air_df['Date']=pd.to_datetime(air_df['Date'])
air_df.dtypes


# # Plotting curve for AQI of Jaipur city

# Creating a smaller database for Jaipur city

# In[51]:


jaipur_df=air_df[air_df['City']=='Jaipur']
jaipur_df.reset_index(inplace=True)
jaipur_df


# In[53]:


jai_df=jaipur_df.copy()
jai_df['Month']=jai_df['Date'].dt.month
jai_df


# Added a Month Column in the dataframe. I will now group this dataframe according to months and plot a graph AQI vs Months for knowing about trends of avg AQI for a month for every year.

# In[56]:


jai_df=jai_df.groupby('Month').mean()
jai_df


# # Reference data for AQI levels

# good = 0 - 50
# satisfactory = 50 - 100
# moderately_polluted = 100 - 200
# poor = 200 - 300
# very_poor = 300 - 400
# severe = 400 - 500 and above

# In[62]:


plt.figure(figsize =(12,8))
plt.axhline(y = 50, color = 'lime', linestyle = '--')
plt.axhline(y = 100, color = 'darkgreen', linestyle = '--')
plt.axhline(y = 200, color = 'mediumaquamarine', linestyle = '--')
plt.axhline(y = 300, color = 'darkorange', linestyle = '--')
plt.axhline(y = 400, color = 'red', linestyle = '--')
plt.axhline(y = 100, color = 'darkred', linestyle = '--')
plt.plot(jai_df.index, jai_df.AQI)
plt.title('Monthly AQI average(Jaipur)')
plt.xlabel('Month')
plt.ylabel('AQI')
plt.legend(['Good','Satisfactory','Moderate','Poor','Very Poor','Severe','Ahmedabad']);


# # Comparing these values with Delhi, the capital city always in news for pollution

# In[63]:


dl_df=air_df[air_df['City']=='Delhi'].reset_index(drop=True)
dl_df


# In[64]:


dl_df['Month'] = dl_df['Date'].dt.month


# In[65]:


dl_df=dl_df.groupby('Month').mean()


# In[68]:


plt.figure(figsize =(12,8))
plt.axhline(y = 50, color = 'lime', linestyle = '--')
plt.axhline(y = 100, color = 'darkgreen', linestyle = '--')
plt.axhline(y = 200, color = 'mediumaquamarine', linestyle = '--')
plt.axhline(y = 300, color = 'darkorange', linestyle = '--')
plt.axhline(y = 400, color = 'red', linestyle = '--')
plt.axhline(y = 100, color = 'darkred', linestyle = '--')
plt.plot(dl_df.index, dl_df.AQI, 'purple')
plt.plot(jai_df.index, jai_df.AQI, 'b')
plt.legend(['Good','Satisfactory','Moderate','Poor','Very Poor','Severe','Delhi','Jaipur'])
plt.title("Jaipur vs Delhi avg AQI(Monthly)");


# # Checking average AQI of Delhi and Jaipur (Yearly average)

# In[71]:


dl2_df = air_df[air_df['City']=='Delhi'].reset_index(drop=True)
jai2_df = air_df[air_df['City']=='Jaipur'].reset_index(drop=True)


# In[75]:


dl2_df['Year'] = dl2_df['Date'].dt.year

jai2_df['Year'] = jai2_df['Date'].dt.year


# In[81]:


dl2_df = dl2_df.groupby('Year').mean()

jai2_df = jai2_df.groupby('Year').mean()


# In[82]:


plt.figure(figsize =(12,8))
plt.axhline(y = 50, color = 'lime', linestyle = '--')
plt.axhline(y = 100, color = 'darkgreen', linestyle = '--')
plt.axhline(y = 200, color = 'mediumaquamarine', linestyle = '--')
plt.axhline(y = 300, color = 'darkorange', linestyle = '--')
plt.axhline(y = 400, color = 'red', linestyle = '--')
plt.axhline(y = 100, color = 'darkred', linestyle = '--')
plt.plot(dl2_df.index, dl2_df.AQI, 'purple')
plt.plot(jai2_df.index, jai2_df.AQI, 'blue')
plt.title('Jaipur vs Delhi Average AQI (Yearly)')
plt.xlabel('Year')
plt.ylabel('Average AQI')
plt.legend(['Good','Satisfactory','Moderate','Poor','Very Poor','Severe','Delhi','Jaipur']);


# So we can conclude that Yearly average AQI as well as monthly average AQI of Delhi is always greater than that of Jaipur in the period of 2015-2020.

# In[ ]:




