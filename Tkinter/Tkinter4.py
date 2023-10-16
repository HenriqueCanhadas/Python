import customtkinter

janela=customtkinter.CTk()
janela.geometry("700x400")
janela.title("TESTE")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

customtkinter.CTkLabel(janela, text="Menu de Opções").pack()

customtkinter.CTkLabel(janela, text="Menu de Opções", font=("arial bold", 20)).pack(pady=20, padx=5)

customtkinter.CTkLabel(janela, text="Escolha seu mes:", font=("arial bold",15)).pack()

mes_var = customtkinter.StringVar(value="Escolha o mes")

meses=["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]

def mesfuncao(escolha):
    print(f"O seu mes foi:{escolha}")



mes = customtkinter.CTkOptionMenu(janela, values=meses, command=mesfuncao, variable=mes_var, width=250, height=50)

mes.pack(pady=10)

#mes.set("Escolha do mes")

janela.mainloop()