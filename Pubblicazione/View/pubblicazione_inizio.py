# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


class pubblicazione_inizio(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 330)
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 140, 151, 31))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setTabletTracking(True)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 200, 151, 31))
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setTabletTracking(True)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(155, 50, 121, 31))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
"font: 30pt \".SF NS Text\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 90, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);\n")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Brano"))
        self.pushButton_2.setText(_translate("Form", "Album"))
        self.label.setText(_translate("Form", "PySound"))
        self.label_2.setText(_translate("Form", "Pubblicazione"))


app = QApplication([])
window = QWidget()
form = pubblicazione_inizio()
form.setupUi(window)
window.show()
app.exec()