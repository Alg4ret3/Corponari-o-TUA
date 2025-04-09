# app/view/LoginView.py
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer
from app.ui.Usos import Ui_Usos
from PyQt5.QtCore import Qt


class Usos_View(QWidget, Ui_Usos):  # Heredamos de QWidget y de la interfaz Ui_Login
    def __init__(self, parent=None):  # Recibimos la referencia de MainWindow
        super(Usos_View, self).__init__(parent)
        self.setupUi(self)  # Configura los widgets generados por Qt Designer
        # Configuración inicial de la interfaz
