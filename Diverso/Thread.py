import threading

def minha_funcao():
    for i in range(5):
        print(f"Executando na thread: {threading.current_thread().name}, valor: {i}")

thread1 = threading.Thread(target=minha_funcao, name="Thread 1")
thread2 = threading.Thread(target=minha_funcao, name="Thread 2")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Todas as threads terminaram.")