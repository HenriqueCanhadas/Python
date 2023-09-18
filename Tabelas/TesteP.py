import pandas as pd

#Pegar Celula Especifica

df = pd.read_excel('Tabelas\Teste.xlsx')

valor_celula = df.at[0, 'Nome']
valor_celula1 = df.iat[7, 1]

print(df)

print(valor_celula)

print(valor_celula1)

#Pegar Celula de Outra Guia

n=1

dp = pd.read_excel('Tabelas\Teste.xlsx', sheet_name=(n))

print(dp)


valor_celula2 = dp.at[4, 'Produto']
valor_celula3 = dp.iat[3, 1]

print(valor_celula2)
print(valor_celula3)

#Escrever Dados e Inseri-los em uma nova planilha

tabela = pd.read_excel('Tabelas\Escrita.xlsx')


tabela.loc[0,'Nomes'] = (valor_celula3)

tabela.loc[0,'Idades'] = (valor_celula2)

tabela.loc[1,'Nomes'] = (valor_celula1)

tabela.loc[1,'Idades'] = (valor_celula)


tabela.to_excel('Tabelas\Escrita.xlsx', index=False)

print(tabela)





