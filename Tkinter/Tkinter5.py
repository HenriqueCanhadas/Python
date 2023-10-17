import customtkinter

janela=customtkinter.CTk()
janela.geometry("700x400")
janela.title("TESTE")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def enviar():
    print(entry.get())
    lab.configure(text=str(entry.get()))
    pass

lab = customtkinter.CTkLabel(janela,text="", width=200, height=25, fg_color="green").pack(pady=10)

entry = customtkinter.CTkEntry(janela, width=200)
entry.pack()

customtkinter.CTkButton(janela, text="Enviar", width=200, command=enviar).pack(pady=10)

button = customtkinter.CTkButton(janela, text="Teste", fg_color=("#DB3E39", "#821D1A")).pack(pady=10)  # tuple color

progressbar = customtkinter.CTkProgressBar(janela, orientation="horizontal").pack()

label = customtkinter.CTkLabel(janela, text="CTkLabel", fg_color="transparent")
print(label)
label.configure(text="new text")

label.configure(text="novo texto")

print (label)

janela.mainloop()