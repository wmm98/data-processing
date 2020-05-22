import pandas as pd
from datetime import date, timedelta

"""skiprows=3 跳过3行， usecols="C:F" 使用列， 
dtype={'ID': str, 'InStore': str, 'Date': str}使得显示的数据是整型
"""


# 月份增加
def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    print("===============")
    print(m)
    if m != 12:
        yd += m // 12
        m = m % 12
        return date(d.year + yd, m, d.day)


books = pd.read_excel("D:\课\数据分析表\Books.xlsx", skiprows=3, usecols="C:F",
                      index_col=None, dtype={'ID': str, 'InStore': str, 'Date': str})

print(books)
print("====================================")
# 设置日期
start = date(2018, 12, 1)
# 第0个元素为1
# books['ID'].at[0] = 1
for i in books.index:
    # books['ID'].at[i] = i + 1
    # 另外一种表示方法
    books.at[i, 'ID'] = i + 1

    # 交替设置
    # books['InStore'].at[i] = 'Yes' if i % 2 == 0 else "No"
    books.at[i, 'InStore'] = 'Yes' if i % 2 == 0 else "No"

    # 设置日增加
    # books['Date'].at[i] = start + timedelta(days=i)
    # 设置年增加
    # books['Date'].at[i] = date(start.year + i, start.month, start.day)
    # 逐月增加
    # books['Date'].at[i] = add_month(start, i)
    books.at[i, 'Date'] = add_month(start, i)
    print("=====================")
    # print(add_month(start, i))
print(books)
books.set_index('ID', inplace=True)
books.to_excel("D:\课\数据分析表\Books_new.xlsx")
