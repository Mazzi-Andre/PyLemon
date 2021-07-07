import sqlite3

from PyQt5 import QtWidgets, QtCore

from Login.view.vista_login import Ui_Outsecure
from Data_Utente.control.Data_control import DataPick


class Login(QtWidgets.QWidget, Ui_Outsecure, DataPick):
    switch_window = QtCore.pyqtSignal()
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3= QtCore.pyqtSignal()


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

    ''' da sistemare che non funziona '''
    def loading(self):
        username = self.txt_username.text()
        password = self.txt_password.text()
        self.pick.put_data(username, password)

    def bool_check_username(self):
        if len(self.txt_password.text()) <= 1:
            self.pop_message(text='Inserire Username e Password validi')
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
                        self.loading()
                        #self.credenziali= x
                        #self.pick.put_data(self.credenziali[0], self.credenziali[1])
                        return True
                    else:
                        pass
            else:
                self.pop_message(text="Utente non trovato ")
                return False

    def btn_submit_handler(self):
        val = self.bool_check_username()
        costante = 0
        if (val):
            self.pop_message(text="Benvenuto ")

            #self.pick.put_data(self.credenziali[0], self.credenziali[1])
            self.pop_message(text=self.pick.return_credenziali()) #posizione 4 è artista
            costante = self.pick.controlla_login()
            self.pop_message(text=costante)
            if costante == 1:
                self.switch_window1.emit()
            if costante == 2:
                self.switch_window2.emit()
            if costante == 3:
                self.switch_window3.emit()


        else:
            self.pop_message("Username o password invalidi ")

    def btn_newuser_handler(self):
        self.switch_window.emit()

    '''def return_credenziali(self):
        return self.credenziali'''