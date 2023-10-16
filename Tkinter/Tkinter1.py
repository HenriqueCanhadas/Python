import customtkinter

janela=customtkinter.CTk()
janela.geometry("700x400")
janela.title("TESTE")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


customtkinter.CTkLabel(janela, text="Labels", font=("arial bold", 20)).pack(pady=20, padx=5)

customtkinter.CTkLabel(janela,text="Este texto e de um label estatico").pack()

text_var = customtkinter.StringVar(value="TESTE")

lab1 = customtkinter.CTkLabel(janela, textvariable=text_var, width=200, height=25, fg_color="blue").pack(pady=10)

text_var1 = customtkinter.StringVar(value=input("Digite Seu Nome"))

lab2 = customtkinter.CTkLabel(janela, textvariable=text_var1, width=200, height=25, fg_color="red").pack(pady=10)

janela.mainloop()