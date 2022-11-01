import numpy as np

class DataProcessing:

    # Method to get Least Square 
    def GetLeastSquare(y1, y2):
        """ 
        Summary:
    
        Method to get Least Square 
    
        Parameters: 
        y1 (float): y training
        y2 (float): y ideal
    
        Returns: 
        least square (float): Least Square 
    
        """
        try:
            print(y1)
            print(y2)
            # Calculate deviation 
            desviations = abs(y1 - y2)
            # Calculate Least Square
            leastSquare = np.sum(np.power(desviations,2))
            return leastSquare

        except Exception as e:

            print ("DataProcessing.GetLeastSquare: ", e.__cause__, "ocurred.")
            return None

    # Method to get Maximun deviation 
    def GetMaxDeviation(y1, y2):

        """ 
        Summary:
    
        Method to get Maximun deviation 
    
        Parameters: 
        y1 (float): y training
        y2 (float): y ideal
    
        Returns: 
        least square (float): Least Square 
    
        """

        try:
            desviations = abs(y1 - y2)
            return desviations.max()

        except Exception as e:

            print ("DataProcessing.GetMaxDeviation: ", e.__cause__, "ocurred.")
            return None

    # Method to get ideal function index with minimun Least Square
    def GetIdealFunctionIndexWithMinLeastSquare(trainingFunction, idealFunctions, SkipFirstColumn):
        
        """ 
        Summary:
    
        Method to get Maximun deviation 
    
        Parameters: 
        trainingFunction (float): Training Function
        idealFunctions (float): Ideal Function
        SkipFirstColumn (float): Skip Firs Column
    
        Returns: 
        minLeastSquareIdealFunctionIndex (integer): Minimum Least Square Ideal Function Index
    
        """

        try:
            print(trainingFunction)
            print(idealFunctions)

            minLeastSquare = None
            minLeastSquareIdealFunctionIndex = 0

            if SkipFirstColumn:
                IndexStartValue = 1
            else:
                IndexStartValue = 0

            IdealFunctionsCount = idealFunctions.shape[1]
            print(IdealFunctionsCount)

            for idealFunctionIndex in range(IndexStartValue, IdealFunctionsCount, 1):

                leastSquare =  DataProcessing.GetLeastSquare(trainingFunction, idealFunctions.iloc[:,idealFunctionIndex].values)
                print(leastSquare)

                if minLeastSquare == None:
                    minLeastSquare = leastSquare
                    minLeastSquareIdealFunctionIndex = idealFunctionIndex
                elif leastSquare < minLeastSquare:
                    minLeastSquare = leastSquare
                    minLeastSquareIdealFunctionIndex = idealFunctionIndex

                print(minLeastSquareIdealFunctionIndex)
                print(minLeastSquareIdealFunctionIndex)

            return minLeastSquareIdealFunctionIndex

        except Exception as e:

            print ("DataProcessing.GetIdealFunctionIndexWithMinLeastSquare: ", e.__cause__, "ocurred.")
            return None

    # Method to get "y" from a list with "x"
    def GetY(xList, yList, TargetX):
        
        """ 
        Summary:
    
        Method to get "y" from a list with "x"
    
        Parameters: 
    
        xList (list): x List
        yList (list): y List
        TargetX (float): x value target
    
        Returns: 
        yList (float): y value target
    
        """

        try:
            Xsize = xList.shape[0]
            Ysize = yList.shape[0]

            if Xsize != Ysize:
                print("XList and YList must have the same number of rows.")
                return None
        
            for rowIndex in range (0, Xsize - 1, 1):
                if xList[rowIndex] == TargetX:
                    return yList[int(rowIndex)]

        except Exception as e:

            print ("DataProcessing.GetY: ", e.__cause__, "ocurred.")
            return None