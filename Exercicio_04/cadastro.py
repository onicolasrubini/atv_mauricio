import sys
from PySide6.QtGui import QPixmap, QIntValidator, QColor
from PySide6.QtCore import QSize, Qt
from datetime import datetime, timedelta, date
from collections import deque
from PySide6.QtWidgets import QApplication,QFrame, QMainWindow, QLineEdit, QCheckBox, QPushButton, QVBoxLayout, QLabel, QDialog, QWidget, QComboBox
from paciente import Paciente

class Fila(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gerenciamento de Fila - Cadastro')
        self.setFixedSize(500,650)
        
        self.layout = QVBoxLayout()
        
        #====================================================#
        #================= img cadastro =====================#
        self.central_widget = QWidget() # Para centralizar
        self.setCentralWidget(self.central_widget)

        self.lbl_img = QLabel(self)
        self.lbl_img.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap("img_cadastro.png")    
        escala = pixmap.scaled(100, 80)
        
        self.lbl_img.setPixmap(escala)
        self.layout.addWidget(self.lbl_img)
        
        self.BK_Color = QColor(176, 196, 222) # Azul claro
        self.setStyleSheet(f'background-color: {self.BK_Color.name()};')

        #=====================================================
        # Titulo  
        self.lbl_Titulo = QLabel('Cadastramento de Dados',self)
        self.layout.addWidget(self.lbl_Titulo)
        
        # Informar o nome completo para cadastro
        self.lbl_nome_completo = QLabel('Nome completo',self)
        self.layout.addWidget(self.lbl_nome_completo)
        self.line_edit_nome_completo = QLineEdit(self)
        self.layout.addWidget(self.line_edit_nome_completo)
        self.line_edit_nome_completo.setPlaceholderText('Digite seu nome completo')
       
        # Informar o número de telefone para contato
        self.lbl_num_telefone = QLabel('Número de telefone',self)
        self.layout.addWidget(self.lbl_num_telefone)
        self.line_edit_num_telefone = QLineEdit(self)
        self.layout.addWidget(self.line_edit_num_telefone)
        self.line_edit_num_telefone.setValidator(QIntValidator())
        self.line_edit_num_telefone.setPlaceholderText('Digite seu número de telefone')
        
        # Informar o email
        self.lbl_email = QLabel('Email',self)
        self.layout.addWidget(self.lbl_email)
        self.line_edit_email = QLineEdit(self)
        self.layout.addWidget(self.line_edit_email)
        self.line_edit_email.setPlaceholderText('Digite seu email')
       
        # Informar o sexo                          
        self.lbl_sexo = QLabel('Sexo',self)
        self.layout.addWidget(self.lbl_sexo)
        
        # ComboBox sexo 
        self.cb_sexo = QComboBox(self)
        self.cb_sexo.addItems(['Masculino','Feminino','Outros'])
        self.layout.addWidget(self.cb_sexo)
        
        self.cb_sexo.currentIndexChanged.connect(self.mudanca_indice)
        self.cb_sexo.currentTextChanged.connect(self.mudanca_texto)
        
        self.cb_sexo.setEditable(True) # Permite que o conteudo editavel
        self.cb_sexo.setMaxCount(20) # Limite maximo do conteudo
        
#===================================================================================
        
        # Informar data de nascimento
        self.lbl_dt_nasc = QLabel('Data de nascimento',self)
        self.layout.addWidget(self.lbl_dt_nasc)
        self.line_edit_dt_nasc = QLineEdit(self)
        self.layout.addWidget(self.line_edit_dt_nasc) 
        self.line_edit_dt_nasc.setPlaceholderText('00/00/0000')
          
        
        # Informar pessoa pcd
        self.lbl_pcd = QLabel('Pessoa com deficiência (PCD) ?')
        self.layout.addWidget(self.lbl_pcd)
        
        # CheckBox Sim 
        self.ck_sim = QCheckBox('Sim',self)
        self.layout.addWidget(self.ck_sim)
        self.ck_sim.stateChanged.connect(self.ck_sim_)
        
         # Button de Cadastro
        self.btn_cadastrar = QPushButton('Cadastrar',self)
        self.layout.addWidget(self.btn_cadastrar)
        self.btn_cadastrar.clicked.connect(self.cadastrar)
        
        
        self.central_widget.setLayout(self.layout)
        
        
        
        self.lista_paciente = [] 
         
    
    # ===============================================     
    def mudanca_indice(self, i):
        print(i)
        
        
    # ===============================================
    def mudanca_texto(self, t):
        print(t)        
             
    
    # ===============================================
    def ck_sim_(self):
        if self.ck_sim.isChecked():
            if self.sender() == self.ck_sim:
                self.ck_sim.setChecked(True)
            else:
                self.ck_sim.setChecked(False)
                
    
    # ===============================================
    def calcular_idade(self):
        today = date.today()
                
                
    # ===============================================
    def cadastrar(self):
        nome = self.line_edit_nome_completo.text()
        fone = self.line_edit_num_telefone.text()
        email = self.line_edit_email.text()
        dt_nasc = self.line_edit_dt_nasc.text()
        pcd = self.ck_sim.isChecked()
        
        paciente = Paciente(nome, fone, email, dt_nasc, pcd)
        self.lista_paciente.append(paciente)
        
        self.line_edit_nome_completo.clear()
        self.line_edit_num_telefone.clear()
        self.line_edit_email.clear()  
        self.line_edit_dt_nasc.clear() 
        self.ck_sim.setChecked(False)
        self.update_pacientes()
        
#===========================================================================================         
        
    def update_pacientes(self):
        nome_p = [f"{paciente.nome}" for paciente in self.lista_paciente]
        
#===========================================================================================
        
        
        
        
if __name__ == "__main__":    
    app = QApplication(sys.argv)
    janela = Fila()
    janela.show()
    app.exec()