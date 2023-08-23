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


class JanelaPessoaFis(QWidget):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_nome = QFrame(self.centralwidget)
        self.frame_nome.setObjectName(u"frame_nome")
        self.frame_nome.setFrameShape(QFrame.StyledPanel)
        self.frame_nome.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_nome)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_pessoaFisica = QLabel(self.frame_nome)
        self.lbl_pessoaFisica.setObjectName(u"lbl_pessoaFisica")
        font = QFont()
        font.setPointSize(10)
        self.lbl_pessoaFisica.setFont(font)

        self.verticalLayout.addWidget(self.lbl_pessoaFisica, 0, Qt.AlignHCenter)

        self.lbl_nome = QLabel(self.frame_nome)
        self.lbl_nome.setObjectName(u"lbl_nome")
        self.lbl_nome.setFont(font)

        self.verticalLayout.addWidget(self.lbl_nome)

        self.input_nome = QLineEdit(self.frame_nome)
        self.input_nome.setObjectName(u"input_nome")

        self.verticalLayout.addWidget(self.input_nome)

        self.verticalLayout_3.addWidget(self.frame_nome)

        self.frame_rendaanual = QFrame(self.centralwidget)
        self.frame_rendaanual.setObjectName(u"frame_rendaanual")
        self.frame_rendaanual.setFrameShape(QFrame.StyledPanel)
        self.frame_rendaanual.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_rendaanual)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_rendaanual = QLabel(self.frame_rendaanual)
        self.lbl_rendaanual.setObjectName(u"lbl_rendaanual")
        self.lbl_rendaanual.setFont(font)

        self.verticalLayout_4.addWidget(self.lbl_rendaanual)

        self.input_rendaanual = QLineEdit(self.frame_rendaanual)
        self.input_rendaanual.setObjectName(u"input_rendaanual")

        self.verticalLayout_4.addWidget(self.input_rendaanual)

        self.verticalLayout_3.addWidget(self.frame_rendaanual)

        self.frame_gastoSaude = QFrame(self.centralwidget)
        self.frame_gastoSaude.setObjectName(u"frame_gastoSaude")
        self.frame_gastoSaude.setFrameShape(QFrame.StyledPanel)
        self.frame_gastoSaude.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_gastoSaude)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_gastosSaude = QLabel(self.frame_gastoSaude)
        self.lbl_gastosSaude.setObjectName(u"lbl_gastosSaude")
        self.lbl_gastosSaude.setFont(font)

        self.verticalLayout_2.addWidget(self.lbl_gastosSaude)

        self.input_gastoSaude = QLineEdit(self.frame_gastoSaude)
        self.input_gastoSaude.setObjectName(u"input_gastoSaude")

        self.verticalLayout_2.addWidget(self.input_gastoSaude)

        self.verticalLayout_3.addWidget(self.frame_gastoSaude)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_calcular = QPushButton(self.frame)
        self.btn_calcular.setObjectName(u"btn_calcular")

        self.horizontalLayout.addWidget(self.btn_calcular)

        self.verticalLayout_3.addWidget(self.frame)

        self.setLayout(self.verticalLayout_3)

        self.lbl_pessoaFisica.setText(QCoreApplication.translate("MainWindow", u"Pessoa Fisica", None))
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_rendaanual.setText(QCoreApplication.translate("MainWindow", u"Renda Anual", None))
        self.lbl_gastosSaude.setText(QCoreApplication.translate("MainWindow", u"Gasto com Sa\u00fade", None))
        self.btn_calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular impostos", None))