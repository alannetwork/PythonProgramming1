
import matplotlib.pyplot as plt 
import numpy as np
from sklearn.cluster import KMeans
from importcsv import openCSV

CSVData = openCSV()
myresult = CSVData.ObtainCSV('heartdataset.csv')

#declaramos una variable como lista 
vector = []

#obtenemos los datos de las cabeceras del csv
age  = [data.get('age') for data in myresult]
trestbps  = [data.get('trestbps') for data in myresult]
chol  = [data.get('chol') for data in myresult]
thalach = [data.get('thalach') for data in myresult]
cp = [data.get('cp') for data in myresult]
ca = [data.get('ca') for data in myresult]
target = [data.get('target') for data in myresult]

for i in range(len(thalach)):
    vector.append([thalach[i],chol[i]])

X = np.array(vector)

kmean = KMeans(n_clusters=2)
kmean.fit(X)
print(kmean.cluster_centers_)
print(kmean.labels_)

plt.scatter(X[:,0],X[:,1], c=kmean.labels_, cmap='rainbow')  
plt.scatter(kmean.cluster_centers_[:,0] ,kmean.cluster_centers_[:,1], color='black')
plt.show()