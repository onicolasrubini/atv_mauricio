import sys
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from datetime import datetime, timedelta 
from collections import deque
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QCheckBox, QPushButton, QVBoxLayout, QLabel, QDialog, QWidget, QComboBox

class Fila(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gerenciamento de Fila - Cadastro')
        self.setFixedSize(500,500)

        self.central_widget = QWidget() # Para centralizar
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        
        self.lbl_Titulo = QLabel('Cadastramento de Dados',self)
        self.layout.addWidget(self.lbl_Titulo)
        
        # Informar o nome completo para cadastro
        self.lbl_nome_completo = QLabel('Nome completo',self)
        self.layout.addWidget(self.lbl_nome_completo)
        self.line_edite_nome_completo = QLineEdit(self)
        self.layout.addWidget(self.line_edite_nome_completo)
       
        # Informar o número de telefone para contato
        self.lbl_num_telefone = QLabel('Número de telefone',self)
        self.layout.addWidget(self.lbl_num_telefone)
        self.line_edit_num_telefone = QLineEdit(self)
        self.layout.addWidget(self.line_edit_num_telefone)
        
        # Informar o email
        self.lbl_email = QLabel('Email',self)
        self.layout.addWidget(self.lbl_email)
        self.line_edit_email = QLineEdit(self)
        self.layout.addWidget(self.line_edit_email)
       
        # Informar o sexo                          
        self.lbl_sexo = QLabel('Sexo',self)
        self.layout.addWidget(self.lbl_sexo)
        
        # CheckBox Masculino 
        self.cb = QComboBox(self)
        self.cb.addItems(['Masculino','Feminino','Outros'])
        self.layout.addWidget(self.cb)
        
        self.cb.currentIndexChanged.connect(self.mudanca_indice)
        self.cb.currentTextChanged.connect(self.mudanca_texto)
        
        self.cb.setEditable(True) # Permite que o conteudo editavel
        self.cb.setMaxCount(10) # Limite maximo do conteudo
        
#===================================================================================
        
        # Informar data de nascimento
        self.lbl_dt_nasc = QLabel('Data de nascimento',self)
        self.layout.addWidget(self.lbl_dt_nasc)
        self.line_edit_dt_nasc = QLineEdit(self)
        self.layout.addWidget(self.line_edit_dt_nasc)   
        
        # Informar pessoa pcd
        self.lbl_pcd = QLabel('Pessoa com deficiência (PCD) ?')
        self.layout.addWidget(self.lbl_pcd)
        
        # CheckBox Sim e Não
        self.ck_sim = QCheckBox('Sim',self)
        self.ck_nao = QCheckBox('Não',self)
        self.layout.addWidget(self.ck_sim)
        self.layout.addWidget(self.ck_nao)
        
        # Button de Cadastro
        self.btn_cadastrar = QPushButton('Cadastrar',self)
        self.layout.addWidget(self.btn_cadastrar)
        
        self.ck_sim.stateChanged.connect(self.ck_sim_nao)
        self.ck_nao.stateChanged.connect(self.ck_sim_nao)  
        
        
        
        self.central_widget.setLayout(self.layout)
         
         
    def mudanca_indice(self, i):
        print(i)
        
    def mudanca_texto(self, t):
        print(t)        
                    
    def ck_sim_nao(self):
        if self.ck_sim.isChecked() and self.ck_nao.isChecked():
            if self.sender() == self.ck_sim:
                self.ck_nao.setChecked(False)
            else:
                self.ck_sim.setChecked(False)
                
        
        
if __name__ == "__main__":    
    app = QApplication(sys.argv)
    janela = fila()
    janela.show()
    app.exec()