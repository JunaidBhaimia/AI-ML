import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("predictive_maintenance.csv")

df.columns = df.columns.str.strip().str.lower()

print("Columns:", df.columns)

X = df[['air temperature [k]', 
        'process temperature [k]', 
        'rotational speed [rpm]', 
        'torque [nm]', 
        'tool wear [min]']]

y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))
