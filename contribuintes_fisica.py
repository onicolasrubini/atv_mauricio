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
 
class JanelaPessoaJuridica(QWidget):
    def __init__(self):
        super().__init__()
        
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_pessoaJuridica = QFrame(self.centralwidget)
        self.frame_pessoaJuridica.setObjectName(u"frame_pessoaJuridica")
        self.frame_pessoaJuridica.setFrameShape(QFrame.StyledPanel)
        self.frame_pessoaJuridica.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_pessoaJuridica)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_pessoaJuridica = QLabel(self.frame_pessoaJuridica)
        self.lbl_pessoaJuridica.setObjectName(u"lbl_pessoaJuridica")
        font = QFont()
        font.setPointSize(10)
        self.lbl_pessoaJuridica.setFont(font)

        self.verticalLayout.addWidget(self.lbl_pessoaJuridica, 0, Qt.AlignHCenter)

        self.verticalLayout_5.addWidget(self.frame_pessoaJuridica)

        self.frame_nome_juridico = QFrame(self.centralwidget)
        self.frame_nome_juridico.setObjectName(u"frame_nome_juridico")
        self.frame_nome_juridico.setFrameShape(QFrame.StyledPanel)
        self.frame_nome_juridico.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_nome_juridico)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_nome_juridico = QLabel(self.frame_nome_juridico)
        self.lbl_nome_juridico.setObjectName(u"lbl_nome_juridico")
        self.lbl_nome_juridico.setFont(font)

        self.verticalLayout_2.addWidget(self.lbl_nome_juridico)

        self.input_nome_juridico = QLineEdit(self.frame_nome_juridico)
        self.input_nome_juridico.setObjectName(u"input_nome_juridico")

        self.verticalLayout_2.addWidget(self.input_nome_juridico)

        self.verticalLayout_5.addWidget(self.frame_nome_juridico)

        self.frame_rendaanual_juridico = QFrame(self.centralwidget)
        self.frame_rendaanual_juridico.setObjectName(u"frame_rendaanual_juridico")
        self.frame_rendaanual_juridico.setFrameShape(QFrame.StyledPanel)
        self.frame_rendaanual_juridico.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_rendaanual_juridico)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_rendaanual_juridico = QLabel(self.frame_rendaanual_juridico)
        self.lbl_rendaanual_juridico.setObjectName(u"lbl_rendaanual_juridico")
        self.lbl_rendaanual_juridico.setFont(font)

        self.verticalLayout_4.addWidget(self.lbl_rendaanual_juridico)

        self.input_rendaanual_juridico = QLineEdit(self.frame_rendaanual_juridico)
        self.input_rendaanual_juridico.setObjectName(u"input_rendaanual_juridico")

        self.verticalLayout_4.addWidget(self.input_rendaanual_juridico)

        self.verticalLayout_5.addWidget(self.frame_rendaanual_juridico)

        self.frame_numFunc = QFrame(self.centralwidget)
        self.frame_numFunc.setObjectName(u"frame_numFunc")
        self.frame_numFunc.setFrameShape(QFrame.StyledPanel)
        self.frame_numFunc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_numFunc)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_numFunc = QLabel(self.frame_numFunc)
        self.lbl_numFunc.setObjectName(u"lbl_numFunc")
        self.lbl_numFunc.setFont(font)

        self.verticalLayout_3.addWidget(self.lbl_numFunc)

        self.input_numFunc = QLineEdit(self.frame_numFunc)
        self.input_numFunc.setObjectName(u"input_numFunc")

        self.verticalLayout_3.addWidget(self.input_numFunc)

        self.verticalLayout_5.addWidget(self.frame_numFunc)

        self.frame_calcularImp_juridico = QFrame(self.centralwidget)
        self.frame_calcularImp_juridico.setObjectName(u"frame_calcularImp_juridico")
        self.frame_calcularImp_juridico.setFrameShape(QFrame.StyledPanel)
        self.frame_calcularImp_juridico.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_calcularImp_juridico)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_imposto_juridico = QPushButton(self.frame_calcularImp_juridico)
        self.btn_imposto_juridico.setObjectName(u"btn_imposto_juridico")

        self.verticalLayout_6.addWidget(self.btn_imposto_juridico)

        self.verticalLayout_5.addWidget(self.frame_calcularImp_juridico)

        self.setLayout(self.verticalLayout_5)

        self.lbl_pessoaJuridica.setText(QCoreApplication.translate("MainWindow", u"Pessoa Juridica", None))
        self.lbl_nome_juridico.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_rendaanual_juridico.setText(QCoreApplication.translate("MainWindow", u"Renda Anual", None))
        self.lbl_numFunc.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de Funcionarios", None))
        self.btn_imposto_juridico.setText(QCoreApplication.translate("MainWindow", u"Calcular Imposto", None))