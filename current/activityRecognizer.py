
# coding: utf-8

# In[10]:


import pandas as pd

from progPath import pathVar
pathToTestData = pathVar + "testData/"

from state_machine import FSM
from globalVars import superStates
from globalVars import eventsDict
from globalVars import internalStatesBySS, SSTransitions, internalTransitionsBySS
from eventStreamPartitioner import find_events
from trainingSetPrepHelper import clip

# activitySequence consists of items, where each item consists of the following tuple:
# (event, eventOffset (time event started), winSize (duration of event), resultantSuperState,
# resultantInternalState.
def activity_recognizer(fileName, startTime, endTime):
    accl_readings = pd.read_csv(fileName)
    accl_readings = clip(accl_readings, startTime, endTime)
    eventSequence = find_events(accl_readings)

    activity_fsm = FSM(superStates,
                       internalStatesBySS, 
                       SSTransitions, 
                       internalTransitionsBySS)

    # get initial state of the FSM. the FSM will remain in this state until the 
    # first event occurs.
    (initSSName, initIntSName) = activity_fsm.currentStateLabels()
    activitySequence = [(eventsDict["unk"][0], 0, eventSequence[0][1], initSSName, initIntSName)]
# print(eventSequence)

    for event in eventSequence:
        activity_fsm.transition(event[0])
        (SSName, intSName) = activity_fsm.currentStateLabels()
    # print(event[0])
    # print(SSName, intSName)
        activitySequence += [(event[0], event[1], event[2], SSName, intSName)]
    
    return activitySequence

