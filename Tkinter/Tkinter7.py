import customtkinter
from tkinter import *

janela=customtkinter.CTk()
janela.geometry("400x400")
janela.title("TESTE")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def evento():
    print("Clicou")
    pass

def inserirnome():

    nova_janela = customtkinter.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("250x250")
    nova_janela.title("Nomes")
    entry = customtkinter.CTkEntry(nova_janela,width=200,placeholder_text="Digite o nome")
    entry.pack(pady=20)

    def pegar():
     global texto
     texto = (entry.get())
     entry.delete(0,END)
     print(texto)
     pass

    def apagar():
        entry.delete(0,END)
        pass

    customtkinter.CTkButton(nova_janela, text="Att Nome",command=pegar).pack(pady=20)
    customtkinter.CTkButton(nova_janela, text="Remover Nome",command=apagar).pack(pady=10)
    
    pass

def botao():
    nova_janela = customtkinter.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("250x250")
    nova_janela.title("Botão")

    customtkinter.CTkButton(nova_janela,
                            text="Youtube",
                            width=300,
                            height=20,
                            fg_color="transparent",
                            hover_color="red",
                            font=("Arial bold", 20),
                            border_color="white",
                            border_width=3,
                            border_spacing=5,
                            corner_radius=20,
                            state="normal"
                            ).pack(pady=30)
   
    pass
   

customtkinter.CTkButton(janela, text="Clique Aqui", command=evento).pack(pady=20)
customtkinter.CTkButton(janela, text="Inserir Nome", command=inserirnome).pack(pady=20)
customtkinter.CTkButton(janela, text="Botão", command=botao).pack(pady=20)

janela.mainloop()