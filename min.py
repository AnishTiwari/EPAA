import glob

with open('C:/Users/home/Downloads/maxmin.txt', 'r') as myfile:
    minmax = myfile.read()
    min=minmax[0:3]
    max=minmax[4:]
    print min
    print max