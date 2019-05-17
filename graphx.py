import matplotlib.pyplot as plt
from linkdb import dbDataset
from importcsv import openCSV
from sklearn.neural_network import MLPClassifier

CSVData = openCSV()
myresult = CSVData.ObtainCSV('heartdataset.csv')
values=[]
target=[]
#print(myresult)
for i in range(len(myresult)):
    target.append(myresult[i].pop("target"))
    values.append(list(myresult[i].values()))
print(len(values))
print(len(target))


X = values
y = target

clf = MLPClassifier(activation='relu',solver='adam', alpha=1e-5,
                    hidden_layer_sizes=(10, 5, 3), max_iter=900, random_state=1)

clf.fit(X, y)

print(clf.predict([[57.0, 0.0, 1.0, 130.0, 236.0, 0.0, 0.0, 174.0, 0.0, 0.0, 1.0, 1.0, 2.0],[59.0, 1.0, 0.0, 164.0, 176.0, 1.0, 0.0, 90.0, 0.0, 1.0, 1.0, 2.0, 1.0]]))
print(clf.score(X,y))
