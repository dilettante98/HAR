 

import pandas as pd

from globalVars import eventsDict
from globalVars import reverseEventsDict
from trainingSetPrepHelper import clip
from trainingSetPrepHelper import convertRawToTrainingInstance

from progPath import pathVar
pathToTrainingData = pathVar + "eventTrainingData/"

# coding: utf-8

# In[36]:

'''
This file contains the following events: 
- sit-down (from standing position)
- lie-down
- turn (on back)
- turn (to left)
- turn (on back)
- turn (to left)
- sit up
- stand up
'''
def trainingDataFrom_standtostand1():

# In[0]:  
    df = pd.read_csv(pathToTrainingData+'standtostand1.csv')
    
    trainingSet = pd.DataFrame()


# In[2]:

    eventWindow = clip(df, 8.5, 12)
    label = eventsDict['sitDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# In[3]:

    eventWindow = clip(df, 16, 20)
    label = eventsDict['lieDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    

# In[4]:

    eventWindow = clip(df, 28, 32)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    

# In[5]:

    eventWindow = clip(df, 34, 37)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[6]:

    eventWindow = clip(df, 45, 49)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[7]:

    eventWindow = clip(df, 51, 55)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    


# In[8]:

    eventWindow = clip(df, 60, 64)
    label = eventsDict['sitUp'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    

    eventWindow = clip(df, 68, 70)
    label = eventsDict['standUp'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    return trainingSet


'''
# In[0]:  
df = pd.read_csv(path+'standtostand1.csv')
print(df.head())
print()
print(df.tail())

trainingSet = pd.DataFrame()


# In[1]:  

fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 0, 15)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()


# In[2]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 8, 15)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 8.5, 12)
label = eventsDict['sitDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

# In[3]:

fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 15, 25)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 16, 20)
label = eventsDict['lieDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[4]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 22, 34)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 28, 32)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[5]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 32, 40)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 34, 37)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[6]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 42, 50)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 45, 49)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[7]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 49, 60)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 51, 55)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)



# In[8]:

fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 58, 65)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 60, 64)
label = eventsDict['sitUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[9]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 64, 76)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
# plt1.xaxis.set_ticks([1.,2.,3.,10.])
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 68, 70)
label = eventsDict['standUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

'''