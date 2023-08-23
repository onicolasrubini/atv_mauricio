import sys
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QCheckBox, QPushButton, QVBoxLayout, QLabel, QDialog, QWidget, QMessageBox

from cadastro_cb import Cadastro

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    janela = Cadastro()
    janela.show()
    app.exec()