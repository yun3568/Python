import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# --- 0. 配置参数 (严禁 Hard Code) ---
MA_WINDOW = 5       # 均线窗口
RSI_WINDOW = 14     # RSI窗口
TEST_SIZE = 0.25    # 考试数据占比
TREES = 100         # 森林里的树

# --- 1. 读取 ---
df = pd.read_csv('real_stock.csv')

# --- 2. 造武器 (特征工程) ---

# 武器 A: MA5 (趋势)
df['MA5'] = df['收盘'].rolling(MA_WINDOW).mean()

# 武器 B: RSI (情绪)
change = df['收盘'].diff()
gain = change.clip(lower=0)
loss = -1 * change.clip(upper=0)
avg_gain = gain.rolling(RSI_WINDOW).mean()
avg_loss = loss.rolling(RSI_WINDOW).mean()
rs = avg_gain / avg_loss
df['RSI'] = 100 - (100 / (1 + rs))

# --- 3. 确定目标 ---
# 还是猜：明天涨(1)还是跌(0)
df['Target'] = (df['涨跌幅'].shift(-1) > 0).astype(int)

# --- 4. 清洗 (极刑) ---
df = df.dropna()

# --- 5. 准备考试 ---
# 这次我们有三个特征！
# [今天涨跌, MA5, RSI]
X = df[['涨跌幅', 'MA5', 'RSI']]
y = df['Target']

# 切分 (shuffle=False 严禁乱序)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, shuffle=False)

# --- 6. 训练 ---
print(f"正在用 {TREES} 棵树组成的森林进行训练...")
print(f"特征列表: {list(X.columns)}")

model = RandomForestClassifier(n_estimators=TREES, random_state=0)
model.fit(X_train, y_train)

# --- 7. 揭榜 ---
score = model.score(X_test, y_test)
print(f"加装了 RSI 后的真实战绩：{score * 100:.2f}%")

# 对比一下无脑猜涨
counts = y_test.value_counts()
blind_guess = counts[1] / (counts[0] + counts[1])
print(f"无脑猜涨的战绩：{blind_guess * 100:.2f}%")
