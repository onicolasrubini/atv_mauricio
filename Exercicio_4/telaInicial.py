import sys
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from datetime import datetime, timedelta
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, 
    QVBoxLayout, QLabel, QWidget, QFrame, 
    QTableView, QTableWidget, QTableWidgetItem,
    QDockWidget, QFormLayout, QLineEdit, QSpinBox,
)

from cadastro import Fila

class tela_inicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gerenciamento de Fila')
        self.setFixedSize(500,650)

        self.central_widget = QWidget() # Para centralizar
        self.setCentralWidget(self.central_widget)
        
        
        # para colocar a imagem 
        self.image_frame = QFrame(self)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame.setFixedSize(500,200)
        self.image_frame.setLayout(QVBoxLayout())
        
        self.image_frame.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.image_frame.setFrameShape(QFrame.StyledPanel)
        
        self.lbl_img = QLabel(self)
        self.lbl_img.setAlignment(Qt.AlignCenter)
        self.image_frame.layout().addWidget(self.lbl_img)
    
        layout = QVBoxLayout()
        layout.addWidget(self.image_frame)
        
        self.setLayout(layout)
        
        pixmap = QPixmap("img_fila.jpg")    
        escala = pixmap.scaled(500, 400)
        self.lbl_img.setPixmap(escala)
        
        
        # Titulo 
        self.lbl_Titulo_tela_inicial = QLabel('Fila de pacientes',self)
        self.lbl_Titulo_tela_inicial.setGeometry(215,200,100,30)   
 
 
        # Botão de cadastro
        self.btn_cadastro = QPushButton('Cadastrar-se',self)
        self.btn_cadastro.setGeometry(126,600,250,30)
        self.btn_cadastro.clicked.connect(self.cadastro)
 
 #===========================================================================================
    def limpar_dados(self):
        self.input_nomet.setText("")
        self.input_hrstt.setText("")
        self.input_valorhrst.setText("")
        self.input_despesa.setText("")
    
    
    def registrar(self):
        nome_tercerizado = self.input_nomet.text()
        
        funcionario = Lista(nome_tercerizado)
        self.lista_ter.append(funcionario)
        self.update_funcionario_tercerizado()
        self.input_nomet.clear()
        
        
    def update_funcionario_tercerizado(self):
        nome_func = [f"{funcionario.nome}" for funcionario in self.lista_ter]
        self.modelo_de_func.setStringList(nome_func)
        
 #===========================================================================================       
    # def para ir para a proxima tela
    def cadastro(self):       
        self.secondary_window = Fila()
        self.secondary_window.show()       
        
               
if __name__ == "__main__":    
    app = QApplication(sys.argv)
    janela = tela_inicial()
    janela.show()
    app.exec()