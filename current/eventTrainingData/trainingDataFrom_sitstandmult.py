 

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
def trainingDataFrom_sitstandmult():

# In[0]:  
    df = pd.read_csv(pathToTrainingData+'sitstandmult.csv')
    
    trainingSet = pd.DataFrame()


# In[1]:  

    eventWindow = clip(df, 9, 12)
    label = eventsDict['sitDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

#    eventWindow = clip(df, 12, 16)
#    label = eventsDict['lieDown'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)


#    eventWindow = clip(df, 19, 23)
#    label = eventsDict['sitUp'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)

#    eventWindow = clip(df, 24, 26)
#    label = eventsDict['standUp'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)


    eventWindow = clip(df, 29, 32)
    label = eventsDict['sitDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

#    eventWindow = clip(df, 33, 36)
#    label = eventsDict['lieDown'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)


#    eventWindow = clip(df, 37, 41)
#    label = eventsDict['sitUp'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)

#    eventWindow = clip(df, 43, 45)
#    label = eventsDict['standUp'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)


    eventWindow = clip(df, 47, 50)
    label = eventsDict['sitDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

#    eventWindow = clip(df, 50, 54)
#    label = eventsDict['lieDown'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)


#    eventWindow = clip(df, 56, 59)
#    label = eventsDict['sitUp'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)

#    eventWindow = clip(df, 60, 62)
#    label = eventsDict['standUp'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)



    eventWindow = clip(df, 65, 68)
    label = eventsDict['sitDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

#    eventWindow = clip(df, 68, 72)
#    label = eventsDict['lieDown'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)



#    eventWindow = clip(df, 73, 77)
#    label = eventsDict['sitUp'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)


#    eventWindow = clip(df, 78, 80)
#    label = eventsDict['standUp'][1]
#    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
#    trainingSet = trainingSet.append(trainingInstance)

    return trainingSet



'''
# In[0]:  
df = pd.read_csv(path+'sitstandmult.csv')
print(df.head())
print()
print(df.tail())

trainingSet = pd.DataFrame()


# In[1]:  

fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 8, 18)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 9, 12)
label = eventsDict['sitDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

eventWindow = clip(df, 12, 16)
label = eventsDict['lieDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)



# In[2]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 17, 30)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 19, 23)
label = eventsDict['sitUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


eventWindow = clip(df, 24, 26)
label = eventsDict['standUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

# In[3]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 28, 36)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 29, 32)
label = eventsDict['sitDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

eventWindow = clip(df, 33, 36)
label = eventsDict['lieDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[2]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 36, 50)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 37, 41)
label = eventsDict['sitUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


eventWindow = clip(df, 43, 45)
label = eventsDict['standUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

# In[3]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 46, 60)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 47, 50)
label = eventsDict['sitDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

eventWindow = clip(df, 50, 54)
label = eventsDict['lieDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[2]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 54, 65)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 56, 59)
label = eventsDict['sitUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


eventWindow = clip(df, 60, 62)
label = eventsDict['standUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

# In[3]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 64, 74)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 65, 68)
label = eventsDict['sitDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

eventWindow = clip(df, 68, 72)
label = eventsDict['lieDown'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


# In[2]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 73, 85)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

eventWindow = clip(df, 73, 77)
label = eventsDict['sitUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)


eventWindow = clip(df, 78, 80)
label = eventsDict['standUp'][1]
trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
trainingSet = trainingSet.append(trainingInstance)

# In[9]:
fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 80, 90)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
# plt1.xaxis.set_ticks([1.,2.,3.,10.])
plt1.grid(True)
plt.legend()
plt.show()
'''