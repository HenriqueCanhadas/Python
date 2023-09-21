import tkinter as tk
from tkinter import filedialog
import xlwings as xw
import openpyxl
import pandas as pd

# Variável global para armazenar o caminho do arquivo Excel
file_path = ""

# Função para carregar o arquivo Excel
def carregar_excel():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx *.xls")])
    if file_path:
        global dataframe
        dataframe = pd.read_excel(file_path)
        status_label.config(text="Arquivo Excel carregado com sucesso!")

# Função para rodar o programa
def rodar_programa():
    

    global file_path  # Acessa a variável global file_path

    wb_xlwings = xw.Book(file_path)
    valores_xlwings = []

    #linha=69
    # Uma lista de números
    numeros = [1, 2, 3, 4, 5]

# Loop for para iterar sobre os números e imprimir cada um
    for numero in numeros:
        print(numero)

    for sheet_name in wb_xlwings.sheets:

        planilha = wb_xlwings.sheets[sheet_name]

        condutividade = planilha.range('E41').value
        oxirreducao = planilha.range('G41').value
        oxigenio = planilha.range('I41').value
        ph = planilha.range('L41').value
        temperatura = planilha.range('N41').value
        turbidez = planilha.range('P41').value

        valores_xlwings.append((condutividade, oxirreducao, oxigenio, ph, temperatura, turbidez))

        print(f'Valores lidos em {sheet_name}:')
        print(f'Condutividade: {condutividade}')
        print(f'Potencial de oxirredução: {oxirreducao}')
        print(f'Oxigênio Dissolvido: {oxigenio}')
        print(f'pH: {ph}')
        print(f'Temperatura: {temperatura}')
        print(f'Turbidez: {turbidez}')
        print("-" * 100)
    
    wb_xlwings.close()

    if file_path:
        # Agora você pode usar a variável file_path aqui na função rodar_programa
        print(f'Caminho do arquivo Excel: {file_path}')
        # Resto do seu código da função rodar_programa 

# Função para salvar o arquivo Excel no local de origem
def salvar_excel():
    if 'dataframe' in globals():
        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*.xlsx *.xls")])
        if save_path:
            dataframe.to_excel(save_path, index=False)
            status_label.config(text="Arquivo Excel salvo com sucesso!")

# Resto do seu código permanece o mesmo

# Criação da janela principal
root = tk.Tk()
root.title("Manipulação de Arquivo Excel")

# Definir tamanho mínimo para a janela (width x height)
root.minsize(250, 250)  # Ajuste os valores de largura e altura conforme necessário


# Botão para carregar o Excel
load_button = tk.Button(root, text="Carregar Excel", command=carregar_excel)
load_button.pack(pady=20)

# Botão para rodar o programa
load_button = tk.Button(root, text="Rodar Programa", command=rodar_programa)
load_button.pack(pady=20)

# Botão para salvar o Excel
save_button = tk.Button(root, text="Salvar Excel", command=salvar_excel)
save_button.pack(pady=20)

# Rótulo de status
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()