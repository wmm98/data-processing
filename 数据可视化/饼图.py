import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel("D:\课\数据分析表\Students_data.xlsx", index_col='Field')
print(students)
# \ counterclock:顺时针， startangle最大值从几度开始
students[2017].plot.pie(fontsize=8, counterclock=False, startangle=-180)
plt.title('Source of International Students', fontsize=16, fontweight='bold')
plt.ylabel('2017', fontsize=12, fontweight='bold')
plt.show()