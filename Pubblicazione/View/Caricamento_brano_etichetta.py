# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Caricamento_brano_etichetta.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class Caricamento_brano_etichetta(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(461, 342)
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 70, 131, 16))
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(172, 30, 131, 41))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
"font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")
        self.btn_Scegli_file = QtWidgets.QPushButton(Form)
        self.btn_Scegli_file.setGeometry(QtCore.QRect(180, 110, 101, 31))
        self.btn_Scegli_file.setMouseTracking(True)
        self.btn_Scegli_file.setTabletTracking(True)
        self.btn_Scegli_file.setStyleSheet("*{border: 1px solid rgb(221, 215, 25);"
                                            "border-radius: 10px;\n"
                                            "color: 'white';}" +
                                            "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Scegli_file.setObjectName("pushButton")
        self.btn_Pubblica = QtWidgets.QPushButton(Form)
        self.btn_Pubblica.setGeometry(QtCore.QRect(190, 280, 81, 21))
        self.btn_Pubblica.setMouseTracking(True)
        self.btn_Pubblica.setTabletTracking(True)
        self.btn_Pubblica.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.btn_Pubblica.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 190, 181, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 101, 16))
        self.label_3.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 190, 181, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 170, 101, 16))
        self.label_4.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Pubblicazione brano"))
        self.label.setText(_translate("Form", "PySound"))
        self.btn_Scegli_file.setText(_translate("Form", "Scegli file"))
        self.btn_Pubblica.setText(_translate("Form", "Pubblica"))
        self.label_3.setText(_translate("Form", "Nome brano:"))
        self.label_4.setText(_translate("Form", "Nome artista:"))

'''app = QApplication([])
window = QWidget()
form = Caricamento_brano_etichetta()
form.setupUi(window)
window.show()
app.exec()'''