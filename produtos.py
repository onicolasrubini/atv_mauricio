from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QSizePolicy, QWidget,QFrame)
import produtos
from cadastroproduto import *

class Prod(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Produtos")
        self.setFixedSize(800,400)
        
        lista_estoque = str()
        self.lbl_estoque = QLabel(self)
        self.lbl_estoque.setGeometry(QRect(30, 20, 140, 48))
        font = QFont()
        font.setPointSize(30)
        self.lbl_estoque.setFont(font)
        self.cb_produtos = QComboBox(self)
        self.cb_produtos.addItem(lista_estoque)
        self.cb_produtos.setObjectName(u"cb_produtos")
        self.cb_produtos.setGeometry(QRect(30, 90, 161, 20))
        self.f_principal=QFrame(self)
        self.f_principal.setObjectName(u"f_principal")

        self.lbl_estoque.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.cb_produtos.setItemText(0, QCoreApplication.translate("MainWindow", u"Produtos", None))