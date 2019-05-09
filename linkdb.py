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
        columns = [col[0] for col in mycursor.description]
        rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]
        #data = mycursor.fetchall()
        return rows


db = dbDataset()
myresult = db.recoverTable("dataset")
print(myresult)
#for x in myresult:
#  print(x)
