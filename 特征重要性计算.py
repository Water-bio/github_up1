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
importance=model.feature_importances_
plt.bar(x.columns, importance, color='steelblue')
plt.xlabel('特征')
plt.ylabel('重要性得分')
plt.title('特征重要性 (Random Forest)')
plt.ylim(0, max(importance) * 1.2)
for i,v in enumerate(importance):
    plt.text(i,v+0.01,f'{v:.3f}', ha='center')
plt.tight_layout()
plt.show()