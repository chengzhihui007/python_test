import pandas as pd

#读取文件
df = pd.read_json("zufang.json")
print(df)
#print(df.columns)
#使用pandas的describe方法，打印基本信息
#print(df.describe())
#按照区，分别统计个数
print(
    df["district"].value_counts()
)