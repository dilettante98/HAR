
# coding: utf-8

# In[173]:


import pickle 

# load the model from disk
v = pickle.load(open('trainedEventClassifier.sav', 'rb'))
scaler = v[0]
model = v[1]


# In[176]:


# get_ipython().magic('run ./trainingSetPrepHelper')

from trainingSetPrepHelper import activity_data_to_features_v2
from globalVars import reverseEventsDict
from globalVars import features

def eventClassifier(win):
    winSize = win['time'].max() - win['time'].min()
    featuresDF = activity_data_to_features_v2(win, window_size=winSize)

    X_test = featuresDF[features].copy()

    # print(X_test)
    X_test[X_test.columns] = scaler.transform(X_test[X_test.columns])
 

    # print(X_test)
    prediction = model.predict(X_test)
    
    return reverseEventsDict[prediction[0]]


# y_test = add_label(X_test, label)


# In[175]:


# win = clip(one_4, 228, 232)
# event = eventClassifier(win)
# event

