 
import sys
from progPath import pathVar
pathToActivityData = pathVar + "activityTestData/"
sys.path.append(pathToActivityData)

from activityTestDataFrom_one import activityTestDataFrom_one

from activityRecognizer import activity_recognizer
from score import matchActivities
from score import matchEvents
from score import scoreFromLabels
from score import accuracyFromCM
# from helperFunctions import printActivitySequence

accel_file_name, activitiesStartTime, activitiesEndTime, activities, events = activityTestDataFrom_one()

activitiesEventsSeq = activity_recognizer(pathToActivityData + accel_file_name, activitiesStartTime, activitiesEndTime)
# printActivitySequence(activitySequence)

eventObsVsPred = matchEvents(activitiesEventsSeq, events)
uniqueEventLabels = list(eventObsVsPred['observed'].unique()) + list(eventObsVsPred['predicted'].unique())
uniqueEventLabels = list(set(uniqueEventLabels))
eventCM = scoreFromLabels(eventObsVsPred['observed'], eventObsVsPred['predicted'], uniqueEventLabels)

activityObsVsPred = matchActivities(activitiesEventsSeq, activities)
uniqueActivityLabels = list(activityObsVsPred['observed'].unique()) + list(activityObsVsPred['predicted'].unique())
uniqueActivityLabels = list(set(uniqueActivityLabels))
activityCM = scoreFromLabels(activityObsVsPred['observed'], activityObsVsPred['predicted'], uniqueActivityLabels)

print(eventObsVsPred)
print(activityObsVsPred)

# print(eventCM)
# print(activityCM)

print(eventCM.index)
print(eventCM.columns)
print(eventCM.values)
print('Event prediction accuracy:', accuracyFromCM(eventCM))

print(activityCM.index)
print(activityCM.columns)
print(activityCM.values)
print('Activity prediction accuracy:', accuracyFromCM(activityCM))