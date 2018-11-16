# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:43:52 2018

@author: vinod
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

web_stats = {'Day' : ['A','B','C','D','E','F','G'],
             'Window_Shoppers' : [100, 120, 130, 145, 160, 200, 300],
             'Buyers' : [80, 105, 116, 130, 155, 180,250]}

shop_data = pd.DataFrame(web_stats)

## Printing the complete dataframe, first and last few observations of the data frame
print(shop_data)
print(shop_data.head())
print(shop_data.tail())
print(shop_data.tail(2))

## Indexing the dataframe by setting the index to day
print(shop_data.set_index('Day'))

shop_data1 = shop_data.set_index('Day')
print(shop_data1.head())

shop_data.set_index('Day', inplace = True)

## Printing specific coloumns in the dataset
print(shop_data['Window_Shoppers'])
print(shop_data['Buyers'])

print(shop_data.Window_Shoppers)
print(shop_data.Buyers)

print(shop_data[['Window_Shoppers','Buyers']])

## Printing one of the coloumn values to list
print(shop_data.Buyers.tolist())
print(shop_data.Window_Shoppers.tolist())

print(np.array(shop_data[['Window_Shoppers','Buyers']]))

## Coverting the array into the dataframe
shop_data2 = pd.DataFrame(web_stats)
shop_data3 = pd.DataFrame(np.array(shop_data2[['Window_Shoppers','Buyers']]))
print(shop_data3)
