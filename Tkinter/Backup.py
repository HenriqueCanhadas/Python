import customtkinter

janela=customtkinter.CTk()
janela.geometry("700x400")
janela.title("TESTE")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela.mainloop()