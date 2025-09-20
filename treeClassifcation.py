import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

trainData = (pd.read_csv("./fraudTrain.csv")).drop(["Unnamed: 0"], axis=1)
testData = (pd.read_csv("./fraudTest.csv")).drop(["Unnamed: 0"], axis=1)

xTrain = trainData[["unix_time", "amt", "city_pop", "lat", "long","merch_lat", "merch_long",]]
yTrain = trainData[["is_fraud"]]
xTest = testData[["unix_time", "amt", "city_pop", "lat", "long","merch_lat", "merch_long",]]
yTest = testData[["is_fraud"]]

clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=4, class_weight="balanced")
clf.fit(xTrain,yTrain)
yPred = clf.predict(xTest)


print(f"accuracy score is: {accuracy_score(yTest,yPred)}")

print(classification_report(yTest, yPred, digits=4))