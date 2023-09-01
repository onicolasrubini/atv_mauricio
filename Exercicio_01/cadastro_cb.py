from PySide6.QtGui import QIntValidator, QFont, QColor
from PySide6.QtWidgets import QMainWindow, QLineEdit, QCheckBox, QPushButton, QVBoxLayout, QLabel, QWidget
from tela_inicial_cb import Tela_Inicial

class Cadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Att Avaliativa Banco')
        self.setFixedSize(500,400)
        
        self.central_widget = QWidget() # Para centralizar
        self.setCentralWidget(self.central_widget)
        
        #self.QFrame = QFrame()
        #self.QFrame.setStyleSheet(u'background-color: rgb(205,201,201);')
        #self.QFrame.setFrameShape(QFrame.StyledPanel)
        #self.QFrame.setGeometry(10,200,400,400)
        
        self.layout = QVBoxLayout()   
        
        self.BK_Color = QColor(156, 156, 156)
        self.setStyleSheet(f'background-color:{self.BK_Color.name()};')
        
        self.lbl_Titulo = QLabel('Conta Bancária',self)
        self.layout.addWidget(self.lbl_Titulo)
        self.font = QFont()
        self.font.setPointSize(25)
        self.font.setBold(True)
        self.lbl_Titulo.setFont(self.font)
        
        self.lbl_Num_Conta = QLabel('Número da conta',self)
        self.layout.addWidget(self.lbl_Num_Conta)
        self.line_Num_Conta = QLineEdit(self)
        self.layout.addWidget(self.line_Num_Conta)
        self.line_Num_Conta.setValidator(QIntValidator())
        self.line_Num_Conta.setPlaceholderText('Digite seu número da conta')
       
        self.lbl_Nome_Titular = QLabel('Nome do Titular',self)
        self.layout.addWidget(self.lbl_Nome_Titular)
        self.line_Nome_Titular = QLineEdit(self)
        self.layout.addWidget(self.line_Nome_Titular)
        self.line_Nome_Titular.setPlaceholderText('Digite seu nome')
        
        self.lbl_Depositar = QLabel('Deseja fazer seu primeiro deposito?',self)
        self.layout.addWidget(self.lbl_Depositar)
        
        self.ck_sim_deposito = QCheckBox('Sim',self)
        self.ck_nao_deposito = QCheckBox('Não',self)
        
        self.layout.addWidget(self.ck_sim_deposito)
        self.layout.addWidget(self.ck_nao_deposito)
        
        self.ck_sim_deposito.clicked.connect(self.ocultar_valor)
        self.ck_nao_deposito.clicked.connect(self.ocultar_valor)
                  
        self.lbl_Info_Quant_Dep = QLabel('Valor do Deposito inicial:',self)
        self.layout.addWidget(self.lbl_Info_Quant_Dep)
        self.line_Info_Quant_Dep = QLineEdit(self)
        self.layout.addWidget(self.line_Info_Quant_Dep)
        self.line_Info_Quant_Dep.setValidator(QIntValidator())
        self.line_Info_Quant_Dep.setPlaceholderText('Digite o valor do deposito inicial')
        
        self.button_Entrar = QPushButton('Entrar',self)
        self.layout.addWidget(self.button_Entrar)
        self.button_Entrar.clicked.connect(self.tela_inicial) 
        
        self.central_widget.setLayout(self.layout)
        
    def ocultar_valor(self):
        if self.ck_sim_deposito.isChecked() and self.ck_nao_deposito.isChecked():
            if self.sender() == self.ck_sim_deposito:
                self.ck_nao_deposito.setChecked(False)
            else:
                self.ck_sim_deposito.setChecked(False)
                
            if self.ck_sim_deposito.isChecked():
                self.lbl_Info_Quant_Dep.show()
                self.line_Info_Quant_Dep.show()
                
            else:
                self.lbl_Info_Quant_Dep.hide()
                self.line_Info_Quant_Dep.hide()        
                
    def tela_inicial(self):
        valor_inicial = float(self.line_Info_Quant_Dep.text()) if self.line_Info_Quant_Dep.text() else 0.0
        nome_Titular = str(self.line_Nome_Titular.text()) if self.line_Nome_Titular.text() else "Usuário"
        num_conta = int(self.line_Num_Conta.text()) if self.line_Num_Conta.text() else '54854325' 
        
        self.secondary_window = Tela_Inicial(valor_inicial, nome_Titular, num_conta)
        self.secondary_window.show()