import unittest
import pandas as pd
from DataProcessing import DataProcessing


class UnitTestDataProcessing(unittest.TestCase):

    def test_GetLeastSquare(self):
        '''
        test Get Least Square
        '''
        testData = {"y1":[1, 2, 3, 4], "y2":[6, 7, 8, 9]}
        testDataFrame = pd.DataFrame(data=testData)
        print(testDataFrame)

        result = DataProcessing.GetLeastSquare(testDataFrame.iloc[:,0].values, testDataFrame.iloc[:,1].values)
        self.assertEqual(result, 100, "The Least Square should be 100")


    def test_GetMaxDeviation(self):
        '''
        test Get Maximun Deviation
        '''
        testData = {"y1":[5, 1, 9, 3], "y2":[18, 9, 18, 29]}
        testDataFrame = pd.DataFrame(data=testData)
        print(testDataFrame)

        result = DataProcessing.GetMaxDeviation(testDataFrame.iloc[:,0].values, testDataFrame.iloc[:,1].values)
        self.assertEqual(result, 26, "The Maximum Deviation should be 26")

    def test_GetIdealFunctionIndexWithMinLeastSquare(self):
        '''
        test Get Ideal Function Index With Min Least Square
        '''
        testTrainingData = {"y":[5, 1, 9, 3]}
        testTrainingtDataFrame = pd.DataFrame(data=testTrainingData)
        print(testTrainingtDataFrame)

        testIdealData = {"x":[5, 1, 9, 3],"y1":[3, 2, 4, 6], "y2":[8, 9, 18, 9], "y3":[1, 5, 3, 2]}
        testIdealDataFrame = pd.DataFrame(data=testIdealData)
        print(testIdealDataFrame)

        result = DataProcessing.GetIdealFunctionIndexWithMinLeastSquare(testTrainingtDataFrame.values, testIdealDataFrame, True)
        self.assertEqual(result, 1, "The Ideal Function Index With Min Least Square should be 1")


    def test_GetY(self):
        '''
        test Get corresponding Y from X
        '''
        testData = {"x":[5, 1, 9, 3],"y1":[3, 2, 4, 6],}
        testDataFrame = pd.DataFrame(data=testData)

        result = DataProcessing.GetY(testDataFrame.iloc[:,0].values, testDataFrame.iloc[:,1].values, 9)
        self.assertEqual(result, 4, "Y value for X = 9 should be 4")

if __name__ == "__main__":
    unittest.main()
