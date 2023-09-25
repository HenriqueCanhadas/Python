import tkinter as tk
from tkinter import filedialog
import xlwings as xw
import openpyxl
import pandas as pd
from tkinter import font

file_path = ""

def carregar_excel():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx *.xls")])
    if file_path:
        global dataframe
        dataframe = pd.read_excel(file_path)
        status_label.config(text="Arquivo Excel Carregado.")

def rodar_programa():
    global file_path 
    global valores_xlwings
    global valores_workbook_openpyxl
    global workbook_openpyxl

    if file_path == "":
        status_label.config(text="Nenhum Excel Carregado!")
        return

    wb_xlwings = xw.Book(file_path)

    status_label.config(text="Rodando o Programa")
    root.update() 

    valores_xlwings = []
    valores_workbook_openpyxl = []

    for sheet_name in wb_xlwings.sheets:

        planilha = wb_xlwings.sheets[sheet_name]

        planilha.activate()

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

    workbook_openpyxl = openpyxl.load_workbook(file_path)

    for sheet_name in workbook_openpyxl.sheetnames:
        planilha_openpyxl = workbook_openpyxl[sheet_name]

        identificacao = planilha_openpyxl['C30'].value
        data = planilha_openpyxl['C6'].value
        horaensaio = planilha_openpyxl['H30'].value
        horaamostragem = planilha_openpyxl['K30'].value
        condicoes = planilha_openpyxl['P30'].value

        valores_workbook_openpyxl.append((identificacao, data, horaensaio, horaamostragem, condicoes))


        print(f'Identificação/Aba/Guia: {identificacao}')
        print(f'Data: {data}')
        print(f'Hora do ensaio: {horaensaio}')
        print(f'Hora da amostragem: {horaamostragem}')
        print(f'Condições ambientais: {condicoes}')

        print("-" * 100)

    status_label.config(text="Todos os dados foram Armazenados")

    print('Todos os dados foram Armazenados')

    print("-" * 100)

def salvar_excel():
    global valores_xlwings
    global valores_workbook_openpyxl
    global workbook_openpyxl
    global file_path
    global status_label

    if file_path == "":
        status_label.config(text="Nenhum Excel Carregado!")
        return
    
    if file_path:
        status_label.config(text="Preparando para salvar o arquivo.")

        print(f"Abrindo o arquivo Excel existente em: {file_path}")
        workbook_openpyxl = openpyxl.load_workbook(file_path)

        sheet = workbook_openpyxl['FINAL']

        linha = 69

        while len(valores_xlwings) > 0 and len(valores_workbook_openpyxl) > 0:
            if len(valores_xlwings) > 0:
                condutividade, oxirreducao, oxigenio, ph, temperatura, turbidez = valores_xlwings.pop(0)

                sheet[f'E{linha}'] = condutividade
                sheet[f'F{linha}'] = oxirreducao
                sheet[f'G{linha}'] = oxigenio
                sheet[f'H{linha}'] = ph
                sheet[f'I{linha}'] = temperatura
                sheet[f'J{linha}'] = turbidez
            
            if len(valores_workbook_openpyxl) > 0:
                identificacao, data, horaensaio, horaamostragem, condicoes = valores_workbook_openpyxl.pop(0)

                sheet[f'A{linha}'] = identificacao
                sheet[f'B{linha}'] = data
                sheet[f'C{linha}'] = horaensaio
                sheet[f'D{linha}'] = horaamostragem
                sheet[f'K{linha}'] = condicoes
            
            linha += 1

    save_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*.xlsx *.xls")])
    if save_path:
        workbook_openpyxl.save(save_path)
        status_label.config(text="Excel salvo com sucesso!")

        print("-" * 100)
        print("Processo concluído com sucesso.")

root = tk.Tk()
root.title("SERVMAR")

root.minsize(250, 250)

root.configure(bg="lightblue")
fonte_negrito = font.Font(family="Helvetica", size=10, weight="bold")

load_button = tk.Button(root, text="Carregar Excel", command=carregar_excel, bg="white", font=fonte_negrito)
load_button.pack(pady=20)

load_button = tk.Button(root, text="Rodar Programa", command=rodar_programa, bg="white", font=fonte_negrito)
load_button.pack(pady=20)

save_button = tk.Button(root, text="Salvar Excel", command=salvar_excel, bg="white", font=fonte_negrito)
save_button.pack(pady=20)

status_label = tk.Label(root, text="", background="lightblue", font=fonte_negrito)
status_label.pack()

root.mainloop()