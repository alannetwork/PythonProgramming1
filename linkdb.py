import mysql.connector

class dbDataset:
    def __init__(self):
        self.mydb = mysql.connector.connect(
          host="workshop-1.cgd5y8wpwke1.us-east-1.rds.amazonaws.com",
          user="admin",
          passwd="82eEzsl5wnuEsX0UG9sZ",
          database="heartdisease_schema"
        )

    def recoverTable(self,table):
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT * FROM " + table)

        data = mycursor.fetchall()
        return data


db = dbDataset()
myresult = db.recoverTable("dataset")
for x in myresult:
  print(x)
