import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("final-project/adult.csv")
x_1 = data["Workclass"]
x_2 = data["Fnlwgt"]
x_3 = data["Education"]
x_4 = data["Education-num"]
x_5 = data["Marital-status"]
x_6 = data["Occupation"]
x_7 = data["Relationship"]
x_8 = data["Race"]
x_9 = data["Sex"]
x_10 = data["Capital-gain"]
x_11 = data["Capital-loss"]
x_12 = data["Hours-per-week"]
x_13 = data["Native-country"]
y = data["Class"]

fig, graph = plt.subplots(13)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("Workclass")
graph[0].set_ylabel("Class")

graph[1].scatter(x_2, y)
graph[1].set_xlabel("Fnlwgt")
graph[1].set_ylabel("Class")

graph[2].scatter(x_3, y)
graph[2].set_xlabel("Education")
graph[2].set_ylabel("Class")

graph[3].scatter(x_4, y)
graph[3].set_xlabel("Education-num")
graph[3].set_ylabel("Class")

graph[4].scatter(x_5, y)
graph[4].set_xlabel("Marital-status")
graph[4].set_ylabel("Class")

graph[5].scatter(x_6, y)
graph[5].set_xlabel("Occupation")
graph[5].set_ylabel("Class")

graph[6].scatter(x_7, y)
graph[6].set_xlabel("Relationship")
graph[6].set_ylabel("Class")

graph[7].scatter(x_8, y)
graph[7].set_xlabel("Race")
graph[7].set_ylabel("Class")

graph[8].scatter(x_9, y)
graph[8].set_xlabel("Sex")
graph[8].set_ylabel("Class")

graph[9].scatter(x_10, y)
graph[9].set_xlabel("Capital-gain")
graph[9].set_ylabel("Class")

graph[10].scatter(x_11, y)
graph[10].set_xlabel("Capital-loss")
graph[10].set_ylabel("Class")

graph[11].scatter(x_12, y)
graph[11].set_xlabel("Hours-per-week")
graph[11].set_ylabel("Class")

graph[12].scatter(x_13, y)
graph[12].set_xlabel("Native-country")
graph[12].set_ylabel("Class")



print("Correlation between Annual Precipitation and income class:",round(x_1.corr(y),2))
print("Correlation between Winter Severity and income class:",round(x_2.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_3.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_4.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_5.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_6.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_7.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_8.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_9.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_10.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_11.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_12.corr(y),2))
print("Correlation between Adult Population and income class:",round(x_13.corr(y),2))

plt.tight_layout()
plt.show()