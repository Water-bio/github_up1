import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from pathlib import Path
import streamlit as st
script_dir=Path(__file__).parent.parent
file=pd.read_excel(script_dir/"数据"/"day10_模拟实验数据.xlsx")
file_encoded=pd.get_dummies(file,columns=["载体类型"],dtype=int,prefix='',prefix_sep='')
feature_cols=['实验天数(d)','温度(℃)',"新型复合载体(A)","未改性纤维载体(B)","纯PVA-SA凝胶球(C)"]
x=file_encoded[feature_cols]
y=file_encoded["COD去除率(%)"]
model=RandomForestRegressor()
model.fit(x,y)
st.sidebar.header("实验条件")
temp=st.sidebar.slider("温度(℃)", 5,17,10)
day=st.sidebar.slider("实验天数(d)",1,14,7)
carriers=["新型复合载体(A)","未改性纤维载体(B)","纯PVA-SA凝胶球(C)"]
carrier=st.sidebar.selectbox("载体类型",carriers)

carrier_col={c:0 for c in ["新型复合载体(A)","未改性纤维载体(B)","纯PVA-SA凝胶球(C)"]}
carrier_col[f'{carrier}']=1
input_=pd.DataFrame([{'实验天数(d)':day,'温度(℃)':temp,**carrier_col}])
pred=model.predict(input_)[0]
st.subheader(f"预测COD去除率：{pred:.1f}%")
st.subheader("特征重要性")
importance = model.feature_importances_
imp=pd.DataFrame({'特征':x.columns,'重要性':importance})
imp=imp.sort_values('重要性',ascending=False)
st.bar_chart(imp.set_index('特征'))