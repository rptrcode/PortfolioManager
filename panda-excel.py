import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("transactions.xlsx",sheetname="data");

stocklist = df["Stocks"]
typelist = df["Type"]
unitlist = df["Units"]
costlist = df["Cost"]

stockbuy = {}

for i in df.index:
	if(costlist[i]>300):
		if not stocklist[i] in stockbuy:
			if typelist[i]=='B':
				stockbuy[stocklist[i]] =  costlist[i]*unitlist[i]
			else:
				stockbuy[stocklist[i]] =  -costlist[i]*unitlist[i]
		else:
			if typelist[i]=='B':
				stockbuy[stocklist[i]] += costlist[i]*unitlist[i]
			else:
				stockbuy[stocklist[i]] -= costlist[i]*unitlist[i]

# for k,v in stockbuy.items():
# 	print("\t",k,"\t",v)

# stocks = range(len(stockbuy))
# plt.bar(stocks, stockbuy.values(), align='center', tick_label=stockbuy.keys())

labels = []
values = []

for k,v in stockbuy.items():
	if(v > 500):
		labels.insert(0, k)
		values.insert(0, v)
		print(k,v)


# labels = list(stockbuy.keys())
# values = list(stockbuy.values())

plt.pie(values,labels=labels)

plt.show()

