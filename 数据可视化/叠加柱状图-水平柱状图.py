import pandas as pd
import matplotlib.pyplot as plt


users = pd.read_excel("D:/课/数据分析表/Users.xlsx")
# 计算总数，按照总和排序
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total', inplace=True)
print(users)

# 纵向 stacked=True叠加h
users.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')
users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')
plt.tight_layout()
plt.show()
