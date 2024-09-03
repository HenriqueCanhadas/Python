'''
def gerar_novos_nomes(qtd_arquivos):
    # Inicializa as variáveis necessárias
    data_start = datetime.now() - timedelta(days=60)  # Exemplo: começando 60 dias atrás
    contador_dias = 1

    # Lista para armazenar os períodos
    periodos = []

    # Pega o período dos últimos 60 dias e gera os nomes no intervalo de 2 em 2
    for i in range(1, qtd_arquivos + 1):
        data_inicio = data_start + timedelta(days=contador_dias - 1)
        data_final = data_start + timedelta(days=contador_dias)
        data_inicio_str = data_inicio.strftime('%d-%m-%Y') + " 00-01"
        data_final_str = data_final.strftime('%d-%m-%Y') + " 23-59"

        periodo = f"({i}) {data_inicio_str} - {data_final_str}.xlsx"
        periodos.append(periodo)

        contador_dias += 2

    return periodos

def renomear_arquivos(pasta):
    # Lista os arquivos na pasta
    arquivos = os.listdir(pasta)
    
    # Gera novos nomes
    novos_nomes = gerar_novos_nomes(len(arquivos))
    
    # Verifica se o número de arquivos corresponde ao número de novos nomes
    if len(arquivos) != len(novos_nomes):
        print("Erro: o número de arquivos na pasta e o número de novos nomes não correspondem.")
        return
    
    # Renomeia os arquivos na ordem correta
    for nome_arquivo, novo_nome in zip(arquivos, novos_nomes):
        caminho_antigo = os.path.join(pasta, nome_arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)
        
        os.rename(caminho_antigo, caminho_novo)
        print(f'{nome_arquivo} renomeado para {novo_nome}')

# Exemplo de uso
pasta = r"C:\Users\henrique.canhadas\OneDrive - Servmar Ambientais\Documentos\Codigos\GitHub\Python\Apagar Arquivos\Teste Apagar"
renomear_arquivos(pasta)
'''