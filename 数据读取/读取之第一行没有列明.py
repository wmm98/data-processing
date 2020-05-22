import pandas as pd

people = pd.read_excel("D:\课\数据分析表\people2.xlsx", header=None)
people.columns = [
    'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
people.set_index("PassengerId", inplace=True)
print(people.columns)
# 保存到另一个文件中
people.to_excel("D:\课\数据分析表\output1.xlsx")
print(people.head())
