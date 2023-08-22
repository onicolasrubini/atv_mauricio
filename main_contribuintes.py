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
        
        
             
      #janela Pessoa Fisica
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
        
        
        
      #janela pessoa juridica  
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


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    janela = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(janela)
    janela.show()
    app.exec()