import pandas as pd

# Leia o arquivo Excel e obtenha os valores das colunas A, B, C, H e I na guia "Table 2"
dados_excel = pd.read_excel('Tabela Cetesb/DD-125-2021-E-Atualizacao-dos-Valores-Orientadores-paa-solo-e-aguas-subterraneas.xlsx', sheet_name='Table 2', header=None, dtype=str)

# Lista de nomes que indicam o início da leitura
nomes_inicio_leitura = [
    "INORGÂNICOS",
    "HIDROCARBONETOS AROMÁTICOS VOLÁTEIS",
    "HIDROCARBONETOS POLICÍCLICOS AROMÁTICOS",
    "BENZENOS CLORADOS",
    "ETANOS CLORADOS",
    "ETENOS CLORADOS",
    "METANOS CLORADOS",
    "FENÓIS CLORADOS",
    "FENÓIS NÃO CLORADOS",
    "ÉSTERES FTÁLICOS",
    "PESTICIDAS",
    "OUTROS",
    "VRQ – Valor de Referência de Qualidade; VP – Valor de Prevenção; VI – Valor de Intervenção",
]

# Inicializar listas para armazenar os valores das colunas A, B, C, H e I
valores_coluna_a = []
valores_coluna_b = []
valores_coluna_c = []
valores_coluna_agricola = []  # Lista única para valores da coluna H e, se necessário, da coluna I
valores_coluna_residencial = []  # Lista única para valores da coluna J e, se necessário, da coluna K
valores_coluna_industrial = []  # Lista única para valores da coluna L e, se necessário, da coluna M
valores_coluna_agua = []  # Lista única para valores da coluna L e, se necessário, da coluna M

# Variável para indicar se a leitura deve começar
comecar_leitura = False

# Variável para indicar se a leitura deve terminar
terminar_leitura = 'VRQ – Valor de Referência de Qualidade; VP – Valor de Prevenção; VI – Valor de Intervenção\n(1) Mantidos os valores orientadores da Resolução CONAMA 420/2009.\n(2) Mantidos os valores de prevenção da Resolução CONAMA 420/2009.\n(3) Substâncias que não constam da planilha CETESB (versão maio de 2013).\n(4) Mantidos os valores de intervenção da Resolução CONAMA 420/2009.\n(5) Somatória  dos  congêneres  28,  52,  101,  118,138,153,180  para  investigação  confirmatória;  na  investigação detalhada a lista de congêneres deve ser ampliada.\n(6) Valores derivados com as propriedades do óxido de tributil (CAS nº 56-35-9).\n(7) Somatória de toxicidade equivalente (TEQ) calculada a partir dos fatores de equivalência de toxicidade (TEFs  - WHO 2005) para cada congênere de dioxinas e furanos (VAN DEN BERG, 2006).\n(a) Adotado valor limite de 1% do peso seco do solo (10.000 mg kg-1).\n(b) Somatória dos isômeros ou metabólitos.\n(c)  Somatória de endossulfan e sais.'

# Iterar sobre os valores das colunas A, B, C, H, I, J e K
for valor_a, valor_b, valor_c, valor_h, valor_i, valor_j, valor_k, valor_l, valor_m, valor_n, valor_o, valor_p in zip(
    dados_excel.iloc[:, 0],
    dados_excel.iloc[:, 1],
    dados_excel.iloc[:, 2],
    dados_excel.iloc[:, 7],
    dados_excel.iloc[:, 8],
    dados_excel.iloc[:, 9],
    dados_excel.iloc[:, 10],
    dados_excel.iloc[:, 11],
    dados_excel.iloc[:, 12],
    dados_excel.iloc[:, 13],
    dados_excel.iloc[:, 14],
    dados_excel.iloc[:, 15],
):
    # Se o valor for igual a terminar_leitura, interrompa o loop
    if comecar_leitura and valor_a == terminar_leitura:
        break
    # Se o valor estiver na lista, comece a leitura
    if valor_a in nomes_inicio_leitura:
        comecar_leitura = True
    # Se a leitura já começou e o valor não está no final da lista e não é igual a nenhum item em nomes_inicio_leitura, adicione os valores às listas
    if comecar_leitura and valor_a != nomes_inicio_leitura[-1] and valor_a not in nomes_inicio_leitura:
        valores_coluna_a.append(valor_a)
        # Use o valor da coluna B se não for nulo; caso contrário, use o valor da coluna C
        valores_coluna_b.append(valor_b if pd.notna(valor_b) else valor_c)
        # Use o valor da coluna H se não for nulo; caso contrário, use o valor da coluna I
        valor_agricola = valor_h if pd.notna(valor_h) else valor_i
        valores_coluna_agricola.append(valor_agricola)
        # Use o valor da coluna J se não for nulo; caso contrário, use o valor da coluna K
        valor_residencial = valor_j if pd.notna(valor_j) else valor_k
        valores_coluna_residencial.append(valor_residencial)
        # Use o valor da coluna L se não for nulo; caso contrário, use o valor da coluna M
        valor_industrial = valor_l if pd.notna(valor_l) else valor_m
        valores_coluna_industrial.append(valor_industrial)
        # Use o valor da coluna J se não for nulo; caso contrário, use o valor da coluna K
        valor_agua = valor_o if pd.notna(valor_o) else (valor_p if pd.notna(valor_p) else valor_n)
        valores_coluna_agua.append(valor_agua)

print(valores_coluna_agua)

quantidade = len(valores_coluna_agua)

print(quantidade)

# Crie um novo DataFrame com os valores das colunas A, B, C e I
novo_dataframe = pd.DataFrame({"Analyte": valores_coluna_a,"CAS": valores_coluna_b,"Agrícola": valores_coluna_agricola,"Residencial": valores_coluna_residencial,"Industrial": valores_coluna_industrial,"Água": valores_coluna_agua})

# Crie um novo arquivo Excel com base no novo DataFrame
novo_dataframe.to_excel('Tabela Cetesb/Tabela_Cetesb.xlsx', index=False)
