 
import pandas as pd 

from progPath import pathVar
pathToTrainingData = pathVar + "eventTrainingData/"

from globalVars import eventsDict
from globalVars import reverseEventsDict
from trainingSetPrepHelper import clip
from trainingSetPrepHelper import convertRawToTrainingInstance

# In[38]:

def trainingDataFrom_walk1():
    trainingSet = pd.DataFrame()
# In[39]:


    dfO = pd.read_csv(pathToTrainingData+'walk1.csv')

    eventWindow = clip(dfO, 7.4, 8.7)
    label = eventsDict['walk'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
    eventWindow = clip(dfO, 8.7, 9.2)
    label = eventsDict['walk'][1]
    
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
    eventWindow = clip(dfO, 9.2, 9.9)
    label = eventsDict['walk'][1]
    
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
    eventWindow = clip(dfO, 9.9, 10.5)
    label = eventsDict['walk'][1]
    
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    return trainingSet