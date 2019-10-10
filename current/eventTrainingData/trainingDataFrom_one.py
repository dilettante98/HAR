
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


def trainingDataFrom_one():
    trainingSet = pd.DataFrame()
# In[39]:


    one = pd.read_csv(pathToTrainingData + 'one.csv')
    one_1 = clip(one, 5, 50)

# First sit down event. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_1, 12, 15)
    label = eventsDict['sitDown'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# First doing nothing event. Add features to training set.
# -----------------------------------------------------------
    eventWindow = clip(one_1, 16, 20)
    label = eventsDict['rest'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# First lyingDown activity. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_1, 21, 25)
    label = eventsDict['lieDown'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# 1st situp event. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_1, 35, 41)
    label = eventsDict['sitUp'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# Second doing nothing event. Add features to training set.
# -----------------------------------------------------------
    eventWindow = clip(one_1, 42, 45)
    label = eventsDict['rest'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# First stand up activity. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_1, 46, 48)
    label = eventsDict['standUp'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[40]:


    one_2 = clip(one, 51, 100)

# Next sit down event. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_2, 57, 60)
    label = eventsDict['sitDown'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# Another doing nothing event. Add features to training set.
# -----------------------------------------------------------
    eventWindow = clip(one_2, 61, 64)
    label = eventsDict['rest'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# First lyingDown activity. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_2, 64, 69)
    label = eventsDict['lieDown'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# 2nd situp event. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_2, 84, 89)
    label = eventsDict['sitUp'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# Second stand up activity. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_2, 94, 98)
    label = eventsDict['standUp'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)


# In[41]:


    one_3 = clip(one, 140, 190)

# Next sit down event. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_3, 146, 149)
    label = eventsDict['sitDown'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# Another doing nothing event. Add features to training set.
# -----------------------------------------------------------
    eventWindow = clip(one_3, 151, 155)
    label = eventsDict['rest'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# First lyingDown activity. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_3, 155, 159)
    label = eventsDict['lieDown'][1]
    
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# 2nd situp event. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_3, 170, 176)
    label = eventsDict['sitUp'][1]
    
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# Second stand up activity. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_3, 180, 183)
    label = eventsDict['standUp'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    

# In[42]:


    one_4 = clip(one, 190, 235)

# Next sit down event. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_4, 191, 195)
    label = eventsDict['sitDown'][1]
    
    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)
    
# Another doing nothing event. Add features to training set.
# -----------------------------------------------------------
    eventWindow = clip(one_4, 204, 210)
    label = eventsDict['rest'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# First lyingDown activity. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_4, 198, 203)
    label = eventsDict['lieDown'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# 2nd situp event. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_4, 218, 223)
    label = eventsDict['sitUp'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

# Second stand up activity. Add features to training set.
# ------------------------------------------------------
    eventWindow = clip(one_4, 228, 232)
    label = eventsDict['standUp'][1]

    trainingInstance = convertRawToTrainingInstance(eventWindow, label, reverseEventsDict[label])
    trainingSet = trainingSet.append(trainingInstance)

    return trainingSet