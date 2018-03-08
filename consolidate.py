import pandas as pd
import matplotlib.pyplot as plt
newpath="D:\\ant\\"
df= pd.read_csv(newpath+"Test.csv")
t1_co=df.filter(regex="CO")
t1=t1_co.tail(1)


df2= pd.read_csv(newpath+"Test2.csv")
t2_co=df2.filter(regex="CO")
t2=t2_co.tail(1)
test=t1.append(t2)

df_max=pd.read_csv(newpath+"max_co.csv",index_col=None)
d1 = dict(zip(df_max['0'],map(int,df_max['1'])))
df_max2=pd.read_csv(newpath+"max_co2.csv",index_col=None)
d2 = dict(zip(df_max2['0'],map(int,df_max2['1'])))

d={}    #MAXIMUM MARKS


try:						#EITHER PSR OR OBJECTIVE
	df3=pd.read_csv(newpath+"Objective.csv")
	t3_co=df3.filter(regex="CO")
	t3=t3_co.tail(1)
	test=test.append(t3)

	df3=df3.filter(regex="CO")
	d3=df3.iloc[0]
	d3=d3.fillna(0)
	d3=d3.reset_index()
	d3=dict(zip(d3['index'],map(lambda x: int(x)*(df3.shape[0]-2) , d3[0])))
	for i in d1:
		d[i]=d1[i]+d2[i]+d3[i]


except:
	df4=pd.read_csv(newpath+"PSR.csv")
	t4_co=df4.filter(regex="CO")
	t4=t4_co.tail(1)
	test=test.append(t4)

	d4 = pd.read_csv(newpath+"PSR.csv")
	d4= d4.filter(regex='CO')
	s=d4.shape[0]-2
	d4=d4.iloc[0]
	d4=d4.fillna(0)
	d4=d4.reset_index()
	d4=dict(zip(d4['index'],map(lambda x: int(x)*s,d4[0])))
	for i in d1:
		d[i]=d1[i]+d2[i]+d4[i]

test=test.fillna(0)
test=test.sum()

#for changing dataframe to dictionary
#obtained total marks of (test)

test=test.reset_index()
test = dict(zip(test['index'],map(int,test[0])))

l={}
for i in d:
	try:
		l[i]=(test[i]*100)/d[i]
	except:
		l[i]=0

print l

plt.bar(l.keys(),l.values())
plt.show()
plt.title('CONSOLIDATED COURSE OUTCOMES')
plt.savefig(newpath +'\Consolidated_CO.pdf')

# plt.bar(l.keys(),l.values())

# # fig.suptitle('OVERALL PERFORMANCE (Internal Test)')
# plt.savefig(newpath+"/consolidated.png")

# plt.show()



print d
print test