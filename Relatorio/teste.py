for i in range(1, 6):
    print(i)
    print(i)

import pandas as pd  # Certifique-se de que a biblioteca pandas esteja importada

n = 5

while n != 0:
    arquivo_excel = f'Relatorio\\REVISÃO - Boletim de Amostragem 7918.xlsx'
    try:
        tabela = pd.read_excel(arquivo_excel, sheet_name=(n))
        print(tabela)
    except FileNotFoundError:
        print(f"Arquivo {arquivo_excel} não encontrado.")
    
    n -= 1  

    import pandas as pd

n = 11

while n != 0:
    tabela_excel = f'Relatorio\\REVISÃO - Boletim de Amostragem 7918.xlsx'

    try:
        tabela = pd.read_excel(tabela_excel, sheet_name=(n))
        print(tabela)

        multiparametro = tabela.iat[12, 8]  # I14 OK
        turbidimetro = tabela.iat[16, 8]    # I18 OK
        identificacao = tabela.iat[28, 2]   # C30 OK
        data = tabela.iat[4, 2]            # C6 OK
        horaensaio = tabela.iat[28, 7]     # H30
        horaamostragem = tabela.iat[28, 10] # K30
        condutividade = tabela.iat[39, 4]   # E41
        oxirreducao = tabela.iat[39, 6]    # G41
        oxigenio = tabela.iat[39, 8]       # I41
        ph = tabela.iat[39, 11]            # L41
        temperatura = tabela.iat[39, 13]    # N41
        turbidez = tabela.iat[39, 15]       # P41
        condicoes = tabela.iat[28, 15]      # P30

        print('-' * 75)
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

        # Abrir o arquivo de resultados fora do loop
        arquivo_resultados = 'Relatorio\Resultados.xlsx'
        tabela_resultados = pd.read_excel(arquivo_resultados)

        # Atualizar as células correspondentes no arquivo de resultados
        tabela_resultados.at[n, 'Multiparâmetro - Patrimônio Nº SRV-ITR-0001'] = multiparametro
        tabela_resultados.at[n, 'Turbidimetro - Patrimônio Nº SRV-ITR-0007'] = turbidimetro
        tabela_resultados.at[n, 'Identificação da amostra:'] = identificacao
        tabela_resultados.at[n, 'Hora do ensaio:'] = horaensaio
        tabela_resultados.at[n, 'Hora da amostragem:'] = horaamostragem
        tabela_resultados.at[n, 'Condutividade'] = condutividade
        tabela_resultados.at[n, 'Potencial de oxirredução'] = oxirreducao
        tabela_resultados.at[n, 'Oxigênio Dissolvido'] = oxigenio
        tabela_resultados.at[n, 'pH'] = ph
        tabela_resultados.at[n, 'Temperatura'] = temperatura
        tabela_resultados.at[n, 'Turbidez'] = turbidez
        tabela_resultados.at[n, 'Condições ambientais: 0 Sem chuva; 1 Leve; '] = condicoes

        # Salvar as alterações no arquivo de resultados
        tabela_resultados.to_excel(arquivo_resultados, index=False)

        n -= 1

    except FileNotFoundError:
        print(f"Arquivo {tabela_excel} não encontrado.")




