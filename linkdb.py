import mysql.connector

class dbDataset:
    def __init__(self):
        #Link to databse
        self.mydb = mysql.connector.connect(
          host="workshop-1.cgd5y8wpwke1.us-east-1.rds.amazonaws.com",
          user="admin",
          passwd="82eEzsl5wnuEsX0UG9sZ",
          database="heartdisease_schema"
        )

    def recoverTable(self,table):
        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target FROM " + table)
        # Extract headers
        columns = [col[0] for col in mycursor.description]
        #Generate list of Dict
        rows = [dict(zip(columns, row)) for row in mycursor.fetchall()]
        return rows
#db = dbDataset()
#myresult = db.recoverTable("dataset")
#print(myresult)
