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
        self.btn_brano = QtWidgets.QPushButton(Form)
        self.btn_brano.setGeometry(QtCore.QRect(140, 140, 151, 31))
        self.btn_brano.setMouseTracking(True)
        self.btn_brano.setTabletTracking(True)
        self.btn_brano.setStyleSheet("*{border: 1px solid rgb(221, 215, 25);"
                                       "border-radius: 10px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_brano.setObjectName("pushButton")
        self.btn_album = QtWidgets.QPushButton(Form)
        self.btn_album.setGeometry(QtCore.QRect(140, 200, 151, 31))
        self.btn_album.setMouseTracking(True)
        self.btn_album.setTabletTracking(True)
        self.btn_album.setStyleSheet("*{border: 1px solid rgb(221, 215, 25);"
                                       "border-radius: 10px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_album.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(155, 50, 130, 34))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
"font: 30pt \".SF NS Text\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(172, 90, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);\n")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.btn_brano.setText(_translate("Form", "Brano"))
        self.btn_album.setText(_translate("Form", "Album"))
        self.label.setText(_translate("Form", "PyLemon"))
        self.label_2.setText(_translate("Form", "Pubblicazione"))


'''app = QApplication([])
window = QWidget()
form = pubblicazione_inizio()
form.setupUi(window)
window.show()
app.exec()'''