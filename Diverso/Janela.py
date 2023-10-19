import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MinhaJanela(QMainWindow):
    def resizeEvent(self, event):
        largura_atual = event.size().width()
        altura_atual = event.size().height()
        print(f"Largura atual da janela: {largura_atual}")
        print(f"Altura atual da janela: {altura_atual}")

app = QApplication(sys.argv)

janela = MinhaJanela()
janela.setGeometry(100, 100, 400, 300)  # Defina a posição e o tamanho inicial da janela
janela.show()

sys.exit(app.exec_())