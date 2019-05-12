import csv

class openCSV:
    def ObtainCSV(self,file):
        with open(file) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            header = next(readCSV) # skip header
            rows = [dict(zip(header, map(float, row))) for row in readCSV]
            return rows

#CSVData = openCSV()
#dataset = CSVData.ObtainCSV('heartdataset.csv')
#print(dataset)
