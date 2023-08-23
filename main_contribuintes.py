from typing import Optional
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import *
import PySide6.QtWidgets
from contribuentes_juridica import *
from contribuintes_fisica import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 566)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_printcipal = QFrame(self.centralwidget)
        self.frame_printcipal.setObjectName(u"frame_printcipal")
        self.frame_printcipal.setFrameShape(QFrame.StyledPanel)
        self.frame_printcipal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_printcipal)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_contribuintes = QFrame(self.frame_printcipal)
        self.frame_contribuintes.setObjectName(u"frame_contribuintes")
        self.frame_contribuintes.setFrameShape(QFrame.StyledPanel)
        self.frame_contribuintes.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_contribuintes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_contribuintes = QLabel(self.frame_contribuintes)
        self.lbl_contribuintes.setObjectName(u"lbl_contribuintes")
        font = QFont()
        font.setPointSize(25)
        self.lbl_contribuintes.setFont(font)

        self.verticalLayout.addWidget(self.lbl_contribuintes, 0, Qt.AlignHCenter)

        self.btn_pFisica = QPushButton(self.frame_contribuintes)
        self.btn_pFisica.setObjectName(u"btn_pFisica")

        self.verticalLayout.addWidget(self.btn_pFisica)

        self.btn_pJuridica = QPushButton(self.frame_contribuintes)
        self.btn_pJuridica.setObjectName(u"btn_pJuridica")

        self.verticalLayout.addWidget(self.btn_pJuridica)

        self.verticalLayout_2.addWidget(self.frame_contribuintes)


        self.verticalLayout_3.addWidget(self.frame_printcipal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.btn_pFisica.clicked.connect(self.pessoaFisica)
        self.btn_pJuridica.clicked.connect(self.pessoaJuridica)
        
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_contribuintes.setText(QCoreApplication.translate("MainWindow", u"CONTRIBUINTES", None))
        self.btn_pFisica.setText(QCoreApplication.translate("MainWindow", u"Pessoa Fisica", None))
        self.btn_pJuridica.setText(QCoreApplication.translate("MainWindow", u"Pessoa Juridica", None))
        
        
    def pessoaFisica(self):
        self.pessoa_fisica = JanelaPessoaFis()
        self.pessoa_fisica.show()
        
        
    def pessoaJuridica(self):
        self.pessoa_juridica = JanelaPessoaJuridica()
        self.pessoa_juridica.show()    
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    janela = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(janela)
    janela.show()
    app.exec()