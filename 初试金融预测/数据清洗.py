import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('real_stock.csv')

df['Tomorrow_Change'] = df['涨跌幅'].shift(-1)

df['Target'] = (df['Tomorrow_Change'] > 0).astype(int)

df = df.dropna()

X = df[['涨跌幅']]
y = df['Target']

print("AI正在学习2023年平安银行的所有走势...")
model = DecisionTreeClassifier(random_state=0)
model.fit(X,y)

scenario_A = [[5.0]]
scenario_B = [[-5.0]]

pred_A = model.predict(scenario_A)
pred_B = model.predict(scenario_B)

print("学习完成！AI的判断如下：")
print(f"如果今天大涨5%，AI预测明天会：{'涨'if pred_A[0]==1 else '跌'}")
print(f"如果今天大跌-5%，AI预测明天会：{'涨'if pred_B[0]==1 else '跌'}")

from sklearn import tree
import matplotlib.pyplot as plt

# 设置一下字体，防止乱码 (又是这一套，是不是很眼熟？)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 准备画布
plt.figure(figsize=(24, 12))

# 画出决策树
# filled=True: 上色
# feature_names: 告诉它我们的 X 叫什么名字
# class_names: 告诉它 0是跌, 1是涨
tree.plot_tree(model, 
               filled=True, 
               feature_names=['今日涨跌幅'], 
               class_names=['跌', '涨'])
# dpi=300 代表 "高清" (300像素/英寸)
# figsize=(20, 10) 把画布拉大，防止字挤在一起
plt.gcf().set_size_inches(20, 10)
plt.savefig('tree.png', dpi=300)
print("图片已保存为 tree.png，去文件夹里打开它！")
