import sqlite3

from PyQt5 import QtWidgets, QtCore

from Login.view.vista_login import Ui_Outsecure
from Data_Utente.control.Data_control import DataPick

''' Classe controller utilizzata per la verifica al login del programma '''

class Login(QtWidgets.QWidget, Ui_Outsecure):
    switch_window = QtCore.pyqtSignal()
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.pick = DataPick()

        self.btn_newuser.clicked.connect(self.btn_newuser_handler)
        self.btn_Submit.clicked.connect(self.btn_submit_handler)

    ''' Messaggio pop-up a comparsa'''

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    ''' Funzione di salvataggio nome e password all'interno di un pickle '''

    def loading(self):
        username = self.txt_username.text()
        password = self.txt_password.text()
        self.pick.put_data(username, password)

    ''' Funzione booleana per la verifica di esistenza dell'account scelto tramite 
        l'inserimento di nome e password '''

    def bool_check_username(self):
        if len(self.txt_password.text()) <= 1:
            self.pop_message(text='Inserire Username e Password validi')
        else:
            username = self.txt_username.text()
            password = self.txt_password.text()
            conn = sqlite3.connect('Data\Database\Data.db')
            cursor = conn.cursor()
            cursor.execute("SELECT username,password FROM credentials")
            val = cursor.fetchall()
            if len(val) >= 1:

                for x in val:
                    if username in x[0] and password in x[1]:
                        self.loading()
                        return True
                    else:
                        pass
            else:
                self.pop_message(text="Utente non trovato ")
                return False

    ''' Funzione utilizzata per l'apertura della home appartenente al tipo di 
        account, che utilizza la funzione "bool_check_username" per la verifica
        dell'esistenza delle credenzialòi '''

    def btn_submit_handler(self):
        val = self.bool_check_username()
        if (val):
            self.pop_message(text="Benvenuto")
            costante = self.pick.controlla_login()

            if costante == 1:
                self.switch_window1.emit()
            if costante == 2:
                self.switch_window2.emit()
            if costante == 3:
                self.switch_window3.emit()


        else:
            self.pop_message("Username o password invalidi ")

    ''' Funzione per l'apertura della finestra del nuovo utente '''

    def btn_newuser_handler(self):
        self.switch_window.emit()
