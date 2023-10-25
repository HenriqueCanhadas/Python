import customtkinter
from tkinter import *
from PIL import Image

janela=customtkinter.CTk()
janela.geometry("345x300")
janela.title("JANELA PRINCIPAL")
janela.resizable(width=False, height=False)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def entry():
    nova_janela = customtkinter.CTkToplevel(janela)
    nova_janela.geometry("300x250")
    nova_janela.title("CtkEntry")
    nova_janela.resizable(width=False, height=False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    texto = "teste"

    label = customtkinter.CTkLabel(nova_janela, text="CTkLabel", fg_color="transparent")
    label.configure(text="new text")
    label.pack()

    entry = customtkinter.CTkEntry(nova_janela, width=300, placeholder_text="Digite Algo", placeholder_text_color="red")
    entry.pack(pady=15)



    def pegar():
        global texto
        texto = (entry.get())
        if texto == "":
            print("Digite algo!!!")
        else:
            entry.delete(0,END)
            print(texto)
        pass

    def apagar():
        entry.delete(0,END)
        pass

    btn = customtkinter.CTkButton(nova_janela,text="Imprimir", width=300, command=pegar)
    btn.pack(pady=10)

    btn = customtkinter.CTkButton(nova_janela,
                                  text="Apagar", 
                                  fg_color="transparent",
                                  width=300, 
                                  command=apagar
                                 )
    btn.pack(pady=5)

    print(texto)

def teste():
    nova_janela = customtkinter.CTkToplevel(janela)
    nova_janela.geometry("250x250")
    nova_janela.title("Teste")
    nova_janela.resizable(width=False, height=False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    def enviar():
        print(entry.get())
        lab.configure(text=str(entry.get()))
        pass

    lab = customtkinter.CTkLabel(nova_janela,text="", width=200, height=25, fg_color="green").pack(pady=10)

    entry = customtkinter.CTkEntry(nova_janela, width=200)
    entry.pack()

    customtkinter.CTkButton(nova_janela, text="Enviar", width=200, command=enviar).pack(pady=10)

    button = customtkinter.CTkButton(nova_janela, text="Teste", fg_color=("#DB3E39", "#821D1A")).pack(pady=10)  # tuple color

    progressbar = customtkinter.CTkProgressBar(nova_janela, orientation="horizontal").pack()

    label = customtkinter.CTkLabel(nova_janela, text="CTkLabel", fg_color="transparent")
    print(label)
    label.configure(text="new text")

    label.configure(text="novo texto")

    label.pack()
    print (label)

def option_menu():
    nova_janela = customtkinter.CTkToplevel(janela)
    nova_janela.geometry("350x300")
    nova_janela.title("Option Menu")
    nova_janela.resizable(width=False, height=False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    customtkinter.CTkLabel(nova_janela, text="Menu de Opções", font=("arial bold", 20)).pack(pady=20, padx=5)

    customtkinter.CTkLabel(nova_janela, text="Escolha seu mes:", font=("arial bold",15)).pack()

    mes_var = customtkinter.StringVar(value="Escolha o mes")

    meses=["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]

    def mesfuncao(escolha):
        print(f"O seu mes foi:{escolha}")

    mes = customtkinter.CTkOptionMenu(nova_janela, values=meses, command=mesfuncao, variable=mes_var, width=250, height=50)

    mes.pack(pady=10)

    #mes.set("Escolha do mes")

def dialog():
    nova_janela = customtkinter.CTkToplevel(janela)
    nova_janela.geometry("350x300")
    nova_janela.title("Dialog")
    nova_janela.resizable(width=False, height=False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    textbox = customtkinter.CTkTextbox(nova_janela,width=300,height=200)
    textbox.pack()

    textbox.insert("0.0", "Titulo do seu texto" + "Teste Teste 123 123")

    def abrir():
        dialog = customtkinter.CTkInputDialog(title="Caixa de dialogo", text="Digite sua Idade:")
        teste=(dialog.get_input())
        print(teste)

    btn = customtkinter.CTkButton(nova_janela, text="Caixa de Dialogo", command=abrir)
    btn.pack()

def tabview():
    nova_janela = customtkinter.CTkToplevel(janela)
    nova_janela.geometry("350x300")
    nova_janela.title("Tabview")
    nova_janela.resizable(width=False, height=False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    tabview = customtkinter.CTkTabview(nova_janela,  width=100, corner_radius=20, border_width=5, border_color="red", segmented_button_selected_color="green", segmented_button_unselected_hover_color="white")
    tabview.pack()

    tabview.add("Nomes")
    tabview.add("Idades")
    tabview.add("Endereço")

    tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
    tabview.tab("Idades").grid_columnconfigure(0, weight=1)
    tabview.tab("Endereço").grid_columnconfigure(0, weight=1)

    text = customtkinter.CTkLabel(tabview.tab("Nomes"),text="Henrique Canhadas")
    text.pack()

    text = customtkinter.CTkLabel(tabview.tab("Idades"),text="20")
    text.pack()

    text = customtkinter.CTkLabel(tabview.tab("Endereço"),text="Grumixamas")
    text.pack()

def verificar_nome():
    nova_janela = customtkinter.CTkToplevel(janela)
    nova_janela.geometry("250x250")
    nova_janela.title("Verificar Nome")
    nova_janela.resizable(width=False, height=False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")



    customtkinter.CTkLabel(nova_janela, text="Labels", font=("arial bold", 20)).pack(pady=20, padx=5)

    customtkinter.CTkLabel(nova_janela,text="Este texto e de um label estatico").pack()

    text_var = customtkinter.StringVar(value="TESTE")

    lab1 = customtkinter.CTkLabel(nova_janela, textvariable=text_var, width=200, height=25, fg_color="blue").pack(pady=10)

    text_var1 = customtkinter.StringVar(value=input("Digite Seu Nome:"))

    lab2 = customtkinter.CTkLabel(nova_janela, textvariable=text_var1, width=200, height=25, fg_color="red").pack(pady=10)

def nova_tela():
   
    nova_janela = customtkinter.CTkToplevel(janela)
    nova_janela.geometry("700x400")
    nova_janela.title("Nova Tela")
    nova_janela.resizable(width=False, height=False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")


    btn= customtkinter.CTkButton(nova_janela, text="ola").pack()

    frame1 = customtkinter.CTkFrame(master= nova_janela, width=200, height=330, fg_color="red", bg_color="green", border_width=10, corner_radius=30).place(x=20, y=60)
    frame2 = customtkinter.CTkFrame(nova_janela, width=200, height=330, fg_color="green").place(x=240, y=60)
    frame2 = customtkinter.CTkFrame(nova_janela, width=200, height=330, fg_color="blue").place(x=460, y=60)

    def tela():
        nova_tela = customtkinter.CTkToplevel(janela)
        nova_tela.geometry("200x200")


    btn_tela = customtkinter.CTkButton(nova_janela, text="Nova Janela", command=tela).place(x=300, y =100)

def evento():
    print("Clicou")
    pass

def inserirnome():

    nova_janela = customtkinter.CTkToplevel(janela)
    nova_janela.geometry("250x250")
    nova_janela.title("Nomes")
    nova_janela.resizable(width=False, height=False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

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

def botao_youtube():
    nova_janela = customtkinter.CTkToplevel(janela, fg_color="teal")
    nova_janela.geometry("250x250")
    nova_janela.title("Botão Youtube")

    img=customtkinter.CTkImage(light_image=Image.open("Tkinter/youtubelogo.png"), dark_image=Image.open("Tkinter/youtubelogo.png"), size=(50,50))

    customtkinter.CTkButton(nova_janela,
                            text="Youtube",
                            width=300,
                            height=20,
                            fg_color="transparent",
                            hover_color="red",
                            text_color="white",
                            font=("Arial bold", 20),
                            border_color="white",
                            border_width=3,
                            border_spacing=5,
                            corner_radius=20,
                            state="normal",
                            image=img
                            ).pack(pady=30)
   
    pass

def slider():
    nova_janela = customtkinter.CTkToplevel(janela)
    nova_janela.geometry("250x250")
    nova_janela.title("Slider")
    nova_janela.resizable(width=False, height=False)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    def slider_value(valor):
        print(valor)

    customtkinter.CTkLabel(nova_janela, text="Valor de um slider").pack(pady=10)
    
    slider = customtkinter.CTkSlider(nova_janela, from_=0, to=100,command=slider_value, width=250,button_color="red",progress_color="green").pack(pady=20)

row = 1
column1=0
column2 =20

largurahorizontal=15
larguravertical=10

customtkinter.CTkButton(janela, text="Botão Youtube", command=botao_youtube).grid        (row=1, column=column1, padx=largurahorizontal, pady=larguravertical)
customtkinter.CTkButton(janela, text="Clique Aqui", command=evento).grid                 (row=1, column=column2, padx=largurahorizontal, pady=larguravertical)
customtkinter.CTkButton(janela, text="CtkEntry", command=entry).grid                     (row=2, column=column1, padx=largurahorizontal, pady=larguravertical)
customtkinter.CTkButton(janela, text="Dialog", command=dialog).grid                      (row=2, column=column2, padx=largurahorizontal, pady=larguravertical)
customtkinter.CTkButton(janela, text="Slider", command=slider).grid                      (row=3, column=column1, padx=largurahorizontal, pady=larguravertical)
customtkinter.CTkButton(janela, text="Inserir Nome", command=inserirnome).grid           (row=3, column=column2, padx=largurahorizontal, pady=larguravertical)
customtkinter.CTkButton(janela, text="Nova Tela", command=nova_tela).grid                (row=4, column=column1, padx=largurahorizontal, pady=larguravertical)
customtkinter.CTkButton(janela, text="Option Menu", command=option_menu).grid            (row=4, column=column2, padx=largurahorizontal, pady=larguravertical)
customtkinter.CTkButton(janela, text="Tabview", command=tabview).grid                    (row=5, column=column1, padx=largurahorizontal, pady=larguravertical)                                                                            
customtkinter.CTkButton(janela, text="Teste", command=teste).grid                        (row=5, column=column2, padx=largurahorizontal, pady=larguravertical)
customtkinter.CTkButton(janela, text="Verificar Nomes", command=verificar_nome).grid     (row=6, column=column1, padx=largurahorizontal, pady=larguravertical)

janela.mainloop()