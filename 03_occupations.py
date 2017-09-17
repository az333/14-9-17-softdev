import csv, random 

jobs = {}


with open('occupations.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    for row in reader:
        jobs[row[0]] = float(row[1])
     

def randomJob ():
    
    


        
