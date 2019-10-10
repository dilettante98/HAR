
# coding: utf-8

# In[36]:


import pandas as pd
# import statistics


# In[37]:


# get_ipython().magic('run ./globalVars')
# get_ipython().magic('run ./trainingSetPrepHelper')

# from globalVars import eventsDict
# from globalVars import reverseEventsDict
# from trainingSetPrepHelper import clip
# from trainingSetPrepHelper import convertRawToTrainingInstance

import sys
from progPath import pathVar
pathToTrainingData = pathVar + "eventTrainingData/"
sys.path.append(pathToTrainingData)

from trainingDataFrom_one import trainingDataFrom_one
from trainingDataFrom_walk1 import trainingDataFrom_walk1
from trainingDataFrom_type1 import trainingDataFrom_type1
from trainingDataFrom_standtostand1 import trainingDataFrom_standtostand1
from trainingDataFrom_standtostand2 import trainingDataFrom_standtostand2
from trainingDataFrom_standtostand3 import trainingDataFrom_standtostand3
from trainingDataFrom_sitstandmult import trainingDataFrom_sitstandmult

# In[38]:

trainingSet = trainingDataFrom_one()

# In[39]:

trainingSetNext = trainingDataFrom_walk1()
trainingSet = pd.concat([trainingSet, trainingSetNext], axis=0)
# In[40]:

trainingSetNext = trainingDataFrom_type1()
trainingSet = pd.concat([trainingSet, trainingSetNext], axis=0)

# In[41]:

# trainingSetNext = trainingDataFrom_lyingTurning1()
# trainingSet = pd.concat([trainingSet, trainingSetNext], axis=0)

# In[42]:

trainingSetNext = trainingDataFrom_standtostand1()
trainingSet = pd.concat([trainingSet, trainingSetNext], axis=0)

# In[43]:

trainingSetNext = trainingDataFrom_standtostand2()
trainingSet = pd.concat([trainingSet, trainingSetNext], axis=0)


# In[44]:

trainingSetNext = trainingDataFrom_standtostand3()
trainingSet = pd.concat([trainingSet, trainingSetNext], axis=0)

# In[45]:

# trainingSetNext = trainingDataFrom_standtostand4()
# trainingSet = pd.concat([trainingSet, trainingSetNext], axis=0)

# In[45]:

trainingSetNext = trainingDataFrom_sitstandmult()
trainingSet = pd.concat([trainingSet, trainingSetNext], axis=0)

# In[0]:

trainingSet.sort_values(['start_time'], ascending=True, inplace=True)
trainingSet.set_index(pd.Series(range(0, trainingSet.shape[0])), inplace=True)

trainingSet.to_csv('trainingSet.csv')

