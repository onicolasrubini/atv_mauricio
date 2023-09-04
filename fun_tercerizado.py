from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QStringListModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget,QListWidget,QMessageBox, QListView)
import fun_tercerizado

# classe das informações dos funcionarios
class Lista:
    def __init__(self,pagamento,nomeTercerizado,h_trabalhadasTercerizado,valor_porH_ter,despesa_add):
        
        self.pagamento = pagamento
        self.nomeTercerizado = nomeTercerizado
        self.h_trabalhadasTercerizado = h_trabalhadasTercerizado
        self.valor_porH_ter = valor_porH_ter
        self.despesa_add = despesa_add
        
        
class Funct(QWidget):
    def __init__(self):
        super().__init__()
        
        self.lista_ter=[]
        self.layout = QVBoxLayout()
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.f_principal = QFrame(self.centralwidget)
        self.f_principal.setObjectName(u"f_principal")
        self.f_principal.setGeometry(QRect(10, 10, 781, 571))
        self.f_principal.setFrameShape(QFrame.StyledPanel)
        self.f_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_principal)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.f_fun_terce = QFrame(self.f_principal)
        self.f_fun_terce.setObjectName(u"f_fun_proprio")
        self.f_fun_terce.setFrameShape(QFrame.StyledPanel)
        self.f_fun_terce.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.f_fun_terce)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_funtercerizado = QLabel(self.f_fun_terce)
        self.lbl_funtercerizado.setObjectName(u"lbl_funtercerizado")
        font = QFont()
        font.setPointSize(20)
        self.lbl_funtercerizado.setFont(font)

        self.verticalLayout.addWidget(self.lbl_funtercerizado)

        self.lbl_nomet = QLabel(self.f_fun_terce)
        self.lbl_nomet.setObjectName(u"lbl_nomet")

        self.verticalLayout.addWidget(self.lbl_nomet)

        self.input_nomet = QLineEdit(self.f_fun_terce)
        self.input_nomet.setObjectName(u"input_nomet")

        self.verticalLayout.addWidget(self.input_nomet)

        self.lbl_hrstt = QLabel(self.f_fun_terce)
        self.lbl_hrstt.setObjectName(u"lbl_hrstt")

        self.verticalLayout.addWidget(self.lbl_hrstt)

        self.input_hrstt = QLineEdit(self.f_fun_terce)
        self.input_hrstt.setObjectName(u"input_hrstt")

        self.verticalLayout.addWidget(self.input_hrstt)

        self.lbl_valorhrst = QLabel(self.f_fun_terce)
        self.lbl_valorhrst.setObjectName(u"lbl_valorhrst")

        self.verticalLayout.addWidget(self.lbl_valorhrst)

        self.input_valorhrst = QLineEdit(self.f_fun_terce)
        self.input_valorhrst.setObjectName(u"input_valorhrst")

        self.verticalLayout.addWidget(self.input_valorhrst)
        
        self.lbl_despesa=QLabel("Despesas",self)
        self.lbl_despesa.setGeometry(10,200,80,30)
        
        self.verticalLayout.addWidget(self.lbl_despesa)
        
        self.input_despesa=QLineEdit(self.f_fun_terce)
        self.input_despesa.setObjectName(u"input_despesa")
        
        self.verticalLayout.addWidget(self.input_despesa)

        self.btn_rgstro = QPushButton(self.f_fun_terce)
        self.btn_rgstro.setObjectName(u"btn_rgstro")

        self.verticalLayout.addWidget(self.btn_rgstro)

        self.verticalLayout_2.addWidget(self.f_fun_terce)

        self.f_dadost = QFrame(self.f_principal)
        self.f_dadost.setObjectName(u"f_dadost")
        self.f_dadost.setFrameShape(QFrame.StyledPanel)
        self.f_dadost.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.f_dadost)

        #conect o botao com a lista
        self.btn_rgstro.clicked.connect(self.registrar)
        self.btn_rgstro.clicked.connect(self.limpar_dados)
        
        self.setLayout(self.verticalLayout_2)
        
        # tela para printar nome e salario
        self.modelo_de_func = QStringListModel(self.f_fun_terce)
        self.func_view = QListView()
        self.func_view.setModel(self.modelo_de_func)
        self.verticalLayout.addWidget(self.func_view)
        
        self.lbl_funtercerizado.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio Tercerizado", None))
        self.lbl_nomet.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.input_nomet.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.lbl_hrstt.setText(QCoreApplication.translate("MainWindow", u"Horas trabalhadas", None))
        self.input_hrstt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite as horas trabalhadas", None))
        self.lbl_valorhrst.setText(QCoreApplication.translate("MainWindow", u"Valor horas", None))
        self.input_valorhrst.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite valor por horas", None))
        self.input_despesa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua despesa", None))
        self.btn_rgstro.setText(QCoreApplication.translate("MainWindow", u"Registra-se", None))
        
    # função para limpar os dados colocados
    def limpar_dados(self):
        self.input_nomet.setText("")
        self.input_hrstt.setText("")
        self.input_valorhrst.setText("")
        self.input_despesa.setText("")
    
    # função para printar a lista dos nomes e salario
    def registrar(self):
        nomeTercerizado = self.input_nomet.text()
        h_trabalhadasTercerizado = float(self.input_hrstt.text())
        valor_porH_ter = float(self.input_valorhrst.text())
        despesa_add = float(self.input_despesa.text())
        
        adicional = 1.1 * despesa_add
        pagamento = h_trabalhadasTercerizado * valor_porH_ter + adicional
        print(pagamento)
    
        
        if nomeTercerizado:
            funcionario = Lista(pagamento,nomeTercerizado,h_trabalhadasTercerizado,valor_porH_ter,despesa_add)
            self.lista_ter.append(funcionario)
            self.update_funcionario_tercerizado()
            self.input_nomet.clear()
        
        
    def update_funcionario_tercerizado(self):
        nome_func = [f"{funcionario.nomeTercerizado} - {funcionario.pagamento}" for funcionario in self.lista_ter]
        self.modelo_de_func.setStringList(nome_func)