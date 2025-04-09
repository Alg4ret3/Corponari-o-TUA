# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlMonitoreo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Control_Monitoreo(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1460, 818)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(300, 600))
        Form.setStyleSheet(
            "background-color: rgb(238, 238, 238);\n"
            "background-color: rgb(255, 255, 255);"
        )
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stackedWidget_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.stackedWidget_2Page1 = QtWidgets.QWidget()
        self.stackedWidget_2Page1.setObjectName("stackedWidget_2Page1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.stackedWidget_2Page1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_5 = QtWidgets.QFrame(self.stackedWidget_2Page1)
        self.frame_5.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 65))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(
            1300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem)
        self.BtnCrear = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnCrear.sizePolicy().hasHeightForWidth())
        self.BtnCrear.setSizePolicy(sizePolicy)
        self.BtnCrear.setMinimumSize(QtCore.QSize(180, 45))
        self.BtnCrear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnCrear.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #16344D; /* Color de fondo */\n"
            "    border-radius: 5px; /* Bordes redondeados */\n"
            "    color: white; /* Color del texto */\n"
            "    padding: 5px 10px; /* Espaciado interno */\n"
            "    border: none; /* Elimina el borde predeterminado */\n"
            "    font-size: 22px; /* Tamaño de fuente */\n"
            "    text-align: center; /* Alinea el texto a la izquierda */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #4C6D8C; /* Color de fondo al pasar el mouse */\n"
            "    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* Sombra al pasar el mouse */\n"
            "    transform: scale(1.02); /* Ligero aumento al pasar el mouse */\n"
            "    transition: all 0.3s ease-in-out; /* Transición suave */\n"
            "}\n"
            "\n"
            "QPushButton::icon {\n"
            "    padding-right: 5px; /* Espaciado entre el icono y el texto */\n"
            "}\n"
            ""
        )
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("assets/iconos/anadir.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.BtnCrear.setIcon(icon)
        self.BtnCrear.setIconSize(QtCore.QSize(24, 24))
        self.BtnCrear.setObjectName("BtnCrear")
        self.horizontalLayout_4.addWidget(self.BtnCrear, 0, QtCore.Qt.AlignRight)
        self.BtnActualizar = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.BtnActualizar.sizePolicy().hasHeightForWidth()
        )
        self.BtnActualizar.setSizePolicy(sizePolicy)
        self.BtnActualizar.setMinimumSize(QtCore.QSize(180, 45))
        self.BtnActualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnActualizar.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #16344D; /* Color de fondo */\n"
            "    border-radius: 2px; /* Bordes redondeados */\n"
            "    color: white; /* Color del texto */\n"
            "    padding: 5px 10px; /* Espaciado interno */\n"
            "    border: none; /* Elimina el borde predeterminado */\n"
            "    font-size: 22px; /* Tamaño de fuente */\n"
            "    text-align: Center; /* Alinea el texto a la izquierda */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #525C5E; /* Color de fondo al pasar el mouse */\n"
            "    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* Sombra al pasar el mouse */\n"
            "    transform: scale(1.02); /* Ligero aumento al pasar el mouse */\n"
            "    transition: all 0.3s ease-in-out; /* Transición suave */\n"
            "}\n"
            "\n"
            "QPushButton::icon {\n"
            "    padding-right: 5px; /* Espaciado entre el icono y el texto */\n"
            "}\n"
            ""
        )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap("assets/iconos/actualizar-flecha.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.BtnActualizar.setIcon(icon1)
        self.BtnActualizar.setIconSize(QtCore.QSize(24, 24))
        self.BtnActualizar.setObjectName("BtnActualizar")
        self.horizontalLayout_4.addWidget(self.BtnActualizar, 0, QtCore.Qt.AlignRight)
        self.BtnBorrar = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BtnBorrar.sizePolicy().hasHeightForWidth())
        self.BtnBorrar.setSizePolicy(sizePolicy)
        self.BtnBorrar.setMinimumSize(QtCore.QSize(180, 45))
        self.BtnBorrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BtnBorrar.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #16344D; /* Color de fondo */\n"
            "    border-radius: 5px; /* Bordes redondeados */\n"
            "    color: white; /* Color del texto */\n"
            "    padding: 5px 10px; /* Espaciado interno */\n"
            "    border: none; /* Elimina el borde predeterminado */\n"
            "    font-size: 22px; /* Tamaño de fuente */\n"
            "    text-align: center; /* Alinea el texto a la izquierda */\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #D32F2F  ; /* Color de fondo al pasar el mouse */\n"
            "    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); /* Sombra al pasar el mouse */\n"
            "    transform: scale(1.02); /* Ligero aumento al pasar el mouse */\n"
            "    transition: all 0.3s ease-in-out; /* Transición suave */\n"
            "}\n"
            "\n"
            "QPushButton::icon {\n"
            "    padding-right: 5px; /* Espaciado entre el icono y el texto */\n"
            "}\n"
            ""
        )
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("assets/iconos/borrar.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.BtnBorrar.setIcon(icon2)
        self.BtnBorrar.setIconSize(QtCore.QSize(28, 28))
        self.BtnBorrar.setObjectName("BtnBorrar")
        self.horizontalLayout_4.addWidget(self.BtnBorrar, 0, QtCore.Qt.AlignRight)
        self.gridLayout_3.addWidget(self.frame_4, 3, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(250, 50))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Linebuscador = QtWidgets.QLineEdit(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Linebuscador.sizePolicy().hasHeightForWidth())
        self.Linebuscador.setSizePolicy(sizePolicy)
        self.Linebuscador.setMinimumSize(QtCore.QSize(500, 40))
        self.Linebuscador.setMaximumSize(QtCore.QSize(300, 25))
        self.Linebuscador.setStyleSheet(
            "QLineEdit {\n"
            "\n"
            "    background-color: #f5f5f5; /* Gris más claro cuando se escribe */\n"
            "    border: none; /* Sin bordes generales */\n"
            "    border-bottom: 1px solid #000000; /* Solo borde inferior inicial */\n"
            "    border-radius: 4px; /* Sin bordes redondeados */\n"
            "    padding: 5px; /* Espaciado interno */\n"
            "    font: 18px;\n"
            "QLineEdit {\n"
            "\n"
            "    background-color: #f5f5f5; /* Gris más claro cuando se escribe */\n"
            "    border: none; /* Sin bordes generales */\n"
            "    border-bottom: 1px solid #000000; /* Solo borde inferior inicial */\n"
            "    border-radius: 0px; /* Sin bordes redondeados */\n"
            "    padding: 5px; /* Espaciado interno */\n"
            "    font: 10px;\n"
            "\n"
            "    margin-right: 8px; /* Margen a la derecha de 10px */\n"
            "}\n"
            "\n"
            "/* Al pasar el mouse, se agregan los bordes izquierdo y derecho */\n"
            "QLineEdit:hover {\n"
            "    border-bottom: 2px solid #16344D; /* Mantiene el borde inferior */\n"
            "}\n"
            "\n"
            "/* Al hacer clic (foco), se mantiene igual que el hover */\n"
            "QLineEdit:focus {\n"
            "    border-bottom: 2px solid #16344D;\n"
            "    background-color: #e0e0e0; /* Gris más claro cuando se escribe */\n"
            "    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Sombra opcional al activar */\n"
            "}\n"
            "\n"
            "}\n"
            "\n"
            "/* Al pasar el mouse, se agregan los bordes izquierdo y derecho */\n"
            "QLineEdit:hover {\n"
            "    border-bottom: 2px solid #16344D; /* Mantiene el borde inferior */\n"
            "}\n"
            "\n"
            "/* Al hacer clic (foco), se mantiene igual que el hover */\n"
            "QLineEdit:focus {\n"
            "    border-bottom: 2px solid #16344D;\n"
            "    background-color: #e0e0e0; /* Gris más claro cuando se escribe */\n"
            "    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Sombra opcional al activar */\n"
            "}\n"
            ""
        )
        self.Linebuscador.setObjectName("Linebuscador")
        self.horizontalLayout_2.addWidget(self.Linebuscador)
        self.toolButton_2 = QtWidgets.QToolButton(self.frame_3)
        self.toolButton_2.setMinimumSize(QtCore.QSize(45, 45))
        self.toolButton_2.setMaximumSize(QtCore.QSize(30, 30))
        self.toolButton_2.setStyleSheet("border:none;")
        self.toolButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap("assets/iconos/people.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        self.toolButton_2.setIcon(icon3)
        self.toolButton_2.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_2.addWidget(self.toolButton_2)
        self.gridLayout_3.addWidget(self.frame_3, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setStyleSheet("border:none;\n" "font:20px;")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.LineObservaciones = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LineObservaciones.sizePolicy().hasHeightForWidth()
        )
        self.LineObservaciones.setSizePolicy(sizePolicy)
        self.LineObservaciones.setMinimumSize(QtCore.QSize(500, 40))
        self.LineObservaciones.setStyleSheet(
            "QLineEdit {\n"
            "\n"
            "    background-color: #f5f5f5; /* Gris más claro cuando se escribe */\n"
            "    border: none; /* Sin bordes generales */\n"
            "    border-bottom: 1px solid #000000; /* Solo borde inferior inicial */\n"
            "    border-radius: 0px; /* Sin bordes redondeados */\n"
            "    padding: 5px; /* Espaciado interno */\n"
            "    font: 20px;\n"
            "QLineEdit {\n"
            "\n"
            "    background-color: #f5f5f5; /* Gris más claro cuando se escribe */\n"
            "    border: none; /* Sin bordes generales */\n"
            "    border-bottom: 1px solid #000000; /* Solo borde inferior inicial */\n"
            "    border-radius: 0px; /* Sin bordes redondeados */\n"
            "    padding: 5px; /* Espaciado interno */\n"
            "    font: 10px;\n"
            "\n"
            "    margin-right: 8px; /* Margen a la derecha de 10px */\n"
            "}\n"
            "\n"
            "/* Al pasar el mouse, se agregan los bordes izquierdo y derecho */\n"
            "QLineEdit:hover {\n"
            "    border-bottom: 2px solid #16344D; /* Mantiene el borde inferior */\n"
            "}\n"
            "\n"
            "/* Al hacer clic (foco), se mantiene igual que el hover */\n"
            "QLineEdit:focus {\n"
            "    border-bottom: 2px solid #16344D;\n"
            "    background-color: #e0e0e0; /* Gris más claro cuando se escribe */\n"
            "    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Sombra opcional al activar */\n"
            "}\n"
            "\n"
            "}\n"
            "\n"
            "/* Al pasar el mouse, se agregan los bordes izquierdo y derecho */\n"
            "QLineEdit:hover {\n"
            "    border-bottom: 2px solid #16344D; /* Mantiene el borde inferior */\n"
            "}\n"
            "\n"
            "/* Al hacer clic (foco), se mantiene igual que el hover */\n"
            "QLineEdit:focus {\n"
            "    border-bottom: 2px solid #16344D;\n"
            "    background-color: #e0e0e0; /* Gris más claro cuando se escribe */\n"
            "    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Sombra opcional al activar */\n"
            "}\n"
            ""
        )
        self.LineObservaciones.setObjectName("LineObservaciones")
        self.gridLayout.addWidget(self.LineObservaciones, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setStyleSheet("border:none;\n" "font:20px;")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setStyleSheet("border:none;\n" "font:20px;")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.LineNumeroDoc = QtWidgets.QLineEdit(self.frame_6)
        self.LineNumeroDoc.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #f5f5f5; /* Fondo gris claro */\n"
            "    border: none; /* Sin bordes generales */\n"
            "    border-bottom: 1px solid #000000; /* Solo borde inferior */\n"
            "    border-radius: 0px; /* Sin bordes redondeados */\n"
            "    padding: 5px; /* Espaciado interno */\n"
            "    font-size: 20px; /* Tamaño de fuente */\n"
            "    margin-right: 8px; /* Margen derecho */\n"
            "    text-align: center; /* Iniciar centrado */\n"
            "}\n"
            "\n"
            "/* Cambia el estilo cuando el cursor pasa por encima */\n"
            "QLineEdit:hover {\n"
            "    border-bottom: 2px solid #16344D; /* Resalta el borde inferior */\n"
            "}\n"
            "\n"
            "/* Cambia el estilo cuando está enfocado */\n"
            "QLineEdit:focus {\n"
            "    border-bottom: 2px solid #16344D;\n"
            "    background-color: #e0e0e0; /* Fondo más claro */\n"
            "    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Efecto de sombra */\n"
            "}\n"
            ""
        )
        self.LineNumeroDoc.setObjectName("LineNumeroDoc")
        self.gridLayout.addWidget(self.LineNumeroDoc, 4, 0, 1, 1)
        self.LineResponsableVisita = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LineResponsableVisita.sizePolicy().hasHeightForWidth()
        )
        self.LineResponsableVisita.setSizePolicy(sizePolicy)
        self.LineResponsableVisita.setMinimumSize(QtCore.QSize(500, 40))
        self.LineResponsableVisita.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #f5f5f5; /* Fondo gris claro */\n"
            "    border: none; /* Sin bordes generales */\n"
            "    border-bottom: 1px solid #000000; /* Solo borde inferior */\n"
            "    border-radius: 0px; /* Sin bordes redondeados */\n"
            "    padding: 5px; /* Espaciado interno */\n"
            "    font-size: 20px; /* Tamaño de fuente */\n"
            "    margin-right: 8px; /* Margen derecho */\n"
            "    text-align: center; /* Iniciar centrado */\n"
            "}\n"
            "\n"
            "/* Cambia el estilo cuando el cursor pasa por encima */\n"
            "QLineEdit:hover {\n"
            "    border-bottom: 2px solid #16344D; /* Resalta el borde inferior */\n"
            "}\n"
            "\n"
            "/* Cambia el estilo cuando está enfocado */\n"
            "QLineEdit:focus {\n"
            "    border-bottom: 2px solid #16344D;\n"
            "    background-color: #e0e0e0; /* Fondo más claro */\n"
            "    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Efecto de sombra */\n"
            "}\n"
            ""
        )
        self.LineResponsableVisita.setObjectName("LineResponsableVisita")
        self.gridLayout.addWidget(self.LineResponsableVisita, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setStyleSheet("border:none;\n" "font:20px;")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setStyleSheet("border:none;\n" "font:20px;")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.LineNumeroExpediente = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LineNumeroExpediente.sizePolicy().hasHeightForWidth()
        )
        self.LineNumeroExpediente.setSizePolicy(sizePolicy)
        self.LineNumeroExpediente.setMinimumSize(QtCore.QSize(500, 40))
        self.LineNumeroExpediente.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #f5f5f5; /* Fondo gris claro */\n"
            "    border: none; /* Sin bordes generales */\n"
            "    border-bottom: 1px solid #000000; /* Solo borde inferior */\n"
            "    border-radius: 0px; /* Sin bordes redondeados */\n"
            "    padding: 5px; /* Espaciado interno */\n"
            "    font-size: 20px; /* Tamaño de fuente */\n"
            "    margin-right: 8px; /* Margen derecho */\n"
            "    text-align: center; /* Iniciar centrado */\n"
            "}\n"
            "\n"
            "/* Cambia el estilo cuando el cursor pasa por encima */\n"
            "QLineEdit:hover {\n"
            "    border-bottom: 2px solid #16344D; /* Resalta el borde inferior */\n"
            "}\n"
            "\n"
            "/* Cambia el estilo cuando está enfocado */\n"
            "QLineEdit:focus {\n"
            "    border-bottom: 2px solid #16344D;\n"
            "    background-color: #e0e0e0; /* Fondo más claro */\n"
            "    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Efecto de sombra */\n"
            "}\n"
            ""
        )
        self.LineNumeroExpediente.setObjectName("LineNumeroExpediente")
        self.gridLayout.addWidget(self.LineNumeroExpediente, 1, 0, 1, 1)
        self.LineFechaControl = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.LineFechaControl.sizePolicy().hasHeightForWidth()
        )
        self.LineFechaControl.setSizePolicy(sizePolicy)
        self.LineFechaControl.setMinimumSize(QtCore.QSize(500, 40))
        self.LineFechaControl.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #f5f5f5; /* Fondo gris claro */\n"
            "    border: none; /* Sin bordes generales */\n"
            "    border-bottom: 1px solid #000000; /* Solo borde inferior */\n"
            "    border-radius: 0px; /* Sin bordes redondeados */\n"
            "    padding: 5px; /* Espaciado interno */\n"
            "    font-size: 20px; /* Tamaño de fuente */\n"
            "    margin-right: 8px; /* Margen derecho */\n"
            "    text-align: center; /* Iniciar centrado */\n"
            "}\n"
            "\n"
            "/* Cambia el estilo cuando el cursor pasa por encima */\n"
            "QLineEdit:hover {\n"
            "    border-bottom: 2px solid #16344D; /* Resalta el borde inferior */\n"
            "}\n"
            "\n"
            "/* Cambia el estilo cuando está enfocado */\n"
            "QLineEdit:focus {\n"
            "    border-bottom: 2px solid #16344D;\n"
            "    background-color: #e0e0e0; /* Fondo más claro */\n"
            "    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Efecto de sombra */\n"
            "}\n"
            ""
        )
        self.LineFechaControl.setText("")
        self.LineFechaControl.setObjectName("LineFechaControl")
        self.gridLayout.addWidget(self.LineFechaControl, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setStyleSheet("border:none;\n" "font:20px;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.LineRazonSocial = QtWidgets.QLineEdit(self.frame_6)
        self.LineRazonSocial.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #f5f5f5; /* Fondo gris claro */\n"
            "    border: none; /* Sin bordes generales */\n"
            "    border-bottom: 1px solid #000000; /* Solo borde inferior */\n"
            "    border-radius: 0px; /* Sin bordes redondeados */\n"
            "    padding: 5px; /* Espaciado interno */\n"
            "    font-size: 20px; /* Tamaño de fuente */\n"
            "    margin-right: 8px; /* Margen derecho */\n"
            "    text-align: center; /* Iniciar centrado */\n"
            "}\n"
            "\n"
            "/* Cambia el estilo cuando el cursor pasa por encima */\n"
            "QLineEdit:hover {\n"
            "    border-bottom: 2px solid #16344D; /* Resalta el borde inferior */\n"
            "}\n"
            "\n"
            "/* Cambia el estilo cuando está enfocado */\n"
            "QLineEdit:focus {\n"
            "    border-bottom: 2px solid #16344D;\n"
            "    background-color: #e0e0e0; /* Fondo más claro */\n"
            "    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3); /* Efecto de sombra */\n"
            "}\n"
            ""
        )
        self.LineRazonSocial.setObjectName("LineRazonSocial")
        self.gridLayout.addWidget(self.LineRazonSocial, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame_6, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.TablaMonitoreo = QtWidgets.QTableWidget(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.TablaMonitoreo.sizePolicy().hasHeightForWidth()
        )
        self.TablaMonitoreo.setSizePolicy(sizePolicy)
        self.TablaMonitoreo.setMinimumSize(QtCore.QSize(500, 150))
        self.TablaMonitoreo.setStyleSheet(
            "QTableWidget {\n"
            "    background-color: #f5f5f5; /* Fondo gris claro */\n"
            "    border: 1px solid #CCCCCC; /* Borde suave */\n"
            "    border-radius: 2px; /* Bordes redondeados */\n"
            "    font-size: 18px; /* Tamaño de fuente */\n"
            "    padding: 5px; /* Espaciado interno */\n"
            "    gridline-color: #DDDDDD; /* Color de las líneas de la cuadrícula */\n"
            "}\n"
            "\n"
            "QTableWidget::item {\n"
            "    padding: 5px; /* Espaciado de las celdas */\n"
            "    border-radius: 2px; /* Bordes redondeados en las celdas */\n"
            "}\n"
            "\n"
            "QTableWidget::item:hover {\n"
            "    background-color: #f0f0f0; /* Fondo claro al pasar el mouse */\n"
            "    color: #16344D; /* Texto azul al pasar el mouse */\n"
            "}\n"
            "\n"
            "/* Barra de desplazamiento vertical y horizontal */\n"
            "QScrollBar:vertical, QScrollBar:horizontal {\n"
            "    \n"
            "    border-radius: 15px; /* Bordes redondeados */\n"
            "    background-color: #f5f5f5; /* Fondo gris claro */\n"
            "    width: 7px; /* Ancho de la barra vertical */\n"
            "    height: 7px; /* Alto de la barra horizontal */\n"
            "}\n"
            "\n"
            '/* Manejador de la barra de desplazamiento (el "handle") */\n'
            "QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
            "    background-color: #16344D; /* Barra de desplazamiento en azul */\n"
            "    border-radius: 15px; /* Bordes redondeados */\n"
            "    min-height: 10px; /* Tamaño mínimo de la barra de desplazamiento vertical */\n"
            "    min-width: 10px; /* Tamaño mínimo de la barra de desplazamiento horizontal */\n"
            "}\n"
            "\n"
            "/* Efecto cuando el mouse pasa por encima del manejador */\n"
            "QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {\n"
            "    background-color: #1A4567; /* Fondo más oscuro al pasar el mouse */\n"
            "}\n"
            "\n"
            "/* Líneas de los botones de desplazamiento (arriba/abajo o izquierda/derecha) */\n"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
            "QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
            "    background: none; /* Quitar los botones de desplazamiento */\n"
            "}\n"
            "\n"
            "/* Flechas de los botones de desplazamiento */\n"
            "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,\n"
            "QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
            "    background: none; /* Quitar las flechas */\n"
            "}\n"
            ""
        )
        self.TablaMonitoreo.setObjectName("TablaMonitoreo")
        self.TablaMonitoreo.setColumnCount(4)
        self.TablaMonitoreo.setRowCount(24)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaMonitoreo.setHorizontalHeaderItem(3, item)
        self.gridLayout_3.addWidget(
            self.TablaMonitoreo, 2, 0, 1, 1, QtCore.Qt.AlignHCenter
        )
        self.verticalLayout.addWidget(self.frame_5)
        self.stackedWidget_2.addWidget(self.stackedWidget_2Page1)
        self.horizontalLayout_5.addWidget(self.stackedWidget_2)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Navbar"))
        self.BtnCrear.setText(_translate("Form", " Crear"))
        self.BtnActualizar.setText(_translate("Form", " Actualizar"))
        self.BtnBorrar.setText(_translate("Form", " Borrar"))
        self.label_6.setText(_translate("Form", "Número de documento:"))
        self.label.setText(_translate("Form", "Número de Expediente:"))
        self.label_3.setText(_translate("Form", "Responsable de la visita:"))
        self.label_4.setText(_translate("Form", "Observaciones:"))
        self.label_2.setText(_translate("Form", "Fecha de Control:"))
        self.label_5.setText(_translate("Form", "Razon Social:"))
        item = self.TablaMonitoreo.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(19)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(20)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(21)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(22)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.verticalHeaderItem(23)
        item.setText(_translate("Form", "New Row"))
        item = self.TablaMonitoreo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Expediente"))
        item = self.TablaMonitoreo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Fecha"))
        item = self.TablaMonitoreo.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Responsable"))
        item = self.TablaMonitoreo.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Observaciones"))
