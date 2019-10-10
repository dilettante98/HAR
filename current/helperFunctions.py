 
# In[83]:
def printActivitySequence(activitySequence):
    
    for activity in activitySequence:
        print()
        print("Event: ", activity[0])
        print("start: ", round(activity[1], 2), "end: ", round(activity[1]+activity[2], 2)) 
        print("SS: ", activity[3])
        print("IS: ", activity[4])


