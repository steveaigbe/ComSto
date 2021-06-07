# import required libraries
import random
from string import Template
import ast
from detailedTemplates import minTemp, maxTemp, meanTemp, stdDevTemp, skewTemp, distTemp
from detailedTemplates import outTemp1, outTemp2, outTemp3, outTemp4, outTemp5
from detailedTemplates import peakRegionTemp, hist1PeakTemp, hist2PeakTemp, shortPeakTemp

# Function to generate detailed minimum sentence
def minSentence(obj1, obj2, mincomp):
    minTemplates = minTemp()
    size = len(minTemplates)
    if obj1 == obj2:
        template = minTemplates[size]
        sentence = Template(template)
        return sentence.substitute(minval1=obj1)
    else:
        randNum = random.randint(1,size-1)
        template = minTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(minval1=obj1, minval2=obj2, mincomp=mincomp)
    
# Function to generate detailed maximum sentence
def maxSentence(obj1, obj2, maxcomp):
    maxTemplates = maxTemp()
    size = len(maxTemplates)
    if obj1 == obj2:
        template = maxTemplates[size]
        sentence = Template(template)
        return sentence.substitute(maxval1=obj1)
    else:
        randNum = random.randint(1,size-1)
        template = maxTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(maxval1=obj1, maxval2=obj2, maxcomp=maxcomp)
    
# Function to generate detailed mean sentence
def meanSentence(obj1, obj2, meancomp):
    meanTemplates = meanTemp()
    size = len(meanTemplates)
    if obj1 == obj2:
        template = meanTemplates[size]
        sentence = Template(template)
        return sentence.substitute(meanval1=obj1)
    else:
        randNum = random.randint(1,size-1)
        template = meanTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(meanval1=obj1, meanval2=obj2, meancomp=meancomp)
    
# Function to generate detailed standard deviation sentence
def stdSentence(obj1, obj2, stdcomp):
    stdDevTemplates = stdDevTemp()
    size = len(stdDevTemplates)
    if obj1 == obj2:
        template = meanTemplates[size]
        sentence = Template(template)
        return sentence.substitute(stdval1=obj1)
    else:
        randNum = random.randint(1,size-1)
        template = stdDevTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(stdval1=obj1, stdval2=obj2, stdcomp=stdcomp)

# Function to generate detailed distance sentence
def distSentence(obj, distcomp):
    distTemplates = distTemp()
    size = len(distTemplates)
    randNum = random.randint(1,size)
    template = distTemplates[randNum]
    sentence = Template(template)
    return sentence.substitute(bdm=obj, bdmcomp=distcomp)

# Function to generate detailed skewness sentence
def skewSentence(obj1, obj2):
    skewTemplates = skewTemp()
    size = len(skewTemplates)
    skewType = ""
    if obj1 < 0 and abs(obj1) < 0.5:
        skewType1 = " somewhat left-skewed "
    elif obj1 < 0 and abs(obj1) > 0.5:
        skewType1 = " left-skewed "
    elif obj1 > 0 and obj1 < 0.5:
        skewType1 = " somewhat right-skewed "
    elif obj1 > 0 and obj1 > 0.5:
        skewType1 = " right-skewed "
        
    if obj2 < 0 and abs(obj2) < 0.5:
        skewType2 = " somewhat left-skewed "
    elif obj2 < 0 and abs(obj2) > 0.5:
        skewType2 = " left-skewed "
    elif obj2 > 0 and obj2 < 0.5:
        skewType2 = " somewhat right-skewed "
    elif obj2 > 0 and obj2 > 0.5:
        skewType2 = " right-skewed "
    if obj1 == obj2:
        template = skewTemplates[size]
        sentence = Template(template)
        return sentence.substitute(skewtype1=obj1)
    else:
        randNum = random.randint(1,size-1)
        template = skewTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(skewtype1=obj1, skewtype2=obj2)

# Function to generate detailed outlier sentence
def outlierSentence(outlier1, outlier2, maxOut1, maxOut2):
    OutTemplates1 = OutTemp1()
    OutTemplates2 = OutTemp2()
    OutTemplates3 = OutTemp3()
    OutTemplates4 = OutTemp4()
    OutTemplates5 = OutTemp5()
    if  outlier1 == 0 and outlier2 == 0:
        size1 = len(OutTemplates1)
        randNum = random.randint(1,size1)
        if randNum == 2:
            template = OutTemplates1[randNum]
            sentence = Template(template)
            return sentence.substitute(numOutlier1=outlier1)
        else:
            return OutTemplates1[randNum]
    elif outlier1 != 0 and outlier2 == 0:
        size2 = len(OutTemplates2)
        randNum = random.randint(1,size2)
        if randNum == 1:
            template = OutTemplates2[randNum]
            sentence = Template(template)
            return sentence.substitute(numOutlier1=outlier1, maxOutlier1=maxOut1, numOutlier2=outlier2)
        else:
            template = OutTemplates2[randNum]
            sentence = Template(template)
            return sentence.substitute(numOutlier1=outlier1, maxOutlier1=maxOut1)
    elif outlier1 == 0 and outlier2 != 0:
        size3 = len(OutTemplates3)
        randNum = random.randint(1,size3)
        if randNum == 1:
            template = OutTemplates3[randNum]
            sentence = Template(template)
            return sentence.substitute(numOutlier1=outlier1, numOutlier2=outlier2, maxOutlier2=maxOut2)
        else:
            template = OutTemplates3[randNum]
            sentence = Template(template)
            return sentence.substitute(numOutlier2=outlier2, maxOutlier2=maxOut2)
    elif outlier1 != 0 and outlier2 != 0:
        size4 = len(OutTemplates4)
        randNum = random.randint(1,size4)
        template = OutTemplates4[randNum]
        sentence = Template(template)
        return sentence.substitute(numOutlier1=outlier1, maxOutlier1=maxOut1, numOutlier2=outlier2, maxOutlier2=maxOut2)
    elif outlier1 != 0 and outlier2 != 0 and outlier1 == outlier2:
        size5 = len(OutTemplates5)
        randNum = random.randint(1,size5)
        template = OutTemplates5[randNum]
        sentence = Template(template)
        return sentence.substitute(numOutlier1=outlier1)
    
# Function to generate detailed peak sentence
def peakSentence(size1, modal1, size2, modal2):
    shortPeakTemplates = shortPeakTemp()
    size = len(shortPeakTemplates)
    if size1 == size2:
        template = shortPeakTemplates[size]
        sentence = Template(template)
        return sentence.substitute(peaksize1=size1, modality1=modal1)
    else:
        randNum = random.randint(1,size-1)
        template = shortPeakTemplates[randNum]
        sentence = Template(template)
        return sentence.substitute(modality1=modal1, modality2=modal2, peaksize1=size1, peaksize2=size2)
    
# Function to generate detailed peak sentence for histogram1
def peak1Story(bins, freq, binsize):
    hist1PeakTemplates = hist1PeakTemp()
    bins = ast.literal_eval(bins)
    freq = ast.literal_eval(freq)
    story = ''
    size = len(freq)
    if size == 0:
        story = story + "Histogram2 has no peaks. "
        return story
    else:
        
        if size > 5:
            size = 5
        for i in range(0,size):
            if type(freq[i]) == list:
                index = (i+1)*10+(i+1)
                template = hist1PeakTemplates[index]
                sentence = Template(template)
                story = story + sentence.substitute(binpos1=bins[i], binpos2=(bins[i] + (binsize * i)), freqnum1=freq[i][0])
            else:
                template = hist1PeakTemplates[i+1]
                sentence = Template(template)
                story = story + sentence.substitute(binpos1=bins[i], freqnum1=freq[i])
        return story
    
# Function to generate detailed peak sentence for histogram2
def peak2Story(bins, freq, binsize):
    hist2PeakTemplates = hist2PeakTemp()
    bins = ast.literal_eval(bins)
    freq = ast.literal_eval(freq)
    story = ''
    size = len(freq)
    if size == 0:
        story = story + "Histogram2 has no peaks. "
        return story
    else:
        
        if size > 5:
            size = 5
        for i in range(0,size):
            if type(freq[i]) == list:
                index = (i+1)*10+(i+1)
                template = hist2PeakTemplates[index]
                sentence = Template(template)
                story = story + sentence.substitute(binpos1=bins[i], binpos2=(bins[i] + (binsize * i)), freqnum1=freq[i][0])
            else:
                template = hist2PeakTemplates[i+1]
                sentence = Template(template)
                story = story + sentence.substitute(binpos1=bins[i], freqnum1=freq[i])
        return story
    
# Function to generate detailed peak region sentence
def peakRegionSent(bins1, bins2):
    peakRegionTemplates = peakRegionTemp()
    bins1 = ast.literal_eval(bins1)
    bins2 = ast.literal_eval(bins2)
    sent = ''
    size1 = len(bins1)
    size2 = len(bins2)
    if size1 == 0 or size2 == 0:
        sent += "The two histograms have no region of peaks agreement. "
        return sent
    else:
        bins1 = set(bins1)
        bins2 = set(bins2)
        agreebins = list(bins1 & bins2)
        agreenum = len(agreebins)
        bins1rem = list(bins1 - (bins1 & bins2))
        bins2rem = list(bins2 - (bins1 & bins2))
        if agreenum == 0:
            sent += "The two histograms have no region of peaks agreement. "
            return sent
        else:
            sizeTemp = len(peakRegionTemplates)
            randNum = random.randint(1,sizeTemp)
            template = peakRegionTemplates[randNum]
            sentence = Template(template)
            phrase = ''
            if agreenum == 1:
                phrase = phrase + "bin " + str(agreebins[0])
            else:
                phrase = phrase + "bins " + str(agreebins[0])
                del(agreebins[0])
                for i in agreebins:
                    if i == agreebins[-1]:
                        phrase = phrase + " and " + str(i)
                    else:
                        phrase = phrase + ", " + str(i)
            sent = sent + sentence.substitute(agreenum=agreenum, agreebins=phrase)
            return sent
        
# Function to generate detailed complete peak sentence
def peakStory(peak1Story, peak2Story, peakSent, peakRegionSent):
    return peakSent + peak1Story + peak2Story + peakRegionSent

# Function to generate detailed story
def storyGen(minSent, maxSent, meanSent, stdSent, distSent, outSent, skewSent, peakStory):
    story = distSent + outSent + skewSent + peakStory
    storyList = [minSent, maxSent, meanSent, stdSent]
    listSize = len(storyList)
    randomSent = random.sample(storyList, listSize)
    for i in randomSent:
        story = story + i
    return story

# Function to print detailed story
def detailedPrint(detailed_story):
    print("The detailed story for the two histograms comparison is: \n")
    print(detailed_story)
    print()

# Function to print detailed story
def fullPrint(short_story, detailed_story):
    print("The short story for the two histograms comparison is: \n")
    print(short_story)
    print()
    print("The detailed story for the two histograms comparison is: \n")
    print(detailed_story)
    print()

