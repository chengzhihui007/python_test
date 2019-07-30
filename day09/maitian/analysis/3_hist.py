import pandas as pd
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_json("zufang.json")

print(df.columns)

unitprice_values = df.price
plt.hist(unitprice_values,bins=50)
plt.xlim(0,20000)
plt.title(u"房屋出售每平米价格分布")
plt.xlabel(u'价格(单位：万/平方米)')
plt.ylabel(u'套数')
plt.show()