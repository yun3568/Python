import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('stock.csv')

X_train = data[['Today_Change']]
y_train = data['Tomorrow_Direction']

model = DecisionTreeClassifier(random_state=0)
model.fit(X_train,y_train)

X_new = [[4]]
prediction = model.predict(X_new)

if prediction[0] == 1:
    print("AI预测：如果今天涨 4，明天会 -> 涨")
else:
    print("AI预测：如果今天涨 4，明天会 -> 跌")
