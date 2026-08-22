import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

script_dir=Path(__file__).parent.parent
file=pd.read_excel(script_dir/"数据"/"day10_模拟实验数据.xlsx")
plt.rcParams['font.sans-serif'] = ['SimHei']      # 黑体
plt.rcParams['axes.unicode_minus'] = False


data_A=file[file["载体类型"]=="新型复合载体(A)"]
fig,(ax1,ax2)= plt.subplots(1,2,figsize=(12,5))

for temp in sorted(data_A["温度(℃)"].unique()):
    sub=data_A[data_A["温度(℃)"]==temp].sort_values("实验天数(d)")
    ax1.plot(sub["实验天数(d)"],sub["COD去除率(%)"],"o-",label=f"{temp}℃")
ax1.set_xlabel("实验天数(d)")
ax1.set_ylabel("COD去除率(%)")
ax1.set_title("COD去除率")
ax1.legend()
ax1.grid(True,alpha=0.3)

for temp in sorted(data_A["温度(℃)"].unique()):
    sub=data_A[data_A["温度(℃)"]==temp].sort_values("实验天数(d)")
    ax2.plot(sub["实验天数(d)"],sub["NH4-N去除率(%)"],"o-",label=f"{temp}℃")
ax2.set_xlabel("实验天数(d)")
ax2.set_ylabel("NH4-N去除率(%)")
ax2.set_title("NH4-N去除率(%)")
ax2.legend()
ax2.grid(True,alpha=0.3)

fig.suptitle("新型复合载体(A) — 去除率随天数变化", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()
    