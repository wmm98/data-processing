import pandas as pd


books = pd.read_excel("D:/课/数据分析表/foods.xlsx", index_col='ID')
# 计算整个列的时候
# books['price'] = books['ListPrice'] * books['Discount']
# books['price'] = books['ListPrice'] * 0.8

# 计算一段数据的时候, 全部遍历的时候，就是一个一个得计算，不高效
# for i in books.index:
#     books['price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]

# for i in range(15, 21):
#     books['price'].at[i] = books['ListPrice'].at[i] * books['Discount'].at[i]

# 价格增加2
# books['ListPrice'] = books['ListPrice'] + 2
books['ListPrice'] = books['ListPrice'].apply(lambda x: x + 2)
print(books)