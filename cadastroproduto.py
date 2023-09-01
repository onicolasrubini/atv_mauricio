

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *
import cadastroproduto
from produtos import *

listac=[]
class Ui_Cadastro(QWidget):
    def __init__(self):
        super().__init__()
        
        font = QFont()
        font.setPointSize(10)
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.f_principal = QFrame(self.centralwidget)
        self.f_principal.setObjectName(u"f_principal")
        self.f_principal.setFrameShape(QFrame.StyledPanel)
        self.f_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.f_principal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_cadastrop = QLabel(self.f_principal)
        self.lbl_cadastrop.setObjectName(u"lbl_cadastrop")
        font1 = QFont()
        font1.setPointSize(17)
        self.lbl_cadastrop.setFont(font1)

        self.verticalLayout.addWidget(self.lbl_cadastrop)

        self.lbl_nome = QLabel(self.f_principal)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setFont(font)

        self.verticalLayout.addWidget(self.lbl_nome)

        self.input_nome = QLineEdit(self.f_principal)
        self.input_nome.setObjectName(u"input_nome")

        self.verticalLayout.addWidget(self.input_nome)

        self.lbl_precouni = QLabel(self.f_principal)
        self.lbl_precouni.setObjectName(u"lbl_precouni")
        self.lbl_precouni.setFont(font)

        self.verticalLayout.addWidget(self.lbl_precouni)

        self.input_precouni = QLineEdit(self.f_principal)
        self.input_precouni.setObjectName(u"input_precouni")

        self.verticalLayout.addWidget(self.input_precouni)

        self.lbl_qntdestq = QLabel(self.f_principal)
        self.lbl_qntdestq.setObjectName(u"lbl_qntdestq")

        self.verticalLayout.addWidget(self.lbl_qntdestq)

        self.input_qntdestq = QLineEdit(self.f_principal)
        self.input_qntdestq.setObjectName(u"input_qntdestq")

        self.verticalLayout.addWidget(self.input_qntdestq)

        self.verticalLayout_2.addWidget(self.f_principal)

        self.setLayout(self.verticalLayout_2)
        
        self.btn_enviar=QPushButton(self.f_principal)
        self.btn_enviar.setGeometry(10,200,90,30)
        
        self.verticalLayout.addWidget(self.btn_enviar)
        
        self.btn_enviar.clicked.connect(self.button_clicked)
        self.btn_enviar.clicked.connect(self.limpar_dados)
        

        
        
    def limpar_dados(self):
        nome = self.input_nome.text()
        listac.append(nome)
        
        self.input_nome.setText("")
        
        self.input_precouni.setText("")
        
        self.input_qntdestq.setText("")
        
        
    def button_clicked(self, s):
        
        dlg = QMessageBox(self)
        dlg.setText("Produto cadastrado com sucesso")
        btn_enviar = dlg.exec_()

        if btn_enviar == QMessageBox.Ok:
            print("OK!")
            
        
            
            
            
        
        
        self.lbl_cadastrop.setText(QCoreApplication.translate("Cadastro", u"Cadastro do Produto", None))
        self.lbl_nome.setText(QCoreApplication.translate("Cadastro", u"Nome", None))
        self.input_nome.setPlaceholderText(QCoreApplication.translate("Cadastro", u"Digite o nome do produto", None))
        self.lbl_precouni.setText(QCoreApplication.translate("Cadastro", u"Pre\u00e7o Unit\u00e1rio", None))
        self.input_precouni.setPlaceholderText(QCoreApplication.translate("Cadastro", u"Digite o pre\u00e7o unit\u00e1rio", None))
        self.lbl_qntdestq.setText(QCoreApplication.translate("Cadastro", u"Quantidade de estoque", None))
        self.input_qntdestq.setPlaceholderText(QCoreApplication.translate("Cadastro", u"Digite a quantidade de estoque", None))
        self.btn_enviar.setText(QCoreApplication.translate("Cadastro", u"Enviar", None))



    def adicionaritem(self):
        self.produto=Produtos()
        self.cb_produtos.addItem