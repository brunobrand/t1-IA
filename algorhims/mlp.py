import pandas as pd
from sklearn.neural_network import MLPClassifier
from utils import divide_datasets, calculate_metrics

def execute_mlp(X_train, y_train, X_val, y_val):
    mlp = MLPClassifier(hidden_layer_sizes=(50, 30), max_iter=500, random_state=42)
    mlp.fit(X_train, y_train)
    y_val_pred = mlp.predict(X_val)
    
    accuracy, precision, recall, f1 = calculate_metrics(y_val, y_val_pred)
    return accuracy, precision, recall, f1

df = pd.read_csv('dataset_balanceado.csv')

X = df.drop(columns=['class'])
y = df['class']

X_train, X_val, X_test, y_train, y_val, y_test = divide_datasets(X, y)

accuracy, precision, recall, f1 = execute_mlp(X_train, y_train, X_val, y_val)
print(f"Resultados do MLP (validação):\nAcurácia: {accuracy}\nPrecisão: {precision}\nRecall: {recall}\nF1-Score: {f1}")

mlp = MLPClassifier(hidden_layer_sizes=(50, 30), max_iter=500, random_state=42)
mlp.fit(X_train, y_train)
y_test_pred = mlp.predict(X_test)
accuracy_test, precision_test, recall_test, f1_test = calculate_metrics(y_test, y_test_pred)
print(f"Resultados do MLP (teste):\nAcurácia: {accuracy_test}\nPrecisão: {precision_test}\nRecall: {recall_test}\nF1-Score: {f1_test}")
