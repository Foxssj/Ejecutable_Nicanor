# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widgets-2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(556, 388)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ruedita = QtWidgets.QDial(Form)
        self.ruedita.setGeometry(QtCore.QRect(380, 40, 91, 81))
        self.ruedita.setObjectName("ruedita")
        self.cantidadGirada = QtWidgets.QProgressBar(Form)
        self.cantidadGirada.setGeometry(QtCore.QRect(370, 140, 118, 23))
        self.cantidadGirada.setProperty("value", 0)
        self.cantidadGirada.setTextVisible(False)
        self.cantidadGirada.setObjectName("cantidadGirada")
        self.dia = QtWidgets.QLabel(Form)
        self.dia.setGeometry(QtCore.QRect(40, 70, 111, 16))
        self.dia.setObjectName("dia")
        self.diaSelec = QtWidgets.QComboBox(Form)
        self.diaSelec.setGeometry(QtCore.QRect(160, 70, 73, 22))
        self.diaSelec.setObjectName("diaSelec")
        self.diaSelec.addItem("")
        self.diaSelec.addItem("")
        self.diaSelec.addItem("")
        self.diaSelec.addItem("")
        self.diaSelec.addItem("")
        self.diaSelec.addItem("")
        self.diaSelec.addItem("")
        self.labelDia = QtWidgets.QLabel(Form)
        self.labelDia.setGeometry(QtCore.QRect(254, 70, 85, 20))
        self.labelDia.setStyleSheet("border: 1px solid black")
        self.labelDia.setObjectName("labelDia")
        self.hora = QtWidgets.QTimeEdit(Form)
        self.hora.setGeometry(QtCore.QRect(40, 120, 118, 23))
        self.hora.setObjectName("hora")
        self.fecha = QtWidgets.QDateEdit(Form)
        self.fecha.setGeometry(QtCore.QRect(40, 170, 90, 22))
        self.fecha.setObjectName("fecha")
        self.labelHora = QtWidgets.QLabel(Form)
        self.labelHora.setGeometry(QtCore.QRect(170, 120, 120, 20))
        self.labelHora.setStyleSheet("border: 1px solid black")
        self.labelHora.setObjectName("labelHora")
        self.labelFecha = QtWidgets.QLabel(Form)
        self.labelFecha.setGeometry(QtCore.QRect(140, 170, 157, 20))
        self.labelFecha.setStyleSheet("border: 1px solid black")
        self.labelFecha.setObjectName("labelFecha")
        self.horizontalScrollBar = QtWidgets.QScrollBar(Form)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(50, 250, 160, 16))
        self.horizontalScrollBar.setMinimum(-100)
        self.horizontalScrollBar.setMaximum(100)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(250, 230, 91, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 300, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(250, 290, 91, 41))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.verticalSlider_2 = QtWidgets.QSlider(Form)
        self.verticalSlider_2.setGeometry(QtCore.QRect(490, 170, 22, 160))
        self.verticalSlider_2.setMinimum(-273)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(Form)
        self.verticalScrollBar.setGeometry(QtCore.QRect(380, 170, 16, 160))
        self.verticalScrollBar.setMaximum(99)
        self.verticalScrollBar.setSliderPosition(99)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setInvertedAppearance(True)
        self.verticalScrollBar.setInvertedControls(False)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 210, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(420, 260, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(300, 120, 61, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("gokusad.ico"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.ruedita.valueChanged["int"].connect(self.cantidadGirada.setValue)  # type: ignore
        self.diaSelec.currentTextChanged["QString"].connect(self.mostrarDia)  # type: ignore
        self.horizontalScrollBar.sliderMoved["int"].connect(self.lcdNumber.display)  # type: ignore
        self.horizontalSlider.sliderMoved["int"].connect(self.lcdNumber_2.display)  # type: ignore
        self.verticalScrollBar.sliderMoved["int"].connect(self.label.setNum)  # type: ignore
        self.verticalSlider_2.sliderMoved["int"].connect(self.label_2.setNum)  # type: ignore
        self.hora.timeChanged["QTime"].connect(self.mostrarHora)  # type: ignore
        self.fecha.dateChanged["QDate"].connect(self.mostrarFecha)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def mostrarDia(self):
        dia = self.diaSelec.itemText(self.diaSelec.currentIndex())
        self.labelDia.setText("es: " + dia)

    def mostrarHora(self):
        horita = self.hora.time().toString("HH:mm")
        self.labelHora.setText("Que hora es? " + horita)

    def mostrarFecha(self):
        fechita = self.fecha.date().toString("dd-MM-yyyy")
        self.labelFecha.setText("Que fecha es? " + fechita)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.dia.setText(_translate("Form", "Dia de la semana:"))
        self.diaSelec.setItemText(0, _translate("Form", "Lunes"))
        self.diaSelec.setItemText(1, _translate("Form", "Martes"))
        self.diaSelec.setItemText(2, _translate("Form", "Miercoles"))
        self.diaSelec.setItemText(3, _translate("Form", "Jueves"))
        self.diaSelec.setItemText(4, _translate("Form", "Viernes"))
        self.diaSelec.setItemText(5, _translate("Form", "Sabado"))
        self.diaSelec.setItemText(6, _translate("Form", "Domingo"))
        self.labelDia.setText(_translate("Form", "es: "))
        self.labelHora.setText(_translate("Form", "Que hora es?"))
        self.labelFecha.setText(_translate("Form", "Que fecha es?"))
        self.label.setText(_translate("Form", "Izquierda"))
        self.label_2.setText(_translate("Form", "Derecha"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
