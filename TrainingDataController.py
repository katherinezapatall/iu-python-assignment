
import sqlalchemy as db
from TableController import TableController

class TrainingDataController(TableController):
  
    def __init__(self, connectionString):
        super().__init__(connectionString, "trainingdata")

    # Method to create a SQL table
    def CreateTable(self):

        try:
            print ("Creating table " + self.tableName + "...")

            if self.TableExists():
                if not self.DropTable():
                    print (self.tableName + " Table Dropping Failed.")
                    return False

            # get connection object
            with self.engine.connect() as connection:
                # get meta data object
                metaData = db.MetaData()
                # set actor creation script table``
                trainingData = db.Table(
                self.tableName, metaData,
                db.Column("x", db.FLOAT, nullable=False),
                db.Column("y1", db.FLOAT, nullable=False),
                db.Column("y2", db.FLOAT, nullable=False),
                db.Column("y3", db.FLOAT, nullable=False),
                db.Column("y4", db.FLOAT, nullable=False))
                # create actor table and stores the information in metadata
                metaData.create_all(self.engine)
            
            print ("Table " + self.tableName + " created.")
            return True
                    
        except Exception as e:
            print ("TrainingDataController.CreateTable: ", e.__cause__, "ocurred.")
            return False

