#Import required libraries
import numpy as np
import statistics as st
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sc
from scipy.signal import find_peaks as fp
from yattag import Doc, indent
import random
import math
import seaborn as sns
from string import Template
import ast
import sys
import logging
logging.getLogger('matplotlib.font_manager').disabled = True

import GenMetrics
from xmlModules import genXMLOutput, xmlToFacts
from miscModules import peakStats, outlierStats, precision
from computeDist import compute_bins, bdm
from detailedStoryGen import minSentence, maxSentence, meanSentence, stdSentence, distSentence, outlierSentence, skewSentence
from detailedStoryGen import peakSentence, peak1Story, peak2Story, peakRegionSent, peakStory, storyGen, detailedPrint, fullPrint

from shortStoryGen import shortMinSentence, shortMaxSentence, shortMeanSentence, shortStdSentence, shortSkewSentence
from shortStoryGen import shortOutlierSentence, shortPeakSentence, shortStoryGen, myPrint

import clips
import logging
env = clips.Environment()
logging.basicConfig(level=10, format='%(message)s')
router = clips.LoggingRouter()
router.add_to_environment(env)

#set random seed
np.random.seed(444)
np.set_printoptions(precision=2)

num_arg = len(sys.argv)
if num_arg != 3:
    print("Please run the program correctly: 'main_prog.py <csv_input_file> <story_type>'")
    sys.exit()
    
data_val = pd.read_csv(sys.argv[1])
data1 = list(data_val.val1)
data2 = list(data_val.val2)

story_type = sys.argv[2]

def parameters(obj1, obj2):
    # Generates the comparison parameters as a json file
    data_input = {'Mean1': GenMetrics.mean(obj1), 'Mean2': GenMetrics.mean(obj2), 
            'StdDev1': GenMetrics.stddev(obj1), 'StdDev2': GenMetrics.stddev(obj2),
            'Max1': GenMetrics.maxval(obj1), 'Max2': GenMetrics.maxval(obj2),
            'Min1': GenMetrics.minval(obj1), 'Min2': GenMetrics.minval(obj2),
            'Skew_Value1': GenMetrics.skewness(obj1), 'Skew_Value2': GenMetrics.skewness(obj2), 
            'Outliers1': GenMetrics.outliers(obj1), 'Outliers2': GenMetrics.outliers(obj2),
            'Peaks1': GenMetrics.peaks(obj1), 'Peaks2': GenMetrics.peaks(obj2)}
    return data_input

# Compute histogram measures
data = parameters(data1, data2)

# Generate xml data object
main = genXMLOutput(data)
hist1, hist2 = xmlToFacts(main)

# Generate peak stats 
size1, binlist1, freq1, binsize1 = peakStats(ast.literal_eval(hist1['peak']))
size2, binlist2, freq2, binsize2 = peakStats(ast.literal_eval(hist2['peak']))
hist1['peakbinlist'] = str(binlist1)
hist2['peakbinlist'] = str(binlist2)
hist1['peakfreq'] = str(freq1)
hist2['peakfreq'] = str(freq2)
hist1['peakbinsize'] = str(binsize1)
hist2['peakbinsize'] = str(binsize2)
hist1['peaksize'] = str(size1)
hist2['peaksize'] = str(size2)

del hist1['peak']
del hist2['peak']

# Generate outliers stats
outlier1, outmax1 = outlierStats(ast.literal_eval(hist1['outlier']))
outlier2, outmax2 = outlierStats(ast.literal_eval(hist2['outlier']))
hist1['outlier'] = str(outlier1)
hist1['outmax'] = str(outmax1)
hist2['outlier'] = str(outlier2)
hist2['outmax'] = str(outmax2)

# Compute distance measure and add to facts
k = len(compute_bins(data1, 10)) - 1
bdmval = bdm(data1, data2)
hist1['distance'] = str(bdmval)
hist2['distance'] = str(bdmval)


env.clear()

template_string1 = """
(deftemplate histogram1
  (slot min1)
  (slot max1)
  (slot mean1)
  (slot std1)
  (slot distance)
  (slot skew1)
  (slot outlier1)
  (slot outlier1max)
  (slot peak1size)
  (slot peak1binlist)
  (slot peak1freq)
  (slot peak1binsize)
  )
"""

env.build(template_string1)
template1 = env.find_template('histogram1')
new_fact1 = template1.new_fact()

new_fact1['min1'] = ast.literal_eval(hist1['min'])
new_fact1['max1'] = ast.literal_eval(hist1['max'])
new_fact1['mean1'] = ast.literal_eval(hist1['mean'])
new_fact1['std1'] = ast.literal_eval(hist1['stdDev'])
new_fact1['distance'] = ast.literal_eval(hist1['distance'])
new_fact1['skew1'] = ast.literal_eval(hist1['skew'])
new_fact1['outlier1'] = ast.literal_eval(hist1['outlier'])
new_fact1['outlier1max'] = ast.literal_eval(hist1['outmax'])
new_fact1['peak1size'] = ast.literal_eval(hist1['peaksize'])
new_fact1['peak1binlist'] = hist1['peakbinlist']
new_fact1['peak1freq'] = hist1['peakfreq']
new_fact1['peak1binsize'] = ast.literal_eval(hist1['peakbinsize'])

new_fact1.assertit()

template_string2 = """
(deftemplate histogram2
  (slot min2)
  (slot max2)
  (slot mean2)
  (slot std2)
  (slot distance)
  (slot skew2)
  (slot outlier2)
  (slot outlier2max)
  (slot peak2size)
  (slot peak2binlist)
  (slot peak2freq)
  (slot peak2binsize)
  )
"""

env.build(template_string2)
template2 = env.find_template('histogram2')
new_fact2 = template2.new_fact()

new_fact2['min2'] = ast.literal_eval(hist2['min'])
new_fact2['max2'] = ast.literal_eval(hist2['max'])
new_fact2['mean2'] = ast.literal_eval(hist2['mean'])
new_fact2['std2'] = ast.literal_eval(hist2['stdDev'])
new_fact2['distance'] = ast.literal_eval(hist2['distance'])
new_fact2['skew2'] = ast.literal_eval(hist2['skew'])
new_fact2['outlier2'] = ast.literal_eval(hist2['outlier'])
new_fact2['outlier2max'] = ast.literal_eval(hist2['outmax'])
new_fact2['peak2size'] = ast.literal_eval(hist2['peaksize'])
new_fact2['peak2binlist'] = hist2['peakbinlist']
new_fact2['peak2freq'] = hist2['peakfreq']
new_fact2['peak2binsize'] = ast.literal_eval(hist2['peakbinsize'])

new_fact2.assertit()

env.define_function(shortMinSentence)
env.define_function(shortMaxSentence)
env.define_function(shortMeanSentence)
env.define_function(shortStdSentence)
env.define_function(shortSkewSentence)
env.define_function(shortOutlierSentence)
env.define_function(shortPeakSentence)
env.define_function(shortStoryGen)
env.define_function(myPrint)

env.define_function(minSentence)
env.define_function(maxSentence)
env.define_function(meanSentence)
env.define_function(stdSentence)
env.define_function(skewSentence)
env.define_function(distSentence)
env.define_function(precision)
env.define_function(outlierSentence)
env.define_function(peakSentence)
env.define_function(peak1Story)
env.define_function(peak2Story)
env.define_function(peakRegionSent)
env.define_function(peakStory)
env.define_function(storyGen)
env.define_function(fullPrint)
env.define_function(detailedPrint)

# Created rules for short story
Short_Rule1 = """
(defrule fill-short-max-template
(histogram1 (max1 ?max1))
(histogram2 (max2 ?max2))
=>
(bind ?max-sentence (shortMaxSentence ?max1 ?max2))
(assert (short-max-sentence ?max-sentence))
)
"""

env.build(Short_Rule1)

Short_Rule2 = """
(defrule fill-short-min-template
(histogram1 (min1 ?min1))
(histogram2 (min2 ?min2))
=>
(bind ?min-sentence (shortMinSentence ?min1 ?min2))
(assert (short-min-sentence ?min-sentence))
)
"""

env.build(Short_Rule2)

Short_Rule3 = """
(defrule fill-short-mean-template
(histogram1 (mean1 ?mean1))
(histogram2 (mean2 ?mean2))
=>
(bind ?mean-sentence (shortMeanSentence ?mean1 ?mean2))
(assert (short-mean-sentence ?mean-sentence))
)
"""

env.build(Short_Rule3)

Short_Rule4 = """
(defrule fill-short-std-template
(histogram1 (std1 ?std1))
(histogram2 (std2 ?std2))
=>
(bind ?std-sentence (shortStdSentence ?std1 ?std2))
(assert (short-std-sentence ?std-sentence))
)
"""
env.build(Short_Rule4)

Short_Rule5 = """
(defrule fill-short-skew-template
(histogram1 (skew1 ?skewness1))
(histogram2 (skew2 ?skewness2))
=>
(bind ?skew-sentence (shortSkewSentence ?skewness1 ?skewness2))
(assert (short-skew-sentence ?skew-sentence))
)
"""
env.build(Short_Rule5)

Short_Rule6 = """
(defrule fill-short-out-template
(histogram1 (outlier1 ?out1-result))
(histogram2 (outlier2 ?out2-result))
=>
(bind ?outlier-sentence (shortOutlierSentence ?out1-result ?out2-result))
(assert (short-outlier-sentence ?outlier-sentence))
)
"""

env.build(Short_Rule6)

Short_Rule7 = """
(defrule fill-short-peak-template
(histogram1 (peak1size ?pk1-result))
(histogram2 (peak2size ?pk2-result))
=>
(bind ?peak-sentence (shortPeakSentence ?pk1-result ?pk2-result))
(assert (short-peak-sentence ?peak-sentence))
)
"""

env.build(Short_Rule7)

Short_Rule8 = """
(defrule short-story-gen
(short-min-sentence ?min-sentence)
(short-max-sentence ?max-sentence)
(short-mean-sentence ?mean-sentence)
(short-std-sentence ?std-sentence)
(short-skew-sentence ?skew-sentence)
(short-outlier-sentence ?outlier-sentence)
(short-peak-sentence ?peak-sentence)
=>
(bind ?short-story (shortStoryGen ?min-sentence ?max-sentence ?mean-sentence ?std-sentence 
        ?skew-sentence ?outlier-sentence ?peak-sentence))
(assert (short-story ?short-story))
)
"""

env.build(Short_Rule8)

env.run()

#Created rules for detailed story
rule1 = """
(defrule max-match1
(histogram1 (max1 ?max1))
(histogram2 (max2 ?max2))
=>
(bind ?max-subs (- ?max1 ?max2))
(bind ?max-sub (precision ?max-subs))
(bind ?max-comp (= ?max-sub 0.00))
(assert (max-comp1 ?max-comp))
)
"""
env.build(rule1)

rule2 = """
(defrule max-match2
(max-comp1 TRUE)
=>
(bind ?max-comp-result "the same as")
(assert (max-compare ?max-comp-result))
)
"""
env.build(rule2)

rule3 = """
(defrule max-match3
(histogram1 (max1 ?max1))
(histogram2 (max2 ?max2))
=>
(bind ?max-subs (- ?max1 ?max2))
(bind ?max-sub (precision ?max-subs))
(bind ?max-subABS (abs ?max-sub))
(bind ?max-comp (and (> ?max-subABS 0.00) (<= ?max-subABS 0.50)))
(assert (max-comp2 ?max-comp))
)
"""
env.build(rule3)

rule4 = """
(defrule max-match4
(max-comp2 TRUE)
=>
(bind ?max-comp-result "similar to")
(assert (max-compare ?max-comp-result))
)
"""
env.build(rule4)

rule5 = """
(defrule max-match5
(histogram1 (max1 ?max1))
(histogram2 (max2 ?max2))
=>
(bind ?max-subs (- ?max1 ?max2))
(bind ?max-sub (precision ?max-subs))
(bind ?max-subABS (abs ?max-sub))
(bind ?max-subNEG (< ?max-sub 0.00))
(bind ?max-compABS (and (> ?max-subABS 0.50) (<= ?max-subABS 1.50)))
(bind ?max-comp (and ?max-subNEG ?max-compABS))
(assert (max-comp3 ?max-comp))
)
"""
env.build(rule5)

rule6 = """
(defrule max-match6
(max-comp3 TRUE)
=>
(bind ?max-comp-result "moderately smaller than")
(assert (max-compare ?max-comp-result))
)
"""
env.build(rule6)

rule7 = """
(defrule max-match7
(histogram1 (max1 ?max1))
(histogram2 (max2 ?max2))
=>
(bind ?max-subs (- ?max1 ?max2))
(bind ?max-sub (precision ?max-subs))
(bind ?max-subABS (abs ?max-sub))
(bind ?max-subNEG (< ?max-sub 0.00))
(bind ?max-compABS (> ?max-subABS 1.50)))
(bind ?max-comp (and ?max-subNEG ?max-compABS))
(assert (max-comp4 ?max-comp))
)
"""
env.build(rule7)

rule8 = """
(defrule max-match8
(max-comp4 TRUE)
=>
(bind ?max-comp-result "significantly smaller than")
(assert (max-compare ?max-comp-result))
)
"""
env.build(rule8)

rule9 = """
(defrule max-match9
(histogram1 (max1 ?max1))
(histogram2 (max2 ?max2))
=>
(bind ?max-subs (- ?max1 ?max2))
(bind ?max-sub (precision ?max-subs))
(bind ?max-subABS (abs ?max-sub))
(bind ?max-subPOS (> ?max-sub 0.00))
(bind ?max-compABS (and (> ?max-subABS 0.50) (<= ?max-subABS 1.50)))
(bind ?max-comp (and ?max-subPOS ?max-compABS))
(assert (max-comp5 ?max-comp))
)
"""
env.build(rule9)

rule10 = """
(defrule max-match10
(max-comp5 TRUE)
=>
(bind ?max-comp-result "moderately larger than")
(assert (max-compare ?max-comp-result))
)
"""
env.build(rule10)

rule11 = """
(defrule max-match11
(histogram1 (max1 ?max1))
(histogram2 (max2 ?max2))
=>
(bind ?max-subs (- ?max1 ?max2))
(bind ?max-sub (precision ?max-subs))
(bind ?max-subABS (abs ?max-sub))
(bind ?max-subPOS (> ?max-sub 0.00))
(bind ?max-compABS (> ?max-subABS 1.50))
(bind ?max-comp (and ?max-subPOS ?max-compABS))
(assert (max-comp6 ?max-comp))
)
"""
env.build(rule11)

rule12 = """
(defrule max-match12
(max-comp6 TRUE)
=>
(bind ?max-comp-result "significantly larger than")
(assert (max-compare ?max-comp-result))
)
"""
env.build(rule12)

rule13 = """
(defrule min-match1
(histogram1 (min1 ?min1))
(histogram2 (min2 ?min2))
=>
(bind ?min-subs (- ?min1 ?min2))
(bind ?min-sub (precision ?min-subs))
(bind ?min-comp (= ?min-sub 0.00))
(assert (min-comp1 ?min-comp))
)
"""
env.build(rule13)

rule14 = """
(defrule min-match2
(min-comp1 TRUE)
=>
(bind ?min-comp-result "the same as")
(assert (min-compare ?min-comp-result))
)
"""
env.build(rule14)

rule15 = """
(defrule min-match3
(histogram1 (min1 ?min1))
(histogram2 (min2 ?min2))
=>
(bind ?min-subs (- ?min1 ?min2))
(bind ?min-sub (precision ?min-subs))
(bind ?min-subABS (abs ?min-sub))
(bind ?min-comp (and (> ?min-subABS 0.00) (<= ?min-subABS 0.50)))
(assert (min-comp2 ?min-comp))
)
"""
env.build(rule15)

rule16 = """
(defrule min-match4
(min-comp2 TRUE)
=>
(bind ?min-comp-result "similar to")
(assert (min-compare ?min-comp-result))
)
"""
env.build(rule16)

rule17 = """
(defrule min-match5
(histogram1 (min1 ?min1))
(histogram2 (min2 ?min2))
=>
(bind ?min-subs (- ?min1 ?min2))
(bind ?min-sub (precision ?min-subs))
(bind ?min-subABS (abs ?min-sub))
(bind ?min-subNEG (< ?min-sub 0.00))
(bind ?min-compABS (and (> ?min-subABS 0.50) (<= ?min-subABS 1.50)))
(bind ?min-comp (and ?min-subNEG ?min-compABS))
(assert (min-comp3 ?min-comp))
)
"""
env.build(rule17)

rule18 = """
(defrule min-match6
(min-comp3 TRUE)
=>
(bind ?min-comp-result "moderately smaller than")
(assert (min-compare ?min-comp-result))
)
"""
env.build(rule18)

rule19 = """
(defrule min-match7
(histogram1 (min1 ?min1))
(histogram2 (min2 ?min2))
=>
(bind ?min-subs (- ?min1 ?min2))
(bind ?min-sub (precision ?min-subs))
(bind ?min-subABS (abs ?min-sub))
(bind ?min-subNEG (< ?min-sub 0.00))
(bind ?min-compABS (> ?min-subABS 1.50)))
(bind ?min-comp (and ?min-subNEG ?min-compABS))
(assert (min-comp4 ?min-comp))
)
"""
env.build(rule19)

rule20 = """
(defrule min-match8
(min-comp4 TRUE)
=>
(bind ?min-comp-result "significantly smaller than")
(assert (min-compare ?min-comp-result))
)
"""
env.build(rule20)

rule21 = """
(defrule min-match9
(histogram1 (min1 ?min1))
(histogram2 (min2 ?min2))
=>
(bind ?min-subs (- ?min1 ?min2))
(bind ?min-sub (precision ?min-subs))
(bind ?min-subABS (abs ?min-sub))
(bind ?min-subPOS (> ?min-sub 0.00))
(bind ?min-compABS (and (> ?min-subABS 0.50) (<= ?min-subABS 1.50)))
(bind ?min-comp (and ?min-subPOS ?min-compABS))
(assert (min-comp5 ?min-comp))
)
"""
env.build(rule21)

rule22 = """
(defrule min-match10
(min-comp5 TRUE)
=>
(bind ?min-comp-result "moderately larger than")
(assert (min-compare ?min-comp-result))
)
"""
env.build(rule22)

rule23 = """
(defrule min-match11
(histogram1 (min1 ?min1))
(histogram2 (min2 ?min2))
=>
(bind ?min-subs (- ?min1 ?min2))
(bind ?min-sub (precision ?min-subs))
(bind ?min-subABS (abs ?min-sub))
(bind ?min-subPOS (> ?min-sub 0.00))
(bind ?min-compABS (> ?min-subABS 1.50))
(bind ?min-comp (and ?min-subPOS ?min-compABS))
(assert (min-comp6 ?min-comp))
)
"""
env.build(rule23)

rule24 = """
(defrule min-match12
(min-comp6 TRUE)
=>
(bind ?min-comp-result "significantly larger than")
(assert (min-compare ?min-comp-result))
)
"""
env.build(rule24)

rule25 = """
(defrule mean-match1
(histogram1 (mean1 ?mean1))
(histogram2 (mean2 ?mean2))
=>
(bind ?mean-subs (- ?mean1 ?mean2))
(bind ?mean-sub (precision ?mean-subs))
(bind ?mean-comp (= ?mean-sub 0.00))
(assert (mean-comp1 ?mean-comp))
)
"""
env.build(rule25)

rule26 = """
(defrule mean-match2
(mean-comp1 TRUE)
=>
(bind ?mean-comp-result "the same as")
(assert (mean-compare ?mean-comp-result))
)
"""
env.build(rule26)

rule27 = """
(defrule mean-match3
(histogram1 (mean1 ?mean1))
(histogram2 (mean2 ?mean2))
=>
(bind ?mean-subs (- ?mean1 ?mean2))
(bind ?mean-sub (precision ?mean-subs))
(bind ?mean-subABS (abs ?mean-sub))
(bind ?mean-comp (and (> ?mean-subABS 0.00) (<= ?mean-subABS 0.50)))
(assert (mean-comp2 ?mean-comp))
)
"""
env.build(rule27)

rule28 = """
(defrule mean-match4
(mean-comp2 TRUE)
=>
(bind ?mean-comp-result "similar to")
(assert (mean-compare ?mean-comp-result))
)
"""
env.build(rule28)

rule29 = """
(defrule mean-match5
(histogram1 (mean1 ?mean1))
(histogram2 (mean2 ?mean2))
=>
(bind ?mean-subs (- ?mean1 ?mean2))
(bind ?mean-sub (precision ?mean-subs))
(bind ?mean-subABS (abs ?mean-sub))
(bind ?mean-subNEG (< ?mean-sub 0.00))
(bind ?mean-compABS (and (> ?mean-subABS 0.50) (<= ?mean-subABS 1.50)))
(bind ?mean-comp (and ?mean-subNEG ?mean-compABS))
(assert (mean-comp3 ?mean-comp))
)
"""
env.build(rule29)

rule30 = """
(defrule mean-match6
(mean-comp3 TRUE)
=>
(bind ?mean-comp-result "moderately smaller than")
(assert (mean-compare ?mean-comp-result))
)
"""
env.build(rule30)

rule31 = """
(defrule mean-match7
(histogram1 (mean1 ?mean1))
(histogram2 (mean2 ?mean2))
=>
(bind ?mean-subs (- ?mean1 ?mean2))
(bind ?mean-sub (precision ?mean-subs))
(bind ?mean-subABS (abs ?mean-sub))
(bind ?mean-subNEG (< ?mean-sub 0.00))
(bind ?mean-compABS (> ?mean-subABS 1.50)))
(bind ?mean-comp (and ?mean-subNEG ?mean-compABS))
(assert (mean-comp4 ?mean-comp))
)
"""
env.build(rule31)

rule32 = """
(defrule mean-match8
(mean-comp4 TRUE)
=>
(bind ?mean-comp-result "significantly smaller than")
(assert (mean-compare ?mean-comp-result))
)
"""
env.build(rule32)

rule33 = """
(defrule mean-match9
(histogram1 (mean1 ?mean1))
(histogram2 (mean2 ?mean2))
=>
(bind ?mean-subs (- ?mean1 ?mean2))
(bind ?mean-sub (precision ?mean-subs))
(bind ?mean-subABS (abs ?mean-sub))
(bind ?mean-subPOS (> ?mean-sub 0.00))
(bind ?mean-compABS (and (> ?mean-subABS 0.50) (<= ?mean-subABS 1.50)))
(bind ?mean-comp (and ?mean-subPOS ?mean-compABS))
(assert (mean-comp5 ?mean-comp))
)
"""
env.build(rule33)

rule34 = """
(defrule mean-match10
(mean-comp5 TRUE)
=>
(bind ?mean-comp-result "moderately larger than")
(assert (mean-compare ?mean-comp-result))
)
"""
env.build(rule34)

rule35 = """
(defrule mean-match11
(histogram1 (mean1 ?mean1))
(histogram2 (mean2 ?mean2))
=>
(bind ?mean-subs (- ?mean1 ?mean2))
(bind ?mean-sub (precision ?mean-subs))
(bind ?mean-subABS (abs ?mean-sub))
(bind ?mean-subPOS (> ?mean-sub 0.00))
(bind ?mean-compABS (> ?mean-subABS 1.50))
(bind ?mean-comp (and ?mean-subPOS ?mean-compABS))
(assert (mean-comp6 ?mean-comp))
)
"""
env.build(rule35)

rule36 = """
(defrule mean-match12
(mean-comp6 TRUE)
=>
(bind ?mean-comp-result "significantly larger than")
(assert (mean-compare ?mean-comp-result))
)
"""
env.build(rule36)

rule37 = """
(defrule std-match1
(histogram1 (std1 ?std1))
(histogram2 (std2 ?std2))
=>
(bind ?std-subs (- ?std1 ?std2))
(bind ?std-sub (precision ?std-subs))
(bind ?std-comp (= ?std-sub 0.00))
(assert (std-comp1 ?std-comp))
)
"""
env.build(rule37)

rule38 = """
(defrule std-match2
(std-comp1 TRUE)
=>
(bind ?std-comp-result "the same as")
(assert (std-compare ?std-comp-result))
)
"""
env.build(rule38)

rule39 = """
(defrule std-match3
(histogram1 (std1 ?std1))
(histogram2 (std2 ?std2))
=>
(bind ?std-subs (- ?std1 ?std2))
(bind ?std-sub (precision ?std-subs))
(bind ?std-subABS (abs ?std-sub))
(bind ?std-comp (and (> ?std-subABS 0.00) (<= ?std-subABS 0.50)))
(assert (std-comp2 ?std-comp))
)
"""
env.build(rule39)

rule40 = """
(defrule std-match4
(std-comp2 TRUE)
=>
(bind ?std-comp-result "similar to")
(assert (std-compare ?std-comp-result))
)
"""
env.build(rule40)

rule41 = """
(defrule std-match5
(histogram1 (std1 ?std1))
(histogram2 (std2 ?std2))
=>
(bind ?std-subs (- ?std1 ?std2))
(bind ?std-sub (precision ?std-subs))
(bind ?std-subABS (abs ?std-sub))
(bind ?std-subNEG (< ?std-sub 0.00))
(bind ?std-compABS (and (> ?std-subABS 0.50) (<= ?std-subABS 1.50)))
(bind ?std-comp (and ?std-subNEG ?std-compABS))
(assert (std-comp3 ?std-comp))
)
"""
env.build(rule41)

rule42 = """
(defrule std-match6
(std-comp3 TRUE)
=>
(bind ?std-comp-result "moderately smaller than")
(assert (std-compare ?std-comp-result))
)
"""
env.build(rule42)

rule43 = """
(defrule std-match7
(histogram1 (std1 ?std1))
(histogram2 (std2 ?std2))
=>
(bind ?std-subs (- ?std1 ?std2))
(bind ?std-sub (precision ?std-subs))
(bind ?std-subABS (abs ?std-sub))
(bind ?std-subNEG (< ?std-sub 0.00))
(bind ?std-compABS (> ?std-subABS 1.50)))
(bind ?std-comp (and ?std-subNEG ?std-compABS))
(assert (std-comp4 ?std-comp))
)
"""
env.build(rule43)

rule44 = """
(defrule std-match8
(std-comp4 TRUE)
=>
(bind ?std-comp-result "significantly smaller than")
(assert (std-compare ?std-comp-result))
)
"""
env.build(rule44)

rule45 = """
(defrule std-match9
(histogram1 (std1 ?std1))
(histogram2 (std2 ?std2))
=>
(bind ?std-subs (- ?std1 ?std2))
(bind ?std-sub (precision ?std-subs))
(bind ?std-subABS (abs ?std-sub))
(bind ?std-subPOS (> ?std-sub 0.00))
(bind ?std-compABS (and (> ?std-subABS 0.50) (<= ?std-subABS 1.50)))
(bind ?std-comp (and ?std-subPOS ?std-compABS))
(assert (std-comp5 ?std-comp))
)
"""
env.build(rule45)

rule46 = """
(defrule std-match10
(std-comp5 TRUE)
=>
(bind ?std-comp-result "moderately larger than")
(assert (std-compare ?std-comp-result))
)
"""
env.build(rule46)

rule47 = """
(defrule std-match11
(histogram1 (std1 ?std1))
(histogram2 (std2 ?std2))
=>
(bind ?std-subs (- ?std1 ?std2))
(bind ?std-sub (precision ?std-subs))
(bind ?std-subABS (abs ?std-sub))
(bind ?std-subPOS (> ?std-sub 0.00))
(bind ?std-compABS (> ?std-subABS 1.50))
(bind ?std-comp (and ?std-subPOS ?std-compABS))
(assert (std-comp6 ?std-comp))
)
"""
env.build(rule47)

rule48 = """
(defrule std-match12
(std-comp6 TRUE)
=>
(bind ?std-comp-result "significantly larger than")
(assert (std-compare ?std-comp-result))
)
"""
env.build(rule48)

rule49 = """
(defrule dist-match1
(histogram1 (distance ?dist))
=>
(bind ?dist-comp (= ?dist 1.00))
(assert (dist-comp1 ?dist-comp))
)
"""
env.build(rule49)

rule50 = """
(defrule dist-match2
(dist-comp1 TRUE)
=>
(bind ?dist-comp-result "perfectly identical")
(assert (dist-compare ?dist-comp-result))
)
"""
env.build(rule50)

rule51 = """
(defrule dist-match3
(histogram1 (distance ?dist))
=>
(bind ?dist-comp (and (>= ?dist 0.98) (< ?dist 1.00)))
(assert (dist-comp2 ?dist-comp))
)
"""
env.build(rule51)

rule52 = """
(defrule dist-match4
(dist-comp2 TRUE)
=>
(bind ?dist-comp-result "similar")
(assert (dist-compare ?dist-comp-result))
)
"""
env.build(rule52)

rule53 = """
(defrule dist-match5
(histogram1 (distance ?dist))
=>
(bind ?dist-comp (< ?dist 0.98))
(assert (dist-comp3 ?dist-comp))
)
"""
env.build(rule53)

rule54 = """
(defrule dist-match6
(dist-comp3 TRUE)
=>
(bind ?dist-comp-result "dissimilar")
(assert (dist-compare ?dist-comp-result))
)
"""
env.build(rule54)

rule55 = """
(defrule skewness1
(histogram1 (skew1 ?skew1))
=>
(bind ?skew1-comp (< ?skew1 -1.00))
(assert (skew1-comp1 ?skew1-comp))
)
"""
env.build(rule55)

rule56 = """
(defrule skewness2
(skew1-comp1 TRUE)
=>
(bind ?skew1-result "highly left skewed")
(assert (skewness1 ?skew1-result))
)
"""
env.build(rule56)

rule57 = """
(defrule skewness3
(histogram1 (skew1 ?skew1))
=>
(bind ?skew1-comp (and (> ?skew1 -1.00) (< ?skew1 -0.50)))
(assert (skew1-comp2 ?skew1-comp))
)
"""
env.build(rule57)

rule58 = """
(defrule skewness4
(skew1-comp2 TRUE)
=>
(bind ?skew1-result "moderately left skewed")
(assert (skewness1 ?skew1-result))
)
"""
env.build(rule58)

rule59 = """
(defrule skewness5
(histogram1 (skew1 ?skew1))
=>
(bind ?skew1-comp (and (> ?skew1 0.50) (< ?skew1 1.00)))
(assert (skew1-comp3 ?skew1-comp))
)
"""
env.build(rule59)

rule60 = """
(defrule skewness6
(skew1-comp3 TRUE)
=>
(bind ?skew1-result "moderately right skewed")
(assert (skewness1 ?skew1-result))
)
"""
env.build(rule60)

rule61 = """
(defrule skewness7
(histogram1 (skew1 ?skew1))
=>
(bind ?skew1-comp (and (>= ?skew1 -0.50) (<= ?skew1 0.50)))
(assert (skew1-comp4 ?skew1-comp))
)
"""
env.build(rule61)

rule62 = """
(defrule skewness8
(skew1-comp4 TRUE)
=>
(bind ?skew1-result "approximately symmetric")
(assert (skewness1 ?skew1-result))
)
"""
env.build(rule62)

rule63 = """
(defrule skewness9
(histogram1 (skew1 ?skew1))
=>
(bind ?skew1-comp (> ?skew1 1.00))
(assert (skew1-comp5 ?skew1-comp))
)
"""
env.build(rule63)

rule64 = """
(defrule skewness10
(skew1-comp5 TRUE)
=>
(bind ?skew1-result "highly right skewed")
(assert (skewness1 ?skew1-result))
)
"""
env.build(rule64)

rule65 = """
(defrule skewness11
(histogram2 (skew2 ?skew2))
=>
(bind ?skew2-comp (< ?skew2 -1.00))
(assert (skew2-comp1 ?skew2-comp))
)
"""
env.build(rule65)

rule66 = """
(defrule skewness12
(skew2-comp1 TRUE)
=>
(bind ?skew2-result "highly left skewed")
(assert (skewness2 ?skew2-result))
)
"""
env.build(rule66)

rule67 = """
(defrule skewness13
(histogram2 (skew2 ?skew2))
=>
(bind ?skew2-comp (and (> ?skew2 -1.00) (< ?skew2 -0.50)))
(assert (skew2-comp2 ?skew2-comp))
)
"""
env.build(rule67)

rule68 = """
(defrule skewness14
(skew2-comp2 TRUE)
=>
(bind ?skew2-result "moderately left skewed")
(assert (skewness2 ?skew2-result))
)
"""
env.build(rule68)

rule69 = """
(defrule skewness15
(histogram2 (skew2 ?skew2))
=>
(bind ?skew2-comp (and (> ?skew2 0.50) (< ?skew2 1.00)))
(assert (skew2-comp3 ?skew2-comp))
)
"""
env.build(rule69)

rule70 = """
(defrule skewness16
(skew2-comp3 TRUE)
=>
(bind ?skew2-result "moderately right skewed")
(assert (skewness2 ?skew2-result))
)
"""
env.build(rule70)

rule71 = """
(defrule skewness17
(histogram2 (skew2 ?skew2))
=>
(bind ?skew2-comp (and (>= ?skew2 -0.50) (<= ?skew2 0.50)))
(assert (skew2-comp4 ?skew2-comp))
)
"""
env.build(rule71)

rule72 = """
(defrule skewness18
(skew2-comp4 TRUE)
=>
(bind ?skew2-result "approximately symmetric")
(assert (skewness2 ?skew2-result))
)
"""
env.build(rule72)

rule73 = """
(defrule skewness19
(histogram2 (skew2 ?skew2))
=>
(bind ?skew2-comp (> ?skew2 1.00))
(assert (skew2-comp5 ?skew2-comp))
)
"""
env.build(rule73)

rule74 = """
(defrule skewness20
(skew2-comp5 TRUE)
=>
(bind ?skew2-result "highly right skewed")
(assert (skewness2 ?skew2-result))
)
"""
env.build(rule74)

rule75 = """
(defrule outliers1
(histogram1 (outlier1 ?outlier1))
=>
(bind ?outlier1-len (= ?outlier1 0))
(assert (outlier1-len1 ?outlier1-len))
)
"""
env.build(rule75)

rule76 = """
(defrule outliers2
(outlier1-len1 TRUE)
=>
(bind ?outlier1-result 0)
(assert (outlier1-value ?outlier1-result))
)
"""
env.build(rule76)

rule77 = """
(defrule outliers3
(histogram1 (outlier1 ?outlier1))
=>
(bind ?outlier1-len (<> ?outlier1 0))
(assert (outlier1-len2 ?outlier1-len))
)
"""
env.build(rule77)

rule78 = """
(defrule outliers4
(histogram1 (outlier1 ?outlier1))
(outlier1-len2 TRUE)
=>
(bind ?outlier1-result ?outlier1)
(assert (outlier1-value ?outlier1-result))
)
"""
env.build(rule78)

rule79 = """
(defrule outliers5
(histogram2 (outlier2 ?outlier2))
=>
(bind ?outlier2-len (= ?outlier2 0))
(assert (outlier2-len1 ?outlier2-len))
)
"""
env.build(rule79)

rule80 = """
(defrule outliers6
(outlier2-len1 TRUE)
=>
(bind ?outlier2-result 0)
(assert (outlier2-value ?outlier2-result))
)
"""
env.build(rule80)

rule81 = """
(defrule outliers7
(histogram2 (outlier2 ?outlier2))
=>
(bind ?outlier2-len (<> ?outlier2 0))
(assert (outlier2-len2 ?outlier2-len))
)
"""
env.build(rule81)

rule82 = """
(defrule outliers8
(histogram2 (outlier2 ?outlier2))
(outlier2-len2 TRUE)
=>
(bind ?outlier2-result ?outlier2)
(assert (outlier2-value ?outlier2-result))
)
"""
env.build(rule82)

rule83 = """
(defrule outliers9
(histogram1 (outlier1max ?outlier1-max))
=>
(bind ?outlier1max-val (= ?outlier1-max 0))
(assert (outlier1max-val1 ?outlier1max-val))
)
"""
env.build(rule83)

rule84 = """
(defrule outliers10
(outlier1max-val1 TRUE)
=>
(bind ?outlier1max-result "zero")
(assert (outlier1max-value ?outlier1max-result))
)
"""
env.build(rule84)

rule85 = """
(defrule outliers11
(histogram1 (outlier1max ?outlier1-max))
=>
(bind ?outlier1max-val (<> ?outlier1-max 0))
(assert (outlier1max-val2 ?outlier1max-val))
)
"""
env.build(rule85)

rule86 = """
(defrule outliers12
(histogram1 (outlier1max ?outlier1-max))
(outlier1max-val2 TRUE)
=>
(bind ?outlier1max-result ?outlier1-max)
(assert (outlier1max-value ?outlier1max-result))
)
"""
env.build(rule86)

rule87 = """
(defrule outliers13
(histogram2 (outlier2max ?outlier2-max))
=>
(bind ?outlier2max-val (= ?outlier2-max 0))
(assert (outlier2max-val1 ?outlier2max-val))
)
"""
env.build(rule87)

rule88 = """
(defrule outliers14
(outlier2max-val1 TRUE)
=>
(bind ?outlier2max-result "zero")
(assert (outlier2max-value ?outlier2max-result))
)
"""
env.build(rule88)

rule89 = """
(defrule outliers15
(histogram2 (outlier2max ?outlier2-max))
=>
(bind ?outlier2max-val (<> ?outlier2-max 0))
(assert (outlier2max-val2 ?outlier2max-val))
)
"""
env.build(rule89)

rule90 = """
(defrule outliers16
(histogram2 (outlier2max ?outlier2-max))
(outlier2max-val2 TRUE)
=>
(bind ?outlier2max-result ?outlier2-max)
(assert (outlier2max-value ?outlier2max-result))
)
"""
env.build(rule90)

rule91 = """
(defrule peakmodal1
(histogram1 (peak1size ?pk1-size))
=>
(bind ?peak1modal-val (= ?pk1-size 0))
(assert (peak1modal-val1 ?peak1modal-val))
)
"""
env.build(rule91)

rule92 = """
(defrule peakmodal2
(peak1modal-val1 TRUE)
=>
(bind ?peak1modal-result "non-modal")
(assert (peak1-modal ?peak1modal-result))
)
"""
env.build(rule92)

rule93 = """
(defrule peakmodal3
(histogram1 (peak1size ?pk1-size))
=>
(bind ?peak1modal-val (= ?pk1-size 1))
(assert (peak1modal-val2 ?peak1modal-val))
)
"""
env.build(rule93)

rule94 = """
(defrule peakmodal4
(peak1modal-val2 TRUE)
=>
(bind ?peak1modal-result "unimodal")
(assert (peak1-modal ?peak1modal-result))
)
"""
env.build(rule94)

rule95 = """
(defrule peakmodal5
(histogram1 (peak1size ?pk1-size))
=>
(bind ?peak1modal-val (= ?pk1-size 2))
(assert (peak1modal-val3 ?peak1modal-val))
)
"""
env.build(rule95)

rule96 = """
(defrule peakmodal6
(peak1modal-val3 TRUE)
=>
(bind ?peak1modal-result "bimodal")
(assert (peak1-modal ?peak1modal-result))
)
"""
env.build(rule96)

rule97 = """
(defrule peakmodal7
(histogram1 (peak1size ?pk1-size))
=>
(bind ?peak1modal-val (> ?pk1-size 2))
(assert (peak1modal-val4 ?peak1modal-val))
)
"""
env.build(rule97)

rule98 = """
(defrule peakmodal8
(peak1modal-val4 TRUE)
=>
(bind ?peak1modal-result "multimodal")
(assert (peak1-modal ?peak1modal-result))
)
"""
env.build(rule98)

rule99 = """
(defrule peakmodal9
(histogram2 (peak2size ?pk2-size))
=>
(bind ?peak2modal-val (= ?pk2-size 0))
(assert (peak2modal-val1 ?peak2modal-val))
)
"""
env.build(rule99)

rule100 = """
(defrule peakmodal10
(peak2modal-val1 TRUE)
=>
(bind ?peak2modal-result "non-modal")
(assert (peak2-modal ?peak2modal-result))
)
"""
env.build(rule100)

rule101 = """
(defrule peakmodal11
(histogram2 (peak2size ?pk2-size))
=>
(bind ?peak2modal-val (= ?pk2-size 1))
(assert (peak2modal-val2 ?peak2modal-val))
)
"""
env.build(rule101)

rule102 = """
(defrule peakmodal12
(peak2modal-val2 TRUE)
=>
(bind ?peak2modal-result "unimodal")
(assert (peak2-modal ?peak2modal-result))
)
"""
env.build(rule102)

rule103 = """
(defrule peakmodal13
(histogram2 (peak2size ?pk2-size))
=>
(bind ?peak2modal-val (= ?pk2-size 2))
(assert (peak2modal-val3 ?peak2modal-val))
)
"""
env.build(rule103)

rule104 = """
(defrule peakmodal14
(peak2modal-val3 TRUE)
=>
(bind ?peak2modal-result "bimodal")
(assert (peak2-modal ?peak2modal-result))
)
"""
env.build(rule104)

rule105 = """
(defrule peakmodal15
(histogram2 (peak2size ?pk2-size))
=>
(bind ?peak2modal-val (> ?pk2-size 2))
(assert (peak2modal-val4 ?peak2modal-val))
)
"""
env.build(rule105)

rule106 = """
(defrule peakmodal16
(peak2modal-val4 TRUE)
=>
(bind ?peak2modal-result "multimodal")
(assert (peak2-modal ?peak2modal-result))
)
"""
env.build(rule106)

rule107 = """
(defrule fill-max-template
(histogram1 (max1 ?max1))
(histogram2 (max2 ?max2))
(max-compare ?max-result)
=>
(bind ?max-sentence (maxSentence ?max1 ?max2 ?max-result))
(assert (max-sentence ?max-sentence))
)
"""
env.build(rule107)

rule108 = """
(defrule fill-min-template
(histogram1 (min1 ?min1))
(histogram2 (min2 ?min2))
(min-compare ?min-result)
=>
(bind ?min-sentence (minSentence ?min1 ?min2 ?min-result))
(assert (min-sentence ?min-sentence))
)
"""
env.build(rule108)

rule109 = """
(defrule fill-mean-template
(histogram1 (mean1 ?mean1))
(histogram2 (mean2 ?mean2))
(mean-compare ?mean-result)
=>
(bind ?mean-sentence (meanSentence ?mean1 ?mean2 ?mean-result))
(assert (mean-sentence ?mean-sentence))
)
"""
env.build(rule109)

rule110 = """
(defrule fill-std-template
(histogram1 (std1 ?std1))
(histogram2 (std2 ?std2))
(std-compare ?std-result)
=>
(bind ?std-sentence (stdSentence ?std1 ?std2 ?std-result))
(assert (std-sentence ?std-sentence))
)
"""
env.build(rule110)

rule111 = """
(defrule fill-dist-template
(histogram1 (distance ?dist))
(dist-compare ?dist-result)
=>
(bind ?dist-sentence (distSentence ?dist ?dist-result))
(assert (dist-sentence ?dist-sentence))
)
"""
env.build(rule111)

rule112 = """
(defrule fill-skew-template
(histogram1 (skew1 ?skew1))
(histogram2 (skew2 ?skew2))
=>
(bind ?skew-sentence (skewSentence ?skew1 ?skew2))
(assert (skew-sentence ?skew-sentence))
)
"""
env.build(rule112)

rule113 = """
(defrule fill-out-template
(outlier1-value ?out1-result)
(outlier2-value ?out2-result)
(outlier1max-value ?out1max-result)
(outlier2max-value ?out2max-result)
=>
(bind ?outlier-sentence (outlierSentence ?out1-result ?out2-result ?out1max-result ?out2max-result))
(assert (outlier-sentence ?outlier-sentence))
)
"""
env.build(rule113)

rule114 = """
(defrule fill-peak-template
(histogram1 (peak1size ?pk1-size))
(histogram2 (peak2size ?pk2-size))
(peak1-modal ?pk1-modal)
(peak2-modal ?pk2-modal)
=>
(bind ?peak-sentence (peakSentence ?pk1-size ?pk1-modal ?pk2-size ?pk2-modal))
(assert (peak-sentence ?peak-sentence))
)
"""
env.build(rule114)

rule115 = """
(defrule gen-peak1-story
(histogram1 (peak1binlist ?peak1binlist))
(histogram1 (peak1freq ?peak1freq))
(histogram1 (peak1binsize ?peak1binsize))
=>
(bind ?peak1-story (peak1Story ?peak1binlist ?peak1freq ?peak1binsize))
(assert (peak1-story ?peak1-story))
)
"""
env.build(rule115)

rule116 = """
(defrule gen-peak2-story
(histogram2 (peak2binlist ?peak2binlist))
(histogram2 (peak2freq ?peak2freq))
(histogram2 (peak2binsize ?peak2binsize))
=>
(bind ?peak2-story (peak2Story ?peak2binlist ?peak2freq ?peak2binsize))
(assert (peak2-story ?peak2-story))
)
"""
env.build(rule116)

rule117 = """
(defrule gen-peak-region-sent
(histogram1 (peak1binlist ?peak1binlist))
(histogram2 (peak2binlist ?peak2binlist))
=>
(bind ?peak-region-sent (peakRegionSent ?peak1binlist ?peak2binlist))
(assert (peak-region-sent ?peak-region-sent))
)
"""
env.build(rule117)

rule118 = """
(defrule gen-peaks-story
(peak1-story ?peak1-story)
(peak2-story ?peak2-story)
(peak-sentence ?peak-sentence)
(peak-region-sent ?peak-region-sent)
=>
(bind ?peak-story (peakStory ?peak1-story ?peak2-story ?peak-sentence ?peak-region-sent))
(assert (peaks-story ?peak-story))
)
"""
env.build(rule118)

rule119 = """
(defrule story-gen
(min-sentence ?min-sentence)
(max-sentence ?max-sentence)
(mean-sentence ?mean-sentence)
(std-sentence ?std-sentence)
(dist-sentence ?dist-sentence)
(outlier-sentence ?outlier-sentence)
(skew-sentence ?skew-sentence)
(peaks-story ?peaks-story)
=>
(bind ?story (storyGen ?min-sentence ?max-sentence ?mean-sentence ?std-sentence ?dist-sentence ?outlier-sentence ?skew-sentence ?peaks-story))
(assert (story ?story))
)
"""
env.build(rule119)

env.run()

if story_type == "short":
    # Display the two histogram
    import matplotlib.pyplot as plt1
    bins=list(compute_bins(data1, 10))
    fig = plt1.figure(figsize=(12,6))
    ax1=fig.add_subplot(121)
    ax1.set_title("Histogram 1", fontsize=14)
    ax1.hist(data1, bins=bins, edgecolor='black')
    ax1.set_xlabel("Bins", fontsize=14)
    ax1.set_ylabel("Frequency", fontsize=14)
    ax2=fig.add_subplot(122)
    ax2.set_title("Histogram 2", fontsize=14)
    ax2.hist(data2, bins=bins, edgecolor='black')
    ax2.set_xlabel("Bins", fontsize=14)
    ax2.set_ylabel("Frequency", fontsize=14)
    plt1.show()
    
    # Print the short story
    Short_Rule9 = """
    (defrule short-story-print
    (short-story ?sstory)
    =>
    (myPrint ?sstory)
    )
    """
    env.build(Short_Rule9)
    env.run()

elif story_type == "detailed":
    # Display the two histogram
    import matplotlib.pyplot as plt1
    bins=list(compute_bins(data1, 10))
    fig = plt1.figure(figsize=(12,6))
    ax1=fig.add_subplot(121)
    ax1.set_title("Histogram 1", fontsize=14)
    ax1.hist(data1, bins=bins, edgecolor='black')
    ax1.set_xlabel("Bins", fontsize=14)
    ax1.set_ylabel("Frequency", fontsize=14)
    ax2=fig.add_subplot(122)
    ax2.set_title("Histogram 2", fontsize=14)
    ax2.hist(data2, bins=bins, edgecolor='black')
    ax2.set_xlabel("Bins", fontsize=14)
    ax2.set_ylabel("Frequency", fontsize=14)
    plt1.show()
    
    # Print the detailed story
    rule120 = """
    (defrule story-print
    (story ?story)
    =>
    (detailedPrint ?story)
    )
    """

    env.build(rule120)
    env.run()
    
elif story_type == "both":
    # Display the two histogram
    import matplotlib.pyplot as plt1
    bins=list(compute_bins(data1, 10))
    fig = plt1.figure(figsize=(12,6))
    ax1=fig.add_subplot(121)
    ax1.set_title("Histogram 1", fontsize=14)
    ax1.hist(data1, bins=bins, edgecolor='black')
    ax1.set_xlabel("Bins", fontsize=14)
    ax1.set_ylabel("Frequency", fontsize=14)
    ax2=fig.add_subplot(122)
    ax2.set_title("Histogram 2", fontsize=14)
    ax2.hist(data2, bins=bins, edgecolor='black')
    ax2.set_xlabel("Bins", fontsize=14)
    ax2.set_ylabel("Frequency", fontsize=14)
    plt1.show()
    
    # Print the combine story
    both_rule1 = """
    (defrule both-story-print
    (story ?story)
    (short-story ?sstory)
    =>
    (fullPrint ?sstory ?story)
    )
    """

    env.build(both_rule1)
    env.run()

else:
    print('please specify the correct story type as second argument i.e. "short" or "detailed" or "both"')
    sys.exit()

