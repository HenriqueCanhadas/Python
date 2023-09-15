import pandas as pd

df = pd.read_excel('Tabelas\Teste.xlsx')

#valor_celula = df.at[1, "A"]
valor_celula1 = df.iat[0, 0]

print(df)

#print(valor_celula)

print(valor_celula1)

