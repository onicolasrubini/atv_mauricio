import sys
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QCheckBox, QPushButton, QVBoxLayout, QLabel, QDialog, QWidget, QMessageBox

#=====================================================================================#
class Tela_Inicial(QMainWindow):
    def __init__(self, valor_inicial, nome_Titular, num_conta):
        super().__init__()
        self.setWindowTitle('Tela Inicial')
        self.setGeometry(200,320,500,400)
        
        self.saldo = valor_inicial
        self.nome = nome_Titular
        self.num_conta = num_conta     
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
                
        # Para aparecer o nome e o saldo da pessoa
        self.lbl_Nome = QLabel(f'Olá {self.nome},',self)
        self.layout.addWidget(self.lbl_Nome)
        self.lbl_saldo = QLabel(f'Saldo {self.saldo}',self)
        self.layout.addWidget(self.lbl_saldo)
        
        self.button_depositos = QPushButton('Deposito',self)
        self.layout.addWidget(self.button_depositos)
        self.button_depositos.clicked.connect(self.pag_dep)
        
        self.button_saque = QPushButton('Saques',self)
        self.layout.addWidget(self.button_saque)
        self.button_saque.clicked.connect(self.pag_saque)
        
        self.button_conf = QPushButton('Configurações',self)
        self.layout.addWidget(self.button_conf)
        self.button_conf.clicked.connect(self.pag_conf)
        
        self.central_widget.setLayout(self.layout)
    
#=====================================================================================#    
    def pag_dep(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Tela Deposito')
        dialog.setGeometry(200,320,500,400)

        self.lbl_Nota = QLabel('Area Deposito',dialog)
        self.lbl_Nota.setGeometry(220,20,100,30)
        
        self.lbl_valor_dep = QLabel('Informe o valor',dialog)
        self.lbl_valor_dep.setGeometry(10,60,200,30)
        
        self.line_edit_valor_dep = QLineEdit(dialog)
        self.line_edit_valor_dep.setGeometry(10,90,480,20)
        
        self.lbl_saldo2 = QLabel(f'Saldo: {self.saldo}',dialog)
        self.lbl_saldo2.setGeometry(10,120,200,30)
        
        self.btn_dep = QPushButton('Depositar',dialog)
        self.btn_dep.setGeometry(10,160,480,25)
        self.btn_dep.clicked.connect(self.depositar)
                    
        dialog.exec()
  
     
    def depositar(self):
        valor_deposito = float(self.line_edit_valor_dep.text())
        
        self.saldo += valor_deposito
        self.lbl_saldo2.setText(f'Saldo: {self.saldo}')
        self.lbl_saldo.setText(f'Saldo {self.saldo}')
        
#=====================================================================================#        
    def pag_saque(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Tela Saque')
        dialog.setGeometry(200,320,500,400)
        
        self.lbl_Nota_saque = QLabel('Area Saque',dialog)
        self.lbl_Nota_saque.setGeometry(220,20,100,30)
        
        self.lbl_valor_saque = QLabel('Informe o valor do saque',dialog)
        self.lbl_valor_saque.setGeometry(10,60,200,30)
        
        self.line_edit_valor_saque = QLineEdit(dialog)
        self.line_edit_valor_saque.setGeometry(10,90,480,20)
        
        self.lbl_saldo_saque = QLabel(f'Saldo: {self.saldo}',dialog)
        self.lbl_saldo_saque.setGeometry(10,120,200,30)
        
        self.btn_saque = QPushButton('Realizar o Saque',dialog)
        self.btn_saque.setGeometry(10,160,480,25)
        self.btn_saque.clicked.connect(self.saque)
        
        dialog.exec()
    
    
    def saque(self):
        valor_saque = float(self.line_edit_valor_saque.text())
        taxa_saque = 5.0
        
        novo_valor = self.saldo - (valor_saque - taxa_saque)
        
        if novo_valor >= 0:
            self.saldo = novo_valor
        else:
            self.saldo = novo_valor
            print('Seu saldo está negativo!')
        
        self.lbl_saldo_saque.setText(f'Saldo: {self.saldo}')
        self.lbl_saldo.setText(f'Saldo {self.saldo}')
        
#=====================================================================================#
    def pag_conf(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Configuração')
        dialog.setGeometry(200,320,500,400)
        
        self.lbl_Nota_conf = QLabel('Alterar Titular',dialog)
        self.lbl_Nota_conf.setGeometry(220,20,100,30)
        
        self.lbl_novo_nome_Titular = QLabel('Novo Titular',dialog)
        self.lbl_novo_nome_Titular.setGeometry(10,60,200,30)
        
        self.line_edit_novo_nome_Titular = QLineEdit(dialog)
        self.line_edit_novo_nome_Titular.setGeometry(10,90,480,20)
        
        self.btn_novo_nome_titular_conf = QPushButton('Confirmar',dialog)
        self.btn_novo_nome_titular_conf.setGeometry(10,120,480,25)
        self.btn_novo_nome_titular_conf.clicked.connect(self.configuracao)
        
        self.lbl_informacoes = QLabel('Informações',dialog)
        self.lbl_informacoes.setGeometry(10,150,200,30)
        
        self.lbl_new_nome = QLabel(f'Nome completo: {self.nome}',dialog)
        self.lbl_new_nome.setGeometry(10,180,400,30)
        
        self.lbl_num_conta_conf = QLabel(f'Número da conta: {self.num_conta}',dialog)
        self.lbl_num_conta_conf.setGeometry(10,210,200,30)
        
        dialog.exec()
        
        
    def configuracao(self):
        new_nome = self.line_edit_novo_nome_Titular.text()
        self.nome = new_nome
        
        self.lbl_new_nome.setText(f'Nome completo: {self.nome}')
        self.lbl_Nome.setText(f'Olá {self.nome}')
         
#=====================================================================================#