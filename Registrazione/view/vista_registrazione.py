from PyQt5 import QtWidgets, QtCore


class Ui_NewUser(object):
    """
    NEW USERS
    """

    def setupUi(self, NewUser):
        NewUser.setObjectName("NewUser")
        NewUser.resize(550,410)
        NewUser.setMinimumSize(QtCore.QSize(550, 410))
        NewUser.setMaximumSize(QtCore.QSize(550, 410))
        NewUser.setStyleSheet("background-color: rgb(40,39,39);")

        '''--------------Titolo finestra-------------'''
        self.l_newuser = QtWidgets.QLabel(NewUser)
        self.l_newuser.setGeometry(QtCore.QRect(160, 10, 220, 35))
        self.l_newuser.setStyleSheet(
                                     "color: rgb(221, 215, 25);\n"
                                     "")
        self.l_newuser.setAlignment(QtCore.Qt.AlignCenter)
        self.l_newuser.setObjectName("l_newuser")

        '''--------------Box nome utente-------------'''
        self.txt_firstname = QtWidgets.QLineEdit(NewUser)
        self.txt_firstname.setEnabled(True)
        self.txt_firstname.setGeometry(QtCore.QRect(30, 80, 230, 41))
        self.txt_firstname.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "color: rgb(55, 55, 55);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_firstname.setText("")
        self.txt_firstname.setObjectName("txt_firstname")

        '''--------------Box cognome utente-------------'''
        self.txt_lastname = QtWidgets.QLineEdit(NewUser)
        self.txt_lastname.setGeometry(QtCore.QRect(290, 80, 230, 41))
        self.txt_lastname.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "color: rgb(55, 55, 55);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_lastname.setObjectName("txt_lastname")

        '''--------------Box telefono utente-------------'''
        self.txt_phone = QtWidgets.QLineEdit(NewUser)
        self.txt_phone.setGeometry(QtCore.QRect(30, 140, 230, 41))
        self.txt_phone.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "color: rgb(55, 55, 55);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_phone.setObjectName("txt_phone")

        '''--------------Box tipologia utente-------------'''
        self.txt_tipo = QtWidgets.QLineEdit(NewUser)
        self.txt_tipo.setGeometry(QtCore.QRect(290, 140, 230, 41))
        self.txt_tipo.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "color: rgb(55, 55, 55);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_tipo.setObjectName("txt_email")

        '''--------------Box username utente-------------'''
        self.txt_username = QtWidgets.QLineEdit(NewUser)
        self.txt_username.setGeometry(QtCore.QRect(30, 200, 230, 41))
        self.txt_username.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "color: rgb(55, 55, 55);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")

        '''--------------Box password utente-------------'''
        self.lineEdit = QtWidgets.QLineEdit(NewUser)
        self.lineEdit.setGeometry(QtCore.QRect(290, 200, 230, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "color: rgb(55, 55, 55);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")

        '''--------------Pulsante submit-------------'''
        self.btn_submit = QtWidgets.QPushButton(NewUser)
        self.btn_submit.setGeometry(QtCore.QRect(190, 270, 159, 31))
        self.btn_submit.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);\n"
                                       "border-radius: 10px;\n"
                                       "font: 14pt \"Arial\";"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);}")
        self.btn_submit.setObjectName("btn_submit")

        '''--------------Messaggio attenzione-------------'''
        self.attenzione = QtWidgets.QLabel(NewUser)
        self.attenzione.setGeometry(QtCore.QRect(10, 360, 531, 41))
        self.attenzione.setStyleSheet("color: rgb(255, 255, 255);")
        self.attenzione.setObjectName("label")

        '''--------------Pulsante back-------------'''
        self.btn_Back = QtWidgets.QPushButton(NewUser)
        self.btn_Back.setGeometry(QtCore.QRect(190, 320, 159, 31))
        self.btn_Back.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);\n"
                                       "border-radius: 10px;\n"
                                       "font: 14pt \"Arial\";"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);}")
        self.btn_Back.setObjectName("Back")

        self.retranslateUi(NewUser)
        QtCore.QMetaObject.connectSlotsByName(NewUser)

    def retranslateUi(self, NewUser):
        _translate = QtCore.QCoreApplication.translate
        NewUser.setWindowTitle(_translate("NewUser", ""))
        self.l_newuser.setText(_translate("NewUser", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic;\">Nuovo utente</span></p></body></html>"))
        self.txt_firstname.setPlaceholderText(_translate("NewUser", "Nome"))
        self.txt_lastname.setPlaceholderText(_translate("NewUser", "Cognome"))
        self.txt_phone.setPlaceholderText(_translate("NewUser", "Telefono/cellulare"))
        self.txt_tipo.setPlaceholderText(_translate("NewUser", "Tipo abbonamento"))
        self.txt_username.setPlaceholderText(_translate("NewUser", "Username"))
        self.lineEdit.setPlaceholderText(_translate("NewUser", "Password"))
        self.btn_submit.setText(_translate("NewUser", "Conferma"))
        self.btn_Back.setText(_translate("NewUser", "Indietro"))
        self.attenzione.setText(_translate("NewUser",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:7pt;\">Attenzione: nel campo TYPE immettere il tipo di abbonamento(ascoltatore, artista, etichetta)</span></p></body></html>"))