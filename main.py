import pandas as pd
from TrainingDataController import TrainingDataController
from IdealDataController import IdealDataController
from TestDataController import TestDataController
from DataProcessing import DataProcessing
import numpy as np
import matplotlib.pyplot as plt
import warnings
import sys
import sqlalchemy as db

np.set_printoptions(threshold=sys.maxsize)
warnings.simplefilter(action='ignore', category=FutureWarning)




def main():
    
    # Set Up DataBase Connection String
    DataBaseConnectionString="mysql+pymysql://root:123456.*Jk@localhost:3306/test"

    MyTrainingDataController = TrainingDataController(DataBaseConnectionString)

    # Create Training Data Table. 
    if not MyTrainingDataController.CreateTable():
        print ("Creating Training Data Table Failed.")
        return

    # Seed Training Data Table. 
    if not MyTrainingDataController.InsertData(pd.read_csv(r'train.csv')):
        print ("Inserting Data in Training Data Table Failed.")
        return

    MyIdealDataController = IdealDataController(DataBaseConnectionString)

    # Create Ideal Data Table. 
    if not MyIdealDataController.CreateTable():
        print ("Creating Ideal Data Table Failed.")
        return

    # Seed Ideal Data Table. 
    if not MyIdealDataController.InsertData(pd.read_csv (r'ideal.csv')):
        print ("Inserting Data in Ideal Data Table Failed.")
        return

    # Get Data from DataBase
    TrainigData = MyTrainingDataController.GetData()
    IdealData = MyIdealDataController.GetData()

    result = pd.DataFrame()
    trainingFunctionCount = TrainigData.shape[1] - 1
   
    # Find the Ideal Function that best fit each Training Function
    for trainingFunctionIndex in range(1,trainingFunctionCount + 1,1):

        print("Evaluating Training function " +  TrainigData.columns[trainingFunctionIndex] + "...")
         
        # Get the Ideal Function with the Minimum Least Square for the current Training Function
        minLeastSquareIdealFunctionIndex = DataProcessing.GetIdealFunctionIndexWithMinLeastSquare(TrainigData.iloc[:,trainingFunctionIndex].values, IdealData, True)

        # Save results for current Training Function in result DataFrame
        result = result.append({'TrainingFunctionName' : TrainigData.columns[trainingFunctionIndex],
                            'IdealFunctionName' : IdealData.columns[minLeastSquareIdealFunctionIndex]},
                            ignore_index = True)


        # Plot Compairing Current Training Data and its Selected Ideal Function
        plt.plot(TrainigData.iloc[:,0].values,TrainigData.iloc[:,trainingFunctionIndex].values, 'ro', linewidth=10, label = 'Training data')
        plt.plot(IdealData.iloc[:,0].values,IdealData.iloc[:,minLeastSquareIdealFunctionIndex].values, 'go',   linewidth=1, label = 'Ideal data')
        plt.title("Training and ideal data")
        plt.xlabel("x values")
        plt.ylabel("y values")
        plt.legend(loc = 'upper right')

        plt.show()
    print (result)
   
    # Get Test Data from file
    testDataFrame = pd.read_csv (r'test.csv')
    testDataSize = testDataFrame.shape[0]
    finalTestDataFrame = pd.DataFrame()

    # For each point in Test Data...
    for rowIndex in range(0, testDataSize, 1):

        # Save Current Point in xi and yi
        xi = testDataFrame.iat[rowIndex,0]      
        yi = testDataFrame.iat[rowIndex,1] 

        # Get x data from Ideal Data
        x = IdealData.iloc[:,0].values

        maxDiff = None
        maxDiffYdelta = 0
        maxDiffIdealFunctionName = "None"

        # For each Training Function Result...
        for index, row in result.iterrows():
            
            # Get Selected Ideal Function y data for current Training Function
            y = IdealData.loc[:,row["IdealFunctionName"]].values

            # Get absolute deviation between Training Data yi and Selected Ideal Function y evalute in xi
            ydelta = abs(yi - DataProcessing.GetY(x, y, xi))

            # Get Maximum Deviation between Current Training Data and its Selected Ideal Function
            maxDeviation = DataProcessing.GetMaxDeviation(TrainigData.loc[:,row["TrainingFunctionName"]].values, IdealData.loc[:,row["IdealFunctionName"]].values)       
            
            # Calculate threshold as Maximum Deviation times root square of two
            threshold = maxDeviation * np.sqrt(2)

            # Take Training Function into account if deviation does not exceed threshold
            if ydelta <= threshold:
                TempDiff = threshold - ydelta

                # Chose Training Function which ydelta is farthest from threshold
                if maxDiff == None or TempDiff > maxDiff:
                    maxDiff = TempDiff
                    maxDiffYdelta = ydelta
                    maxDiffIdealFunctionName = row["IdealFunctionName"]

        # Save results temporary in a DataFrame
        finalTestDataFrame = finalTestDataFrame.append({'x': xi, 'y' : yi,
                                'deltaY' : maxDiffYdelta,
                                'N' : maxDiffIdealFunctionName},
                                ignore_index = True)

    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(finalTestDataFrame)

    MyTestDataController = TestDataController(DataBaseConnectionString)

    # Create table Test Data
    if not MyTestDataController.CreateTable():
        print ("Creating Test Data Table Failed.")
        return

    # Save Test Data with mapping and y-deviation in DataBase
    if not MyTestDataController.InsertData(finalTestDataFrame):
        print ("Inserting Data in Test Data Table Failed.")
        return

if __name__ == '__main__':
    main()
