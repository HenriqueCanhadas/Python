import customtkinter

janela=customtkinter.CTk()
janela.geometry("700x400")
janela.title("TESTE")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

btn= customtkinter.CTkButton(janela, text="ola")
btn.pack()

tabview = customtkinter.CTkTabview(janela,  width=400)
tabview.pack()

tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Endereço")

tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idades").grid_columnconfigure(0, weight=1)
tabview.tab("Endereço").grid_columnconfigure(0, weight=1)

text = customtkinter.CTkLabel(tabview.tab("Nomes"),text="Henrique Canhadas")




janela.mainloop()