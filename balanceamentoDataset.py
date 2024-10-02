import pandas as pd

columns = ['top-left', 'top-middle', 'top-right', 'middle-left', 'middle-middle', 'middle-right', 
           'bottom-left', 'bottom-middle', 'bottom-right', 'class']

df = pd.read_csv('tic-tac-toe.data', header=None, names=columns)

print("distribuicao original:")
print(df['class'].value_counts())

dfPositive = df[df['class'] == 'positive'].sample(332)
dfNegative = df[df['class'] == 'negative']

dfBalanceado = pd.concat([dfPositive, dfNegative]).sample(frac=1).reset_index(drop=True)

print("distribuicao balanceada:")
print(dfBalanceado['class'].value_counts())

dfBalanceado.to_csv('dataset_balanceado.csv', index=False)
