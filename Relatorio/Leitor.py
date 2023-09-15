import pandas as pd

#Pegar Celula Especifica

tabela = pd.read_excel('Relatorio\REVISÃO - Boletim de Amostragem 7918.xlsx', sheet_name='PMN-03')
print(tabela)

multiparametro = tabela.iat[12, 8] #I14 OK

turbidimetro = tabela.iat[16, 8]#I18 OK

identificacao  = tabela.iat[28, 2]#C30 OK

data = tabela.iat[4, 2]#C6 OK

horaensaio = tabela.iat[28, 7]#H30

horaamostragem = tabela.iat[28, 10]#K30

condutividade = tabela.iat[39, 4]#E41

oxirreducao = tabela.iat[39, 6]#G41

oxigenio = tabela.iat[39, 8]#I41

ph = tabela.iat[39, 11]#L41

temperatura = tabela.iat[39, 13]#N41

turbidez = tabela.iat[39, 15]#P41

condicoes = tabela.iat[28, 15]#P30



print('-'*75)


print(multiparametro)
print(turbidimetro)
print(identificacao)
print(data)
print(horaensaio)
print(horaamostragem)
print(condutividade)
print(oxirreducao)
print(oxigenio)
print(ph)
print(temperatura)
print(turbidez)
print(condicoes)

#Escrever Resultado

tabela = pd.read_excel('Relatorio\Resultados.xlsx')


tabela.loc[0,'Multiparâmetro - Patrimônio Nº SRV-ITR-0001'] = (multiparametro)
tabela.loc[0,'Turbidimetro - Patrimônio Nº SRV-ITR-0007'] = (turbidimetro)
tabela.loc[0,'Identificação da amostra:'] = (identificacao)
tabela.loc[0,'Hora do ensaio:'] = (horaensaio)
tabela.loc[0,'Hora da amostragem:'] = (horaamostragem)
tabela.loc[0,'Condutividade'] = (condutividade)
tabela.loc[0,'Potencial de oxirredução'] = (oxirreducao)
tabela.loc[0,'Oxigênio Dissolvido'] = (oxigenio)
tabela.loc[0,'pH'] = (ph)
tabela.loc[0,'Temperatura'] = (temperatura)
tabela.loc[0,'Turbidez'] = (turbidez)
tabela.loc[0,'Condições ambientais: 0 Sem chuva; 1 Leve; '] = (condicoes)

tabela.to_excel('Relatorio\Resultados.xlsx', index=False)


