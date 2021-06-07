# Templates to generate minimum measure sentence
def minTemp():
    minTemplates = {1:"Histogram1 has a minimum value of $minval1 $mincomp the minimum value $minval2 of histogram2. ", 
                2:"Histogram1's minimum value of $minval1 is $mincomp the minimum value $minval2 of histogram2. ",
                3:"Histogram1 with a minimum value of $minval1 is $mincomp histogram2's minimum value of $minval2. ",
                4:"Histogram1 and histogram2 have the same minimum value of $minval1. "}
    return minTemplates

# Templates to generate maximum measure sentence
def maxTemp():
    maxTemplates = {1:"Histogram1 has a maximum value of $maxval1 $maxcomp the maximum value $maxval2 of histogram2. ", 
                2:"Histogram1's maximum value of $maxval1 is $maxcomp the maximum value $maxval2 of histogram2. ",
                3:"Histogram1 with a maximum value of $maxval1 is $maxcomp histogram2's maximum value of $maxval2. ",
                4:"Histogram1 and histogram2 have the same maximum value of $maxval1. "}
    return maxTemplates

# Templates to generate mean measure sentence
def meanTemp():
    meanTemplates = {1:"Histogram1 has a mean of $meanval1 $meancomp the mean $meanval2 of histogram2. ", 
                2:"Histogram1's mean value of $meanval1 is $meancomp the mean $meanval2 of histogram2. ",
                3:"Histogram1 with a mean of $meanval1 is $meancomp histogram2's mean of $meanval2. ",
                4:"Histogram1 and histogram2 have the same mean value of $meanval1. "}
    return meanTemplates

# Templates to generate standard deviation measure sentence
def stdDevTemp():
    stdDevTemplates = {1:"Histogram1 has a standard deviation of $stdval1 $stdcomp the standard deviation $stdval2 of histogram2. ", 
                   2:"Histogram1's standard deviation of $stdval1 is $stdcomp the standard deviation $stdval2 of histogram2. ",
                   3:"Histogram1 with a standard deviation of $stdval1 is $stdcomp histogram2's standard deviation of $stdval2. ",
                   4:"Histogram1 and histogram2 have the same standard deviation value of $stdval1. "}
    return stdDevTemplates

# Templates to generate skewness measure sentence
def skewTemp():
    skewTemplates = {1:"Histogram1 has a skewness value of $skewtype1 while histogram2 has a skewness value of $skewtype2. ",
                 2:"Histogram1 has a skewness value of $skewtype1 but histogram2 has a skewness value of $skewtype2. ",
                 3:"Histogram1 and histogram2 both have the same skewness value of $skewtype1. "}
    return skewTemplates

# Templates to generate distance measure sentence
def distTemp():
    distTemplates = {1: "Histogram1 and histogram2 have a distance of $bdm and are $bdmcomp. Distance value close to 1 signifies histograms dissimilarity while value close to 0 signifies that the two histograms are identical. ",
                2: "Histogram1 and histogram2 are $bdmcomp with a distance value of $bdm. Distance value close to 1 signifies histograms dissimilarity while value close to 0 signifies that the two histograms are identical. "}
    return distTemplates

# Templates to generate Outlier measure sentence
def outTemp1():
    outTemplates1 = {1: "Both histograms have no outliers. ",
                 2: "Both histograms have $numOutlier1 outliers. "}
    return outTemplates1

# Templates to generate Outlier measure sentence
def outTemp2():
    outTemplates2 = {1: "Histogram1 has $numOutlier1 outliers with a maximum outlier of $maxOutlier1 while Histogram2 has $numOutlier2 outliers. ",
                 2: "Histogram1 has $numOutlier1 outliers with a maximum outlier of $maxOutlier1 but Histogram2 has no outliers. "}
    return outTemplates2

# Templates to generate Outlier measure sentence
def outTemp3():
    outTemplates3 = {1: "Histogram1 has $numOutlier1 outliers while Histogram2 has $numOutlier2 outliers with a maximum outlier of $maxOutlier2. ",
                 2: "Histogram1 has no outliers but Histogram2 has $numOutlier2 outliers with a maximum outlier of $maxOutlier2. "}
    return outTemplates3

# Templates to generate Outlier measure sentence
def outTemp4():
    outTemplates4 = {1: "Histogram1 has $numOutlier1 outliers with a maximum outlier of $maxOutlier1 while Histogram2 has $numOutlier2 outliers with a maximum outlier of $maxOutlier2. ",
                 2: "Histogram1 has $numOutlier1 outliers with a maximum outlier of $maxOutlier1 but Histogram2 has $numOutlier2 outliers with a maximum outlier of $maxOutlier2. "}
    return outTemplates4

# Templates to generate Outlier measure sentence
def outTemp5():
    outTemplates5 = {1: "Histogram1 has $numOutlier1 outliers same as histogram2. ",
                 2: "Both histograms have $numOutlier1 outliers. "}
    return outTemplates5

# Templates to generate peak measure sentence
def peakRegionTemp():
    peakRegionTemplates = {1: "The two histograms agree at $agreenum peaks region at $agreebins. ",
                       2: "The two histograms have $agreenum peaks region of agreement at $agreebins. "}
    return peakRegionTemplates

# Templates to generate peak measure sentence for histogram1
def hist1PeakTemp():
    hist1PeakTemplates = {1: "Histogram1's first peak is at bin $binpos1 with a height of $freqnum1. ",
                      11: "Histogram1's first peak is at bin $binpos1 to $binpos2 with a height of $freqnum1. ",
                      2: "Histogram1's second peak is at bin $binpos1 with a height of $freqnum1. ",
                      22: "Histogram1's second peak is at bin $binpos1 to $binpos2 with a height of $freqnum1. ",
                      3: "Histogram1's third peak is at bin $binpos1 with a height of $freqnum1. ",
                      33: "Histogram1's third peak is at bin $binpos1 to $binpos2 with a height of $freqnum1. ",
                      4: "Histogram1's fourth peak is at bin $binpos1 with a height of $freqnum1. ",
                      44: "Histogram1's fourth peak is at bin $binpos1 to $binpos2 with a height of $freqnum1. ",
                      5: "Histogram1's fifth peak is at bin $binpos1 with a height of $freqnum1. ",
                      55: "Histogram1's fifth peak is at bin $binpos1 to $binpos2 with a height of $freqnum1. "}
    return hist1PeakTemplates

# Templates to generate peak measure sentence for histogram1
def hist2PeakTemp():
    hist2PeakTemplates = {1: "Histogram2's first peak is at bin $binpos1 with a height of $freqnum1. ",
                      11: "Histogram2's first peak is at bin $binpos1 to $binpos2 with a height of $freqnum1. ",
                      2: "Histogram2's second peak is at bin $binpos1 with a height of $freqnum1. ",
                      22: "Histogram2's second peak is at bin $binpos1 to $binpos2 with a height of $freqnum1. ",
                      3: "Histogram2's third peak is at bin $binpos1 with a height of $freqnum1. ",
                      33: "Histogram2's third peak is at bin $binpos1 to $binpos2 with a height of $freqnum1. ",
                      4: "Histogram2's fourth peak is at bin $binpos1 with a height of $freqnum1. ",
                      44: "Histogram2's fourth peak is at bin $binpos1 to $binpos2 with a height of $freqnum1. ",
                      5: "Histogram2's fifth peak is at bin $binpos1 with a height of $freqnum1. ",
                      55: "Histogram2's fifth peak is at bin $binpos1 to $binpos2 with a height of $freqnum1. "}
    return hist2PeakTemplates

# Templates to generate peak measure sentence for short story
def shortPeakTemp():
    shortPeakTemplates = {1: "Histogram1 is $modality1 with $peaksize1 peaks while histogram2 is $modality2 with $peaksize2 peaks. ",
                      2: "Histogram1 with $peaksize1 peaks is $modality1 while Histogram2 with $peaksize2 peaks is $modality2. ",
                      3: "Histogram1 and Histogram2 are both $modality1 with $peaksize1 peaks. "}
    return shortPeakTemplates

