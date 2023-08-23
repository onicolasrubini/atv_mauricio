import sys
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize, Qt
from datetime import datetime, timedelta
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit, QCheckBox, QPushButton, QVBoxLayout, QLabel, QDialog, QWidget, QFrame

from cadastro_fila import fila

class fila(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gerenciamento de Fila')
        self.setFixedSize(500,500)

        self.central_widget = QWidget() # Para centralizar
        self.setCentralWidget(self.central_widget)
        
        
        self.image_frame = QFrame(self)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame.setFixedSize(500,150)
        self.image_frame.setLayout(QVBoxLayout())
        
        self.image_frame.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.image_frame.setFrameShape(QFrame.StyledPanel)
        
        self.lbl_img = QLabel(self)
        self.lbl_img.setAlignment(Qt.AlignCenter)
        self.image_frame.layout().addWidget(self.lbl_img)
        
        # self.lbl_img.setPixmap(QPixmap('img_fila.jpg')) 
        # self.lbl_img.setScaledContents(True) 
        # self.lbl_img.setGeometry(10,100,200,250)
    
        layout = QVBoxLayout()
        # layout.addWidget(self.lbl_img)
        layout.addWidget(self.image_frame)
        
        self.setLayout(layout)
        
        pixmap = QPixmap("img_fila.jpg")    
        escala = pixmap.scaled(500, 400)
        self.lbl_img.setPixmap(escala)
        
        
        self.lbl_Titulo_tela_inicial = QLabel('Pacientes',self)
        self.lbl_Titulo_tela_inicial.setGeometry(220,150,100,30)
        
        
        

        
        
        
        
        
        
        
        
if __name__ == "__main__":    
    app = QApplication(sys.argv)
    janela = fila()
    janela.show()
    app.exec()