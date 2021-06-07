# Templates to generate minimum measure sentence for short story
def shortMinTemp():
    shortMinTemplates = {1:"Histogram1 has a minimum value of $minval1 while histogram2 has a minimum value of $minval2. ",
                    2:"Histogram1's minimum value is $minval1 and histogram2’s minimum value is $minval2. ",
                    3:"Histogram1 and histogram2 have the same minimum value of $minval1. "}
    return shortMinTemplates

# Templates to generate maximum measure sentence for short story
def shortMaxTemp():
    shortMaxTemplates = {1:"Histogram1 has a maximum value of $maxval1 while histogram2 has a maximum value of $maxval2. ",
                     2:"Histogram1's maximum value is $maxval1 and histogram2’s maximum value is $maxval2. ",
                     3:"Histogram1 and histogram2 have the same maximum value of $maxval1. "}
    return shortMaxTemplates

# Templates to generate maximum measure sentence for short story
def shortMeanTemp():
    shortMeanTemplates = {1:"Histogram1 has a mean of $meanval1 but histogram2 has a mean of $meanval2. ",
                      2:"Histogram1's mean is $meanval1 and histogram2’s mean is $meanval2. ",
                      3:"Histogram1's mean is $meanval1 while histogram2’s mean is $meanval2. ",
                      4:"Histogram1 and histogram2 have the same mean value of $meanval1. "}
    return shortMeanTemplates

# Templates to generate standard deviation measure sentence for short story
def shortStdTemp():
    shortStdTemplates = {1:"Histogram1 has a standard deviation of $stdval1 while histogram2 has a standard deviation of $stdval2. ",
                     2:"Histogram1's standard deviation is $stdval1 and histogram2’s standard deviation is $stdval2. ",
                     3:"Histogram1 and histogram2 the same standard deviation value of $stdval1. "}
    return shortStdTemplates

# Templates to generate skewness measure sentence for short story
def shortSkewTemp():
    shortSkewTemplates = {1:"Histogram1 has a skewness value of $skewtype1 while histogram2 has a skewness value of $skewtype2. ",
                     2:"Histogram1 has a skewness value of $skewtype1 but histogram2 has a skewness value of $skewtype2. ",
                     3:"Histogram1 and histogram2 both have the same skewness value of $skewtype1. "}
    return shortSkewTemplates

# Templates to generate outlier measure sentence for short story
def shortOutTemp():
    shortOutTemplates = {1:"Histogram1 has $numOutlier1 outliers while Histogram2 has $numOutlier2 outliers. ",
                     2:"Both histograms have $numOutlier1 outliers. "}
    return shortOutTemplates

# Templates to generate peak measure sentence for short story
def shortPeakTemp():
    shortPeakTemplates = {1:"Histogram1 is $modality1 with $peaksize1 peaks while histogram2 is $modality2 with $peaksize2 peaks. ",
                      2:"Histogram1 with $peaksize1 peaks is $modality1 while Histogram2 with $peaksize2 peaks is $modality2. ",
                      3:"Histogram1 and Histogram2 are both $modality1 with $peaksize1 peaks. "}
    return shortPeakTemplates
