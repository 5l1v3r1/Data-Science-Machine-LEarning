# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 17:09:12 2020

@author: Deep Chokshi
"""


import numpy as np
import pandas as pd
import seaborn as sns

#Importing CSV file and store into dataframe.
dataframe = pd.read_csv("House_Price.csv", header=0)

#Looking at top 5 row of datasets
print (dataframe.head())

#Looking at shape of data (no.of rows and no. of coloums)
print (dataframe.shape)

#Looking Extended Data Dictionary
print (dataframe.describe())

#Looking at information of data (counts and datatype)
print (dataframe.info())

#Ploting scatter plot to visulize (prise to number of rooms)
_ = sns.jointplot(x='n_hot_rooms', y='price', data=dataframe)
_ = sns.jointplot(x='rainfall', y='price', data=dataframe)

#Plotting categorical data
_ = sns.countplot(x='airport', data=dataframe)
_ = sns.countplot(x='waterbody', data=dataframe)
_ = sns.countplot(x='bus_ter', data=dataframe)
''' Observation till now
    1. Missing value in n_hot_beds
    2. Skewness or outliers in crimerate
    3. Outliers in n_hot_rooms and rainfall
    4. Bus_ter has only "Yes" Values'''
    
#Removing outlier using capping & flooring method for n_hot_rooms.
upper_limit = np.percentile(dataframe.n_hot_rooms,[99])[0]                        #Find the 99th percentile value
print (dataframe.n_hot_rooms[(dataframe.n_hot_rooms > upper_limit)])              #before removing outlier

#Change the value which is more than the 3 time of the upper limit anf assing it with 3*upper_limit.
dataframe.n_hot_rooms[(dataframe.n_hot_rooms > 3*upper_limit)] = 3*upper_limit
print (dataframe.n_hot_rooms[(dataframe.n_hot_rooms > upper_limit)])              #After removing outlier

#Removing outlier using capping & flooring method for rainfall.
lower_limit = np.percentile(dataframe.rainfall,[1])[0]                            #Find the 1st percentile calue
print (dataframe.rainfall[(dataframe.rainfall < lower_limit)])                    #befor removing outlier

#Change the value which is less than the 0.3 time of the lower limit anf assing it with 0.3*upper_limit
dataframe.rainfall[(dataframe.rainfall < 0.3*lower_limit)] = 0.3*lower_limit
print (dataframe.rainfall[(dataframe.rainfall < lower_limit)])                    #after removing outlier

#Filling the missing value in n_hot_beds.
print (dataframe.info())                                                          #check in which column data is missing
dataframe.n_hos_beds = dataframe.n_hos_beds.fillna(dataframe.n_hos_beds.mean())
print (dataframe.info())                                                          #Again check is it filled or not


