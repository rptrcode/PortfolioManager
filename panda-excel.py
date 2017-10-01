import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
from pandas import ExcelWriter
from openpyxl import load_workbook

df = pd.read_excel("transactions.xlsx",sheetname="data");

stocklist = df["Stock"]
typelist = df["Type"]
unitlist = df["Unit"]
costlist = df["Cost"]


# stocklist = ["SBI","SBI","SBI","SBI"]
# typelist = ['B','B','S','B']
# costlist = [1000,2000,1000,1000]
# unitlist = [2,1,1,3]


stockbuy = {}

# for i in df.index:
for i,stock in enumerate(stocklist):
	if not stocklist[i] in stockbuy:
		if typelist[i]=='B':
			stockbuy[stocklist[i]] =  costlist[i]*unitlist[i]
			# print("First Buy adding value=",stockbuy[stocklist[i]],"\n")
		elif typelist[i]=='S':
			stockbuy[stocklist[i]] =  -costlist[i]*unitlist[i]
			# print("First Sell adding value=",stockbuy[stocklist[i]],"\n")
	else:
		# print("already in list ",i,typelist[i])
		if str(typelist[i])==str('B'):
			# print("buying value=",costlist[i]*unitlist[i])
			stockbuy[stocklist[i]] += costlist[i]*unitlist[i]
			# print("total now =",stockbuy[stocklist[i]],"\n")
		elif str(typelist[i])==str('S'):
			# print("selling value=",costlist[i]*unitlist[i])			
			stockbuy[stocklist[i]] -= costlist[i]*unitlist[i]
			# print("total now =",stockbuy[stocklist[i]],"\n")

# for k,v in stockbuy.items():
# 	print("\t",k,"\t",v)

# stocks = range(len(stockbuy))
# plt.bar(stocks, stockbuy.values(), align='center', tick_label=stockbuy.keys())

labels = []
values = []

for k,v in stockbuy.items():
	if(v>300):
		labels.insert(0, k)
		values.insert(0, v)
		# print(k,v)

# print("total=",len(labels))

# labels = list(stockbuy.keys())
# values = list(stockbuy.values())
# plt.pie(values,labels=labels)
# plt.show()


sortedl, sortedv = zip(*sorted(zip(labels, values),key=lambda x:x[1]))

d = {'stock':sortedl,'values':sortedv}


datafr = pd.DataFrame(d)

# print(datafr)
# writer = ExcelWriter('transactions.xlsx')
# datafr.to_excel(writer, sheet_name='python')
# writer.save()


book = load_workbook('transactions.xlsx')
exclwriter = ExcelWriter('transactions.xlsx', engine='openpyxl') 
exclwriter.book = book
deletesheet = book.get_sheet_by_name("python")
book.remove_sheet(deletesheet)
exclwriter.sheets = dict((ws.title, ws) for ws in book.worksheets)
datafr.to_excel(exclwriter, "python")
exclwriter.save()