from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

X_train = [
    [1,0], #一等舱，女
    [3,1],
    [1,1]
]

y_train = [
    1,#乘客1：活
    0,
    0
]

model = DecisionTreeClassifier(random_state=0)

model.fit(X_train,y_train)

X_new = [[3,0]]

prediction = model.predict(X_new)

if prediction[0] == 1:
    print("预测：生还")
else:
    print("预测：死亡")
