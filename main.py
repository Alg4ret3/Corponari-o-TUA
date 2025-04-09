from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStackedWidget,
    QMessageBox,  # Para mostrar mensajes de error
)
from PyQt5.QtGui import QIcon
import sys
from app.view.LoginView import Login_View  # Importamos la clase Login_View
from app.VentanasView import MainApp  # Importamos la clase MainApp


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Corponariño")
        self.setWindowIcon(QIcon("assets/iconoTitulo.png"))
        self.resize(600, 700)  # Tamaño inicial de la ventana
        self.setStyleSheet("background-color: white;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Crear el diseño principal
        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes
        layout.setSpacing(0)

        self.stacked_widget = QStackedWidget()  # Contenedor de vistas
        layout.addWidget(self.stacked_widget)

        # Instanciar las vistas
        self.Login = Login_View()  # Vista de Login
        self.MainApp = (
            MainApp()
        )  # Vista principal de la aplicación después del inicio de sesión

        # Agregar vistas al QStackedWidget
        self.stacked_widget.addWidget(self.Login)
        self.stacked_widget.addWidget(self.MainApp)

        # Conectar el botón de login para verificar las credenciales
        self.Login.BtnIngresar.clicked.connect(self.iniciar_sesion)
        self.Login.lineEditPassword.returnPressed.connect(self.iniciar_sesion)
        self.MainApp.sidebar.BtnSalir.clicked.connect(self.cerrar_sesion)

    def cerrar_sesion(self):
        """
        Manejar el evento de cierre de sesión y restaurar el tamaño de la ventana."""
        self.stacked_widget.setCurrentWidget(self.Login)  # Cambiar a la vista de Login
        self.limpiar_campos()
        self.resize(600, 700)  # Restaurar el tamaño inicial de la ventana
        print("Sesión cerrada, tamaño restaurado a 500x600")

    def limpiar_campos(self):
        """
        Limpiar los campos de entrada del formulario de login.
        """
        self.Login.lineEditUsuario.clear()
        self.Login.lineEditPassword.clear()

    def iniciar_sesion(self):
        # Obtener los datos de usuario y contraseña
        usuario = self.Login.lineEditUsuario.text()
        contrasena = self.Login.lineEditPassword.text()

        # Verificación simple de las credenciales (sin base de datos)
        if usuario == "admin" and contrasena == "12345":
            # Si las credenciales son correctas, cambiar a MainApp y maximizar la ventana
            self.stacked_widget.setCurrentWidget(self.MainApp)
            self.showMaximized()  # Maximizar la ventana principal
            print("Inicio de sesión exitoso")
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            QMessageBox.critical(
                self, "Error de inicio de sesión", "Usuario o contraseña incorrectos."
            )
            print("Inicio de sesión fallido")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()  # Esto sigue siendo necesario para la ventana principal
    sys.exit(app.exec_())
