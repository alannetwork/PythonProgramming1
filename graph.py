import matplotlib.pyplot as plt
from linkdb import dbDataset
from importcsv import openCSV
 #BASIC PLOTTING OF DATASET WITHOUT PROCCESING INFORMATION WITH LABELED DATA
#db = dbDataset()
#myresult = db.recoverTable("dataset")
CSVData = openCSV()
myresult = CSVData.ObtainCSV('heartdataset.csv')

age0  = [d.get('age') for d in myresult if d['target']==0]
trestbps0  = [d.get('trestbps') for d in myresult if d['target']==0]
chol0  = [d.get('chol') for d in myresult if d['target']==0]
thalach0  = [d.get('thalach') for d in myresult if d['target']==0]
cp0  = [d.get('cp') for d in myresult if d['target']==0]
ca0  = [d.get('ca') for d in myresult if d['target']==0]

age1  = [d.get('age') for d in myresult if d['target']==1]
trestbps1  = [d.get('trestbps') for d in myresult if d['target']==1]
chol1  = [d.get('chol') for d in myresult if d['target']==1]
thalach1  = [d.get('thalach') for d in myresult if d['target']==1]
cp1  = [d.get('cp') for d in myresult if d['target']==1]
ca1  = [d.get('ca') for d in myresult if d['target']==1]

#Plotting Age in Y-Axis
plt.subplot(4, 1, 1)
plt.title('Dataset with labeled data')
plt.plot( thalach0, age0, 'bo', thalach1, age1,'ro')
plt.ylabel('Age')
#Plotting Resting BPS in Y-Axis
plt.subplot(4, 1, 2)
plt.plot(thalach0, trestbps0,'bo',thalach1,trestbps1,'ro')
plt.ylabel('Resting BPS')
#Plotting Cholestoral in Y-Axis
plt.subplot(4, 1, 3)
plt.plot(thalach0, chol0,'bo',thalach1,chol1,'ro')
plt.ylabel('Cholestoral')
#Plotting ChestPain Range in Y-AXIS
plt.subplot(4, 1, 4)
plt.plot(thalach0, cp0,'bo',thalach1,cp1,'ro')
plt.ylabel('ChestPain')

# X-Axis means for the max heart rate
plt.xlabel('Max Heart Rate')


plt.show()
