import pandas as pd
from matplotlib.font_manager import FontProperties
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']

myfront = FontProperties(fname='C:\WINDOWS\FONTS\ARVO-REGULAR.ttf')
myfont = mpl.font_manager.FontProperties(fname='C:\WINDOWS\FONTS\ARVO-REGULAR.ttf')
labels = '天通苑 天通苑北一区' , '苏州桥 小南庄' , '新街口 如意里小区' , '和平里 小黄庄一区'
df_zf = pd.read_json("zufang.json")
tiantongyuan_count = df_zf['district'].value_counts()['天通苑 天通苑北一区']
suzhouqiao_count = df_zf['district'].value_counts()['苏州桥 小南庄']
xinjiekou_count = df_zf['district'].value_counts()['新街口 如意里小区']
hepingli_count = df_zf['district'].value_counts()['和平里 小黄庄一区']

sizes = [tiantongyuan_count,suzhouqiao_count,xinjiekou_count,hepingli_count]
explode = (0.1,0,0,0)
plt.subplot(111)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.title(u'我',fontproperties=myfont)
plt.rc('font',family=['SimHei'])
plt.show()