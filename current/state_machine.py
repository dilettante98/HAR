
# coding: utf-8

# In[28]:


# FSM specification.
# FSM consists of super states, internal states and events.

# Super states will have a list of internal states including a internal state which 
# is a default/start state for the super state.
# Super states are simply an encapsulation of minor states. They are not real states
# and hence do not have their own transition function.
# For example, there may be a super state called "sitting" with corresponding minor states
# "default" (corresponds to sitting doing nothing for example), "eating", "talking", "typing"
# etc.

# Transitions are defined for each state.
# There are events which cause transition from one super state to another. 
# For example "stand-up" event can cause transition from super state "sitting" to "standing".
# In actuality, this corresponds to a transition from the internal state of "sitting", regardless of
# the internal state, to the "default" internal state of super state "standing".
# Again, for convenience, super state transition functions will be defined, but
# it should be noted that these functions correspond to transitions for each
# internal state of the source super state to the default internal state of the target
# super state.

# Each internal state will ofcourse have its next state function.

# A dictionary will be used to describe next state function.
# Keys will correspond to events.
# Values will correspond to next state.
# States should belong to a global list of states. 
# Events should belong to a global list of events.

# Special functions may be defined for every state. For example,
# 1. Number of times state has been visited can be stored.
# 2. Transition on "none" events. For "numNone" consecutive "none" events, a transition 
#   is made to a default minor state.


# In[43]:


# 1. It is assumed that the state with an integer label of "0" is the default state.
# 2. It is assumed that if an event is not listed for a given state, then on that event,
#    the state remains unchanged.
# 3. If an event causes super state to change, internal state gets set to default state
#    of the super state.

# get_ipython().magic('run ./globalVars')


# In[44]:

from globalVars import ISDict
from globalVars import SSDict

class superState:
    
    def __init__(self, 
                 name, 
                 internalStatesBySS, 
                 internalTransitionsBySS):
        self.name = name
    
        # create the internal states and their transitions.
        self.intStateObjs = {}
        
        SSinternalStates = internalStatesBySS[name]
        
        # TBD: there should be an exception if no internal states, since default state 
        # atleast should be there.
        
        for intStateName in SSinternalStates:
            intStateObj = state(intStateName)
            self.intStateObjs[intStateName] = intStateObj
            
            if (intStateName == ISDict['default']):
                self.defaultIntStateObj = intStateObj
                self.setInternalState(intStateObj)
                
        # TBD: check if default internal state has been defined. if not, raise an exception.
        # now add the transitions for every internal state.
        # there should be atleast one internal state, the default state.
        # but there may not be any state transitions for the internal states.
        if self.name in internalTransitionsBySS:
            intTransitions = internalTransitionsBySS[self.name]
        else:
            intTransitions = None
            
        for intStateName in self.intStateObjs:    
            intStateObj = self.intStateObjs[intStateName]
            intStateObj.createTransitions(self.intStateObjs,
                                          intTransitions)

    def createTransitions(self,
                          superStates,
                          SSTransitions):
        self.transitions = {} # This will be a dict of event:SuperState's.
        
        thisSSTransitions = SSTransitions[self.name]
        for event in thisSSTransitions:
            nextSSName = thisSSTransitions[event]
            nextSSObj = superStates[nextSSName]
            self.transitions[event] = nextSSObj

        return
    
    def transition(self, 
                   event):
        
        # super state is going to change. Internal state of self is no longer relevant.
        if event in self.transitions:
            nextSSObj = self.transitions[event]
            return nextSSObj
        
        # super state unchanged. internal state might change.
        nextSObj = self.intStateObj.transition(event)
        self.setInternalState(nextSObj)
        
        # return next superState as self.
        return self
    
    def setInternalState(self, 
                         internalState):
        self.intStateObj = internalState

    def setDefaultInternalState(self):
        self.intStateObj = self.defaultIntStateObj

    def internalState(self):
        return self.intStateObj
    
    def getName(self):
        return self.name
    


# In[45]:


class state:
    
    def __init__(self, name):
        self.name = name
        
    def createTransitions(self,
                          intStateObjs,
                          internalTransitions):
        
        self.transitions = {} # This will be a dict of event:intState's.
        
        if (internalTransitions == None):
            return
        
        for event in internalTransitions:
            nextStateName = internalTransitions[event]
            nextStateObj = intStateObjs[nextStateName]
            self.transitions[event] = nextStateObj
            
        return
        
    def transition(self, 
                   event):
        if event in self.transitions:
            return self.transitions[event]
 
        # else state is unchanged.
        return self
    
    def getName(self):
        return self.name
    


# In[46]:


class FSM:
    
    def __init__(self, 
                 superStates, 
                 internalStatesBySS, 
                 SSTransitions, 
                 internalTransitionsBySS):
        
        self.superStateObjs = {}
        
        # create a superState object for each superState.
        # superStates will create their internalStates in turn.
        for stateName in superStates:
            SSObj = superState(stateName, 
                               internalStatesBySS, 
                               internalTransitionsBySS)
            
            if (stateName == SSDict["unknown"]): # We got the starting or default super state.
                self.currSSObj = SSObj
            
            self.superStateObjs[stateName] = SSObj
            
        # create the transitions between the superStates.
        for stateName in self.superStateObjs:
            SSObj = self.superStateObjs[stateName]
            SSObj.createTransitions(self.superStateObjs,
                                    SSTransitions)
            
    def transition(self, 
                   event):
        nextSSObj = self.currSSObj.transition(event)
        if (nextSSObj != self.currSSObj):
            nextSSObj.setDefaultInternalState()
            self.currSSObj = nextSSObj
            
        return (self.currSSObj, self.currSSObj.internalState())
    
    def currentStateLabels(self):
        return (self.currSSObj.getName(), self.currSSObj.internalState().getName())


# In[48]:


# activity_fsm = FSM(superStates,
#                    internalStatesBySS, 
#                    SSTransitions, 
#                    internalTransitionsBySS)

# (SSName, intSName) = activity_fsm.currentStateLabels()
# print(SSName, intSName)

# activity_fsm.transition("standUp")
# (SSName, intSName) = activity_fsm.currentStateLabels()
# print(SSName, intSName)

# activity_fsm.transition("sitDown")
# (SSName, intSName) = activity_fsm.currentStateLabels()
# print(SSName, intSName)

# activity_fsm.transition("talk")
# (SSName, intSName) = activity_fsm.currentStateLabels()
# print(SSName, intSName)

# activity_fsm.transition("liedown")
# (SSName, intSName) = activity_fsm.currentStateLabels()
# print(SSName, intSName)

# "none": 0, 
# "situp": 1,
# "liedown": 2,
# "standUp": 3,
# "sitDown": 4,
# "walk": 5,
# "talk": 6,
# "read": 7,
# "type": 8,
# "unknown": 9


# In[50]:


# activity_fsm.transition("talk")
# (SSName, intSName) = activity_fsm.currentStateLabels()
# print(SSName, intSName)

