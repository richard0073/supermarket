# -*- coding: utf-8 -*-
"""Copy of datad6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ad7iHiCP12ks_aRq2RFrhxxn81rKsh0V
"""

import pandas as pd

m=pd.read_excel("/content/Sample - Superstore.xls")

m

m.describe()

#we will want state level using  want  data
m.isnull().sum()

m['Sales'].describe()

m.groupby('State')['Sales'].describe()

import seaborn as cat

cat.catplot(data=m,kind="bar",
            y="Sub-Category",x="Profit")