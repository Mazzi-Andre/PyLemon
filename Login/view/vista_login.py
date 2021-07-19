from PyQt5 import QtWidgets, QtCore



class vista_login(object):

    """ Classe della view Login  """

    def setupUi(self, Outsecure):
        Outsecure.setObjectName("Outsecure")
        Outsecure.resize(530, 340)
        Outsecure.setMinimumSize(QtCore.QSize(530, 340))
        Outsecure.setMaximumSize(QtCore.QSize(530, 340))
        Outsecure.setMouseTracking(True)
        Outsecure.setStyleSheet(
            "border-color: rgb(255, 42, 245);\n"
            "border-color: rgb(20, 255, 55);\n"
            "background-color: rgb(40, 39, 39);\n"
            "")

        """----------Label del titolo----------"""

        self.l_title = QtWidgets.QLabel(Outsecure)
        self.l_title.setGeometry(QtCore.QRect(150, 20, 300, 71))
        self.l_title.setStyleSheet("color: rgb(221, 215, 25);\n"
                                   "font: 30pt \".SF NS Text\";")
        self.l_title.setObjectName("l_title")

        """----------pulsante del submit----------"""

        self.btn_Submit = QtWidgets.QPushButton(Outsecure)
        self.btn_Submit.setGeometry(QtCore.QRect(180, 200, 161, 31))
        self.btn_Submit.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);\n"
                                       "border-radius: 10px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);}")
        self.btn_Submit.setObjectName("btn_Submit")

        """----------pulstante del nuovo utente----------"""

        self.btn_newuser = QtWidgets.QPushButton(Outsecure)
        self.btn_newuser.setGeometry(QtCore.QRect(180, 240, 161, 31))
        self.btn_newuser.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);\n"
                                       "border-radius: 10px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(221, 215, 25);}")
        self.btn_newuser.setObjectName("btn_newuser")

        """----------textline del nome utente----------"""

        self.txt_username = QtWidgets.QLineEdit(Outsecure)
        self.txt_username.setGeometry(QtCore.QRect(130, 100, 275, 31))
        self.txt_username.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "color: rgb(55, 55, 55);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n")
        self.txt_username.setObjectName("txt_username")

        """----------textline della password----------"""

        self.txt_password = QtWidgets.QLineEdit(Outsecure)
        self.txt_password.setGeometry(QtCore.QRect(130, 150, 271, 31))
        self.txt_password.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                        "color: rgb(55, 55, 55);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n")
        self.txt_password.setObjectName("txt_password")

        self.retranslateUi(Outsecure)
        QtCore.QMetaObject.connectSlotsByName(Outsecure)

    def retranslateUi(self, Outsecure):
        _translate = QtCore.QCoreApplication.translate
        Outsecure.setWindowTitle(_translate("Outsecure", ""))
        self.l_title.setText(_translate("Outsecure",
                                        "<html><head/><body><p><span style=\" font-size:30pt; font-weight:600; font-style:italic;\">PyLemon</span></p></body></html>"))

        self.btn_Submit.setText(_translate("Outsecure", "Accedi"))
        self.btn_newuser.setText(_translate("Outsecure", "Nuovo utente"))
        self.txt_username.setPlaceholderText(_translate("Outsecure", "Username"))
        self.txt_password.setPlaceholderText(_translate("Outsecure", "Password"))