import pandas as pd
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
district = ('天通苑 天通苑北一区' , '苏州桥 小南庄' , '新街口 如意里小区' , '和平里 小黄庄一区')

#读取租房数据
df_zf = pd.read_json("zufang.json")
unitprice_zf = (df_zf['price'])/(df_zf['area'])
df_zf['price'] = unitprice_zf
month_price = df_zf.groupby(by=['district']).sum()['price'] / df_zf['district'].value_counts()

#print(month_price)

Jan_ratio = month_price/31
Feb_ratio = month_price/28
Mar_ratio = month_price/31
Apr_ratio = month_price/30

ratio = (Jan_ratio,Feb_ratio,Mar_ratio,Apr_ratio)


fig, ax = plt.subplots()

y_pos = np.arange(len(district))
print(y_pos)
ax.barh(y_pos,ratio,align='center',color='green',ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(district)
ax.set_xlabel('售租比(单位：月)')
ax.set_title('各区房屋租售比')

plt.show()


