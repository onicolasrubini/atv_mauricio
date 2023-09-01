import sys
from PySide6.QtWidgets import QApplication

from cadastro_cb import Cadastro

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    janela = Cadastro()
    janela.show()
    app.exec()