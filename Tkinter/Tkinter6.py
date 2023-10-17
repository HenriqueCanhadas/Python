import customtkinter
from tkinter import *

janela=customtkinter.CTk()
janela.geometry("700x400")
janela.title("TESTE")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

texto = "teste"

label = customtkinter.CTkLabel(janela, text="CTkLabel", fg_color="transparent")
label.configure(text="new text")
label.pack()

entry = customtkinter.CTkEntry(janela, width=300, placeholder_text="Digite Algo", placeholder_text_color="red")
entry.pack(pady=15)



def pegar():
    global texto
    texto = (entry.get())
    entry.delete(0,END)
    print(texto)
    pass

def apagar():
    entry.delete(0,END)
    pass

btn = customtkinter.CTkButton(janela,text="Imprimir", width=300, command=pegar)
btn.pack(pady=10)

btn = customtkinter.CTkButton(janela,
                              text="Apagar", 
                              fg_color="transparent",
                              width=300, 
                              command=apagar
                             )
btn.pack(pady=5)

print(texto)

janela.mainloop()