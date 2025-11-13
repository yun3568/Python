import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#尝试读取刚创建的数据
data = pd.read_csv('fengsheng.csv')

#打印出来，判断是否读取
print(data)

#数角色列的值
character_counts = data['角色'].value_counts()
print(character_counts)

character_counts.plot(kind='bar')
plt.show()
