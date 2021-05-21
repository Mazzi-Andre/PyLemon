import sqlite3

from PyQt5 import QtWidgets, QtCore

from Login.view.vista_login import Ui_Outsecure
from Data_Utente.control.Data_control import DataPick


class Login(QtWidgets.QWidget, Ui_Outsecure, DataPick):
    switch_window = QtCore.pyqtSignal()
    switch_window1 = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pick= DataPick()

        self.btn_newuser.clicked.connect(self.btn_newuser_handler)
        self.btn_Submit.clicked.connect(self.btn_submit_handler)

        self.credenziali=[]

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def bool_check_username(self):
        if len(self.txt_password.text()) <= 1:
            self.pop_message(text='Enter Valid Username and Password !')
        else:
            username = self.txt_username.text()
            password = self.txt_password.text()
            conn = sqlite3.connect('Data.db')
            cursor = conn.cursor()
            cursor.execute("SELECT username,password FROM credentials")
            val = cursor.fetchall()
            if len(val) >= 1:

                for x in val:
                    if username in x[0] and password in x[1]:
                        self.credenziali= x
                        return True
                    else:
                        pass
            else:
                self.pop_message(text="No users Found ")
                return False

    def btn_submit_handler(self):
        val = self.bool_check_username()

        if (val):
            self.pop_message(text="Welcome ")

            self.pick.put_data(self.credenziali[0], self.credenziali[1])
            self.pop_message(text=self.pick.return_credenziali())

            self.switch_window1.emit()

        else:
            self.pop_message("Invalid username or password ")

    def btn_newuser_handler(self):
        self.switch_window.emit()

    def return_credenziali(self):
        return self.credenziali