#LinearRegression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data={'Hours':[2.5,5.2,3.2,8.5,3.5,1.5,9.2,5.5,8.3,2.7,7.7,5.9,4.5,3.3,1.1,8.9,2.5,1.9,6.1,7.4,2.7,4.8,3.8,6.9,7.8],'Scores':[21,47,27,75,30,20,88,60,81,25,85,62,41,42,17,95,30,24,67,69,30,54,35,76,86]}
df=pd.DataFrame(data)
print(df.head())
X=df[['Hours']]
y=df['Scores']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Model Coefficient (slope):",model.coef_[0])
print("Model Intercept:",model.intercept_)
print("R2 Score:",r2_score(y_test,y_pred))
new_hours=pd.DataFrame([[9]],columns=['Hours'])
predicted_score=model.predict(new_hours)
print("Predicted Score for 9 hours of study:",predicted_score[0])
plt.scatter(X,y)
plt.plot(X,model.predict(X))
plt.scatter(9,predicted_score[0])
plt.xlabel("Hours Studied")
plt.ylabel("Scores")
plt.title("Linear Regression - Hours vs Scores")
plt.show()
