#import required libraries
import numpy as np
import statistics as st
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sc
from scipy.signal import find_peaks as fp
import math

from computeDist import compute_bins

"""Generate metrics to be used to compare histogram"""

# mean
def mean(obj):
    return round(st.mean(obj), 2)
    
# Standard Deviation
def stddev(obj):
    return round(st.stdev(obj), 2)

# Maximum Value
def maxval(obj):
    return round(max(obj), 2)

# Minimum Value
def minval(obj):
    return round(min(obj), 2)

# Skewness
def skewness(obj):
    xbar = st.mean(obj)
    n = len(obj)
    m2sum = 0
    for i in range(n):
        m2sum = m2sum + (obj[i] - xbar)**2
    m2 = m2sum/n
    m3sum = 0
    for i in range(n):
        m3sum = m3sum + (obj[i] - xbar) ** 3
    m3 = m3sum / n
    g1 = m3/(m2**(3/2))
    G1 = (math.sqrt(n*(n-1)) / (n - 2)) * g1
    return round(G1, 2)

# Outliers
def outliers(obj):
    b = 1.4826
    med1 = st.median(obj)
    newObj = []
    for i in obj:
        newObj.append(abs(i-med1))
    newObj = sorted(newObj)
    med2 = st.median(newObj)
    MAD = b * med2
    lowerLimit = med1 - (3.5*MAD)
    upperLimit = med1 + (3.5*MAD)
    outlier = []
    for i in obj:
        if i < lowerLimit or i > upperLimit:
            outlier.append(i)
    return outlier
    
# Peaks
def peaks(obj, D=0, setT=False):
    freq, bns, _ = plt.hist(x=obj, bins=compute_bins(obj, 10))
    n = len(freq)
    binsize = bns[2] - bns[1]
    peak = {}
    index = []
    if setT:
        T = np.quantile(freq, .25)
    else:
        T = 0
    if D == 0:
        for i in range(1,n-1):
            if freq[i] >= T:
                if freq[i] > freq[i-1]:
                    if freq[i] > freq[i+1]:
                        peak[bns[i]] = freq[i]
                    else:
                        k = 0
                        for j in range(1,n-i):
                            if freq[i] == freq[i+j]:
                                k = k+1
                            else:
                                break
                        if i+k+1 < n and freq[i] > freq[i+k+1]:
                            peak[bns[i]] = list(freq[i:i+k+1])
        return (peak, binsize)
    else:
        for i in range(1,n-1):
            if freq[i] >= T:
                if freq[i] > freq[i-1]:
                    if freq[i] > freq[i+1]:
                        peak[bns[i]] = freq[i]
                        index.append(i)
                        if len(index) > 1 and (index[-1] - index[-2]) < D:
                            del peak[bns[i]]
                    else:
                        k = 0
                        for j in range(1,n-i):
                            if freq[i] == freq[i+j]:
                                k = k+1
                            else:
                                break
                        if i+k+1 < n and freq[i] > freq[i+k+1]:
                            peak[bns[i]] = list(freq[i:i+k+1])
                            index.append(i)
                            if len(index) > 1 and (index[-1] - index[-2]) < D:
                                del peak[bns[i]]
        return (peak, binsize)

