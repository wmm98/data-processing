import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel("D:\课\数据分析表\Students_data.xlsx")
# 排序数据
students.sort_values(by=[2016, 2017], inplace=True, ascending=[False, False])
# print(students)
# 此plot为DataFrame的plot
students.plot.bar(x='Field', y=[2016, 2017], color=['orange', 'red', 'blue'])
plt.title('international Student by Field', fontsize=16, fontweight='bold')
plt.xlabel('Field', fontweight='bold')
plt.ylabel('Number', fontweight='bold')
# 调整整个图X坐标的位置
"""
rotation旋转45度
 ha='right'以右为中心点
"""
ax = plt.gca()
ax.set_xticklabels(students['Field'], rotation=45, ha='right')
# 调整图的整个位置，去除多余空白
f = plt.gcf()
# 调左边和底部的位置
f.subplots_adjust(left=0.2, bottom=0.42)
plt.tight_layout()
plt.show()

