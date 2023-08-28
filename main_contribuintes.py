# main 
import sys
from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *

from contribuintes import Contribuintes

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = QMainWindow()
    ui = Contribuintes()
    ui.setupUi(janela)
    janela.show()
    app.exec()