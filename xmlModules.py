# Import required libraries
from yattag import Doc, indent
import xml.etree.ElementTree as ET

# Create xml object from computed measures
def genXMLOutput(obj):
    doc, tag, text = Doc().tagtext()
    with tag('data'):
        with tag('max'):
            with tag('maxHist1'):
                text(obj['Max1'])
            with tag('maxHist2'):
                text(obj['Max2'])
        with tag('min'):
            with tag('minHist1'):
                text(obj['Min1'])
            with tag('minHist2'):
                text(obj['Min2'])
        with tag('mean'):
            with tag('meanHist1'):
                text(obj['Mean1'])
            with tag('meanHist2'):
                text(obj['Mean2'])
        with tag('stdDev'):
            with tag('stdDevHist1'):
                text(obj['StdDev1'])
            with tag('stdDevHist2'):
                text(obj['StdDev2'])
        with tag('skew'):
            with tag('skewHist1'):
                text(obj['Skew_Value1'])
            with tag('skewHist2'):
                text(obj['Skew_Value2'])
        with tag('outlier'):
            with tag('outlierHist1'):
                text(repr(obj['Outliers1']))
            with tag('outlierHist2'):
                text(repr(obj['Outliers2']))
        with tag('peak'):
            with tag('peakHist1'):
                text(repr(obj['Peaks1']))
            with tag('peakHist2'):
                text(repr(obj['Peaks2']))

    result = indent(
        doc.getvalue(),
        indentation = ' '*3,
        newline = '\r\n'
    )
    return result

# Convert xml to Facts
def xmlToFacts(xmldata):
    root = ET.fromstring(xmldata)
    a = {}
    b = {}
    for elem in root:
        #print('\n',elem.tag)
        for subelem in elem:
            if subelem.tag[-1] == '1':
                a[elem.tag] = subelem.text
            elif subelem.tag[-1] == '2':
                b[elem.tag] = subelem.text
    return a, b

