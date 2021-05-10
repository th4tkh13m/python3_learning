import pylab, random
import numpy as np

####LOAD FILE####
def loadData():
    """Load ImdbTitleRatings.csv and returns 
    math, reading and writing scores"""
    inFile = open('ImdbTitleRatings.csv')
    rating = []
    numVote = []
    for line in inFile:
        try:
            rating.append(float(line.split(',')[1]))
            numVote.append(float(line.split(',')[2]))
        except ValueError:
            continue
    return rating, numVote

####MAKE_HIST FUNCTION####
def makeHist(data, title, xlabel, ylabel, figure = None, bins = 30):
    """Graphing the histogram with the given parameters"""
    pylab.figure(figure)
    pylab.hist(data,bins= bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)

####CALCULATING MEAN AND STANDARD DEVIATION####
def getMeansAndSDs(population, sample, verbose = True):
    """Returns the Means and the Standard deviation of the given 
    population and sample.
    Graph histograms if verbose is True"""
    popMean = sum(population) / len(population)
    sampleMean = sum(sample) / len(sample)
    popStd = pylab.std(population)
    sampleStd = pylab.std(sample)
    if verbose:
        makeHist(population, 'IMDB Rating, Population '\
            + str(round(popMean, 2)), 'Rating', 'Number of Movies')
        makeHist(sample, 'IMDB Rating, Sample '\
            + str(round(sampleMean, 2)), 'Score', 'Number of Movies')
        print('Population Mean', popMean)
        print('Population SD', popStd)
        print('Sample Mean', sampleMean)
        print('Sample SD', sampleStd)
    return popMean, sampleMean, popStd, sampleStd


####TRY WITH NUMSAMPLE TIMES####
def graphNumSample(population, sampleSize, numSamples):
    sampleMeans = []
    meanDiff = 0
    StdDiff = 0
    for count in range(numSamples):
        sample = random.sample(population, sampleSize)
        popMean, sampleMean, popStd, sampleStd =\
        getMeansAndSDs(population, sample, verbose = False)
        sampleMeans.append(sampleMean)
        if np.abs(sampleMean - popMean) > meanDiff:
            meanDiff = np.abs(sampleMean - popMean)
        if np.abs(sampleStd - popStd) > StdDiff:
            StdDiff = np.abs(sampleStd - popStd)
    meanOfSM = sum(sampleMeans)/len(sampleMeans)
    makeHist(sampleMeans, 'Sample Means ' +\
        str(round(meanOfSM, 2)), 'Rating', 'Frequency', 'Sample Means')
    print('Max Mean Difference', meanDiff)
    print('Max STD Difference', StdDiff)
    print('Mean of Sample Mean', meanOfSM)
    print('Mean of Population', popMean)
    pylab.axvline(x = popMean, color = 'r')

####SHOW ERROR BARS####
def showErrorBars(population, sampleSize, numSamples):
    xVals = []
    sizeMeans, sizeSDs = [], []
    for size in sampleSize:
        xVals.append(size)
        sampleMeans = []
        for count in range(numSamples):
            sample = random.sample(population, size)
            popMean, sampleMean, popStd,\
                sampleStd = getMeansAndSDs(population, sample, False)
            sampleMeans.append(sampleMean)
        sizeMeans.append(sum(sampleMeans) / len(sampleMeans))
        sizeSDs.append(np.std(sampleMeans))
    pylab.errorbar(xVals, sizeMeans, yerr = 1.96*np.array(sizeSDs),\
            fmt = 'ko', label = '95% Confidence Interval')
    pylab.title('Mean Rating')
    pylab.xlabel('Sample Size')
    pylab.ylabel('Rating')
    pylab.axhline(y = popMean, label = 'Population Mean', color = 'r')
    pylab.legend(loc = 'best')

random.seed(0)
sampleSize = 1000
rating, numVote = loadData()
# sample = random.sample(rating, sampleSize)
# getMeansAndSDs(rating, sample)
# graphNumSample(rating, sampleSize, 1000)
# showErrorBars(rating, (10, 20, 50, 100, 200, 500), 1000)
for x in (100, 200, 500, 1000, 2000, 5000):
    print('size', x)
    for t in range(1000):
        sample = random.sample(rating, x)
        popMean, sampleMean = getMeansAndSDs(rating, sample)
pylab.show()