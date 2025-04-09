from PyQt5.QtWidgets import QWidget, QHBoxLayout, QStackedWidget
from PyQt5.QtGui import QIcon
from app.view import (
    SidebarView,
    PersonalView,
    Tecnico_juridicaView,
    PUEAA_View,
    ControlView,
    Registro_View,
    Usuarios_View,
    Usos_View,
)  


class MainApp(QWidget):
    def __init__(self, parent=None):  # Recibe la referencia de MainWindow
        super(MainApp, self).__init__(parent)

        # Configuración de la ventana principal
        self.setWindowTitle("Corponariño")
        self.setWindowIcon(QIcon("assets/iconoTitulo.png"))
        self.resize(800, 600)
        self.setStyleSheet("background-color: white;")

        # Widget central que contiene el diseño principal
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes
        layout.setSpacing(0)

        # Crear el Sidebar (equivalente al Navbar)
        self.sidebar = SidebarView()
        layout.addWidget(self.sidebar)  # Sidebar a la izquierda

        # Crear el QStackedWidget para el contenido
        self.stacked_widget = QStackedWidget()
        layout.addWidget(
            self.stacked_widget
        )  # Agregar el QStackedWidget al lado derecho

        # Crear las vistas
        self.personal = PersonalView()
        self.tecnico = Tecnico_juridicaView()  # Corregido el nombre de la vista
        self.PUEAA = PUEAA_View()
        self.Control = ControlView()
        self.registro = Registro_View()
        self.usuarios = Usuarios_View()
        self.Usos = Usos_View()

        # Agregar las vistas al QStackedWidget
        self.stacked_widget.addWidget(self.personal)  # Índice 0 (Vista de Personal)
        self.stacked_widget.addWidget(
            self.tecnico
        )  # Añadir la vista de Técnico Jurídico
        self.stacked_widget.addWidget(self.PUEAA)  # Añadir la vista de PUEAA
        self.stacked_widget.addWidget(self.Control)
        self.stacked_widget.addWidget(self.registro)  # Añadir la vista de Registro
        self.stacked_widget.addWidget(self.usuarios)  # Añadir la vista de Usuarios
        self.stacked_widget.addWidget(self.Usos)  # Añadir la vista de Usos

        # Conectar los botones a sus respectivas funciones
        self.sidebar.BtnExpediente.clicked.connect(self.mostrar_personal)
        self.sidebar.BtnResolucion.clicked.connect(self.mostrar_tecnico)
        self.sidebar.BtnPUEAA.clicked.connect(self.mostrar_pueaa)
        self.sidebar.BtnMonitoreo.clicked.connect(self.mostrar_control)
        self.sidebar.BtnRegistros.clicked.connect(self.mostrar_registro)
        self.sidebar.BtnUsuarios.clicked.connect(
            self.mostrar_usuarios
        )  # Conectar el botón de Usuarios
        self.sidebar.BtnUso.clicked.connect(
            self.mostrar_usos
        )  # Conectar el botón de Usos

        # Conectar los botones a la función set_button_style
        self.sidebar.BtnExpediente.clicked.connect(
            lambda: self.set_button_style(self.sidebar.BtnExpediente)
        )
        self.sidebar.BtnResolucion.clicked.connect(
            lambda: self.set_button_style(self.sidebar.BtnResolucion)
        )
        self.sidebar.BtnPUEAA.clicked.connect(
            lambda: self.set_button_style(self.sidebar.BtnPUEAA)
        )
        self.sidebar.BtnMonitoreo.clicked.connect(
            lambda: self.set_button_style(self.sidebar.BtnMonitoreo)
        )
        self.sidebar.BtnRegistros.clicked.connect(
            lambda: self.set_button_style(self.sidebar.BtnRegistros)
        )
        self.sidebar.BtnUsuarios.clicked.connect(
            lambda: self.set_button_style(self.sidebar.BtnUsuarios)
        )
        self.sidebar.BtnUso.clicked.connect(
            lambda: self.set_button_style(self.sidebar.BtnUso)
        )

        # Establecer la vista inicial
        self.stacked_widget.setCurrentWidget(self.personal)

    def set_button_style(self, clicked_button):
        """Configura el color del botón presionado y restablece los demás botones."""
        # Estilo común para todos los botones (color predeterminado)
        common_style = """
        background-color: #16344D;  /* Color de fondo por defecto */
        border-radius: 2px; /* Bordes redondeados */
        color: white; /* Color del texto */
        padding: 5px 10px; /* Espaciado interno */
        border: none; /* Elimina el borde predeterminado */
        font-size: 22px; /* Tamaño de fuente */
        text-align: left; /* Alinea el texto a la izquierda */
        """

        # Lista de todos los botones
        buttons = [
            self.sidebar.BtnExpediente,
            self.sidebar.BtnResolucion,
            self.sidebar.BtnPUEAA,
            self.sidebar.BtnMonitoreo,
            self.sidebar.BtnRegistros,
            self.sidebar.BtnUsuarios,
            self.sidebar.BtnUso,
        ]

        # Restablecer todos los botones al color predeterminado
        for btn in buttons:
            btn.setStyleSheet(common_style)

        # Estilo para el botón presionado (color azul)
        active_button_style = """
        background-color: #1A4567;  /* Color de fondo cuando el botón está presionado */
        border-radius: 2px;  /* Bordes redondeados */
        color: white;  /* Color del texto */
        padding: 5px 10px;  /* Espaciado interno */
        border: none;  /* Elimina el borde predeterminado */
        font-size: 22px;  /* Tamaño de fuente */
        text-align: left;  /* Alinea el texto a la izquierda */
        """

        # Aplicar el estilo activo solo al botón presionado
        clicked_button.setStyleSheet(active_button_style)

    def mostrar_personal(self):
        """Cambia la vista a la de Personal."""
        self.stacked_widget.setCurrentWidget(self.personal)

    def mostrar_tecnico(self):
        """Cambia la vista a la de Técnico Jurídico."""
        self.stacked_widget.setCurrentWidget(self.tecnico)

    def mostrar_pueaa(self):
        """Cambia la vista a la de PUEAA."""
        self.stacked_widget.setCurrentWidget(self.PUEAA)

    def mostrar_control(self):
        """Cambia la vista a la de Control."""
        self.stacked_widget.setCurrentWidget(self.Control)

    def mostrar_registro(self):
        """Cambia la vista a la de Registro."""
        self.stacked_widget.setCurrentWidget(self.registro)

    def mostrar_usuarios(self):
        """Cambia la vista a la de Usuarios."""
        self.stacked_widget.setCurrentWidget(self.usuarios)

    def mostrar_usos(self):
        """Cambia la vista a la de Usos."""
        self.stacked_widget.setCurrentWidget(self.Usos)
