#comp Linear vs Decision tree
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("day.csv")

features = ['temp', 'atemp', 'hum', 'windspeed', 'season', 'workingday']
X = data[features]

y = data['cnt']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

lr_predictions = lr_model.predict(X_test)

lr_mse = mean_squared_error(y_test, lr_predictions)
lr_r2 = r2_score(y_test, lr_predictions)

dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train, y_train)

dt_predictions = dt_model.predict(X_test)

dt_mse = mean_squared_error(y_test, dt_predictions)
dt_r2 = r2_score(y_test, dt_predictions)


print("Linear Regression Results")
print("MSE:", lr_mse)
print("R2 Score:", lr_r2)

print("\nDecision Tree Results")
print("MSE:", dt_mse)
print("R2 Score:", dt_r2)


models = ['Linear Regression', 'Decision Tree']
r2_scores = [lr_r2, dt_r2]

plt.bar(models, r2_scores, color=['blue', 'green'])
plt.title("Model Comparison (R2 Score)")
plt.ylabel("R2 Score")
plt.show()
