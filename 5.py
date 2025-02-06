import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

file_path = 'subway_1.csv'
data = pd.read_csv(file_path, encoding='cp949')

print("Columns in CSV:", data.columns)

X = data[['승차총승객수', '하차총승객수']]
y = data['노선명']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

input_data = pd.DataFrame([[1000, 5000], [6000, 20000]], columns=['승차총승객수', '하차총승객수'])
input_scaled = scaler.transform(input_data)
predictions = model.predict(input_scaled)

for i, pred in enumerate(predictions):
    print(f"Input {input_data.iloc[i].values} => Predicted Line: {pred}")
