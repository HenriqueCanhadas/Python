import pandas
import openpyxl
import xlwings

workbook = openpyxl.load_workbook('TestePivot/Export_Toyota_SBC_Geral.xlsx')

sheet = workbook['Amostras Resultados (2)']



def case_1():
    '''
    def printLinhaLaboratorio(linha):
        for linha in sheet.iter_rows(min_row=linha, max_row=linha):
            for cell in linha:
                print(cell.column,cell.value, end=', ')
            print()
 
    contador = 0


    for row in sheet.iter_rows(min_col=5, max_col=5, max_row=sheet.max_row):

        for cell in row:
            if cell.value is not None and "<" not in str(cell.value):
                linha = cell.row
                printLinhaLaboratorio(linha)
                contador += 1

    print("Total:",contador)
    '''


    #print("A célula atual é igual à próxima célula")

def case_2(row):
    def case_2_inner():
        #print("Celula anterior:", cell1)
        #print (sheet.cell(row=row, column=1))

        global id
        global tipo
        global data


        id.append(sheet.cell(row=row, column=1).value)
        tipo.append(sheet.cell(row=row, column=2).value)
        data.append(sheet.cell(row=row, column=3).value)
        
        #print("A célula atual é diferente da próxima célula")
        
        #print (sheet.cell(row=row +1, column=1))
        #print("Celula seguinte:", cell2)
        #print (sheet.cell(row=row+1, column=1))

        #!!!! Ele esta pegando o ultimo e nao atualizando o penultimo
    
    
    return case_2_inner  # Retorna a função interna sem argumentos

def default_case():
    print("Caso padrão")

id=[]
tipo=[]
data=[]

column_number = 1  # Número da coluna desejada (1 para A, 2 para B, etc.)
row = 1

for row in range(1, sheet.max_row):
    cell1 = sheet.cell(row=row, column=1).value
    cell2 = sheet.cell(row=row + 1, column=1).value

    print(cell2)

    if cell1 is not None and cell2 is not None:
        switch = {
            cell1 == cell2: case_1,
            cell1 != cell2: case_2(row)
        }
        switch.get(True, default_case)()



print("\n",id)
print("\n",tipo)
print("\n",data)



'''
for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column):
             for cell in row:
                print(print(cell.value, end=' '))
'''



cell = sheet['A1'].value

print("\n",cell)

print(f'Valores lidos em {sheet}:')

