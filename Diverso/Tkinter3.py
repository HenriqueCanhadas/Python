import customtkinter

janela=customtkinter.CTk()
janela.geometry("700x400")
janela.title("TESTE")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

textbox = customtkinter.CTkTextbox(janela,width=300,height=200)
textbox.pack()

textbox.insert("0.0", "Titulo do seu texto" + "Teste Teste 123 123")

def abrir():
    dialog = customtkinter.CTkInputDialog(title="Caixa de dialogo")

btn = customtkinter.CTkButton(janela, text="Caixa de Dialogo", command=abrir)
btn.pack()






janela.mainloop()