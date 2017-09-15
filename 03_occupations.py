dictionary = {} 

f = open("occupations.csv", 'r')
lines = f.read().strip("\n").strip("\r"); 
for line in lines:

    data = line.split(",")
    print data
   # dictionary[data[0]] = data[1];

#print dictionary
