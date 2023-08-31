import sys
from PySide6.QtWidgets import *

from telainicialfunc import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(janela)
    janela.show()
    app.exec()