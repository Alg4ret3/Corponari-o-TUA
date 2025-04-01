from PyQt5.QtWidgets import QWidget, QHBoxLayout, QStackedWidget
from PyQt5.QtGui import QIcon
from app.view import (
    SidebarView,
    PersonalView,
    Tecnico_juridicaView,
    PUEAA_View,
    ControlView,
    Registro_View,
    Usuarios_View
)  # Asegúrate de importar correctamente SidebarView, PersonalView y Tecnico_juridicaView


class MainApp(QWidget):
    def __init__(self, parent=None):  # Recibe la referencia de MainWindow
        super(MainApp, self).__init__(parent)

        print("MainApp inicializada.")

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
        print("Sidebar añadido a MainApp.")

        # Crear el QStackedWidget para el contenido
        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)  # Agregar el QStackedWidget al lado derecho

        # Crear las vistas
        self.personal = PersonalView()
        print("Vista de PersonalView creada.")
        self.tecnico = Tecnico_juridicaView()  # Corregido el nombre de la vista
        self.PUEAA = PUEAA_View()
        self.Control = ControlView()
        self.registro = Registro_View()
        self.usuarios = Usuarios_View()
        
        # Agregar las vistas al QStackedWidget
        self.stacked_widget.addWidget(self.personal)  # Índice 0 (Vista de Personal)
        self.stacked_widget.addWidget(self.tecnico)  # Añadir la vista de Técnico Jurídico
        self.stacked_widget.addWidget(self.PUEAA)  # Añadir la vista de PUEAA
        self.stacked_widget.addWidget(self.Control)
        self.stacked_widget.addWidget(self.registro)  # Añadir la vista de Registro
        self.stacked_widget.addWidget(self.usuarios)  # Añadir la vista de Usuarios
        print("Vista de PersonalView y Tecnico_juridicaView añadidas al QStackedWidget.")

        # Conectar los botones a sus respectivas funciones
        self.sidebar.BtnExpediente.clicked.connect(self.mostrar_personal)
        self.sidebar.BtnResolucion.clicked.connect(self.mostrar_tecnico)
        self.sidebar.BtnPUEAA.clicked.connect(self.mostrar_pueaa)
        self.sidebar.BtnMonitoreo.clicked.connect(self.mostrar_control)
        self.sidebar.BtnRegistros.clicked.connect(self.mostrar_registro)
        self.sidebar.BtnUsuarios.clicked.connect(self.mostrar_usuarios)  # Conectar el botón de Usuarios
        # Establecer la vista inicial
        self.stacked_widget.setCurrentWidget(self.personal)

    def mostrar_personal(self):
        print("Botón presionado: BtnExpediente")  # Mensaje cuando el botón es presionado
        # Cambiar a la vista de Personal
        self.stacked_widget.setCurrentWidget(self.personal)
        print("Vista de PersonalView mostrada.")

    def mostrar_tecnico(self):
        print("Botón presionado: BtnResolucion")  # Mensaje cuando el botón es presionado
        # Cambiar a la vista de Técnico Jurídico
        self.stacked_widget.setCurrentWidget(self.tecnico)
        print("Vista de Tecnico_juridicaView mostrada.")
        
    def mostrar_pueaa(self):
        print("Botón presionado: BtnPUEAA")  # Mensaje cuando el botón es presionado
        # Cambiar a la vista de PUEAA
        self.stacked_widget.setCurrentWidget(self.PUEAA)
        print("Vista de PUEAAView mostrada.")   
        
    def mostrar_control(self):
        print("Botón presionado: BtnMonitoreo")  # Mensaje cuando el botón es presionado
        # Cambiar a la vista de Control
        self.stacked_widget.setCurrentWidget(self.Control)        
        print("Vista de ControlView mostrada.") 
    def mostrar_registro(self):
        print("Botón presionado: BtnRegistros")  # Mensaje cuando el botón es presionado
        # Cambiar a la vista de Registro
        self.stacked_widget.setCurrentWidget(self.registro)                
        print("Vista de RegistroView mostrada.")
        
    def mostrar_usuarios(self):
        print("Botón presionado: BtnUsuarios")  # Mensaje cuando el botón es presionado
        # Cambiar a la vista de Usuarios
        self.stacked_widget.setCurrentWidget(self.usuarios)                
        print("Vista de UsuariosView mostrada.")
