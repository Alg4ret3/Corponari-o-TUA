# app/view/LoginView.py
from PyQt5.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer
from app.ui.Login import (
    Ui_Login,
)  # Asegúrate de importar correctamente la interfaz generada por Qt Designer
from PyQt5.QtCore import Qt


class Login_View(QWidget, Ui_Login):  # Heredamos de QWidget y de la interfaz Ui_Login
    def __init__(self, parent=None):  # Recibimos la referencia de MainWindow
        super(Login_View, self).__init__(parent)
        self.setupUi(self)  # Configura los widgets generados por Qt Designer
        # Configuración inicial de la interfaz
        QTimer.singleShot(
            0, self.lineEditUsuario.setFocus
        )  # Pone el foco en el campo de usuario
        self.lineEditPassword.setEchoMode(
            QLineEdit.Password
        )  # Establece el campo de contraseña como oculto

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            # Asegurarte de que el foco esté en lineEditUsuario primero
            if self.focusWidget() != self.lineEditUsuario:
                self.lineEditUsuario.setFocus()
            else:
                self.navegar_widgets()  # Continúa con la navegación normal
        elif event.key() == Qt.Key_Down:
            self.navegar_widgets_atras()

        # Llamar al método original para procesar otros eventos
        super().keyPressEvent(event)

    def navegar_widgets(self):
        if self.focusWidget() == self.lineEditUsuario:
            self.lineEditPassword.setFocus()
        elif self.focusWidget() == self.lineEditPassword:
            self.lineEditUsuario.setFocus()

    def navegar_widgets_atras(self):
        if self.focusWidget() == self.lineEditPassword:
            self.lineEditUsuario.setFocus()
        elif self.focusWidget() == self.lineEditUsuario:
            self.lineEditPassword.setFocus()
