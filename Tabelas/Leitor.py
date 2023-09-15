import pandas as pd

print('-'*75)

#Leitura de Tabela Padrão

tabela = pd.read_excel("Tabelas\Arquivo.xlsx")

print(tabela)

print('-'*75)

#Leitura de Tabela por Nome

tabela = pd.read_excel("Tabelas\Arquivo.xlsx", sheet_name='Produtos')

print(tabela)

print('-'*75)

#Leitura de Tabela por Índice

tabela = pd.read_excel("Tabelas\Arquivo.xlsx", sheet_name=1) 

print(tabela)

print('-'*75)

#Seleção de Colunas, pelo Índice

tabela = pd.read_excel("Tabelas\Arquivo.xlsx", sheet_name='Inventario', usecols="A,I")

print(tabela)

print('-'*75)

#Buscando todas as informações

tabela = pd.read_excel("Tabelas\Arquivo.xlsx", sheet_name=None)

print(tabela)

print('-'*75)

#Buscando informações diretas

tabela = pd.read_excel("Tabelas\Arquivo.xlsx", sheet_name="Inventario", usecols="I,J", skiprows=10)

print(tabela)

print('-'*75)

#Celula Especifica

valor_celula1 = tabela.iat[1, 1]

print(valor_celula1)