from sklearn.ensemble import RandomForestRegressor
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']      # 黑体
plt.rcParams['axes.unicode_minus'] = False
script_dir=Path(__file__).parent.parent
file=pd.read_excel(script_dir/"数据"/"day10_模拟实验数据.xlsx")
file2=pd.read_excel(script_dir/"数据"/"day10_模拟实验数据.xlsx")
x=file[["温度(℃)","实验天数(d)"]]
y=file["COD去除率(%)"]
model=RandomForestRegressor()
model.fit(x,y)
y_pred=model.predict(x)
plt.figure(figsize=(6,6))
sns.scatterplot(x=y,y=y_pred)
plt.plot([y.min(),y.max()],[y.min(),y.max()],"r--")
plt.xlabel("真实值")
plt.ylabel("预测值")
plt.title("预测值vs真实值")
plt.show()