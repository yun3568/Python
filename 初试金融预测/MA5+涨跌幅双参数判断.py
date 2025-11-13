import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# 1. 读取数据
df = pd.read_csv('real_stock.csv')

# 2. 制造特征 (Features) - AI 的 "眼睛"
# 左眼：涨跌幅 (本来就有)
# 右眼：MA5 (5日均线)
df['MA5'] = df['收盘'].rolling(5).mean()

# 3. 制造目标 (Target) - AI 要猜的 "答案"
df['Tomorrow_Change'] = df['涨跌幅'].shift(-1)
df['Target'] = (df['Tomorrow_Change'] > 0).astype(int)

# 4. 极刑 (数据清洗)
# dropna(): 把任何含有 "空值" (NaN) 的行全部删掉
# 因为前4天算不出MA5，最后1天算不出明天，统统杀掉
df = df.dropna()

# 5. 训练 "双核" AI
# 注意：这里有两个列名！
X = df[['涨跌幅', 'MA5']] 
y = df['Target']

print("正在训练双核 AI (涨跌幅 + MA5)...")
model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

# 6. 刁难 AI (复杂预测)
# 假设一种纠结的情况：
# 今天 "跌" 了 -2% (看起来要完)
# 但是！MA5 还是 15块钱 (比现在的价格高，说明长期还是强的？或者弱的？让AI去判断)

# 我们构造一个测试数据：[涨跌幅=-2.0, MA5=15.0]
X_new = [[-2.0, 15.0]]

prediction = model.predict(X_new)

print("训练完成！")
if prediction[0] == 1:
    print("AI双核判定：虽然今天跌了-2%，但看在MA5的面子上 -> 明天会涨！(抄底)")
else:
    print("AI双核判定：今天跌了，MA5也没救回来 -> 明天会跌！(快跑)")

    # --- 给 AI 打分 ---
# score = 猜对的天数 / 总天数
accuracy = model.score(X, y)

print(f"AI 在历史数据上的准确率是：{accuracy * 100:.2f}%")
