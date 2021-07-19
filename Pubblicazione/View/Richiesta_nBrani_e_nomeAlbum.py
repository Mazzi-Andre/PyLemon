
from PyQt5 import QtCore, QtWidgets


'''-----------------Classe view richiesta numero di brani in album----------------'''

class caricamento_album(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 329)
        Form.setMinimumSize(QtCore.QSize(411, 329))
        Form.setMaximumSize(QtCore.QSize(411, 329))
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")


        '''-------------Titolo finestra-----------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(145, 20, 130, 41))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")


        '''-------------Sottotitolo--------------'''

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(142, 60, 131, 16))
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_2.setObjectName("label_2")


        '''-------------Nome album---------------'''

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 120, 101, 16))
        self.label_4.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_4.setObjectName("label_4")

        self.numero_brani = QtWidgets.QLineEdit(Form)
        self.numero_brani.setGeometry(QtCore.QRect(300, 210, 51, 21))
        self.numero_brani.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                          "color: rgb(55, 55, 55);\n"
                                          "border-radius: 5px;")
        self.numero_brani.setObjectName("txt_nome_album")




        '''--------------Numero di brani nell'album-----------'''

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 210, 231, 21))
        self.label_3.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_3.setObjectName("label_3")

        self.nome_album = QtWidgets.QLineEdit(Form)
        self.nome_album.setGeometry(QtCore.QRect(110, 140, 191, 31))
        self.nome_album.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                      "color: rgb(55, 55, 55);\n"
                                      "border-radius: 5px;")
        self.nome_album.setObjectName("txt_nBrani")


        '''--------------Bottone Ok-------------'''

        self.btn_ok = QtWidgets.QPushButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(230, 280, 71, 21))
        self.btn_ok.setMouseTracking(True)
        self.btn_ok.setTabletTracking(True)
        self.btn_ok.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                  "border-radius: 10px;\n"
                                  "color: 'white';}" +
                                  "*:hover{background: rgb(221, 215, 25);\n}")

        self.btn_ok.setObjectName("pushButton_2")


        '''--------------Bottone indietro------------'''

        self.btn_Back = QtWidgets.QPushButton(Form)
        self.btn_Back.setGeometry(QtCore.QRect(120, 280, 71, 21))
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
        self.label_3.setText(_translate("Form", "Inserisci il numero di brani dell\'album:"))
        self.btn_ok.setText(_translate("Form", "Ok"))
        self.label_4.setText(_translate("Form", "Nome album:"))
        self.label_2.setText(_translate("Form", "Pubblicazione album"))
        self.btn_Back.setText(_translate("Form", "Indietro"))
