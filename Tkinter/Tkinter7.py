import customtkinter

janela=customtkinter.CTk()
janela.geometry("300x300")
janela.title("TESTE")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def evento():
    print("Clicou")
    pass

def nova_tela():
    nova_janela = customtkinter.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("200x200")
    pass

customtkinter.CTkButton(janela, text="Clique Aqui", command=evento).pack(pady=20)
customtkinter.CTkButton(janela, text="Clique Aqui", command=nova_tela).pack(pady=20)



janela.mainloop()