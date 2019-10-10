
# coding: utf-8

# In[165]:


# import pandas as pd
# import statistics
# import matplotlib.pyplot as plt
# import seaborn as sns


# In[166]:


# get_ipython().magic('run ./globalVars')

# get_ipython().magic('run ./createTrainingSet')

from createEventTrainingSet import trainingSet
# from createEventTrainingSetMini import trainingSet
from globalVars import eventsDict
from globalVars import features

# In[167]:


import numpy as np
from sklearn.preprocessing import StandardScaler

np.random.seed(166)

def train():
    
    # X_train = trainingSet[['ZCRY', 
    #                       'ZCRZ',
    #                       'maxY',
    #                       'maxZ']]
    
    X_train = trainingSet[features].copy()
        
    y_train = trainingSet[['label']].values.ravel()
    
    # first scale the training data.
    scaler = StandardScaler()

    X_train[X_train.columns] = scaler.fit_transform(X_train[X_train.columns])

    # print(type(X_train))
    
    classifier = 'xgb'

    if (classifier == 'xgb'):
        import xgboost as xgb
        
#        params = list(booster = "gbtree", objective = "binary:logistic", 
#                      eta=0.3, gamma=0, max_depth=6, min_child_weight=1, 
#                      subsample=1, colsample_bytree=1)

        xg_clf = xgb.XGBClassifier(objective ='multi:softmax', 
                                   colsample_bytree = 1.0, 
                                   learning_rate = 0.1,
                                   subsample=1.0,
                                   max_depth = 5, 
                                   n_estimators = 20)

        xg_clf.fit(X_train, y_train)
        return (scaler, xg_clf)
    

    if (classifier == 'SVC'):
        from sklearn.svm import SVC 
        svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train) 

        return (scaler, svm_model_linear)

    if (classifier == 'knn'):
        # from sklearn.neighbors import KNeighborsClassifier
        # model = KNeighborsClassifier(n_neighbors=1)

        from augmentedKNN import KNNA
        model = KNNA(n_neighbors=1, NOTA=eventsDict["unk"][1], TP=0.5)

        model.fit(X_train, y_train)
    
        return (scaler, model)


# In[168]:


(scaler, model) = train()


# In[169]:


import pickle 

file_pi = open('trainedEventClassifier.sav', 'wb') 
temp = (scaler, model)
pickle.dump(temp, file_pi)
file_pi.close()

