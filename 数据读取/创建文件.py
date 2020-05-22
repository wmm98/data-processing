import pandas as pd

# 设置数据
df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tim', 'Victor', 'Nick']})
# 打印数据
print(df)
print("================================")
# 设置ID为索引
df = df.set_index('ID')
df.to_excel('D:/课/数据分析表/ouput.xlsx')
# 打印数据
print(df)
print("完成")
