import tkinter as tk
import threading

def tarefa_demorada():
    print("oi")

def iniciar_tarefa():
    thread = threading.Thread(target=tarefa_demorada)
    thread.start()

root = tk.Tk()
botao = tk.Button(root, text="Iniciar Tarefa Demorada", command=iniciar_tarefa)
botao.pack()
root.mainloop()

