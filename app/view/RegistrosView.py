# app/view/LoginView.py
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer
from app.ui.Registro import (
    Ui_Registro,
)  # Asegúrate de importar correctamente la interfaz generada por Qt Designer
from PyQt5.QtCore import Qt


class Registro_View(
    QWidget, Ui_Registro
):  # Heredamos de QWidget y de la interfaz Ui_Login
    def __init__(self, parent=None):  # Recibimos la referencia de MainWindow
        super(Registro_View, self).__init__(parent)
        self.setupUi(self)  # Configura los widgets generados por Qt Designer
        # Configuración inicial de la interfaz
