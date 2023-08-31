from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QStringListModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget,QListWidget, QListView)
import fun_proprio

# classe das informações dos funcionarios
class ListaP:
    def __init__(self,pagamento,nome,h_trabalhadas,valor_porH):
        
        self.pagamento = pagamento
        self.nome = nome
        self.h_trabalhadas = h_trabalhadas
        self.valor_porH = valor_porH


class Funcp(QWidget):
    def __init__(self):
        super().__init__()
        self.lista_propria=[]
        self.layout = QVBoxLayout()
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.f_principal = QFrame(self.centralwidget)
        self.f_principal.setObjectName(u"f_principal")
        self.f_principal.setGeometry(QRect(10, 10, 781, 571))
        self.f_principal.setFrameShape(QFrame.StyledPanel)
        self.f_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_principal)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.f_fun_proprio = QFrame(self.f_principal)
        self.f_fun_proprio.setObjectName(u"f_fun_proprio")
        self.f_fun_proprio.setFrameShape(QFrame.StyledPanel)
        self.f_fun_proprio.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.f_fun_proprio)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_funproprio = QLabel(self.f_fun_proprio)
        self.lbl_funproprio.setObjectName(u"lbl_funproprio")
        font = QFont()
        font.setPointSize(20)
        self.lbl_funproprio.setFont(font)

        self.verticalLayout.addWidget(self.lbl_funproprio)

        self.lbl_nomep = QLabel(self.f_fun_proprio)
        self.lbl_nomep.setObjectName(u"lbl_nomep")

        self.verticalLayout.addWidget(self.lbl_nomep)

        self.input_nomep = QLineEdit(self.f_fun_proprio)
        self.input_nomep.setObjectName(u"input_nomep")

        self.verticalLayout.addWidget(self.input_nomep)

        self.lbl_hrstp = QLabel(self.f_fun_proprio)
        self.lbl_hrstp.setObjectName(u"lbl_hrstp")

        self.verticalLayout.addWidget(self.lbl_hrstp)

        self.input_hrstp = QLineEdit(self.f_fun_proprio)
        self.input_hrstp.setObjectName(u"input_hrstp")

        self.verticalLayout.addWidget(self.input_hrstp)

        self.lbl_valorhrsp = QLabel(self.f_fun_proprio)
        self.lbl_valorhrsp.setObjectName(u"lbl_valorhrsp")

        self.verticalLayout.addWidget(self.lbl_valorhrsp)

        self.input_valorhrsp = QLineEdit(self.f_fun_proprio)
        self.input_valorhrsp.setObjectName(u"input_valorhrsp")

        self.verticalLayout.addWidget(self.input_valorhrsp)

        self.btn_rgstro = QPushButton(self.f_fun_proprio)
        self.btn_rgstro.setObjectName(u"btn_rgstro")

        self.verticalLayout.addWidget(self.btn_rgstro)

        self.verticalLayout_2.addWidget(self.f_fun_proprio)

        self.f_dadosp = QFrame(self.f_principal)
        self.f_dadosp.setObjectName(u"f_dadosp")
        self.f_dadosp.setFrameShape(QFrame.StyledPanel)
        self.f_dadosp.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.f_dadosp)

        self.btn_rgstro.clicked.connect(self.registrar)
        self.btn_rgstro.clicked.connect(self.limpar_dados_propria)  
        
        self.setLayout(self.verticalLayout_2)        
        
        # tela para printar nome e salario
        self.modelo_de_func = QStringListModel(self.f_fun_proprio)
        self.func_view = QListView()
        self.func_view.setModel(self.modelo_de_func)
        self.verticalLayout.addWidget(self.func_view)
   
        self.lbl_funproprio.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio Pr\u00f3prio", None))
        self.lbl_nomep.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.input_nomep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.lbl_hrstp.setText(QCoreApplication.translate("MainWindow", u"Horas trabalhadas", None))
        self.input_hrstp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite as horas trabalhadas", None))
        self.lbl_valorhrsp.setText(QCoreApplication.translate("MainWindow", u"Valor horas", None))
        self.input_valorhrsp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite valor por horas", None))
        self.btn_rgstro.setText(QCoreApplication.translate("MainWindow", u"Registra-se", None))
    
    # função para limpar os dados colocados
    def limpar_dados_propria(self):        
        self.input_nomep.setText("")
        self.input_hrstp.setText("")
        self.input_valorhrsp.setText("")        
        
    # função para printar a lista dos nomes e salario
    def registrar(self):
        nome = self.input_nomep.text()
        h_trabalhadas = float(self.input_hrstp.text())
        valor_porH = float(self.input_valorhrsp.text())
        
        pagamento = h_trabalhadas * valor_porH
        print(pagamento)
    
        
        if nome:
            funcionario = ListaP(pagamento,nome,h_trabalhadas,valor_porH)
            self.lista_propria.append(funcionario)
            self.update_funcionario_proprio()
            self.input_nomep.clear()
        
        
    def update_funcionario_proprio(self):
        nome_func = [f"{funcionario.nome} - {funcionario.pagamento}" for funcionario in self.lista_propria]
        self.modelo_de_func.setStringList(nome_func)