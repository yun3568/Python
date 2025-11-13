import akshare as ak
import pandas as pd

print("正在启动...准备从互联网抓取数据...")

df=ak.stock_zh_a_hist(symbol="000001",period="daily",start_date="20230101",end_date="20231231",adjust='qfq')

subset = df[['日期','收盘','涨跌幅']]
subset.to_csv('real_stock.csv',index=False)

print("任务完成")
print("前五行数据如下：")
print(subset.head())
