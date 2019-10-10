
# coding: utf-8

# In[36]:


import pandas as pd
# import statistics


# In[37]:


from progPath import pathVar
pathToTrainingData = pathVar + "eventTrainingData/"

from globalVars import eventsDict
from globalVars import reverseEventsDict
from trainingSetPrepHelper import clip
from trainingSetPrepHelper import convertRawToTrainingInstance

# In[38]:

def trainingDataFrom_type1():
    trainingSet = pd.DataFrame()
# In[39]:

    dfO = pd.read_csv(pathToTrainingData+'type1.csv')

    eventWindow = clip(dfO, 5.0, 6.0)
    label = eventsDict['type'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 6.0, 7.0)
    label = eventsDict['type'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
    eventWindow = clip(dfO, 7.0, 8.0)
    label = eventsDict['type'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
    eventWindow = clip(dfO, 8.0, 9.0)
    label = eventsDict['type'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 21.0, 22.0)
    label = eventsDict['type'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
    eventWindow = clip(dfO, 24.0, 25.0)
    label = eventsDict['type'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
    eventWindow = clip(dfO, 26.0, 27.0)
    label = eventsDict['type'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
    eventWindow = clip(dfO, 28.0, 29.0)
    label = eventsDict['type'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
    return trainingSet

'''
# In[0]:  
df = pd.read_csv(path+'type1.csv')
print(df.head())
print()
print(df.tail())

trainingSet = pd.DataFrame()


# In[1]:  

fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 10, 20)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()

# In[1]:  

fig=plt.figure(figsize=(15, 8), dpi= 80, facecolor='w', edgecolor='k')
df1 = clip(df, 20, 30)
plt1 = fig.add_subplot(111)
plt1.plot(df1['time'], df1['ay'], color='blue', label='df1')
plt1.grid(True)
plt.legend()
plt.show()
'''