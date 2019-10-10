
# coding: utf-8

# In[ ]:


import pandas as pd
import statistics as stats

# In[1]:


# features from cmu papers (2 axes accelerometer and light sensor used.)
# features were generated for 4 second windows, with 20 samples per second.
# 1. empirical mean: mean
# 2. rms: arithmetic mean of the squares of a group of values.
# 3. std deviation: square root( 1/N sum( (xi - mean)^2 )
# 4. variance: std-dev^2
# 5. mean absolute deviation: mean of absolute value of deviation from the mean, i.e. 1/N sum(abs(xi - mean)).
# 6. zero crossing rate: average number of times the measured value crosses zero.
# 7. mean crossing rate: average number of times the measured value crosses mean of the values.
# 8. cumulative histogram (256 bins): ?
# 9. nth percentile (n = 5, 10,...95): 
#    the 20th percentile is the value (or score) below which 20% of the observations may be found. 
# 10. Interquartile range.
#     In descriptive statistics, the interquartile range (IQR), also called the midspread or middle 50%, 
#     or technically H-spread, is a measure of statistical dispersion, 
#     being equal to the difference between 75th and 25th percentiles, or between upper and lower quartiles,
#     IQR = Q3 −  Q1.
# 11. Sq of x^2, y^2
# 12. Decision Tree Classifier (18 nodes): ?

def start_times(DF, window_size):
    l = []
    activity_start_time = DF['time'].min()
    activity_end_time = DF['time'].max()    
    
    curr_window_start_time = activity_start_time
    while(curr_window_start_time < activity_end_time):
        curr_window_end_time = curr_window_start_time + window_size
        if (curr_window_end_time > activity_end_time):
            curr_window_end_time = activity_end_time
        
        l.append(curr_window_start_time)
        
        curr_window_start_time += window_size
        
    return l

def end_times(DF, window_size):
    l = []
    activity_start_time = DF['time'].min()
    activity_end_time = DF['time'].max()    
    
    curr_window_start_time = activity_start_time
    while(curr_window_start_time < activity_end_time):
        curr_window_end_time = curr_window_start_time + window_size
        if (curr_window_end_time > activity_end_time):
            curr_window_end_time = activity_end_time
        
        l.append(curr_window_end_time)
        
        curr_window_start_time += window_size
        
    return l

def absAvg(DF, colName, window_size):
    l = []
    activity_start_time = DF['time'].min()
    activity_end_time = DF['time'].max()    
    
    curr_window_start_time = activity_start_time
    while(curr_window_start_time < activity_end_time):
        curr_window_end_time = curr_window_start_time + window_size
        if (curr_window_end_time > activity_end_time):
            curr_window_end_time = activity_end_time
 
        activity_window = DF.loc[(DF.time >= curr_window_start_time) & (DF.time <= curr_window_end_time)]
        vals = activity_window[colName]
        absVals = [abs(x) for x in vals]
        
        l.append( sum(absVals)/len(absVals))
        
        curr_window_start_time += window_size
        
    return l

def ZCR(DF, colName, window_size):
    l = []
    activity_start_time = DF['time'].min()
    activity_end_time = DF['time'].max()    
    
    curr_window_start_time = activity_start_time
    while(curr_window_start_time < activity_end_time):
        curr_window_end_time = curr_window_start_time + window_size
        if (curr_window_end_time > activity_end_time):
            curr_window_end_time = activity_end_time
 
        activity_window = DF.loc[(DF.time >= curr_window_start_time) & (DF.time <= curr_window_end_time)]
        vals = activity_window[colName]

        crossings = 0
        for i in range(0, len(vals)-1):
            if (vals.iloc[i]*vals.iloc[i+1] < 0):
                crossings += 1
        l.append(crossings/(curr_window_end_time - curr_window_start_time))
        
        curr_window_start_time += window_size
        
    return l

def sampleVals(vals, sampleStep):
    sampleIndices = range(0, len(vals), sampleStep)
    samples = [vals.iloc[i] for i in sampleIndices]
    
    return samples

# find the number of times the waveform changes direction.
# Use sampling.
def OSCR(DF, colName, window_size, sampleStep):
    l = []
    activity_start_time = DF['time'].min()
    activity_end_time = DF['time'].max()    
    
    curr_window_start_time = activity_start_time
    while(curr_window_start_time < activity_end_time):
        curr_window_end_time = curr_window_start_time + window_size
        if (curr_window_end_time > activity_end_time):
            curr_window_end_time = activity_end_time
 
        activity_window = DF.loc[(DF.time >= curr_window_start_time) & (DF.time <= curr_window_end_time)]
        vals = activity_window[colName]
        sampledVals = sampleVals(vals, sampleStep)
        # sampledVals = vals

        oscCount = 0
        for i in range(0, len(sampledVals)-2):
            if ((sampledVals[i+1] - sampledVals[i]) * 
                (sampledVals[i+1] - sampledVals[i+2])) > 0:
                oscCount += 1
        l.append(oscCount/len(sampledVals))
        
        curr_window_start_time += window_size
        
    return l

def stdDev(DF, colName, window_size):
    l = []
    activity_start_time = DF['time'].min()
    activity_end_time = DF['time'].max()    
    
    curr_window_start_time = activity_start_time
    while(curr_window_start_time < activity_end_time):
        curr_window_end_time = curr_window_start_time + window_size
        if (curr_window_end_time > activity_end_time):
            curr_window_end_time = activity_end_time
 
        activity_window = DF.loc[(DF.time >= curr_window_start_time) & (DF.time <= curr_window_end_time)]
        vals = activity_window[colName]
    
        l.append(stats.stdev(vals))
        
        curr_window_start_time += window_size
        
    return l

def custMax(DF, colName, window_size):
    l = []
    activity_start_time = DF['time'].min()
    activity_end_time = DF['time'].max()    
    
    curr_window_start_time = activity_start_time
    while(curr_window_start_time < activity_end_time):
        curr_window_end_time = curr_window_start_time + window_size
        if (curr_window_end_time > activity_end_time):
            curr_window_end_time = activity_end_time
 
        activity_window = DF.loc[(DF.time >= curr_window_start_time) & (DF.time <= curr_window_end_time)]
        vals = activity_window[colName]
    
        l.append(max(vals))
        
        curr_window_start_time += window_size
        
    return l

def minMax(DF, colName, window_size):
    l = []
    activity_start_time = DF['time'].min()
    activity_end_time = DF['time'].max()    
    
    curr_window_start_time = activity_start_time
    while(curr_window_start_time < activity_end_time):
        curr_window_end_time = curr_window_start_time + window_size
        if (curr_window_end_time > activity_end_time):
            curr_window_end_time = activity_end_time
 
        activity_window = DF.loc[(DF.time >= curr_window_start_time) & (DF.time <= curr_window_end_time)]
        vals = activity_window[colName]
    
        l.append(max(vals) + min(vals))
        
        curr_window_start_time += window_size
        
    return l

# In[2]:

sampleStep = 4

def activity_data_to_features_v2(DF, window_size):
    featuresDF = pd.DataFrame()

    start_times_feat = start_times(DF, window_size)
    featuresDF = featuresDF.assign(start_time = start_times_feat)

    end_times_feat = end_times(DF, window_size)
    featuresDF = featuresDF.assign(end_time = end_times_feat)
    
    stdDevX_feat = stdDev(DF, 'ax', window_size)
    featuresDF = featuresDF.assign(stdDevX = stdDevX_feat)

    absAvgX_feat = absAvg(DF, 'ax', window_size)
    featuresDF = featuresDF.assign(absAvgX = absAvgX_feat)
    
    ZCRX_feat = ZCR(DF, 'ax', window_size)
    featuresDF = featuresDF.assign(ZCRX = ZCRX_feat)

    OSCRX_feat = OSCR(DF, 'ax', window_size, sampleStep)
    featuresDF = featuresDF.assign(OSCRX = OSCRX_feat)
    
    minMaxX_feat = minMax(DF, 'ax', window_size)
    featuresDF = featuresDF.assign(minMaxX = minMaxX_feat)
       
    stdDevY_feat = stdDev(DF, 'ay', window_size)
    featuresDF = featuresDF.assign(stdDevY = stdDevY_feat)

    absAvgY_feat = absAvg(DF, 'ay', window_size)
    featuresDF = featuresDF.assign(absAvgY = absAvgY_feat)
    
    ZCRY_feat = ZCR(DF, 'ay', window_size)
    featuresDF = featuresDF.assign(ZCRY = ZCRY_feat)
    
    OSCRY_feat = OSCR(DF, 'ay', window_size, sampleStep)
    featuresDF = featuresDF.assign(OSCRY = OSCRY_feat)
    
    minMaxY_feat = minMax(DF, 'ay', window_size)
    featuresDF = featuresDF.assign(minMaxY = minMaxY_feat)
   
    stdDevZ_feat = stdDev(DF, 'az', window_size)
    featuresDF = featuresDF.assign(stdDevZ = stdDevZ_feat)

    absAvgZ_feat = absAvg(DF, 'az', window_size)
    featuresDF = featuresDF.assign(absAvgZ = absAvgZ_feat)
    
    ZCRZ_feat = ZCR(DF, 'az', window_size)
    featuresDF = featuresDF.assign(ZCRZ = ZCRZ_feat)

    OSCRZ_feat = OSCR(DF, 'az', window_size, sampleStep)
    featuresDF = featuresDF.assign(OSCRZ = OSCRZ_feat)
    
    minMaxZ_feat = minMax(DF, 'az', window_size)
    featuresDF = featuresDF.assign(minMaxZ = minMaxZ_feat)
    
    maxX_feat = custMax(DF, 'ax', window_size)
    featuresDF = featuresDF.assign(maxX = maxX_feat)    
    
    maxY_feat = custMax(DF, 'ay', window_size)
    featuresDF = featuresDF.assign(maxY = maxY_feat)    
    
    maxZ_feat = custMax(DF, 'az', window_size)
    featuresDF = featuresDF.assign(maxZ = maxZ_feat)    
    
    return featuresDF


# In[3]:


def clip(DF, start, end):
    
    return DF.loc[(DF.time >= start) & (DF.time <= end)]


# In[4]:


def clip_boundaries(DF, clipSize):
    activity_start_time = DF['time'].min()
    activity_end_time = DF['time'].max()  
    
    return DF.loc[(DF.time >= activity_start_time + clipSize) & (DF.time <= activity_end_time - clipSize)]


# In[5]:


def add_label(DF, label):
    l = []
    for i in range(0, DF.shape[0]):
        l.append(label)
        
    return l


# In[8]:


def convertRawToTrainingInstance(eventWindow, label, intLabel):
  
    featuresDF = activity_data_to_features_v2(eventWindow,
                                              eventWindow['time'].max() - eventWindow['time'].min())
    label_col = add_label(featuresDF, label)
    featuresDFL = featuresDF.assign(label = label_col)
    activity_col = add_label(featuresDF, intLabel)
    featuresDFL = featuresDFL.assign(activity = activity_col)
  
    return featuresDFL

