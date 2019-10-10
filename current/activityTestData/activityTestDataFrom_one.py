 
import pandas as pd
import sys

from progPath import pathVar
pathToActivityData = pathVar + "activityTestData/"
sys.path.append(pathVar)


""" activity recordings file """
# activity will be recorded in a csv file produced by the accelerometer recorder. 
# Each row will contain a time stamp as well as the ax, ay, az, and aT values.
# The csv file can contain recording of multiple activities performed in sequence.
# an activity is defined as a major/minor pair such as 
# sitting/doing nothing, sitting/typing, lying/doing nothing, standing/doing nothing etc.
# the activities are expected to be performed in sequence.
# It is expected that the values in the time column should be increasing.
# It is also expected that the difference between the time stamps between two
# successive rows is always the same.
# EXample:
# --------
# time	ax	ay	az	aT
# 0.004	-0.2454	0.2262	-0.4795	0.584
# 0.005	-0.3421	0.2586	-0.2835	0.514
# 0.005	-0.3983	0.259	-0.2176	0.523
# 0.019	-0.4523	0.2249	-0.1254	0.52
# 0.020	-0.4957	0.1862	 0.0505	0.532

""" 
activityRecognition (FYI)
"""
# activity recordings file is used by the activityRecognizer to detect activities as major/minor activity pairs.
# The activityRecognizer takes the recording as an input and creates a sequence where each sequence contains the 
# following fields:
# event startTime endTime majorActivity minorActivity.
# since an event may not change the activity Type, a following sequence is possible:

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


""" activity labels file """
# ---------------------------
# a separate csv file should contain the activity labels as a pair of major/minor pairs along with the start and
# end times.
# If the activity in row i of the csv be activity[i].
# start time of activity[i] should be same as end time of activity[i-1].
# Also start time should be less than end time.
# Example
# --------
# startTime  endTime    major    minor
# 0.005      10.500   sitting  default
# 10.500     15.500   sitting  typing
# 15.500     20.000   sitting  default
# 20.000     25.000   standing default

def activity_windows():
    activityLabels = pd.DataFrame(columns = ['startTime', 'endTime', 'majorActivity', 'minorActivity'])
    
    labelID = 0
    activityLabels.loc[labelID] = [11.00, 21.00, 'sitting', 'default']
    labelID += 1
    activityLabels.loc[labelID] = [21.00, 35.00, 'lying', 'default']
    labelID += 1
    activityLabels.loc[labelID] = [35.00, 46.00, 'sitting', 'default']
#    labelID += 1
#    activityLabels.loc[labelID] = [46.00, 48.00, 'standing', 'default']
    
    return activityLabels
    

""" events label file """
# Activity consists of a sequence of events, some which are vigorous (strong events)
# some which are not vigorous (weak events). 
# From the point of view of activity characterization, an huge number of possibilites of events
# exist such as waving one's hand, flicking a coin, stretching or shifting one's position and we do not
# expect all different event types will be characterized. So if we do not have a characterization of an
# event or if we are unaware of the event type, we will call it an unknown (unk) event.

# An activity recordings file can also be accompanied by an events label file.
# This file can contain event types, event start time and event end time.
# Example
# --------
# startTime  endTime   event
#   0.005     10.500   rest   
#  15.000     18.000  standUp

# It will be assumed that start time of event[i] is >= endTime of event[i-1].
# Since all events may not be recorded, there can be a gap between the end time of event[i-1]
# and start time of event[i].

def event_windows():
    eventLabels = pd.DataFrame(columns = ['startTime', 'endTime', 'event'])
    
    labelID = 0
    eventLabels.loc[labelID] = [11.00, 16.00, 'sitDown']
    labelID += 1
    eventLabels.loc[labelID] = [21.00, 25.00, 'lieDown']
    labelID += 1
    eventLabels.loc[labelID] = [35.00, 41.00, 'sitUp']
#    labelID += 1
#    eventLabels.loc[labelID] = [46.00, 48.00, 'standUp']
    
    return eventLabels
   

def activityTestDataFrom_one():
    accel_file_name = 'one.csv'
    activitiesStartTime = 11
    activitiesEndTime = 48
   
    activities = activity_windows()
    events = event_windows()
    
    return (accel_file_name, activitiesStartTime, activitiesEndTime, activities, events)

# _, _, _, _, events = activityTestDataFrom_one()
# print(events)