from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
data = load_diabetes()
model = RandomForestRegressor()
model.fit(data.data, data.target)
print(model.predict([data.data[0]]))