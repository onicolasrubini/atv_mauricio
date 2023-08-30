from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import telainicialfunc
from fun_proprio import *
from fun_tercerizado import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.f_principal = QFrame(self.centralwidget)
        self.f_principal.setObjectName(u"f_principal")
        self.f_principal.setFrameShape(QFrame.StyledPanel)
        self.f_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_principal)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_telainicial = QLabel(self.f_principal)
        self.lb_telainicial.setObjectName(u"lb_telainicial")
        font = QFont()
        font.setPointSize(30)
        self.lb_telainicial.setFont(font)

        self.verticalLayout_2.addWidget(self.lb_telainicial, 0, Qt.AlignHCenter)

        self.btn_cadastrofp = QPushButton(self.f_principal)
        self.btn_cadastrofp.setObjectName(u"btn_cadastrofp")

        self.verticalLayout_2.addWidget(self.btn_cadastrofp)

        self.btn_cadastroft = QPushButton(self.f_principal)
        self.btn_cadastroft.setObjectName(u"btn_cadastroft")

        self.verticalLayout_2.addWidget(self.btn_cadastroft)
        
        self.verticalLayout.addWidget(self.f_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.btn_cadastrofp.clicked.connect(self.funcproprio)
        self.btn_cadastroft.clicked.connect(self.functerce)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_telainicial.setText(QCoreApplication.translate("MainWindow", u"Tela Inicial", None))
        self.btn_cadastrofp.setText(QCoreApplication.translate("MainWindow", u"Cadastro funcion\u00e1rio pr\u00f3prio", None))
        self.btn_cadastroft.setText(QCoreApplication.translate("MainWindow", u"Cadastro funcion\u00e1rio tercerizado", None))


    def funcproprio(self):
        self.cadastrop = Funcp()
        self.cadastrop.show()
        
        
    def functerce(self):
        nomeTercerizado=str()
        h_trabalhadasTercerizado=str()
        valor_porH_ter=float()
        despesa_add=float()
        
        self.cadastro_ter = Funct()
        self.cadastro_ter.show()
        
        self.cadastro_lista = Lista(nomeTercerizado,h_trabalhadasTercerizado,valor_porH_ter,despesa_add)
        self.cadastro_lista()
        
        
if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    ui=QMainWindow()
    janela=Ui_MainWindow()
    janela.setupUi(ui)
    ui.show()
    app.exec()