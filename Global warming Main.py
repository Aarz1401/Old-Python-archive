print('Hello')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Globalwarmingdata.csv')
print(df)
a=df.values.tolist()
year=[]
anomaly=[]
for x,y in a:
    year.append(x)
    anomaly.append(y)

print(year)
print(anomaly)
listX=[]
listY=[]


def plotline(y1,y2):
    for y in range(y1, y2):
        listX.append(year[y - 1880])
        listY.append(anomaly[y - 1880])
    plt.plot(listX,listY)
    plt.show()
def plotbar(y1,y2):
    if y1>y2:
        print('Invalid input as start year is greater than end year')
    elif y1 not in range(1880,2022) or y2 not in range(1880,2022):
        print('Range specified is out of the dataset.The dataset is for the years 1880-2022.Please specify years in the given range')
    else:
        for y in range(y1, y2):
            listX.append(year[y - 1880])
            listY.append(anomaly[y - 1880])
        plt.bar(listX,listY,width=0.4)
        plt.show()

plotline(1880,2020)
plotbar(1880,2021)
