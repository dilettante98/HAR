 
import pandas as pd
import sys

from globalVars import reverseEventsDict

testSet = pd.DataFrame()

from progPath import pathVar
pathToTestData = pathVar + "eventTestData/"
sys.path.append(pathToTestData)

from testDataFrom_ME1 import testDataFrom_ME1

# In[38]:

testSet = testDataFrom_ME1()

# In[39]:

"""
 load trained model and perform predictions.
 """

import pickle 

# load the model from disk
v = pickle.load(open('trainedEventClassifier.sav', 'rb'))
scaler = v[0]
model = v[1]

from globalVars import features
# testSet = trainingSet

# X_test = testSet[['ZCRY',
#                  'ZCRZ',
#                  'maxY',
#                  'maxZ']]

X_test = testSet[features].copy()

X_test[X_test.columns] = scaler.transform(X_test[X_test.columns])

predictionEvents = model.predict(X_test)

i = 0
matches = 0
for event in predictionEvents:
    print('Observed: ', testSet.iloc[i]['activity'],
          'Predicted: ', reverseEventsDict[event])
    if (testSet.iloc[i]['activity'] == reverseEventsDict[event]):
        matches = matches + 1
    i = i + 1
    
print(matches, 'out of', len(predictionEvents), 'correct.')

# add more events to the testSet