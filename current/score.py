# -*- coding: utf-8 -*-
 
import pandas as pd
import numpy as np
from pandas_ml import ConfusionMatrix

""" 
Example activitySequence
"""

# ('sitDown', 11.001, 2, 'sitting', 'default'),
# ('unk', 13.001, 1, 'sitting', 'default'),
# ('unk', 14.001, 1, 'sitting', 'default'),
# ('none', 15.001, 1, 'sitting', 'default'),
# ('none', 16.000999999999998, 1, 'sitting', 'default'),
# ('none', 17.000999999999998, 1, 'sitting', 'default'),
# ('none', 18.000999999999998, 1, 'sitting', 'default'),
# ('none', 19.000999999999998, 1, 'sitting', 'default'),
# ('none', 20.000999999999998, 1, 'sitting', 'default'),
# ('lieDown', 21.000999999999998, 3, 'lying', 'default')

""" 
Example eventLabels
"""
# startTime  endTime   event
#   0.005     10.500   rest   
#  15.000     18.000  standUp

""" 
Example activityLabels
"""

# startTime  endTime    major    minor
# 0.005      10.500   sitting  default
# 10.500     15.500   sitting  typing
# 15.500     20.000   sitting  default
# 20.000     25.000   standing default

"""
We assume that events/activities occur in windows which are a multiple of 1s.
Hence scoring is done over 1s windows.
"""

windowSize = 1

"""
Example: 
Input:
  Activity Sequence:    
  ('sitDown', 11.001, 2, 'sitting', 'default'),
  ('unk', 13.001, 1, 'sitting', 'default'),

  leftBound: 13.5
  
Output:
    sitting-default

"""

def findActivityLabels(leftBound, activitySequence):
    activitySeqStartTime = activitySequence[0][1]
    activitySeqEndTime = activitySequence[len(activitySequence)-1][1]
    
    if (leftBound < activitySeqStartTime) | (leftBound > activitySeqEndTime):
        return None
    
    for activity in activitySequence:
        activityStartTime = round(activity[1])
        activityEndTime = activityStartTime + round(activity[2])
        if (leftBound >= activityStartTime) & (leftBound+windowSize <= activityEndTime):
            return activity[3] + "-" + activity[4]

"""
Example: 
Input:
  Activity Sequence:    
  ('sitDown', 11.001, 2, 'sitting', 'default'),
  ('unk', 13.001, 1, 'sitting', 'default'),

  leftBound: 13.5
  
Output:
    unk

"""

def findEventLabel(leftBound, activitySequence):
    activitySeqStartTime = activitySequence[0][1]
    activitySeqEndTime = activitySequence[len(activitySequence)-1][1]
    
    if (leftBound < activitySeqStartTime) | (leftBound > activitySeqEndTime):
        return None
    
    for activity in activitySequence:
        activityStartTime = round(activity[1])
        activityEndTime = activityStartTime + round(activity[2])
        if (leftBound >= activityStartTime) & (leftBound+windowSize <= activityEndTime):
            return activity[0]
        
def matchActivities(activitySequence, activityLabels):
    
    obsVsPredLabels = pd.DataFrame(columns=['startTime', 'endTime', 'observed', 'predicted'])
    i = 0
    for index, obsActivity in activityLabels.iterrows():
        startTime = round(obsActivity['startTime'])
        endTime = round(obsActivity['endTime'])
        
        for leftBound in range(startTime, endTime):
            predActivity = findActivityLabels(leftBound, activitySequence)
            obsVsPredLabels.loc[i] = [leftBound, leftBound+windowSize, 
                               obsActivity['majorActivity'] + "-" + obsActivity['minorActivity'], 
                               predActivity]
            i += 1
    return obsVsPredLabels

def matchEvents(activitySequence, eventLabels):

    obsVsPredLabels = pd.DataFrame(columns=['startTime', 'endTime', 'observed', 'predicted'])
    i = 0
    for index, obsEvent in eventLabels.iterrows():
        startTime = round(obsEvent['startTime'])
        endTime = round(obsEvent['endTime'])
        
        for leftBound in range(startTime, endTime):
            predEvent = findEventLabel(leftBound, activitySequence)
            obsVsPredLabels.loc[i] = [leftBound, leftBound+windowSize, obsEvent['event'], predEvent]
            i += 1
    
    return obsVsPredLabels

def scoreFromLabels(obsLabels, predLabels, labelOrder):

    # s1 = pd.Series(obsLabels)
    # s1Int = s1.astype("category", categories=labelOrder).cat.codes
    # s2 = pd.Series(predLabels)
    # s2Int = s2.astype("category", categories=labelOrder).cat.codes
    
    # cm = ConfusionMatrix(s1Int, s2Int, labelOrder)
    # return (cm)
    return pd.crosstab(obsLabels, predLabels)

def accuracyFromCM(cm):
    correctPreds = 0
    numRows = cm.shape[0]
    for i in range(numRows):
        correctPreds = correctPreds + cm.iloc[i, i]

    totalSamples = np.sum(cm.values)
    return correctPreds/totalSamples
        
    
    
    
