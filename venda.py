

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget,QMessageBox)
import sys
import venda
from cadastroproduto import *


class Vendas(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Janela de Venda")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.produto_cb = QComboBox()
        self.produto_cb.addItem("Produto 1")
        self.produto_cb.addItem("Produto 2")
        self.layout.addWidget(self.produto_cb)

        self.quantidade_input = QLineEdit()
        self.quantidade_input.setPlaceholderText("Quantidade")
        self.layout.addWidget(self.quantidade_input)

        self.total_label = QLabel("Total: R$ 0.00")
        self.layout.addWidget(self.total_label)

        self.btn_comprar = QPushButton("Comprar")
        self.btn_comprar.clicked.connect(self.adicionar_venda)
        self.layout.addWidget(self.btn_comprar)
        
        self.btn_comprar.clicked.connect(self.button_clicked)

        self.venda_total = 0

    def adicionar_venda(self):
        produto = self.produto_cb.currentText()
        quantidade = int(self.quantidade_input.text())
        preco_unitario = self.obter_preco_unitario(produto)
        total_produto = quantidade * preco_unitario
        self.venda_total += total_produto
        self.total_label.setText(f"Total: R$ {self.venda_total:.2f}")
        self.atualizar_estoque(produto, quantidade)

    def obter_preco_unitario(self, produto):

        precos = {"Produto 1": 10.00, "Produto 2": 20.00}
        return precos.get(produto, 0.00)

    def atualizar_estoque(self, produto, quantidade):

        print(f"Atualizando estoque para {produto}: -{quantidade} unidades")


    def button_clicked(self, s):
        
        dlg = QMessageBox(self)
        dlg.setText("Produto Vendido")
        btn_comprar = dlg.exec_()

        if btn_comprar == QMessageBox.Ok:
            print("OK!")