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

dataset.shape
dataset.columns

dataset = dataset.drop("PassengerId", axis=1)
#if you take a close look, not all features like PassengerID
#function to remove 