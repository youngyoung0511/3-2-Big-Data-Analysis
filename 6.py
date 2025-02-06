import pandas as pd, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('subway_2.csv', encoding='cp949')
data['노선명'] = data['노선명'].map({"1호선": "Line_1", "2호선": "Line_2", "3호선": "Line_3", "4호선": "Line_4"})
data.rename(columns={'승차총승객수': 'Boarding', '하차총승객수': 'Alighting'}, inplace=True)

mean_values = data.groupby('노선명')[['Boarding', 'Alighting']].mean()
mean_values.plot(kind='bar', figsize=(8, 6), title='Mean Boarding and Alighting by Line')
plt.xlabel('Line'), plt.ylabel('Average Count'), plt.show()

X, y = data[['Boarding', 'Alighting']], data['노선명']
X_train, X_test, y_train, y_test = train_test_split(StandardScaler().fit_transform(X), y, test_size=0.2)

models = {"KNN": KNeighborsClassifier(3), "Logistic Regression": LogisticRegression(max_iter=1000), "Decision Tree": DecisionTreeClassifier()}
accuracies = {name: accuracy_score(y_test, model.fit(X_train, y_train).predict(X_test)) for name, model in models.items()}

best_model_name = max(accuracies, key=accuracies.get)
print("\n".join([f" - {name}: {acc:.2f}" for name, acc in accuracies.items()]))
print(f"\nThe best model is: {best_model_name}")

input_scaled = StandardScaler().fit(X).transform([[30000, 30000]])
print(f"Prediction for input (30000, 30000): {models[best_model_name].predict(input_scaled)[0]}")
