import pandas as pd

people = pd.read_excel("D:\课\数据分析表\people.xlsx")
# 打印出行列 (891, 12)
print(people.shape)
# 打印列名
print(people.columns)
"""Index(['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
      dtype='object')"""

# 打印前5行数据
print(people.head())
# 打印前10行数据
print(people.head(10))
print("===================")
# 后面5行数据
print(people.tail())