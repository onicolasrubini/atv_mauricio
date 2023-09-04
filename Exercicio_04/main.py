import sys
from PySide6.QtWidgets import QApplication

from telaInicial import tela_inicial


if __name__ == "__main__":    
    app = QApplication(sys.argv)
    janela = tela_inicial()
    janela.show()
    app.exec()