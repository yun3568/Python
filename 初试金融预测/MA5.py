import akshare as ak
import pandas as pd

# 1. 读取数据
df = pd.read_csv('real_stock.csv')

# 2. 计算 "MA5" (5日均线)
# 翻译：这一天的值 = 过去5天(包括今天)收盘价的平均数
df['MA5'] = df['收盘'].rolling(5).mean()

# 3. 打印看看 (dropna() 是为了把前4天算不出来的空行删掉)
print(df[['日期', '收盘', 'MA5']].dropna().head())
