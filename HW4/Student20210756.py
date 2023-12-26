import sys
import numpy as np
import operator
from os import listdir

def createDataSet(dir):
    labels = []
    trainingList = listdir(dir)
    length = len(trainingList)
    matrix = np.zeros((length, 1024))

    for i in range(length):
        fileName = trainingList[i]
        answer = int(fileName.split('_')[0]) 
        labels.append(answer)
        matrix[i, :] = createVector(dir + '/' + fileName)
    return matrix, labels 

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}

    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createVector(file):
    vector = np.zeros((1, 1024))
    with open(file) as f:
        for i in range(32):
            line = f.readline()
            for j in range(32):
                vector[0, 32 * i + j] = int(line[j])
        return vector        

if __name__ == "__main__":
    trainingDirName = sys.argv[1]
    testDirName = sys.argv[2]

    testFileList = listdir(testDirName)
    length = len(testFileList)

    matrix, labels = createDataSet(trainingDirName)

    for k in range(1, 21):
        count = 0 
        errorCount = 0
    
        for i in range(length):
            answer = int(testFileList[i].split('_')[0])
            testData = createVector(testDirName + '/' + testFileList[i])
            result = classify0(testData, matrix, labels, k)
        
            count += 1
            if answer != result:
                errorCount += 1
    
        print(int(errorCount / count * 100))
