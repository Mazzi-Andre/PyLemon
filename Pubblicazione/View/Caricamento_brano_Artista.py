
from PyQt5 import QtCore, QtWidgets


'''---------------Classe view caricamento brano artista-------------'''

class Caricamento_brano_artista(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(469, 367)
        Form.setMinimumSize(QtCore.QSize(469, 367))
        Form.setMaximumSize(QtCore.QSize(469, 367))
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")


        '''--------------Titolo finestra-------------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 40, 170, 55))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 25pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")


        '''---------------Sottotitolo---------------'''

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(175, 90, 131, 16))
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_2.setObjectName("label_2")


        '''---------------Nome brano----------------'''

        self.txt_nome_brano = QtWidgets.QLineEdit(Form)
        self.txt_nome_brano.setGeometry(QtCore.QRect(140, 220, 181, 31))
        self.txt_nome_brano.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                          "color: rgb(55, 55, 55);\n"
                                          "border-radius: 5px;")
        self.txt_nome_brano.setObjectName("txt_nome_brano")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 200, 101, 16))
        self.label_3.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_3.setObjectName("label_3")


        '''----------------Bottone scegli file--------------'''

        self.btn_scegli_file = QtWidgets.QPushButton(Form)
        self.btn_scegli_file.setGeometry(QtCore.QRect(180, 140, 101, 31))
        self.btn_scegli_file.setMouseTracking(True)
        self.btn_scegli_file.setTabletTracking(True)
        self.btn_scegli_file.setStyleSheet("*{background-color: rgb(207, 207, 207);\n"
                                           "color: rgb(0, 0, 0);\n"
                                           "border-radius: 10px;\n"
                                           "color: rgb(0, 0, 0);\n}"
                                           "*:hover{border: 5px solid rgb(221, 215, 25);\n}")
        self.btn_scegli_file.setObjectName("btn_scegli_file")


        '''----------------Bottone pubblica-----------------'''

        self.btn_pubblica = QtWidgets.QPushButton(Form)
        self.btn_pubblica.setGeometry(QtCore.QRect(250, 310, 81, 21))
        self.btn_pubblica.setMouseTracking(True)
        self.btn_pubblica.setTabletTracking(True)
        self.btn_pubblica.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                        "border-radius: 10px;\n"
                                        "color: 'white';}" +
                                        "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_pubblica.setObjectName("btn_pubblica")


        '''----------------Bottone indietro------------------'''

        self.btn_Back = QtWidgets.QPushButton(Form)
        self.btn_Back.setGeometry(QtCore.QRect(130, 310, 81, 21))
        self.btn_Back.setMouseTracking(True)
        self.btn_Back.setTabletTracking(True)
        self.btn_Back.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                    "border-radius: 10px;\n"
                                    "color: 'white';}" +
                                    "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Back.setObjectName("btn_back")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.label.setText(_translate("Form", "PyLemon"))
        self.label_2.setText(_translate("Form", "Pubblicazione brano"))
        self.label_3.setText(_translate("Form", "Nome brano:"))

        self.btn_scegli_file.setText(_translate("Form", "Scegli file"))
        self.btn_pubblica.setText(_translate("Form", "Pubblica"))
        self.btn_Back.setText(_translate("Form", "Indietro"))
