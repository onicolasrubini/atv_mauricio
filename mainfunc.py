from typing import Optional
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import mainfunc
from fun_teladados import *
from func_poo import *
# while True:
listaf=[]
class MainWindow(QMainWindow):   
    
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"\n"
        "background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.f_principal = QFrame(self.centralwidget)
        self.f_principal.setObjectName(u"f_principal")
        self.f_principal.setFrameShape(QFrame.StyledPanel)
        self.f_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.f_principal)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lbl_rgfunp = QLabel(self.f_principal)
        self.lbl_rgfunp.setObjectName(u"lbl_rgfunp")

        self.verticalLayout_8.addWidget(self.lbl_rgfunp)

        self.f_nomefunt = QFrame(self.f_principal)
        self.f_nomefunt.setObjectName(u"f_nomefunt")
        self.f_nomefunt.setFrameShape(QFrame.StyledPanel)
        self.f_nomefunt.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.f_nomefunt)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_nomefunt = QLabel(self.f_nomefunt)
        self.lbl_nomefunt.setObjectName(u"lbl_nomefunt")

        self.verticalLayout_4.addWidget(self.lbl_nomefunt)

        self.input_nomet = QLineEdit(self.f_nomefunt)
        self.input_nomet.setObjectName(u"input_nomet")
        listaf.append(self.input_nomet)

        self.verticalLayout_4.addWidget(self.input_nomet)


        self.verticalLayout_8.addWidget(self.f_nomefunt)

        self.f_hrstfunt = QFrame(self.f_principal)
        self.f_hrstfunt.setObjectName(u"f_hrstfunt")
        self.f_hrstfunt.setFrameShape(QFrame.StyledPanel)
        self.f_hrstfunt.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.f_hrstfunt)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_hrstfunt = QLabel(self.f_hrstfunt)
        self.lbl_hrstfunt.setObjectName(u"lbl_hrstfunt")

        self.verticalLayout_3.addWidget(self.lbl_hrstfunt)

        self.input_hrstfunt = QLineEdit(self.f_hrstfunt)
        self.input_hrstfunt.setObjectName(u"input_hrstfunt")

        self.verticalLayout_3.addWidget(self.input_hrstfunt)

        self.f_valorhrsfunt = QFrame(self.f_hrstfunt)
        self.f_valorhrsfunt.setObjectName(u"f_valorhrsfunt")
        self.f_valorhrsfunt.setFrameShape(QFrame.StyledPanel)
        self.f_valorhrsfunt.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_valorhrsfunt)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_valorhrsfunt = QLabel(self.f_valorhrsfunt)
        self.lbl_valorhrsfunt.setObjectName(u"lbl_valorhrsfunt")

        self.verticalLayout_2.addWidget(self.lbl_valorhrsfunt)

        self.input_valorshrsfunt = QLineEdit(self.f_valorhrsfunt)
        self.input_valorshrsfunt.setObjectName(u"input_valorshrsfunt")

        self.verticalLayout_2.addWidget(self.input_valorshrsfunt)


        self.verticalLayout_3.addWidget(self.f_valorhrsfunt)


        self.verticalLayout_8.addWidget(self.f_hrstfunt)

        self.lbl_rgfunt = QLabel(self.f_principal)
        self.lbl_rgfunt.setObjectName(u"lbl_rgfunt")

        self.verticalLayout_8.addWidget(self.lbl_rgfunt)

        self.f_nomefup = QFrame(self.f_principal)
        self.f_nomefup.setObjectName(u"f_nomefup")
        self.f_nomefup.setFrameShape(QFrame.StyledPanel)
        self.f_nomefup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.f_nomefup)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_nomefunp = QLabel(self.f_nomefup)
        self.lbl_nomefunp.setObjectName(u"lbl_nomefunp")

        self.verticalLayout_5.addWidget(self.lbl_nomefunp)

        self.input_nomefuncp = QLineEdit(self.f_nomefup)
        self.input_nomefuncp.setObjectName(u"input_nomefuncp")
        listaf.append(self.input_nomefuncp)

        self.verticalLayout_5.addWidget(self.input_nomefuncp)


        self.verticalLayout_8.addWidget(self.f_nomefup)

        self.f_hrstfup = QFrame(self.f_principal)
        self.f_hrstfup.setObjectName(u"f_hrstfup")
        self.f_hrstfup.setFrameShape(QFrame.StyledPanel)
        self.f_hrstfup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.f_hrstfup)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_hrstfuncp = QLabel(self.f_hrstfup)
        self.lbl_hrstfuncp.setObjectName(u"lbl_hrstfuncp")

        self.verticalLayout_6.addWidget(self.lbl_hrstfuncp)

        self.input_hrstfuncp = QLineEdit(self.f_hrstfup)
        self.input_hrstfuncp.setObjectName(u"input_hrstfuncp")

        self.verticalLayout_6.addWidget(self.input_hrstfuncp)


        self.verticalLayout_8.addWidget(self.f_hrstfup)

        self.f_valorshrsfup = QFrame(self.f_principal)
        self.f_valorshrsfup.setObjectName(u"f_valorshrsfup")
        self.f_valorshrsfup.setFrameShape(QFrame.StyledPanel)
        self.f_valorshrsfup.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.f_valorshrsfup)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.lbl_valorhrsfuncp = QLabel(self.f_valorshrsfup)
        self.lbl_valorhrsfuncp.setObjectName(u"lbl_valorhrsfuncp")

        self.verticalLayout_7.addWidget(self.lbl_valorhrsfuncp)

        self.input_valorshrsfuncp = QLineEdit(self.f_valorshrsfup)
        self.input_valorshrsfuncp.setObjectName(u"input_valorshrsfuncp")

        self.verticalLayout_7.addWidget(self.input_valorshrsfuncp)


        self.verticalLayout_8.addWidget(self.f_valorshrsfup)

        self.f_despfunt = QFrame(self.f_principal)
        self.f_despfunt.setObjectName(u"f_despfunt")
        self.f_despfunt.setFrameShape(QFrame.StyledPanel)
        self.f_despfunt.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.f_despfunt)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_despesat = QLabel(self.f_despfunt)
        self.lbl_despesat.setObjectName(u"lbl_despesat")

        self.verticalLayout.addWidget(self.lbl_despesat)

        self.input_desfunt = QLineEdit(self.f_despfunt)
        self.input_desfunt.setObjectName(u"input_desfunt")

        self.verticalLayout.addWidget(self.input_desfunt)


        self.verticalLayout_8.addWidget(self.f_despfunt)

        self.btn_registro = QPushButton(self.f_principal)
        self.btn_registro.setObjectName(u"btn_registro")
        self.btn_registro.setStyleSheet(u"")
        

        

        self.verticalLayout_8.addWidget(self.btn_registro)


        self.horizontalLayout.addWidget(self.f_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        funcionario=Funcionario(self.input_nomefuncp,self.input_nomet,self.input_hrstfuncp,self.input_hrstfunt,self.input_valorshrsfuncp,self.input_valorshrsfunt,self.input_desfunt)
        self.btn_registro.clicked.connect(self.limpar_dados)
        self.btn_registro.clicked.connect(self.abrirdados)
        self.result_label=QLabel(self)
        self.result_label.setGeometry(10,110,280,30)      
         
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_rgfunp.setText(QCoreApplication.translate("MainWindow", u"Registro do funcion\u00e1rio pr\u00f3prio", None))
        self.lbl_nomefunt.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_hrstfunt.setText(QCoreApplication.translate("MainWindow", u"Horas trabalhadas", None))
        self.lbl_valorhrsfunt.setText(QCoreApplication.translate("MainWindow", u"Valor por horas", None))
        self.lbl_rgfunt.setText(QCoreApplication.translate("MainWindow", u"Registro do funcion\u00e1rio tercerizado", None))
        self.lbl_nomefunp.setText(QCoreApplication.translate("MainWindow", u"Nome ", None))
        self.lbl_hrstfuncp.setText(QCoreApplication.translate("MainWindow", u"Horas trabalhadas", None))
        self.lbl_valorhrsfuncp.setText(QCoreApplication.translate("MainWindow", u"Valor por horas", None))
        self.lbl_despesat.setText(QCoreApplication.translate("MainWindow", u"Despesa", None))
        self.btn_registro.setText(QCoreApplication.translate("MainWindow", u"Registra-se", None))
     
        
    
        
    def limpar_dados(self):
        self.input_nomet.setText("")
        
        self.input_hrstfunt.setText("")
        
        self.input_valorshrsfunt.setText("")
        
        
        self.input_nomefuncp.setText("")
       
        
        self.input_hrstfuncp.setText("")
       
        
        self.input_valorshrsfuncp.setText("")
        
        
        self.input_desfunt.setText("")
        
        
    def abrirdados(self):
        self.abrir_dados=Telasecundaria()
        self.abrir_dados.show()
        self.result_label.setText(self.input_nomefuncp)
        print(self.input_nomefuncp)
           
  
    

if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    w=QMainWindow()
    janela=MainWindow()
    janela.setupUi(w)
    w.show()
    app.exec()

