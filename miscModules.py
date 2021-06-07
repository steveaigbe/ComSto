# Function that analyzes and generates outlierstats
def outlierStats(outList):
    size = len(outList)
    if size == 0:
        outlier = 0
        maxOutlier = 0
        return (outlier, maxOutlier)
    else:
        outDict = {}
        for i in outList:
            if i not in outDict.keys():
                outDict[i] = 1
            else:
                outDict[i] = outDict[i] + 1
        outlier = sum(outDict.values())
        maxOutlier = max(outDict.keys())
        return (outlier, maxOutlier)

# Function that analyzes and generates peak stats
def peakStats(peak):
    peaks = peak[0]
    binsize = peak[1]
    modality = None
    bins = []
    modes = []
    size = len(peaks)
    for i in peaks.keys():
        bins.append(i)
        modes.append(peaks[i])
    return size, bins, modes, binsize

# Set precision function
def precision(val):
    return round(val, 2)

