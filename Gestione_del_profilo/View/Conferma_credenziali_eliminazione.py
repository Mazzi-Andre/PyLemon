
from PyQt5 import QtCore, QtWidgets


'''--------------Classe view conferma credenziali-------------'''

class conferma_credenziali(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(322, 311)
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")


        '''------------Titolo finestra-------------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 30, 130, 41))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")


        '''-----------Sottotitolo-----------'''

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(47, 70, 240, 20))
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_2.setObjectName("label_2")


        '''------------Username-------------'''

        self.label_Username = QtWidgets.QLabel(Form)
        self.label_Username.setGeometry(QtCore.QRect(50, 120, 81, 20))
        self.label_Username.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_Username.setObjectName("label_3")

        self.txt_username = QtWidgets.QLineEdit(Form)
        self.txt_username.setGeometry(QtCore.QRect(50, 140, 221, 31))
        self.txt_username.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "color: rgb(55, 55, 55);\n"
                                        "border-style:outset;\n"
                                        "border-radius:3px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")


        '''-------------Password-------------'''

        self.label_Password = QtWidgets.QLabel(Form)
        self.label_Password.setGeometry(QtCore.QRect(50, 180, 81, 20))
        self.label_Password.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_Password.setObjectName("label_4")

        self.txt_password = QtWidgets.QLineEdit(Form)
        self.txt_password.setGeometry(QtCore.QRect(50, 200, 221, 31))
        self.txt_password.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "color: rgb(55, 55, 55);\n"
                                        "border-style:outset;\n"
                                        "border-radius:3px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_password.setObjectName("txt_password")


        '''--------------Bottone indietro-------------'''

        self.btn_Back = QtWidgets.QPushButton(Form)
        self.btn_Back.setGeometry(QtCore.QRect(70, 260, 81, 21))
        self.btn_Back.setMouseTracking(True)
        self.btn_Back.setTabletTracking(True)
        self.btn_Back.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                    "border-radius: 10px;\n"
                                    "color: 'white';}" +
                                    "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Back.setObjectName("pushButton_3")


        '''---------------Bottone Ok-------------'''

        self.btn_Ok = QtWidgets.QPushButton(Form)
        self.btn_Ok.setGeometry(QtCore.QRect(170, 260, 81, 21))
        self.btn_Ok.setMouseTracking(True)
        self.btn_Ok.setTabletTracking(True)
        self.btn_Ok.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                  "border-radius: 10px;\n"
                                  "color: 'white';}" +
                                  "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Ok.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.label.setText(_translate("Form", "PyLemon"))
        self.label_2.setText(_translate("Form", "Per confermare inserire le credenziali"))
        self.label_Username.setText(_translate("Form", "Username:"))
        self.label_Password.setText(_translate("Form", "Password:"))
        self.btn_Back.setText(_translate("Form", "Indietro"))
        self.btn_Ok.setText(_translate("Form", "Ok"))

        self.txt_username.setPlaceholderText(_translate("Form", ""))
        self.txt_password.setPlaceholderText(_translate("Form", ""))

