import pandas as pd

# 指定ID便不会生成多余的ID
df = pd.read_excel("D:\课\数据分析表\output1.xlsx", index_col='PassengerId')
print(df.columns)
print(df.head())
df.to_excel("D:\课\数据分析表\output2.xlsx")
print("Done!")