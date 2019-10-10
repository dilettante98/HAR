
# coding: utf-8

# In[79]:


# An event is some movement or action such as:
# - standup, 
# - sitdown, 
# - (taking a) step,
# - utter (a word).

# When no movement is occurring, we call the situation a "nothing" or "none" event.

# Sometimes there is no gap between events, e.g. when we are walking, we take one step after another.
# But with events like "standing up", we can not have multiple "standing up" events one after the other.

# To distinguish between such events, we call the ones which do not occur more than once without some other
# event in between (e.g. situp liedown situp) as transition events.

# And the ones which can happen repetitively with possibly some "none" events in between as repetitive events.

# So we have three categories of events:
# transition events
# repetitive events
# none events

# We need to detect these different events given a stream of measurements taken while these events are being
# performed.

# Events will have a start time and an end time. The challenge is to identify the start and end time correctly.
# Once the start time and end time is identified correctly, the measurements between these two times need to be
# mapped to one of the many possible events.

# The problem of identifying the start and end time itself is a difficult one.
# One can start by assuming each event will have a none event before and after.
# However, this may not be true for repetitive events.
# For transition events, even if there is a none event before and after, the period of the none event may be very short 
# and hence it may be difficult to detect.

# method 1:
# if events, are bounded before and after by none events, detecting none events and then detecting the event 
# bounded by the none events is expected to provide higher accuracy in detection of events.

# consider the following sequence:
# none (3s), liedown(4s), none (3s).
#
# if event detection used 2s windows without consideration for none events, then the above sequence will be split
# into 
# window1: none (2s), 
# window2: none (1s) liedown(1s), 
# window3: liedown(2s), 
# window4: liedown(1s) none(1s), 
# window5: none(2s)
# Since window 2 and 4 contains a mix of events, and window 3 contains a subset of events, it may be hard to detect the
# correct event for these windows.
#
# on the other hand, if none windows of 1s duration are used to detect other events, and the other events
# are allowed to be of duration say 1 to 6s, then the above sequence would be split into:
# window1: none(1s)
# window2: none(1s)
# window3: none(1s)
# window4: liedown(4s)
# window5: none(1s)
# ...
# Since the windows are pure in the sense that they contain complete events of only a single type, it
# should be easier to identify the actual events in this case.

# we also split the activities into strong and weak events. 
# The idea is, strong events, if not considered over their full duration, may be identified as weak events.


# In[80]:


# it is assumed that there is an event identifier, which given a window of accelerometer readings, identified
# the event from a set of events that the readings most closely resemble. The event identifier in our case will be
# an ML pipeline.

# it is assumed that the shortest duration of an event is 1s, longest is 6s.
# from random import randint

# get_ipython().magic('run ./globalVars')
# get_ipython().magic('run ./eventClassifier')

from eventClassifier import eventClassifier

from globalVars import strongEvents
from globalVars import eventsDict

minWinSize = 1
maxWinSize = 6


# In[81]:


def find_event(accl_readings, offset):
    
    offset = round(offset)
    win = accl_readings.loc[(accl_readings.time >= offset) & (accl_readings.time < offset+minWinSize)]
    if(win.shape[0] == 0):
        return (None, offset)
    
    initEvent = eventClassifier(win)
#    if ((initEvent == "none")  | (initEvent in strongEvents)):
#         return (initEvent, minWinSize)
    
    if (initEvent == eventsDict["rest"][0]):
        return (initEvent, minWinSize)
    

    # try to find a strongEvent.
    # if for the given window size, the event is not recognized, extend window till maxWinSize.
    # if for the given window size, event is recognized as a strongEvent, try to extent window size
    # to max possible but still within maxWinSize such that event still remains a strongEvent.
    strongEventFound = False
    winSize = minWinSize + 1
    maxRecordedTime = round(accl_readings['time'].max())
    while (winSize <= maxWinSize) & (offset+winSize <= maxRecordedTime):
        win = accl_readings.loc[(accl_readings.time >= offset) & (accl_readings.time < offset+winSize)]
        # print(win)
        event = eventClassifier(win)
        if (event in strongEvents):
            strongEventFound = True
            strongEvent = event
            longestWinSize = winSize
        winSize = winSize + 1
        
    if (strongEventFound == True):
        return (strongEvent, longestWinSize)
    
    return (initEvent, minWinSize)
    


# In[82]:


def find_events(accl_readings):
    currOffset = accl_readings['time'].min()
    eventsSequence = []
    (nextEvent, winSize) = find_event(accl_readings, currOffset)
    while (nextEvent != None):
        eventsSequence.append((nextEvent, currOffset, winSize))
        currOffset = currOffset + winSize
        (nextEvent, winSize) = find_event(accl_readings, currOffset)
    return eventsSequence


