
from PyQt5 import QtCore, QtWidgets


'''--------------Classe view prima finestra di pubblicazione--------------'''

class pubblicazione_inizio(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 330)
        Form.setMinimumSize(QtCore.QSize(430, 330))
        Form.setMaximumSize(QtCore.QSize(430, 330))
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")


        '''-------------Titolo finestra------------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(155, 50, 130, 34))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 30pt \".SF NS Text\";")
        self.label.setObjectName("label")


        '''-------------Sottotitolo--------------'''

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(172, 90, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);\n")



        '''--------------Bottone brano------------'''

        self.btn_brano = QtWidgets.QPushButton(Form)
        self.btn_brano.setGeometry(QtCore.QRect(140, 140, 151, 31))
        self.btn_brano.setMouseTracking(True)
        self.btn_brano.setTabletTracking(True)
        self.btn_brano.setStyleSheet("*{border: 1px solid rgb(221, 215, 25);"
                                       "border-radius: 10px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_brano.setObjectName("pushButton")


        '''---------------Bottone album----------------'''

        self.btn_album = QtWidgets.QPushButton(Form)
        self.btn_album.setGeometry(QtCore.QRect(140, 200, 151, 31))
        self.btn_album.setMouseTracking(True)
        self.btn_album.setTabletTracking(True)
        self.btn_album.setStyleSheet("*{border: 1px solid rgb(221, 215, 25);"
                                       "border-radius: 10px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_album.setObjectName("pushButton_2")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.btn_brano.setText(_translate("Form", "Brano"))
        self.btn_album.setText(_translate("Form", "Album"))
        self.label.setText(_translate("Form", "PyLemon"))
        self.label_2.setText(_translate("Form", "Pubblicazione"))

