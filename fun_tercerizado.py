from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget,QListWidget)
import fun_tercerizado

listav=[]
listah=[]
listap=[]
class Funct(QWidget):
    def __init__(self):
        super().__init__()
        self.centralwidget = QWidget()
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
        self.lbl_funtercerizado.setObjectName(u"lbl_funproprio")
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
        
        self.lbl_despesa=QLabel(self.f_fun_terce)
        self.lbl_despesa.setObjectName(u"lbl_despesa")
        
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


        
        self.btn_mdados = QPushButton(self.f_principal)
        self.btn_mdados.setObjectName(u"btn_apgrrg")
        self.btn_mdados.setGeometry(20,300,150,30)
        self.btn_mdados.setText(QCoreApplication.translate("MainWindow", u"Mostrar dados", None))

        self.btn_rgstro.clicked.connect(self.limpar_dados)
        self.btn_mdados.clicked.connect(self.mostrardados)
        self.result_label=QLabel(self.f_principal)
        self.result_label.setGeometry(100,10,80,30)
        
       
        self.setLayout(self.verticalLayout_2)
        
   
        self.lbl_funtercerizado.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio Pr\u00f3prio", None))
        self.lbl_nomet.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.input_nomet.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.lbl_hrstt.setText(QCoreApplication.translate("MainWindow", u"Horas trabalhadas", None))
        self.input_hrstt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite as horas trabalhadas", None))
        self.lbl_valorhrst.setText(QCoreApplication.translate("MainWindow", u"Valor horas", None))
        self.input_valorhrst.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite valor por horas", None))
        self.btn_rgstro.setText(QCoreApplication.translate("MainWindow", u"Registra-se", None))
        
    
            
    def limpar_dados(self):
        nome = self.input_nomet.text()
        listap.append(nome)
        
        self.input_nomet.setText("")
        
        self.input_hrstt.setText("")
        
        self.input_valorhrst.setText("")
        
    def mostrardados(self):
         for i in listap:
            self.result_label.setText(i)
            
