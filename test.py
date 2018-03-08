import glob
import pandas as pd

download_path = raw_input('Enter the Downloads directory location...')
with open('C:/Users/admin/Downloads/maxmin.txt', 'r') as myfile:
    minmax = myfile.read()
    min=minmax[0:3]
    max=minmax[4:]

with open('C:/Users/admin/Downloads/file.txt', 'r') as myfile:
    newpath = myfile.read().replace('\n', '')
    print(newpath)

source_dir = "C:/Users/admin/Downloads"  # Path where your files are at the moment
allFiles = glob.glob(source_dir + "/*test*.csv")
df = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_, index_col=None)
    list_.append(df)
df = pd.concat(list_)
df = df[
    ['NO', 'NAME', 'ROLLNO', 'QN1', 'QN2', 'QN3', 'QN4', 'QN5', 'QN6', 'QN7', 'QN8', 'QN9', 'QN10', 'QN11a',
     'QN11b',
     'QN12a', 'QN12b', 'QN13a', 'QN13b', 'TOTAL', 'PERCENT', 'RESULT']]
df.drop(df.index[2])

# raw_data = dict(QN1=1, QN2=1, QN3=1, QN4=1, QN5=1, QN6=3, QN7=3, QN8=3, QN9=3, QN10=3, QN11a=8, QN11b=7,
#                 QN12a=8, QN12b=7, QN13a=8, QN13b=7)
# df = df.append(raw_data, ignore_index=True)
summa = df
new_header = summa.iloc[0]  # grab the first row for the header
summa = summa[1:]  # take the data less the header row
summa.columns = new_header  # set the header row as the summa header
orgco = summa.iloc[2:]
orgcovalue = orgco.groupby(orgco.columns, axis=1).sum()
orgcovalue = orgcovalue.reset_index()
orgcovalue['index'] = orgcovalue.index + 3
df = df.reset_index()
df['index'] = df.index
new = df.set_index('index').join(orgcovalue.set_index('index'))
summa = df
new_header = summa.iloc[1]
summa = summa[3:]  # getting rows for cl's
summa.columns = new_header
orgcl = summa
orgclvalue = orgcl.groupby(orgcl.columns, axis=1).sum()
orgclvalue = orgclvalue.reset_index()
del orgclvalue[1]
old = df.set_index('index').join(orgclvalue.set_index('index'))
answer = new.merge(old)
col_list = list(answer)
col_list.remove('ROLLNO')
col_list.remove('NAME')
col_list.remove('NO')
col_list.remove('RESULT')
answer.loc['Column_Total'] = answer[col_list].sum(axis=0)

df = answer
header_ = list(df)
cos = df.iloc[0]
cl = df.iloc[1]

# for calculating the total marks of each COS


cos_total = {'CO1': 0, 'CO2': 0, 'CO3': 0, 'CO4': 0, 'CO5': 0, 'CO6': 0, 'CO7': 0}
cl_total = {'CL1': 0, 'CL2': 0, 'CL3': 0, 'CL4': 0, 'CL5': 0, 'CL6': 0}

for i in range(header_.index('QN1'), header_.index('QN13b')+1):
    # print df[header_[i]][2]
    try:
        cos_total[cos[i]] += int(df[header_[i]][2])
    except:
        cos_total[cos[i]] += 0

    try:
        cl_total[cl[i]] += int(df[header_[i]][2])
    except:
        cl_total[cl[i]] += 0

####To store the total of COs and CLs in CSV file

for i in range(header_.index(min), header_.index(max) + 1):
    try:
        df.at[2, header_[i]] = cos_total[header_[i]]
    except:
        df.at[2, header_[i]] = cl_total[header_[i]]

df.sort_values('ROLLNO')
df.to_csv(newpath + "/Test/Test1.csv")


cos_max = {'CO1': 0, 'CO2': 0, 'CO3': 0, 'CO4': 0, 'CO5': 0, 'CO6': 0, 'CO7': 0}
cl_max = {'CL1': 0, 'CL2': 0, 'CL3': 0, 'CL4': 0, 'CL5': 0, 'CL6': 0}

for j in range(3,df.shape[0]):

	for i in range(header_.index('QN1'), header_.index('QN13b')+1):

		try :
			int(df[header_[i]][j])
			cos_max[cos[i]] += int(df[header_[i]][2])
			cl_max[cl[i]] += int(df[header_[i]][2])
		except:
			x=1


# x=[]
# for i in range(header_.index('CO1'), header_.index('CL6') + 1):
	# x.append(df[header_[i]][df.shape[0]-1])

y=[]
x = [cos_max[i] for i in cos_max]

print sorted(cos_max,key = lambda k: k)

for i in sorted(cos_max,key = lambda k: k):
	if cos_max[i]!=0:
		y.append(df[header_[header_.index(i)]][df.shape[0]-1] / cos_max[i] *100)
		
print y

# print co_df
# df2 = df.filter(regex='CO')
# v = df.shape[0] - 4
# divided = df2.iloc[v+3] / df2.iloc[2]
# divided = (divided[0:] / v) * 100
# coplot = divided.plot.bar()
# fig = coplot.get_figure()
# fig.suptitle('COURSE OUTCOMES(Internal Test)')
# fig.savefig(newpath + "/Test_CO.pdf")
v = df.shape[0] - 4
df3 = df.filter(regex='CL')
dividedcl = df3.iloc[v+3] / df3.iloc[2]
#  formula:(total/fullmark*no of students)*100
dividedcl = (dividedcl[0:] / v) * 100
clplot = dividedcl.plot.bar()
fig = clplot.get_figure()
fig.suptitle('COGNITIVE LEVEL(Internal Test 1)')
fig.savefig(newpath + "/Test1_CL.pdf")


new = pd.DataFrame({'COs':y})
new = new.plot.bar()
fig9 = new.get_figure()
fig9.suptitle('COURSE OUTCOMES (Internal Test 1)')
fig9.savefig(newpath+"/Test1_CO.pdf")











# for calculating the number of pass students in each COs and CLs
pass_co = {'CO1': 0, 'CO2': 0, 'CO3': 0, 'CO4': 0, 'CO5': 0, 'CO6': 0, 'CO7': 0}  # number of pass student in each COs
pass_cl = {'CL1': 0, 'CL2': 0, 'CL3': 0, 'CL4': 0, 'CL5': 0, 'CL6': 0}  # number of pass student in each CLs

for i in range(header_.index(min), header_.index(max) + 1):
    pass_marks = df[header_[i]][2] // 2
    c = 0
    for j in range(3, len(df)):
        if df[header_[i]][j] >= pass_marks:
            c += 1
    if header_[i][1] == 'O':
        pass_co[header_[i]] = c
    else:
        pass_cl[header_[i]] = c

        # df.at[2,header_[i]]=c

co_column = [i for i in pass_co]
cl_column = [i for i in pass_cl]

co_data = [pass_co[i] for i in pass_co]
cl_data = [pass_cl[i] for i in pass_cl]

co_df = pd.DataFrame(index=range(3), columns=co_column)
for i in range(len(co_data)):
    co_df.at[0, co_column[i]] = co_data[i]

cl_df = pd.DataFrame(index=range(3), columns=cl_column)
for i in range(len(cl_data)):
    cl_df.at[0, cl_column[i]] = cl_data[i]



co_df.to_csv(newpath + "/co_pass_test1.csv")
cl_df.to_csv(newpath + "/cl_pass_test1.csv")

#			IMPORTANT THINGS
#		>>	TO CHANGE THE VALUE IN DATAFRAME
#			df.at[3,'NAME']='rahul'
#		>> To ADD the new column
#		    df['new_column_name'] = None     // with all values No ne
total = df['PERCENT']
below50 = total<50
sum(below50)
btw50to60 = (total>=50)&(total<60)
sum(btw50to60)
btw60to70 = (total>=60)&(total<70)
sum(btw60to70)
btw70to80 = (total>=70)&(total<80)
sum(btw70to80)
btw80to90 = (total>=80)&(total<90)
sum(btw80to90)
above90 = (total>=90)&(total<=100)
sum(above90)

x = [sum(below50)]
y = [sum(btw50to60)]
z = [sum(btw60to70)]
a = [sum(btw70to80)]
b = [sum(btw80to90)]
c = [sum(above90)]

vdf = pd.DataFrame({'Below50':x, '50-60':y, '60-70':z, '70-80':a,'80-90':b,'Above90':c})
vdf = vdf.plot.bar()
fig = vdf.get_figure()
fig.suptitle('OVERALL PERFORMANCE (Internal Test 1)')
fig.savefig(newpath+"/Overall_Performance_test1.pdf")


cos_max_csv=pd.DataFrame(cos_max.items())
cos_max_csv.to_csv(newpath+"max_co.csv")
