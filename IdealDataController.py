import sqlalchemy as db
from TableController import TableController

class IdealDataController(TableController):
  
    def __init__(self, connectionString):
        super().__init__(connectionString, "idealdata")

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
                idealData = db.Table(
                self.tableName, metaData,
                    db.Column("x", db.FLOAT, nullable=False),
                    db.Column("y1", db.FLOAT, nullable=False),
                    db.Column("y2", db.FLOAT, nullable=False),
                    db.Column("y3", db.FLOAT, nullable=False),
                    db.Column("y4", db.FLOAT, nullable=False),
                    db.Column("y5", db.FLOAT, nullable=False),
                    db.Column("y6", db.FLOAT, nullable=False),
                    db.Column("y7", db.FLOAT, nullable=False),
                    db.Column("y8", db.FLOAT, nullable=False),
                    db.Column("y9", db.FLOAT, nullable=False),
                    db.Column("y10", db.FLOAT, nullable=False),
                    db.Column("y11", db.FLOAT, nullable=False),
                    db.Column("y12", db.FLOAT, nullable=False),
                    db.Column("y13", db.FLOAT, nullable=False),
                    db.Column("y14", db.FLOAT, nullable=False),
                    db.Column("y15", db.FLOAT, nullable=False),
                    db.Column("y16", db.FLOAT, nullable=False),
                    db.Column("y17", db.FLOAT, nullable=False),
                    db.Column("y18", db.FLOAT, nullable=False),
                    db.Column("y19", db.FLOAT, nullable=False),
                    db.Column("y20", db.FLOAT, nullable=False),
                    db.Column("y21", db.FLOAT, nullable=False),
                    db.Column("y22", db.FLOAT, nullable=False),
                    db.Column("y23", db.FLOAT, nullable=False),
                    db.Column("y24", db.FLOAT, nullable=False),
                    db.Column("y25", db.FLOAT, nullable=False),
                    db.Column("y26", db.FLOAT, nullable=False),
                    db.Column("y27", db.FLOAT, nullable=False),
                    db.Column("y28", db.FLOAT, nullable=False),
                    db.Column("y29", db.FLOAT, nullable=False),
                    db.Column("y30", db.FLOAT, nullable=False),
                    db.Column("y31", db.FLOAT, nullable=False),
                    db.Column("y32", db.FLOAT, nullable=False),
                    db.Column("y33", db.FLOAT, nullable=False),
                    db.Column("y34", db.FLOAT, nullable=False),
                    db.Column("y35", db.FLOAT, nullable=False),
                    db.Column("y36", db.FLOAT, nullable=False),
                    db.Column("y37", db.FLOAT, nullable=False),
                    db.Column("y38", db.FLOAT, nullable=False),
                    db.Column("y39", db.FLOAT, nullable=False),
                    db.Column("y40", db.FLOAT, nullable=False),
                    db.Column("y41", db.FLOAT, nullable=False),
                    db.Column("y42", db.FLOAT, nullable=False),
                    db.Column("y43", db.FLOAT, nullable=False),
                    db.Column("y44", db.FLOAT, nullable=False),
                    db.Column("y45", db.FLOAT, nullable=False),
                    db.Column("y46", db.FLOAT, nullable=False),
                    db.Column("y47", db.FLOAT, nullable=False),
                    db.Column("y48", db.FLOAT, nullable=False),
                    db.Column("y49", db.FLOAT, nullable=False),
                    db.Column("y50", db.FLOAT, nullable=False))
                # create actor table and stores the information in metadata
                metaData.create_all(self.engine)
            
            print ("Table " + self.tableName + " created.")
            return True
                    
        except Exception as e:
            print ("IdealDataController.CreateTable: ", e.__cause__, "ocurred.")
            return False
