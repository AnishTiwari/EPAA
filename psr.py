import pandas as pd
import glob

with open('C:/Users/home/Downloads/file.txt', 'r') as myfile:
    newpath = myfile.read().replace('\n', '')
    print(newpath)
print(newpath)

source_dir = "C:/Users/home/Downloads"  # Path where your files are at the moment
allFiles = glob.glob(source_dir + "/*psr*.csv")
df = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, index_col=None)
    list_.append(df)
df = pd.concat(list_)

df = df[['NAME','ROLLNO','CO1', 'CO2', 'CO3', 'CO4', 'CO5', 'CO6', 'CO7']]
cos_max = {'CO1': 0, 'CO2': 0, 'CO3': 0, 'CO4': 0, 'CO5': 0, 'CO6': 0, 'CO7': 0}
header_=list(df)
cos = df.iloc[0]

for i in range(header_.index('CO1'),header_.index('CO7')+1):
	for j in range(df.shape[0]):
			print df[header_[i]][j]