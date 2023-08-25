

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import telaini
from cadastroproduto import *
from produtos import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 602)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.f_principal = QFrame(self.centralwidget)
        self.f_principal.setObjectName(u"f_principal")
        self.f_principal.setFrameShape(QFrame.StyledPanel)
        self.f_principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.f_principal)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_telainicial = QLabel(self.f_principal)
        self.lbl_telainicial.setObjectName(u"lbl_telainicial")
        font = QFont()
        font.setPointSize(30)
        self.lbl_telainicial.setFont(font)

        self.verticalLayout.addWidget(self.lbl_telainicial, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.f_principal)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.btn_estoque = QPushButton(self.f_principal)
        self.btn_estoque.setObjectName(u"btn_estoque")

        self.verticalLayout.addWidget(self.btn_estoque)

        self.btn_cadastrarp = QPushButton(self.f_principal)
        self.btn_cadastrarp.setObjectName(u"btn_cadastrarp")

        self.verticalLayout.addWidget(self.btn_cadastrarp)


        self.verticalLayout_2.addWidget(self.f_principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.btn_cadastrarp.clicked.connect(self.cadastro_produto)
        self.btn_estoque.clicked.connect(self.estq)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_telainicial.setText(QCoreApplication.translate("MainWindow", u"Tela Inicial", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Comprar", None))
        self.btn_estoque.setText(QCoreApplication.translate("MainWindow", u"Ver Estoque", None))
        self.btn_cadastrarp.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Produto", None))
    def estq(self):
        self.estoque=Produtos()
        self.estoque.show()
    def cadastro_produto(self):
        self.cadastro = Ui_Cadastro()
        self.cadastro.show()

if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    w=QMainWindow()
    janela=Ui_MainWindow()
    janela.setupUi(w)
    w.show()
    app.exec()