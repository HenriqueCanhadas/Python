import customtkinter

janela=customtkinter.CTk()
janela.geometry("700x400")
janela.title("TESTE")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

btn= customtkinter.CTkButton(janela, text="ola")
btn.pack()

frame1 = customtkinter.CTkFrame(master= janela, width=200, height=330, fg_color="red", bg_color="green", border_width=10, corner_radius=30).place(x=20, y=60)
frame2 = customtkinter.CTkFrame(janela, width=200, height=330, fg_color="green").place(x=240, y=60)
frame2 = customtkinter.CTkFrame(janela, width=200, height=330, fg_color="blue").place(x=460, y=60)


janela.mainloop()