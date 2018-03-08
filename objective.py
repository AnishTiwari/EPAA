import pandas as pd
import glob

with open('C:/Users/home/Downloads/file.txt', 'r') as myfile:
    newpath = myfile.read().replace('\n', '')
    print(newpath)
print(newpath)

source_dir = "C:/Users/home/Downloads"  # Path where your files are at the moment
allFiles = glob.glob(source_dir + "/*obj*.csv")
df = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, index_col=None)
    list_.append(df)
df = pd.concat(list_)

df = df[
    ['NAME', 'ROLLNO', 'CO1', 'CO2', 'CO3', 'CO4', 'CO5', 'CO6', 'CO7']]
coonly = df.iloc[1:, 2:]
col_list = list(df)
col_list.remove('ROLLNO')
col_list.remove('NAME')
df.loc['Column_Total'] = coonly[col_list].sum(axis=0)
v = df.shape[0] - 2
df2 = df
divided = df2.iloc[v + 1] / df2.iloc[0, 2:]
divided = (divided[0:7] / v) * 100
divided.to_csv(newpath +"/obj_co.csv")
coplot = divided.plot.bar()
fig = coplot.get_figure()
fig.suptitle('COURSE OUTCOMES')
fig.savefig(newpath +"/Objective_CO.pdf")
df.sort_values('ROLLNO')
df.to_csv(newpath + "/Objective.csv")
