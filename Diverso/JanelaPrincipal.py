import customtkinter
from PIL import Image


def executar_mark4():
    import Mark4  # Importe o arquivo Mark4

janela=customtkinter.CTk()
janela.geometry("345x300")
janela.title("JANELA PRINCIPAL")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

img=customtkinter.CTkImage(light_image=Image.open("Tkinter/youtubelogo.png"), dark_image=Image.open("Tkinter/youtubelogo.png"), size=(50,50))

customtkinter.CTkButton(janela, text="Mark4", command=executar_mark4).pack()
janela.mainloop()
