 

import pandas as pd
from progPath import pathVar
pathToTrainingData = pathVar + "eventTrainingData/"

from globalVars import eventsDict
from globalVars import reverseEventsDict
from trainingSetPrepHelper import clip
from trainingSetPrepHelper import convertRawToTrainingInstance

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
def trainingDataFrom_standtostand2():

# In[0]:  
    df = pd.read_csv(pathToTrainingData+'standtostand2.csv')
    
    trainingSet = pd.DataFrame()


# In[1]:  

    eventWindow = clip(df, 18, 21)
    label = eventsDict['sitDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
# In[2]:

    eventWindow = clip(df, 23, 27)
    label = eventsDict['lieDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[3]:

    eventWindow = clip(df, 33, 37)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[4]:

    eventWindow = clip(df, 42, 46)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
# In[5]:

    eventWindow = clip(df, 55, 58)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[6]:

    eventWindow = clip(df, 66, 70)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[7]:

    eventWindow = clip(df, 77, 81)
    label = eventsDict['sitUp'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[8]:

    eventWindow = clip(df, 87, 90)
    label = eventsDict['standUp'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    return trainingSet


'''
# In[0]:  
df = pd.read_csv(path+'standtostand2.csv')
print(df.head())
print()
print(df.tail())

trainingSet = pd.DataFrame()


# In[1]:  

fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 15, 23)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 18, 21)
label = eventsDict['sitDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[2]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 22, 35)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 23, 27)
label = eventsDict['lieDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

# In[3]:

fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 32, 38)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 33, 37)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[4]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 38, 47)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 42, 46)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[5]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 52, 60)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 55, 58)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[6]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 62, 72)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 66, 70)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[7]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 72, 85)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 77, 81)
label = eventsDict['sitUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)



# In[8]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 85, 95)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 87, 90)
label = eventsDict['standUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)



# In[9]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 95, 105)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
# plt1.xaxis.set_ticks([1.,2.,3.,10.])
plt1.grid(True)
plt.legend()
plt.show()
'''