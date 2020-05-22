import pandas as pd

# 按照索引对齐生成数据
# s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
# s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
# s3 = pd.Series([100, 200, 300], index=[1, 2, 3], name='C')
#
# df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
# print(df.index)
# print("===========================================")
# print(df)
"""
   A   B    C
1  1  10  100
2  2  20  200
3  3  30  300
"""


# 索引不对齐
s1 = pd.Series([1, 2, 3], index=[1, 2, 3], name='A')
s2 = pd.Series([10, 20, 30], index=[1, 2, 3], name='B')
s3 = pd.Series([100, 200, 300], index=[2, 3, 4], name='C')

df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})
print(df.index)
print("===========================================")
print(df)
"""
     A     B      C
1  1.0  10.0    NaN
2  2.0  20.0  100.0
3  3.0  30.0  200.0
4  NaN   NaN  300.0
"""