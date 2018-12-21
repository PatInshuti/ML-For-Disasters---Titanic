#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 03:17:43 2018

@author: inshutimakubapatrick
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import dataset

dataset = pd.read_csv("train.csv")
data = dataset.describe()
#dataset = dataset.iloc[:].values

#lets use nearest k-nearest neigbours classfiers
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit()
