

from PyQt5 import QtCore, QtWidgets


'''-------------------Classe view edit ascoltatore--------------------'''

class edit_ascoltatore(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(281, 282)
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")


        '''-------------Titolo finestra------------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 150, 41))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")



        '''-------------Sottotitolo------------'''

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 220, 16))
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_2.setObjectName("label_2")


        '''-------------Bottone artista----------'''

        self.btn_Artista = QtWidgets.QPushButton(Form)
        self.btn_Artista.setGeometry(QtCore.QRect(80, 100, 121, 31))
        self.btn_Artista.setMouseTracking(True)
        self.btn_Artista.setTabletTracking(True)
        self.btn_Artista.setStyleSheet("*{background-color: rgb(207, 207, 207);\n"
                                       "color: rgb(0, 0, 0);\n"
                                       "border-radius: 10px;\n"
                                       "color: rgb(0, 0, 0);\n}"
                                       "*:hover{border: 5px solid rgb(221, 215, 25);\n}")
        self.btn_Artista.setObjectName("pushButton")


        '''-------------Bottone etichetta-------------'''

        self.btn_Etichetta = QtWidgets.QPushButton(Form)
        self.btn_Etichetta.setGeometry(QtCore.QRect(80, 150, 121, 31))
        self.btn_Etichetta.setMouseTracking(True)
        self.btn_Etichetta.setTabletTracking(True)
        self.btn_Etichetta.setStyleSheet("*{background-color: rgb(207, 207, 207);\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "border-radius: 10px;\n"
                                         "color: rgb(0, 0, 0);\n}"
                                         "*:hover{border: 5px solid rgb(221, 215, 25);\n}")
        self.btn_Etichetta.setObjectName("pushButton_2")


        '''------------Bottone indietro-------------'''

        self.btn_Back = QtWidgets.QPushButton(Form)
        self.btn_Back.setGeometry(QtCore.QRect(100, 220, 81, 21))
        self.btn_Back.setMouseTracking(True)
        self.btn_Back.setTabletTracking(True)
        self.btn_Back.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                       "border-radius: 10px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Back.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.label.setText(_translate("Form", "PyLemon"))
        self.label_2.setText(_translate("Form", "Scegli il tuo nuovo LemonAccount"))
        self.btn_Artista.setText(_translate("Form", "Artista"))
        self.btn_Etichetta.setText(_translate("Form", "Etichetta"))
        self.btn_Back.setText(_translate("Form", "Indietro"))
