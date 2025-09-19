import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score

trainData = (pd.read_csv("./fraudTrain.csv")).drop(["Unnamed: 0"], axis=1)
transDateTimeSpit = trainData["trans_date_trans_time"].str.split(expand=True)

transDate = transDateTimeSpit.iloc[:,0]
transTime = transDateTimeSpit.iloc[:,1]
print(transDate)
print(transTime)






