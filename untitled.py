import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class MarketApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.products = []

        self.setWindowTitle("Sistema de Mercado")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.show_home()

    def show_home(self):
        self.clear_layout()
        layout = QVBoxLayout()

        home_label = QLabel("Bem-vindo ao Sistema de Mercado", self)
        layout.addWidget(home_label)

        self.central_widget.setLayout(layout)

    def show_registration(self):
        self.clear_layout()
        layout = QVBoxLayout()

        name_label = QLabel("Nome do Produto:", self)
        self.product_name = QLineEdit(self)
        price_label = QLabel("Preço do Produto:", self)
        self.product_price = QLineEdit(self)
        stock_label = QLabel("Estoque do Produto:", self)
        self.product_stock = QLineEdit(self)

        layout.addWidget(name_label)
        layout.addWidget(self.product_name)
        layout.addWidget(price_label)
        layout.addWidget(self.product_price)
        layout.addWidget(stock_label)
        layout.addWidget(self.product_stock)

        register_button = QPushButton("Cadastrar Produto", self)
        register_button.clicked.connect(self.register_product)
        layout.addWidget(register_button)

        self.central_widget.setLayout(layout)

    def register_product(self):
        name = self.product_name.text()
        price = float(self.product_price.text())
        stock = int(self.product_stock.text())

        new_product = Product(name, price, stock)
        self.products.append(new_product)

        self.product_name.clear()
        self.product_price.clear()
        self.product_stock.clear()

        self.show_status_message(f"Produto {name} cadastrado com sucesso!")

    def clear_layout(self):
        for i in reversed(range(self.central_widget.layout().count())):
            widget = self.central_widget.layout().itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def show_status_message(self, message):
        status_bar = self.statusBar()
        status_bar.showMessage(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarketApp()
    window.show()
    sys.exit(app.exec_())