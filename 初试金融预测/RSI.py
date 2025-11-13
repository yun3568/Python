import pandas as pd

# 1. 读取数据
df = pd.read_csv('real_stock.csv')

# 2. 计算 RSI (我帮你写好了，不需要你动脑子，只需要看着)
# 算出每天变化的钱
change = df['收盘'].diff()

# 分离涨跌
gain = change.clip(lower=0)
loss = -1 * change.clip(upper=0)

# 算出14天的平均涨幅和跌幅
avg_gain = gain.rolling(14).mean()
avg_loss = loss.rolling(14).mean()

# RSI 公式
rs = avg_gain / avg_loss
df['RSI'] = 100 - (100 / (1 + rs))

# 3. 侦查报告 (这是你要回答我的问题)
print("--- RSI 侦查报告 ---")
print(f"RSI 最大值: {df['RSI'].max()}")
print(f"RSI 最小值: {df['RSI'].min()}")

# 4. 看看前 20 行 (观察 NaN)
print("\n--- 前 20 行数据 ---")
print(df[['日期', '收盘', 'RSI']].head(20))
