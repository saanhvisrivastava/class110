# -*- coding: utf-8 -*-
"""class110.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n8GcpffSsXXr4y9TjgCq9RcQ65XD9pgm
"""

import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import random

df=pd.read_csv("data.csv")
#print(df)
data=df["temp"].tolist()
#print(data)
population_mean=sum(data)/len(data)
print("Population Mean",population_mean)
#median=statistics.median(data)
#(median)
#mode=statistics.mode(data)
#print("Mode=",mode)
stdev=statistics.stdev(data)
print("Standard deviation of population =",stdev)

dataset=[]
for i in range(0,100):
  random_index=random.randint(0,len(data))
  value=data[random_index]
  dataset.append(value)

#print(dataset)

mean=statistics.mean(dataset)
print("Mean of sample=",mean)

stdev=statistics.stdev(dataset)
print("Standard deviation of sample data set=",stdev)

#def calculate_deviation():


def random_set_of_mean(counter):
  dataset=[]
  for i in range(0,counter):
    random_index=random.randint(0,len(data)-1)
    value1=data[random_index]
    dataset.append(value1)
  
  mean=statistics.mean(dataset)
  return mean

def show_fig(mean_list):
  df=mean_list
  fig=ff.create_distplot([dataset],["Temperature mean"],show_hist=False)
  fig.show()

def setup():
  mean_list=[]
  for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)
  show_fig(mean_list)
  mean=statistics.mean(mean_list)
  print("Mean of sampling data=",mean)

  
  

setup()

  

   







#fig=ff.create_distplot([data],["Temperature"],show_hist=False)
#fig.show()