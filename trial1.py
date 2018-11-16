# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:15:59 2018

@author: vinod
"""

import pandas as pd
import datetime
import pandas_datareader as web
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 1, 1)

df = web.DataReader("XOM", "yahoo", start, end)

print(df.head())

df['Adj Close'].plot()
plt.show()
