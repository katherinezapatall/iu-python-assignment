import unittest
from sqlalchemy.engine import reflection
from IdealDataController import IdealDataController
import sqlalchemy as db
import pandas as pd


class UnitTestIdealDataController(unittest.TestCase):

    connectionDabaBase="mysql+pymysql://root:123456.*Jk@localhost:3306/test"
    engine = db.create_engine(connectionDabaBase)
    
    def test_CreateTable(self):
        '''
        test create SQL table
        '''
        MyIdealDataController = IdealDataController(self.connectionDabaBase)
        insp = reflection.Inspector.from_engine(self.engine)
        tablesList = insp.get_table_names()
        
        tableExists = False

        if MyIdealDataController.TableName in tablesList:
            tableExists = True
    
        self.assertEqual(tableExists, True, "The SQL table was create")

    def test_InsertData(self):
        '''
        Test Insert Data in SQL table

        '''
        MyIdealDataController = IdealDataController(self.connectionDabaBase)

        MyIdealDataController.InsertData(pd.read_csv (r'ideal.csv'))

        with self.engine.connect() as connection:
            dataFrame = pd.read_sql('SELECT * FROM ' + MyIdealDataController.TableName, connection)
            dataFrame.head()

        dataInserted = False
        if not dataFrame.empty:
            dataInserted = True

        self.assertEqual(dataInserted, True, "Data was inserted in Table")


    def test_TableExists(self):
        '''
        Test if Table Exists in SQL table
        
        '''
        MyIdealDataController = IdealDataController(self.connectionDabaBase)

        insp = reflection.Inspector.from_engine(self.engine)
        tablesList = insp.get_table_names()

        tableExists = False
        if MyIdealDataController.TableName in tablesList:
            return True

        self.assertEqual(tableExists, True, "Table Exist")

if __name__ == "__main__":
    unittest.main()
