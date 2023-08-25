

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QSizePolicy, QWidget)
import produtos

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_estoque = QLabel(self.centralwidget)
        self.lbl_estoque.setObjectName(u"lbl_estoque")
        self.lbl_estoque.setGeometry(QRect(30, 20, 140, 48))
        font = QFont()
        font.setPointSize(30)
        self.lbl_estoque.setFont(font)
        self.cb_produtos = QComboBox(self.centralwidget)
        self.cb_produtos.addItem("")
        self.cb_produtos.setObjectName(u"cb_produtos")
        self.cb_produtos.setGeometry(QRect(30, 90, 161, 20))
        MainWindow.setCentralWidget(self.centralwidget)

        self.setLa
        self.lbl_estoque.setText(QCoreApplication.translate("MainWindow", u"Estoque", None))
        self.cb_produtos.setItemText(0, QCoreApplication.translate("MainWindow", u"Produtos", None))




if __name__=='__main__':
    import sys
    app = QApplication(sys.argv)
    w=QMainWindow()
    janela=Ui_MainWindow()
    janela.setupUi(w)
    w.show()
    app.exec()