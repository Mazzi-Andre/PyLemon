import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets


# ---------- We dont Touch --------------------
from Data_Utente.control.Data_control import DataPick
from Gestione_del_profilo.Controller.Controller_artista import controller_artista
from Gestione_del_profilo.Controller.Controller_ascoltatore import controller_ascoltatore
from Gestione_del_profilo.Controller.Controller_conferma_credenziali import controller_conferma_credenziali
from Gestione_del_profilo.Controller.Controller_conferma_edit import controller_conferma_edit
from Gestione_del_profilo.Controller.Controller_edit_artista import controller_edit_artista
from Gestione_del_profilo.Controller.Controller_edit_ascoltatore import controller_edit_ascoltatore
from Gestione_del_profilo.Controller.Controller_impostazioni import controller_impostazioni
from Gestione_del_profilo.Controller.controller_etichetta import controller_etichetta
from Login.controller.controller_login import Login
from Pubblicazione.Controller.Controller_pubblicazione_inizio import controller_pubblicazione_inizio
from Pubblicazione.Controller.Controller_Caricamento_Brano_Artista import Controller_Caricamento_Brano_Artista
from Pubblicazione.Controller.Controller_Richiesta_nBrani import Controller_Richiesta_nBrani


class Ui_Discovery(object):

    """" clesse riguardante l'applicazione """

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(682, 443)
        Form.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(140, 70, 441, 251))
        self.tableWidget.setStyleSheet("background-color: rgb(189, 193, 193);\n" #sfondo
                                       "color: rgb(27, 28, 28);")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_submit = QtWidgets.QPushButton(Form)
        self.btn_submit.setGeometry(QtCore.QRect(270, 340, 181, 31))
        self.btn_submit.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(73, 199, 41);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 14pt \"Arial\";")
        self.btn_submit.setObjectName("btn_submit")
        self.l_title = QtWidgets.QLabel(Form)
        self.l_title.setGeometry(QtCore.QRect(220, 20, 251, 21))
        self.l_title.setStyleSheet("\n"
                                   "color:White;\n"
                                   "font: 18pt \".SF NS Text\";")
        self.l_title.setObjectName("l_title")
        self.btn_back = QtWidgets.QPushButton(Form)
        self.btn_back.setGeometry(QtCore.QRect(270, 390, 181, 31))
        self.btn_back.setStyleSheet("color: rgb(250, 255, 255);\n"
                                    "background-color: rgb(73, 199, 41);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 14pt \"Arial\";")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btn_submit.clicked.connect(self.load_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_submit.setText(_translate("Form", "Submit"))
        self.l_title.setText(_translate("Form", "Automated Host Discovery "))
        self.btn_back.setText(_translate("Form", "Back"))


# ----------------------------------------------
from Registrazione.controller.controller_registrazione import Newuser


class Discovery(QtWidgets.QWidget, Ui_Discovery):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn_submit.clicked.connect(self.btn_submit_handler)
        self.btn_back.clicked.connect(self.btn_back_handler)



    def load_data(self):

        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str("Sr No")))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(" Ip Address")))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str("Mac Address")))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str("Vendor")))

    def btn_submit_handler(self):
        self.load_data()

    def btn_back_handler(self):
        self.switch_window.emit()


class Controller:

    def __init__(self):
        self.cont_ascoltatore = False
        self.cont_artista = False
        self.check_conferma_credenziali = False
        self.check_conferma_edit = False


    """FINESTRA POP UP"""
    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


    def show_login_page(self):
        self.login = Login()
        self.data = DataPick()
        self.login.switch_window.connect(self.show_newuser_page)
        # self.login.switch_window1.connect(self.show_discovery)
        self.login.switch_window1.connect(self.show_home_ascoltatore)
        self.login.switch_window2.connect(self.show_home_artista)
        self.login.switch_window3.connect(self.show_home_etichetta)
        self.login.show()

    '''
    def loading(self):
        self.load= controller_loading()
        if self.load.controlla_login() == 1:
            self.load.switch_window_1.connect(self.show_home_ascoltatore)
        if self.load.controlla_login() == 2:
            self.load.switch_window_2.connect(self.show_home_artista)
        if self.load.controlla_login() == 3:
            self.load.switch_window_3.connect(self.show_home_etichetta)
            '''

    def show_newuser_page(self):

        self.newuser = Newuser()
        self.newuser.switch_window.connect(self.show_login_page)
        self.login.close()
        self.newuser.show()

    def show_discovery(self):
        self.discovery = Discovery()
        self.discovery.switch_window.connect(self.show_login_page)
        self.login.close()
        self.discovery.show()

    """---------------------------------------------------------------------------------------------"""

    """Home PySound"""
    def show_home_ascoltatore(self):
        self.ascoltatore = controller_ascoltatore()
        self.ascoltatore.switch_window_1.connect(self.show_impostazioni_ascoltatore)
        self.login.close()
        self.ascoltatore.show()

    def show_home_artista(self):
        self.artista = controller_artista()
        self.artista.switch_window_1.connect(self.show_impostazioni_artista)
        self.artista.switch_window_3.connect(self.show_pubblicazione_inizio)
        self.login.close()
        self.artista.show()

    def show_home_etichetta(self):
        self.etichetta = controller_etichetta()
        self.etichetta.switch_window_3.connect(self.show_pubblicazione_inizio)
        self.etichetta.switch_window_1.connect(self.show_impostazioni_etichetta)
        self.login.close()
        self.etichetta.show()


    """---------------------------------------------------------------------------------------------"""

    """Controller pubblicazione"""
    def show_pubblicazione_inizio(self):
        self.pubblicazione_inizio = controller_pubblicazione_inizio()
        self.pubblicazione_inizio.show()
        self.pubblicazione_inizio.switch_window_1.connect(self.show_pubblicazione_brano)
        self.pubblicazione_inizio.switch_window_2.connect(self.show_pubblicazione_album)



    def show_pubblicazione_brano(self):
        self.Caricamento_Brano_Artista = Controller_Caricamento_Brano_Artista()
        self.Caricamento_Brano_Artista.show()



    def show_pubblicazione_album(self):
        self.Richiesta_nBrani = Controller_Richiesta_nBrani
        n = self.Richiesta_nBrani.nBrani
        for i in n:
            self.show_pubblicazione_brano()

    """---------------------------------------------------------------------------------------------"""


    """Controller impostazioni ascoltatore"""
    def show_impostazioni_ascoltatore(self):
        self.impostazioni_ascoltatore = controller_impostazioni()
        # self.home.switch_window.connect(self.show_login_page)
        self.impostazioni_ascoltatore.switch_window_1.connect(self.show_conferma_edit)
        self.impostazioni_ascoltatore.switch_window.connect(self.show_conferma_credenziali)

        if self.cont_ascoltatore is True:
            self.EditAscoltatore.close()
            self.cont_ascoltatore = False

        if self.check_conferma_credenziali is True:
            self.conferma_credenziali.close()
            self.check_conferma_credenziali = False

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False

        self.impostazioni_ascoltatore.show()

    def show_edit_ascoltatore(self):
        self.EditAscoltatore = controller_edit_ascoltatore()
        self.EditAscoltatore.switch_window_1.connect(self.show_impostazioni_ascoltatore)
        self.impostazioni_ascoltatore.close()

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False

        self.cont_ascoltatore = True
        self.EditAscoltatore.show()





    """Controller impostazioni artista"""

    def show_impostazioni_artista(self):
        self.impostazioni_artista = controller_impostazioni()
        # self.home.switch_window.connect(self.show_login_page)
        self.impostazioni_artista.switch_window_1.connect(self.show_conferma_edit)
        self.impostazioni_artista.switch_window.connect(self.show_conferma_credenziali)

        if self.cont_artista is True:
            self.EditArtista.close()
            self.cont_artista = False

        if self.check_conferma_credenziali is True:
            self.conferma_credenziali.close()
            self.check_conferma_credenziali = False

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False

        self.impostazioni_artista.show()

    def show_edit_artista(self):
        self.EditArtista = controller_edit_artista()
        self.EditArtista.switch_window_1.connect(self.show_impostazioni_artista)
        self.impostazioni_artista.close()

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False

        self.cont_artista = True
        self.EditArtista.show()


    """Controller impostazioni etichetta"""

    def show_impostazioni_etichetta(self):
        self.impostazioni_etichetta = controller_impostazioni()
        self.impostazioni_etichetta.switch_window_1.connect(self.show_edit_etichetta)
        self.impostazioni_etichetta.switch_window.connect(self.show_conferma_credenziali)

        if self.check_conferma_credenziali is True:
            self.conferma_credenziali.close()
            self.check_conferma_credenziali = False

        self.impostazioni_etichetta.show()


    def show_edit_etichetta(self):
        self.pop_message(text="Il suo account non può subire variazioni.")



    """Controlle conferma eliminazione universale"""

    def show_conferma_credenziali(self):
        self.conferma_credenziali = controller_conferma_credenziali()
        self.conferma_credenziali.switch_window_1.connect(self.show_impostazioni_ascoltatore)
        self.conferma_credenziali.switch_window_2.connect(self.show_impostazioni_artista)
        self.conferma_credenziali.switch_window_3.connect(self.show_impostazioni_etichetta)
        self.check_conferma_credenziali = True
        self.conferma_credenziali.show()


    def show_conferma_edit(self):
        self.conferma_edit = controller_conferma_edit()
        self.conferma_edit.switch_window_1.connect(self.show_impostazioni_ascoltatore)
        self.conferma_edit.switch_window_2.connect(self.show_impostazioni_artista)
        self.conferma_edit.switch_window_3.connect(self.show_impostazioni_etichetta)

        self.conferma_edit.switch_window_4.connect(self.show_edit_ascoltatore)
        self.conferma_edit.switch_window_5.connect(self.show_edit_artista)
        self.check_conferma_edit = True
        self.conferma_edit.show()



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login_page()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


