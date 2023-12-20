import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("final-project/adult.csv")
x_1 = data["workclass"]
x_2 = data["fnlwgt"]
x_3 = data["education"]
x_4 = data["education-num"]
x_5 = data["marital-status"]
x_6 = data["occupation"]
x_7 = data["relationship"]
x_8 = data["race"]
x_9 = data["sex"]
x_10 = data["capital-gain"]
x_11 = data["capital-loss"]
x_12 = data["hours-per-week"]
x_13 = data["native-country"]
y = data["class"]

fig, graph = plt.subplots(13)
graph[0].scatter(x_1, y)
graph[0].set_xlabel("workclass")
graph[0].set_ylabel("class")

graph[1].scatter(x_2, y)
graph[1].set_xlabel("fnlwgt")
graph[1].set_ylabel("class")

graph[2].scatter(x_3, y)
graph[2].set_xlabel("education")
graph[2].set_ylabel("class")

graph[3].scatter(x_4, y)
graph[3].set_xlabel("education-num")
graph[3].set_ylabel("class")

graph[4].scatter(x_5, y)
graph[4].set_xlabel("marital-status")
graph[4].set_ylabel("class")

graph[5].scatter(x_6, y)
graph[5].set_xlabel("occupation")
graph[5].set_ylabel("class")

graph[6].scatter(x_7, y)
graph[6].set_xlabel("relationship")
graph[6].set_ylabel("class")

graph[7].scatter(x_8, y)
graph[7].set_xlabel("race")
graph[7].set_ylabel("class")

graph[8].scatter(x_9, y)
graph[8].set_xlabel("sex")
graph[8].set_ylabel("class")

graph[9].scatter(x_10, y)
graph[9].set_xlabel("capital-gain")
graph[9].set_ylabel("class")

graph[10].scatter(x_11, y)
graph[10].set_xlabel("capital-loss")
graph[10].set_ylabel("class")

graph[11].scatter(x_12, y)
graph[11].set_xlabel("hours-per-week")
graph[11].set_ylabel("class")

graph[12].scatter(x_13, y)
graph[12].set_xlabel("native-country")
graph[12].set_ylabel("class")



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