import csv
import os
import sys

class DataSet():
    data = []
    featureNames = []
    target = []
    targetNames = []

    def addTrainingData(self, attributes, targetValue):
        self.data.append(attributes)
        self.target.append(targetValue)

def doKNN(csvFilePath, ):
    with open(os.path.join('.', '7146875/IST_MIR.csv'), 'r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            pass

def main(argv):
    csvFilePath = argv[1]


if __name__ == "__main__":
    main(sys.argv)