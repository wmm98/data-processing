import pandas as pd

people = pd.read_excel("D:\课\数据分析表\people1.xlsx", header=1)
"""
这个时候第一行就不是标题名，需要设置header=1
第一行是空的时候不需要设置，可以正常识别
"""
print(people.columns)