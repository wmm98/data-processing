import pandas as pd


# def age_18_to_30(age):
#     return 18 <= age < 30
#
#
# def level_a(score):
#     return 85 <= score <= 100


students = pd.read_excel("D:/课/数据分析表/Students.xlsx", index_col='ID')
# loc定位
# students.Age = students["Age"]
# students = students.loc[students.Age.apply(age_18_to_30)].loc[students.Score.apply(level_a)]
# 使用lambda函数
students = students.loc[students.Age.apply(lambda age: 18 <= age < 30)].loc[students.Score.apply(lambda score: 85 <= score <= 100)]

# 按照年龄得升序
# print(students.sort_values(by='Age', inplace=True, ascending=True))
print(students)
