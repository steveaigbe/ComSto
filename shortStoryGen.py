# import required libraries
import random
from string import Template
import ast
from shortTemplates import shortPeakTemp, shortMinTemp, shortMaxTemp, shortMeanTemp, shortStdTemp, shortSkewTemp, shortOutTemp

# Check modlity of the peaks for short story
def peakModal(size):
    modality = ''
    if size == 0:
        modality = 'non-modal'
    elif size == 1:
        modality = 'unimodal'
    elif size == 2:
        modality = 'bimodal'
    else:
        modality = 'multimodal'
    return modality



# Function to generate short minimum sentence
def shortMinSentence(obj1, obj2):
    shortMinTemplates = shortMinTemp()
    size = len(shortMinTemplates)
    if obj1 == obj2:
        template = shortMinTemplates[size]
        sentence = Template(template)
        return sentence.substitute(minval1=obj1)
    else:
        randNum = random.randint(1,size-1)
        template = shortMinTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(minval1=obj1, minval2=obj2)
    
# Function to generate short maximum sentence
def shortMaxSentence(obj1, obj2):
    shortMaxTemplates = shortMaxTemp()
    size = len(shortMaxTemplates)
    if obj1 == obj2:
        template = shortMaxTemplates[size]
        sentence = Template(template)
        return sentence.substitute(maxval1=obj1)
    else:
        randNum = random.randint(1,size-1)
        template = shortMaxTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(maxval1=obj1, maxval2=obj2)

# Function to generate short mean sentence
def shortMeanSentence(obj1, obj2):
    shortMeanTemplates = shortMeanTemp()
    size = len(shortMeanTemplates)
    if obj1 == obj2:
        template = shortMeanTemplates[size]
        sentence = Template(template)
        return sentence.substitute(meanval1=obj1)
    else:
        randNum = random.randint(1,size-1)
        template = shortMeanTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(meanval1=obj1, meanval2=obj2)
    
# Function to generate short standard deviation sentence
def shortStdSentence(obj1, obj2):
    shortStdTemplates = shortStdTemp()
    size = len(shortStdTemplates)
    if obj1 == obj2:
        template = shortStdTemplates[size]
        sentence = Template(template)
        return sentence.substitute(stdval1=obj1)
    else:
        randNum = random.randint(1,size-1)
        template = shortStdTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(stdval1=obj1, stdval2=obj2)

# Function to generate short skewness sentence
def shortSkewSentence(obj1, obj2):
    shortSkewTemplates = shortSkewTemp()
    size = len(shortSkewTemplates)
    if obj1 == obj2:
        template = shortSkewTemplates[size]
        sentence = Template(template)
        return sentence.substitute(skewtype1=obj1)
    else:
        randNum = random.randint(1,size-1)
        template = shortSkewTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(skewtype1=obj1, skewtype2=obj2)

# Function to generate short outlier sentence    
def shortOutlierSentence(obj1, obj2):
    shortOutTemplates = shortOutTemp()
    size = len(shortOutTemplates)
    if obj1 == 0:
        numOutlier1 = 'zero'
    else:
        numOutlier1 = obj1
    if obj2 == 0:
        numOutlier2 = 'zero'
    else:
        numOutlier2 = obj2
    if numOutlier1 == numOutlier2:
        template = shortOutTemplates[size]
        sentence = Template(template)
        return sentence.substitute(numOutlier1=numOutlier1)
    else:
        randNum = random.randint(1,size-1)
        template = shortOutTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(numOutlier1=numOutlier1, numOutlier2=numOutlier2)
    
# Function to generate short peak sentence
def shortPeakSentence(obj1, obj2):
    shortPeakTemplates = shortPeakTemp()
    size = len(shortPeakTemplates)
    peaksize1 = obj1
    peaksize2 = obj2
    modality1 = peakModal(obj1) 
    modality2 = peakModal(obj2)
    if peaksize1 == peaksize2:
        template = shortPeakTemplates[size]
        sentence = Template(template)
        return sentence.substitute(peaksize1=peaksize1, modality1=modality1)
    else:
        randNum = random.randint(1,size-1)
        template = shortPeakTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(modality1=modality1, modality2=modality2, peaksize1=peaksize1, peaksize2=peaksize2)

# Function to generate short story
def shortStoryGen(minSent, maxSent, meanSent, stdSent, skewSent, outSent, peakSent):
    story = outSent + skewSent + peakSent
    storyList = [minSent, maxSent, meanSent, stdSent]
    randomSent = random.sample(storyList, len(storyList))
    for i in randomSent:
        story = story + i
    return story

# Function to print short story
def myPrint(short_story):
    print("The short story for the two histograms comparison is: \n")
    print(short_story)
    print()

