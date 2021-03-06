import sqlite3

from PyQt5 import QtWidgets, QtCore

from Registrazione.view.vista_registrazione import Ui_NewUser


class Newuser(QtWidgets.QWidget, Ui_NewUser):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn_Back.clicked.connect(self.back_handler)
        self.btn_submit.clicked.connect(self.btn_submit_handler)


    """ messaggio pop up per l'aggiunta al database """

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    """ funzione per richiamare la funzione del database """

    def btn_submit_handler(self):
        self.create_db_newuser()

    """ funzione per tornare alla schermata di login """

    def back_handler(self):
        self.switch_window.emit()

    """ funzione di creazione di un'account """

    def create_db_newuser(self):
        txt_firstname_v = self.txt_firstname.text()
        txt_lastname_v = self.txt_lastname.text()
        txt_phone_v = self.txt_phone.text()
        txt_tipo_v = self.txt_tipo.text()
        txt_username_v = self.txt_username.text()
        txt_password_v = self.lineEdit.text()

        bol = self.confronta_stringhe(txt_tipo_v, txt_firstname_v, txt_lastname_v, txt_phone_v, txt_username_v,
                                      txt_password_v)

        if self.bool_account_esistente(txt_username_v, txt_password_v) is True:
            if bol is True:

                conn = sqlite3.connect('Data/Database/Data.db')
                cursor = conn.cursor()

                cursor.execute("""
                                    CREATE TABLE IF NOT EXISTS credentials 
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                    fname TEXT, 
                                    lname TEXT, 
                                    Phone TEXT, 
                                    tipo TEXT,
                                    username TEXT, 
                                    password TEXT)""")

                cursor.execute(""" INSERT INTO credentials 
                                    (fname,
                                    lname,
                                    Phone,
                                    tipo,
                                    username, 
                                    password)
    
                                VALUES 
                                (?,?,?,?,?,?)
                                """,
                               (txt_firstname_v, txt_lastname_v, txt_phone_v, txt_tipo_v, txt_username_v, txt_password_v))

                conn.commit()
                cursor.close()
                conn.close()
                self.pop_message(text="Ora sei un membro di PyLemon!")

            else:
                self.pop_message(text="Campi mancanti o incorretti.")
        else:
            self.pop_message(text="Credenziali account esistenti")

    """ Funzione per la verifica del corretto inserimento dei valori per la creazione di un nuovo account"""

    def confronta_stringhe(self, tipo, nome, cognome, telefono, username, password):
        if len(password) > 1:
            if len(username) > 1:
                if len(telefono) > 9:
                    if tipo == 'Ascoltatore' or tipo == 'ascoltatore' or tipo == 'Artista' or tipo == 'artista' or tipo == 'Etichetta' or tipo == 'etichetta':
                        if len(cognome) > 1:
                            if len(nome) > 1:
                                return True


    '''---Funzione per il controllo dell'esistenza di un account con le stesse credenziali di accesso---'''
    def bool_account_esistente(self, nome, password):
        username = nome
        password = password
        conn = sqlite3.connect('Data/Database/Data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username,password FROM credentials")
        val = cursor.fetchall()
        if len(val) >= 1:

            for x in val:
                if username in x[0] and password in x[1]:
                    return False
                else:
                    pass
            return True
        else:
            return True