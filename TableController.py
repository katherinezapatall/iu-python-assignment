
import sqlalchemy as db
import pandas as pd

from sqlalchemy.engine import reflection

class TableController:

    def __init__(self, connectionString, tableName):
        self.engine = db.create_engine(connectionString)
        self.tableName = tableName

    def TableName(self):
        return self.tableName 

    def InsertData(self, dataList):

        try:

            print ("Inserting Data into table " + self.tableName + "...")
            metaData = db.MetaData()
            records = dataList.to_dict(orient='records')

            #note rather than creating a sql string you can also create the Table with a table object, checkout the sqlalchemy tutorial I linked

            targetTable = db.Table(self.tableName, metaData, autoload_with =self.engine)

            with self.engine.connect() as connection:
                connection.execute(targetTable.insert(),records)

            print ("Data into table " + self.tableName + " inserted.")
            return True

        except Exception as e:
            print ("TableController.InsertData." + self.tableName + ": ", e.__cause__, "ocurred.")
            return False


    def TableExists(self):

        try:
            print ("Validating if table " + self.tableName + " exists...")

            insp = reflection.Inspector.from_engine(self.engine)
            tablesList = insp.get_table_names()

            if self.tableName in tablesList:
                print ("Table " + self.tableName + " found.")
                return True
            else:
                print ("Table " + self.tableName + " not found.")
                return False

        except Exception as e:
            print ("TableController.TableExists." + self.tableName + ": ", e.__cause__, "ocurred.")
            return False


    def DropTable(self):

        try:
            print ("Dropping " + self.tableName + " table...")
            metadata = db.MetaData()
            metadata.reflect(bind=self.engine)
            table = metadata.tables[self.tableName]

            if table is not None:
                metadata.drop_all(self.engine,[table], checkfirst=True)

            print ("Table " + self.tableName + " dropped.")
            return True

        except Exception as e:
            print ("TableController.DropTable." + self.tableName + ": ", e.__cause__, "ocurred.")
            return False


    def GetData(self):

        try:

            print ("Recovering data from table " + self.tableName + "...")
            with self.engine.connect() as connection:
                dataFrame = pd.read_sql('SELECT * FROM '+ self.tableName, connection)
                dataFrame.head()

            print ("Data from table " + self.tableName + " recovered.")
            return dataFrame

        except Exception as e:
            print ("TableController.GetData." + self.tableName + ": ", e.__cause__, "ocurred.")
            return None

