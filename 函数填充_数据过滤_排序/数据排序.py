import pandas as pd

products = pd.read_excel("D:/课/数据分析表/List.xlsx", index_col='ID')
# 排序
"""
inplace=True在原来的数据上进行排序
ascending=True 升序排序
"""
# products.sort_values(by='Wealthy', inplace=True, ascending=True)
# 多个条件进行排序,
products.sort_values(by=['Wealthy', 'Price'], inplace=True, ascending=[True, False])
print(products)
