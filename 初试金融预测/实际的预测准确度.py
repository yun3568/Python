import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split # <--- 新工具：切分器

# 1. 还是老规矩，读取和制造特征
df = pd.read_csv('real_stock.csv')
df['MA5'] = df['收盘'].rolling(5).mean()
df['Tomorrow_Change'] = df['涨跌幅'].shift(-1)
df['Target'] = (df['Tomorrow_Change'] > 0).astype(int)
df = df.dropna()

X = df[['涨跌幅', 'MA5']]
y = df['Target']

# 2. "切蛋糕" (黄金分割)
# shuffle=False: 这一点极其重要！
# 因为是股票时间序列，我们必须"按时间切"。不能把12月的数据切到训练集里去。
# 前面 75% 给 train (训练)，后面 25% 给 test (测试)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=False)

# 3. 只用 "过去" 的数据训练
print("AI 正在闭关修炼 (只看前9个月的数据)...")
print("正在组建由 100 棵树组成的森林...")
model = RandomForestClassifier(n_estimators=100, random_state=0)
model.fit(X_train, y_train)

# 4. 用 "未来" 的数据考试
# AI 没见过 X_test 里的数据，它必须靠"猜"
real_score = model.score(X_test, y_test)

print(f"原本作弊的分数：99.58%")
print(f"真实的实战分数：{real_score * 100:.2f}%")

# 看看测试集里，到底有多少天是涨的 (1)，多少天是跌的 (0)
counts = y_test.value_counts()
print("测试集（最后3个月）的真实情况：")
print(counts)

# 算出"无脑猜涨"的胜率
# 假设总共有 N 天，其中 M 天是涨的。胜率就是 M/N。
guess_up_score = counts[1] / (counts[0] + counts[1])
print(f"如果我每天闭眼猜'涨'，准确率是：{guess_up_score * 100:.2f}%")
