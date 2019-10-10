 
import pandas as pd
import matplotlib.pyplot as plt
import math

import sys
from progPath import pathVar
pathToTrainingData = pathVar + "eventTrainingData/"
sys.path += (pathToTrainingData)

def clip(DF, start, end):
    
    return DF.loc[(DF.time >= start) & (DF.time <= end)]

def duration(DF):
    return DF.time.min(), DF.time.max(), DF.time.max() - DF.time.min()


# dfO = pd.read_csv(path+'one.csv')
dfO = pd.read_csv('one.csv')

start, end, duration = duration(dfO)
print(start, end, duration)

fig=plt.figure(figsize=(15, 6), dpi= 80, facecolor='w', edgecolor='k')

plotDuration = 50
numPlots = math.ceil(duration/plotDuration)

for i in range(numPlots):
    df = clip(dfO, i*plotDuration, (i+1)*plotDuration)
    
    fig=plt.figure(figsize=(15, 4), dpi= 80, facecolor='w', edgecolor='k')
    plt1 = fig.add_subplot(111)
    plt1.plot(df['time'], df['ay'], color='blue')
    plt.grid(True)
    plt.show()
    
