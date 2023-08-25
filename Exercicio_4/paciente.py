import sys
from PySide6.QtWidgets import QMainWindow, QApplication

class Paciente(QMainWindow):
    def __init__(self,nome,fone,email,horario):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.horario = horario