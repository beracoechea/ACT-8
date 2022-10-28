
from PySide2.QtWidgets import QMainWindow , QFileDialog, QMessageBox , QTableWidgetItem
from PySide2.QtCore import Slot
from ui_mainwindow  import Ui_MainWindow
from particulas import Particula
from Lista import Lista


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.lista = Lista()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.inicio_pushButton.clicked.connect(self.click_agregar)
        self.ui.FINAL_pushButton.clicked.connect(self.click_final)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

    @Slot()
    def buscar_id(self):
        id = self.ui.Buscar_lineEdit.text()
        encontrado = False
        for Particula in self.lista:
            if id == (str(Particula.id)):

                self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(1)

                id_widget = QTableWidgetItem (str(Particula.id))
                origen_x_widget = QTableWidgetItem (str(Particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(Particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(Particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(Particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
                red_widget = QTableWidgetItem(str(Particula.red))
                blue_widget = QTableWidgetItem(str(Particula.blue))
                green_widget = QTableWidgetItem(str(Particula.green))
                distancia_widget = QTableWidgetItem(str(Particula.distancia))

                self.ui.tableWidget.setItem(0,0,id_widget)
                self.ui.tableWidget.setItem(0,1,origen_x_widget)
                self.ui.tableWidget.setItem(0,2,origen_y_widget)
                self.ui.tableWidget.setItem(0,3,destino_x_widget)
                self.ui.tableWidget.setItem(0,4,destino_y_widget)
                self.ui.tableWidget.setItem(0,5,velocidad_widget)
                self.ui.tableWidget.setItem(0,6,red_widget)
                self.ui.tableWidget.setItem(0,7,blue_widget)
                self.ui.tableWidget.setItem(0,8,green_widget)
                self.ui.tableWidget.setItem(0,9,distancia_widget)

                encontrado = True
                return 
        if not encontrado:
               QMessageBox.warning(
               self,
               "ATENCION",
               f'LA PARTICULA"{id}"NO FUE ENCONTADA'
               )



    @Slot()
    def mostrar_tabla(self):
        self.ui.tableWidget.setColumnCount(10)
        headers = ["id","origen_x", "origen_y","destino_x","destino_y","velocidad","red","green","blue","distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

        self.ui.tableWidget.setRowCount(len(self.lista))

        row = 0
        for Particula in self.lista:
            id_widget = QTableWidgetItem (str(Particula.id))
            origen_x_widget = QTableWidgetItem (str(Particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(Particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(Particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(Particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(Particula.velocidad))
            red_widget = QTableWidgetItem(str(Particula.red))
            blue_widget = QTableWidgetItem(str(Particula.blue))
            green_widget = QTableWidgetItem(str(Particula.green))
            distancia_widget = QTableWidgetItem(str(Particula.distancia))

            self.ui.tableWidget.setItem(row,0,id_widget)
            self.ui.tableWidget.setItem(row,1,origen_x_widget)
            self.ui.tableWidget.setItem(row,2,origen_y_widget)
            self.ui.tableWidget.setItem(row,3,destino_x_widget)
            self.ui.tableWidget.setItem(row,4,destino_y_widget)
            self.ui.tableWidget.setItem(row,5,velocidad_widget)
            self.ui.tableWidget.setItem(row,6,red_widget)
            self.ui.tableWidget.setItem(row,7,blue_widget)
            self.ui.tableWidget.setItem(row,8,green_widget)
            self.ui.tableWidget.setItem(row,9,distancia_widget)

            row += 1
            

    @Slot()
    def action_abrir_archivo(self):
      
       ubicacion = QFileDialog.getOpenFileName(
        self,
        'Abrir archivo',
        '.',
        'JSON (*.json)'
       )[0]
       if self.lista.abrir(ubicacion):
          QMessageBox.information(
            self,
            "EXITO",
            "SE ABRIO CON EXITO EL ARCHIVO" + ubicacion
        )
       else:
            QMessageBox.critical(
                self,
                "ERORR",
                "ERROR AL ABRIR EL ARCHIVO" + ubicacion
        )
       
        
        

    @Slot()
    def action_guardar_archivo(self):
      ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar',
            '.',
            'JSON (*.json)'
        )[0]
      print(ubicacion)
      if self.lista.guardar(ubicacion):
        QMessageBox.information(
            self,
            "EXITO",
            "SE PUDO CREAR EL ARCHIVO" + ubicacion,
        )

      else :
        QMessageBox.critical(
            self,
            "ERROR",
            "NO SE PUDO CREAR EL ARCHIVO" + ubicacion
        )


    @Slot()
    def click_mostrar(self):
        self.ui.salida.insertPlainText(str(self.lista))


    @Slot()
    def click_agregar(self):
        id = self.ui.ID_spinBox.value()
        origen_x = self.ui.ORIGEN_X_spinBox.value()
        origen_y = self.ui.ORIGEN_Y_spinBox.value()

        destino_x = self.ui.x_spinBox.value()
        destino_y = self.ui.y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        rojo = self.ui.rojo_spinBox.value()
        verde = self.ui.verde_spinBox.value()
        azul = self.ui.azul_spinBox.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.agregar_inicio(particula)

    
    @Slot()
    def click_final(self):
        id = self.ui.ID_spinBox.value()
        origen_x = self.ui.ORIGEN_X_spinBox.value()
        origen_y = self.ui.ORIGEN_Y_spinBox.value()

        destino_x = self.ui.x_spinBox.value()
        destino_y = self.ui.y_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        rojo = self.ui.rojo_spinBox.value()
        verde = self.ui.verde_spinBox.value()
        azul = self.ui.azul_spinBox.value()

        particula = Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,rojo,verde,azul)
        self.lista.agregar_final(particula)

    

        
