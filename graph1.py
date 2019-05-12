import matplotlib.pyplot as plt
from linkdb import dbDataset
from importcsv import openCSV
 #BASIC PLOTTING OF DATASET WITHOUT PROCCESING INFORMATION WITH UNLABELED DATA

#db = dbDataset()
#myresult = db.recoverTable("dataset")
CSVData = openCSV()
myresult = CSVData.ObtainCSV('heartdataset.csv')

age  = [d.get('age') for d in myresult]
trestbps  = [d.get('trestbps') for d in myresult]
chol  = [d.get('chol') for d in myresult]
thalach = [d.get('thalach') for d in myresult]
cp = [d.get('cp') for d in myresult]
ca = [d.get('ca') for d in myresult]


#Plotting Age in Y-Axis
plt.subplot(4, 1, 1)
plt.title('Dataset with unlabeled data')
plt.plot( thalach, age, 'go')
plt.ylabel('Age')
#Plotting Resting BPS in Y-Axis
plt.subplot(4, 1, 2)
plt.plot(thalach, trestbps,'go')
plt.ylabel('Resting BPS')
#Plotting Cholestoral in Y-Axis
plt.subplot(4, 1, 3)
plt.plot(thalach, chol,'go')
plt.ylabel('Cholestoral')
#Plotting ChestPain Range in Y-AXIS
plt.subplot(4, 1, 4)
plt.plot(thalach, cp,'go')
plt.ylabel('ChestPain')

plt.xlabel('Max Heart Rate')


plt.show()
