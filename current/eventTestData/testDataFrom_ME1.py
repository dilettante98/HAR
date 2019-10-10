 


import pandas as pd

from progPath import pathVar
pathToTestData = pathVar + "eventTestData/"

from globalVars import eventsDict
from globalVars import reverseEventsDict
from trainingSetPrepHelper import clip
from trainingSetPrepHelper import convertRawToTrainingInstance

# In[38]:


def testDataFrom_ME1():
    trainingSet = pd.DataFrame()
# In[39]:

    dfO = pd.read_csv(pathToTestData + 'multEvents1.csv')

    eventWindow = clip(dfO, 6, 7)
    label = eventsDict['rest'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 8, 10)
    label = eventsDict['walk'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 25, 28)
    label = eventsDict['sitDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 31, 57)
    label = eventsDict['type'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 71, 74)
    label = eventsDict['standUp'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 88, 90)
    label = eventsDict['sitDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 92, 96)
    label = eventsDict['lieDown'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 101, 104)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 109, 112)
    label = eventsDict['turn'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    eventWindow = clip(dfO, 115, 119)
    label = eventsDict['sitUp'][1]
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    return trainingSet