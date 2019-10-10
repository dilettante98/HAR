
# coding: utf-8

# In[12]:

events = ["rest", 
          "sitUp",
          "lieDown",
          "standUp",
          "sitDown",
          "walk",
          "turn",
          "type",
          "unk"
         ]

eventsDict = dict(zip(events, zip(events, range(0, len(events))))) 
reverseEventsDict = dict(zip(range(0, len(events)), events)) 

strongEvents = [eventsDict["sitUp"][0],
                eventsDict["lieDown"][0],
                eventsDict["standUp"][0],
                eventsDict["sitDown"][0],
                eventsDict["walk"][0]
               ]

weakEvents = list(set(events) - set(strongEvents))

superStates = ["unknown",
               "lying", 
               "sitting", 
               "standing", 
               "walking"]

SSDict = dict(zip(superStates, superStates))

internalStates = ["default",
                  "typing"]

ISDict = dict(zip(internalStates, internalStates))

internalStatesBySS = {SSDict["unknown"]: [ISDict["default"]],
                      SSDict["lying"]: [ISDict["default"]],
                      SSDict["sitting"]: [ISDict["default"], ISDict["typing"]],
                      SSDict["standing"]: [ISDict["default"]],
                      SSDict["walking"]: [ISDict["default"]]}


# transitions of super states
SSTransitions = {
        SSDict["unknown"]: 
            {eventsDict["sitDown"][0]: SSDict["sitting"],
             eventsDict["lieDown"][0]: SSDict["lying"],
             eventsDict["standUp"][0]: SSDict["standing"],
             eventsDict["sitUp"][0]: SSDict["sitting"],
             eventsDict["walk"][0]: SSDict["walking"]
             },
        SSDict["lying"]: 
            {eventsDict["sitUp"][0]: SSDict["sitting"]
            },
        SSDict["sitting"]: 
            {eventsDict["lieDown"][0]: SSDict["lying"],
             eventsDict["standUp"][0]: SSDict["standing"]
             }, 
        SSDict["standing"]: 
            {eventsDict["sitDown"][0]: SSDict["sitting"],
             eventsDict["walk"][0]: SSDict["walking"]
             },
        SSDict["walking"]: {eventsDict["rest"][0]: SSDict["standing"]
        }
    }

# transitions of internal states of a super state.
# two super state may have internal states with the same name.
# however, these internal states are considered to be different states.
internalTransitionsBySS = {
    SSDict["lying"]: {eventsDict["turn"][0]: ISDict["default"]},
    SSDict["sitting"]: {eventsDict["type"][0]: ISDict["typing"]}
}

# features = ['ZCRY', 'OSCRY', 'minMaxZ']
# features = ['ZCRY', 'OSCRY', 'minMaxZ', 'absAvgZ']
features = ['ZCRY', 'OSCRY', 'minMaxY', 'absAvgY', 'minMaxZ', 'absAvgZ']

# features = ['ZCRY', 'OSCRY', 'minMaxY', 'absAvgY']
# features = ['ZCRY', 'OSCRY', 'minMaxY', 'OSCRZ', 'minMaxZ']
# features = ['maxY']