

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
import fun_proprio

listav=[]
listah=[]
listap=[]
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 594)
        self.centralwidget = QWidget(MainWindow)
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        self.btn_mdados = QPushButton(self.f_principal)
        self.btn_mdados.setObjectName(u"btn_apgrrg")
        self.btn_mdados.setGeometry(20,300,150,30)
        self.btn_mdados.setText(QCoreApplication.translate("MainWindow", u"Mostrar dados", None))

        self.btn_rgstro.clicked.connect(self.limpar_dados)
        self.btn_mdados.clicked.connect(self.mostrardados)
        self.result_label=QLabel(self.f_principal)
        self.result_label.setGeometry(100,10,80,30)
        
       
        
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_funproprio.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio Pr\u00f3prio", None))
        self.lbl_nomep.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.input_nomep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu nome", None))
        self.lbl_hrstp.setText(QCoreApplication.translate("MainWindow", u"Horas trabalhadas", None))
        self.input_hrstp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite as horas trabalhadas", None))
        self.lbl_valorhrsp.setText(QCoreApplication.translate("MainWindow", u"Valor horas", None))
        self.input_valorhrsp.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite valor por horas", None))
        self.btn_rgstro.setText(QCoreApplication.translate("MainWindow", u"Registra-se", None))
        
    
            
    def limpar_dados(self):
        nome = self.input_nomep.text()
        listap.append(nome)
        
        self.input_nomep.setText("")
        
        self.input_hrstp.setText("")
        
        self.input_valorhrsp.setText("")
        
    def mostrardados(self):
         for i in listap:
            self.result_label.setText(i)

            

            
            
    
   
        
        
          


if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    w=QMainWindow()
    janela=Ui_MainWindow()
    janela.setupUi(w)
    w.show()
    app.exec()

