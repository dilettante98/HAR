 
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
def trainingDataFrom_standtostand3():

# In[0]:  
    df = pd.read_csv(pathToTrainingData+'standtostand3.csv')
    
    trainingSet = pd.DataFrame()


# In[1]:  

    eventWindow = clip(df, 11, 15)
    label = eventsDict['sitDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    
# In[2]:

    eventWindow = clip(df, 16, 21)
    label = eventsDict['lieDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[3]:

    eventWindow = clip(df, 26, 31)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[4]:

    eventWindow = clip(df, 34, 38)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
# In[5]:

    eventWindow = clip(df, 44, 48)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[6]:

    eventWindow = clip(df, 60, 65)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)



# In[7]:

    eventWindow = clip(df, 68, 70)
    label = eventsDict['sitUp'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


    return trainingSet



'''
# In[0]:  
df = pd.read_csv(path+'standtostand3.csv')
print(df.head())
print()
print(df.tail())

trainingSet = pd.DataFrame()


# In[1]:  

fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 10, 17)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 11, 15)
label = eventsDict['sitDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[2]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 16, 25)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 16, 21)
label = eventsDict['lieDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

# In[3]:

fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 25, 38)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 26, 31)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[4]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 32, 47)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 34, 38)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[5]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 42, 50)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 44, 48)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[6]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 50, 69)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 60, 65)
label = eventsDict['turn'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[7]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 66, 75)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 68, 70)
label = eventsDict['sitUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)



# In[8]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 72, 88)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

'''