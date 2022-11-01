from TrainingDataController import TrainingDataController
from IdealDataController import IdealDataController
from TestDataController import TestDataController
from DataProcessing import DataProcessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import sys

np.set_printoptions(threshold=sys.maxsize)
warnings.simplefilter(action='ignore', category=FutureWarning)


def main():
    
    connectionDabaBase="mysql+pymysql://root:123456.*Jk@localhost:3306/test"

    MyTrainingDataController = TrainingDataController(connectionDabaBase)

    if not MyTrainingDataController.CreateTable():
        print ("Creating Training Data Table Failed.")
        return

    if not MyTrainingDataController.InsertData(pd.read_csv(r'train.csv')):
        print ("Inserting Data in Training Data Table Failed.")
        return

    MyIdealDataController = IdealDataController(connectionDabaBase)

    if not MyIdealDataController.CreateTable():
        print ("Creating Ideal Data Table Failed.")
        return

    if not MyIdealDataController.InsertData(pd.read_csv (r'ideal.csv')):
        print ("Inserting Data in Ideal Data Table Failed.")
        return

    TrainigData = MyTrainingDataController.GetData()
    IdealData = MyIdealDataController.GetData()

    result = pd.DataFrame()
    trainingFunctionCount = TrainigData.shape[1] - 1
   
    for trainingFunctionIndex in range(1,trainingFunctionCount + 1,1):

        print("Evaluating Training function " +  TrainigData.columns[trainingFunctionIndex] + "...")

        minLeastSquareIdealFunctionIndex = DataProcessing.GetIdealFunctionIndexWithMinLeastSquare(TrainigData.iloc[:,trainingFunctionIndex].values, IdealData, True)
         
        result = result.append({'TrainingFunctionName' : TrainigData.columns[trainingFunctionIndex],
                            'IdealFunctionName' : IdealData.columns[minLeastSquareIdealFunctionIndex]},
                            ignore_index = True)


        plt.plot(TrainigData.iloc[:,0].values,TrainigData.iloc[:,trainingFunctionIndex].values, 'ro', linewidth=10, label = 'Training data')
        plt.plot(IdealData.iloc[:,0].values,IdealData.iloc[:,minLeastSquareIdealFunctionIndex].values, 'go',   linewidth=1, label = 'Ideal data')
        plt.title("Training and ideal data")
        plt.xlabel("x values")
        plt.ylabel("y values")
        plt.legend(loc = 'upper right')

        plt.show()
    print (result)
   

    testDataFrame = pd.read_csv (r'test.csv')
    testDataSize = testDataFrame.shape[0]
    finalTestDataFrame = pd.DataFrame()

    for rowIndex in range(0, testDataSize, 1):

        xi = testDataFrame.iat[rowIndex,0]      
        yi = testDataFrame.iat[rowIndex,1] 
        x = IdealData.iloc[:,0].values

        maxDiff = None
        maxDiffYdelta = 0
        maxDiffIdealFunctionName = "None"

        for index, row in result.iterrows():
            
            y = IdealData.loc[:,row["IdealFunctionName"]].values
            ydelta = abs(yi - DataProcessing.GetY(x, y, xi))

            maxDeviation = DataProcessing.GetMaxDeviation(TrainigData.loc[:,row["TrainingFunctionName"]].values, IdealData.loc[:,row["IdealFunctionName"]].values)       
            factor = maxDeviation * np.sqrt(2)

            if ydelta <= factor:
                TempDiff = factor - ydelta
                    
                if maxDiff == None or TempDiff > maxDiff:
                    maxDiff = TempDiff
                    maxDiffYdelta = ydelta
                    maxDiffIdealFunctionName = row["IdealFunctionName"]

        finalTestDataFrame = finalTestDataFrame.append({'x': xi, 'y' : yi,
                                'deltaY' : maxDiffYdelta,
                                'N' : maxDiffIdealFunctionName},
                                ignore_index = True)

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(finalTestDataFrame)

    MyTestDataController = TestDataController(connectionDabaBase)

    if not MyTestDataController.CreateTable():
        print ("Creating Test Data Table Failed.")
        return

    if not MyTestDataController.InsertData(finalTestDataFrame):
        print ("Inserting Data in Test Data Table Failed.")
        return

if __name__ == '__main__':
    main()
