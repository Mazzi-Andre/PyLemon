from PyQt5 import QtCore, QtWidgets

from Gestione_del_profilo.Model.Gestione_profilo import DataPick

'''-------------------Classe view impostazioni--------------------'''

class impostazioni_ascoltatore(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(281, 311)
        Form.setMinimumSize(QtCore.QSize(281, 311))
        Form.setMaximumSize(QtCore.QSize(281, 311))
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")


        '''-------------Titolo finestra------------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(77, 30, 150, 41))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 20pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")


        '''---------------Sottotitolo----------------'''

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(105, 70, 90, 16))
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_2.setObjectName("label_2")


        '''----------------Tipo di account----------------'''

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 120, 250, 16))
        self.label_3.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_3.setObjectName("label_3")


        '''-----------------Bottone elimina account-------------------'''

        self.btn_EliminaAccount = QtWidgets.QPushButton(Form)
        self.btn_EliminaAccount.setGeometry(QtCore.QRect(70, 240, 150, 31))
        self.btn_EliminaAccount.setMouseTracking(True)
        self.btn_EliminaAccount.setTabletTracking(True)
        self.btn_EliminaAccount.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                              "border-radius: 10px;\n"
                                              "color: 'white';}" +
                                              "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_EliminaAccount.setObjectName("pushButton")


        '''-----------------Bottone edit account----------------'''

        self.btn_EditProfilo = QtWidgets.QPushButton(Form)
        self.btn_EditProfilo.setGeometry(QtCore.QRect(70, 190, 150, 31))
        self.btn_EditProfilo.setMouseTracking(True)
        self.btn_EditProfilo.setTabletTracking(True)
        self.btn_EditProfilo.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                           "border-radius: 10px;\n"
                                           "color: 'white';}" +
                                           "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_EditProfilo.setObjectName("pushButton_3")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.label.setText(_translate("Form", "PyLemon"))
        self.label_2.setText(_translate("Form", "Impostazioni"))
        self.label_3.setText(_translate("Form", "Tipo di LemonAccount: " + self.Dati()))

        self.btn_EliminaAccount.setText(_translate("Form", "Elimina LemonAccount"))
        self.btn_EditProfilo.setText(_translate("Form", "Edit LemonAccount"))



    def Dati(self):
        self.pick = DataPick()
        self.myData = self.pick.return_credenziali()
        self.tipo = self.myData[4]
        return self.tipo