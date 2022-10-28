# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(611, 537)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 30, 414, 393))
        self.tap = QWidget()
        self.tap.setObjectName(u"tap")
        self.gridLayout = QGridLayout(self.tap)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.tap)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.ID_spinBox = QSpinBox(self.groupBox)
        self.ID_spinBox.setObjectName(u"ID_spinBox")

        self.gridLayout_2.addWidget(self.ID_spinBox, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.ORIGEN_X_spinBox = QSpinBox(self.groupBox)
        self.ORIGEN_X_spinBox.setObjectName(u"ORIGEN_X_spinBox")

        self.gridLayout_2.addWidget(self.ORIGEN_X_spinBox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.ORIGEN_Y_spinBox = QSpinBox(self.groupBox)
        self.ORIGEN_Y_spinBox.setObjectName(u"ORIGEN_Y_spinBox")

        self.gridLayout_2.addWidget(self.ORIGEN_Y_spinBox, 2, 1, 1, 1)

        self.x_label = QLabel(self.groupBox)
        self.x_label.setObjectName(u"x_label")

        self.gridLayout_2.addWidget(self.x_label, 3, 0, 1, 1)

        self.x_spinBox = QSpinBox(self.groupBox)
        self.x_spinBox.setObjectName(u"x_spinBox")
        self.x_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.x_spinBox, 3, 1, 1, 1)

        self.y_label = QLabel(self.groupBox)
        self.y_label.setObjectName(u"y_label")

        self.gridLayout_2.addWidget(self.y_label, 4, 0, 1, 1)

        self.y_spinBox = QSpinBox(self.groupBox)
        self.y_spinBox.setObjectName(u"y_spinBox")
        self.y_spinBox.setMaximum(500)

        self.gridLayout_2.addWidget(self.y_spinBox, 4, 1, 1, 1)

        self.velocidad_label = QLabel(self.groupBox)
        self.velocidad_label.setObjectName(u"velocidad_label")

        self.gridLayout_2.addWidget(self.velocidad_label, 5, 0, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.groupBox)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")
        self.velocidad_spinBox.setMaximum(1000)

        self.gridLayout_2.addWidget(self.velocidad_spinBox, 5, 1, 1, 1)

        self.rojo_label = QLabel(self.groupBox)
        self.rojo_label.setObjectName(u"rojo_label")

        self.gridLayout_2.addWidget(self.rojo_label, 6, 0, 1, 1)

        self.rojo_spinBox = QSpinBox(self.groupBox)
        self.rojo_spinBox.setObjectName(u"rojo_spinBox")
        self.rojo_spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.rojo_spinBox, 6, 1, 1, 1)

        self.verde_label = QLabel(self.groupBox)
        self.verde_label.setObjectName(u"verde_label")

        self.gridLayout_2.addWidget(self.verde_label, 7, 0, 1, 1)

        self.verde_spinBox = QSpinBox(self.groupBox)
        self.verde_spinBox.setObjectName(u"verde_spinBox")

        self.gridLayout_2.addWidget(self.verde_spinBox, 7, 1, 1, 1)

        self.azul_label = QLabel(self.groupBox)
        self.azul_label.setObjectName(u"azul_label")

        self.gridLayout_2.addWidget(self.azul_label, 8, 0, 1, 1)

        self.azul_spinBox = QSpinBox(self.groupBox)
        self.azul_spinBox.setObjectName(u"azul_spinBox")

        self.gridLayout_2.addWidget(self.azul_spinBox, 8, 1, 1, 1)

        self.FINAL_pushButton = QPushButton(self.groupBox)
        self.FINAL_pushButton.setObjectName(u"FINAL_pushButton")

        self.gridLayout_2.addWidget(self.FINAL_pushButton, 9, 0, 1, 2)

        self.inicio_pushButton = QPushButton(self.groupBox)
        self.inicio_pushButton.setObjectName(u"inicio_pushButton")

        self.gridLayout_2.addWidget(self.inicio_pushButton, 10, 0, 1, 2)

        self.mostrar_pushButton = QPushButton(self.groupBox)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_2.addWidget(self.mostrar_pushButton, 11, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tap)
        self.salida.setObjectName(u"salida")

        self.gridLayout.addWidget(self.salida, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tap, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget = QTableWidget(self.tab_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 3)

        self.Buscar_lineEdit = QLineEdit(self.tab_2)
        self.Buscar_lineEdit.setObjectName(u"Buscar_lineEdit")

        self.gridLayout_3.addWidget(self.Buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_3.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_3.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 611, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"PARTICULAS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ORIGEN X", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ORIGEN Y", None))
        self.x_label.setText(QCoreApplication.translate("MainWindow", u"DESTINO X", None))
        self.y_label.setText(QCoreApplication.translate("MainWindow", u"DESTINO Y", None))
        self.velocidad_label.setText(QCoreApplication.translate("MainWindow", u"VELOCIDAD", None))
        self.rojo_label.setText(QCoreApplication.translate("MainWindow", u"ROJO", None))
        self.verde_label.setText(QCoreApplication.translate("MainWindow", u"VERDE", None))
        self.azul_label.setText(QCoreApplication.translate("MainWindow", u"AZUL", None))
        self.FINAL_pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR AL FINAL", None))
        self.inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR AL INICIO", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"MOSTRAR", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tap), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.Buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

