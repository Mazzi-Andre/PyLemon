import pickle
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets


# ---------- We dont Touch --------------------
from Data_Utente.control.Data_control import DataPick
from Gestione_Ascolto.Contenuti.View.controller_mostra_search import controller_mostra_search
from Gestione_Ascolto.Contenuti.View.controller_mostra_tutto import controller_mostra_tutto
from Gestione_del_profilo.Controller.Controller_artista import controller_artista
from Gestione_del_profilo.Controller.Controller_ascoltatore import controller_ascoltatore
from Gestione_del_profilo.Controller.Controller_conferma_credenziali import controller_conferma_credenziali
from Gestione_del_profilo.Controller.Controller_conferma_edit import controller_conferma_edit
from Gestione_del_profilo.Controller.Controller_easter_egg import controller_easter_egg
from Gestione_del_profilo.Controller.Controller_edit_artista import controller_edit_artista
from Gestione_del_profilo.Controller.Controller_edit_ascoltatore import controller_edit_ascoltatore
from Gestione_del_profilo.Controller.Controller_impostazioni import controller_impostazioni
from Gestione_del_profilo.Controller.controller_etichetta import controller_etichetta
from Login.controller.controller_login import Login
from Pubblicazione.Controller.Controller_Caricamento_Brano_Etichetta import Controller_Caricamento_Brano_Etichetta

from Pubblicazione.Controller.Controller_pubblicazione_inizio import controller_pubblicazione_inizio
from Pubblicazione.Controller.Controller_Caricamento_Brano_Artista import Controller_Caricamento_Brano_Artista
from Pubblicazione.Controller.Controller_Richiesta_nBrani import Controller_Richiesta_nBrani
from Pubblicazione.Controller.Gestione_json import Gestione_json
from Top5.Controller.ControllerTop5 import TopFive


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





class Controller():

    def __init__(self):
        self.check_login_page = False
        self.check_newuser_page = False
        self.check_home_ascoltatore = False
        self.check_home_artista = False
        self.check_home_etichetta = False
        self.check_pubblicazione_inizio = False
        self.check_pubblicazione_brano = False
        self.check_pubblicazione_album = False
        self.check_impostazioni_ascoltatore = False
        self.check_edit_ascoltatore = False
        self.check_impostazioni_artista = False
        self.check_edit_artista = False
        self.check_impostazioni_etichetta = False
        self.check_conferma_credenziali = False
        self.check_conferma_edit = False
        self.check_mostra_tutto = False
        self.check_mostra_search = False
        self.check_pubblicazione_album = False
        self.check_verifica_etichetta = False
        self.check_pubblicazione_brano_artista = False
        self.check_richiesta_nBrani = False
        self.check_pubblicazione_brano_etichetta = False
        self.Richiesta_nBrani = Controller_Richiesta_nBrani()
        self.conta_brani_artista = 0
        self.conta_brani_etichetta = 0

        


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
        if self.check_newuser_page is True:
            self.newuser.close()
            self.check_newuser_page = False
        self.check_login_page = True
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
        if self.check_login_page is True:
            self.login.close()
            self.check_login_page = False
        self.check_newuser_page = True
        self.newuser.show()

    """
    def show_discovery(self):
        self.discovery = Discovery()
        self.discovery.switch_window.connect(self.show_login_page)
        self.login.close()
        self.discovery.show()"""

    """---------------------------------------------------------------------------------------------"""

    """Home PySound"""
    def show_home_ascoltatore(self):
        Titoli_top = self.statistica_top5()
        self.ascoltatore = controller_ascoltatore(Titoli_top)
        self.ascoltatore.switch_window_1.connect(self.show_impostazioni_ascoltatore)
        self.ascoltatore.switch_window_2.connect(self.show_mostra_tutto)
        self.ascoltatore.switch_window_4.connect(self.show_mostra_search)
        self.ascoltatore.switch_window_5.connect(self.show_easter_egg)
        self.ascoltatore.switch_window_k.connect(self.show_logout)
        if self.check_login_page is True:
            self.login.close()
            self.check_login_page = False
        self.check_home_ascoltatore = True
        self.ascoltatore.show()

    def show_home_artista(self):
        Titoli_top = self.statistica_top5()
        Brani_artisti = self.statistica_mie_brani_artista()
        self.artista = controller_artista(Titoli_top,Brani_artisti)
        self.artista.switch_window_1.connect(self.show_impostazioni_artista)
        self.artista.switch_window_2.connect(self.show_mostra_tutto)
        self.artista.switch_window_3.connect(self.show_pubblicazione_inizio)
        self.artista.switch_window_4.connect(self.show_mostra_search)
        self.artista.switch_window_5.connect(self.show_easter_egg)
        self.artista.switch_window_k.connect(self.show_logout)
        if self.check_login_page is True:
            self.login.close()
            self.check_login_page = False
        self.check_home_artista = True
        self.artista.show()

    def show_home_etichetta(self):
        Titoli_top = self.statistica_top5()
        self.etichetta = controller_etichetta(Titoli_top)
        self.etichetta.switch_window_3.connect(self.show_pubblicazione_inizio)
        self.etichetta.switch_window_2.connect(self.show_mostra_tutto)
        self.etichetta.switch_window_1.connect(self.show_impostazioni_etichetta)
        self.etichetta.switch_window_4.connect(self.show_mostra_search)
        self.check_verifica_etichetta = True
        self.etichetta.switch_window_5.connect(self.show_easter_egg)

        self.verifica_etichetta = True
        self.login.close()
        self.etichetta.switch_window_k.connect(self.show_logout)
        if self.check_login_page is True:
            self.login.close()
            self.check_login_page = False
        self.check_home_etichetta= True
        self.etichetta.show()


    '''-------------------------------------------------------------------'''

    def show_easter_egg(self):
        self.easter = controller_easter_egg()
        self.easter.show()



    """---------------------------------------------------------------------------------------------"""

    """Controller pubblicazione"""
    def show_pubblicazione_inizio(self):
        self.pubblicazione_inizio = controller_pubblicazione_inizio()
        self.pubblicazione_inizio.show()
        if self.check_verifica_etichetta:
            self.pubblicazione_inizio.switch_window_1.connect(self.show_pubblicazione_brano_etichetta)
        else: self.pubblicazione_inizio.switch_window_1.connect(self.show_pubblicazione_brano_artista)
        self.pubblicazione_inizio.switch_window_2.connect(self.show_pubblicazione_album)
        if self.check_pubblicazione_brano_artista is True:
            self.Caricamento_Brano_Artista.close()
            self.check_pubblicazione_brano_artista = False
        if self.check_richiesta_nBrani is True:
            self.Richiesta_nBrani.close()
            self.check_richiesta_nBrani = False
        if self.check_pubblicazione_brano_etichetta is True:
            self.Caricamento_Brano_etichetta.close()
            self.check_pubblicazione_brano_etichetta = False



    def show_pubblicazione_brano_artista(self):
        self.check_pubblicazione_brano_artista = True
        if self.check_pubblicazione_album:
            self.conta_brani_artista = self.conta_brani_artista + 1
            self.nome_album = self.Richiesta_nBrani.nBrani
            self.nBrani = self.Richiesta_nBrani.nome_album
        else: self.nome_album = None
        self.Caricamento_Brano_Artista = Controller_Caricamento_Brano_Artista(self.check_pubblicazione_album, self.nome_album)
        self.Caricamento_Brano_Artista.switch_window.connect(self.show_pubblicazione_brano_artista)
        if self.check_pubblicazione_album is True:
            if self.conta_brani_artista <= int(self.nBrani):
                self.Caricamento_Brano_Artista.show()
        else: self.Caricamento_Brano_Artista.show()
        self.Caricamento_Brano_Artista.switch_window_2.connect(self.show_pubblicazione_inizio)
        self.pubblicazione_inizio.close()



    def show_pubblicazione_brano_etichetta(self):
        self.check_pubblicazione_brano_etichetta = True
        if self.check_pubblicazione_album:
            self.check_pubblicazione_album = False
            self.conta_brani_etichetta = self.conta_brani_etichetta + 1
            self.nome_album_etichetta = self.Richiesta_nBrani.nBrani
            self.nBrani_etichetta = self.Richiesta_nBrani.nome_album
        else: self.nome_album_etichetta = None
        self.Caricamento_Brano_etichetta = Controller_Caricamento_Brano_Etichetta(self.check_pubblicazione_album, self.nome_album_etichetta)
        self.Caricamento_Brano_etichetta.switch_window.connect(self.show_pubblicazione_brano_etichetta)
        if self.check_pubblicazione_album is True:
            if self.conta_brani_etichetta <= int(self.nBrani_etichetta):
                self.Caricamento_Brano_etichetta.show()
        else:
            self.Caricamento_Brano_etichetta.show()
        self.Caricamento_Brano_etichetta.switch_window_2.connect(self.show_pubblicazione_inizio)
        self.pubblicazione_inizio.close()




    def show_pubblicazione_album(self):
        self.check_richiesta_nBrani = True
        self.Richiesta_nBrani.show()
        if self.check_verifica_etichetta:
            self.Richiesta_nBrani.switch_window.connect(self.show_pubblicazione_brano_etichetta)
            self.check_pubblicazione_album = True
        else:
            self.Richiesta_nBrani.switch_window.connect(self.show_pubblicazione_brano_artista)
            self.check_pubblicazione_album = True
        self.Richiesta_nBrani.switch_window_2.connect(self.show_pubblicazione_inizio)
        self.pubblicazione_inizio.close()







    """---------------------------------------------------------------------------------------------"""


    """Controller impostazioni ascoltatore"""
    def show_impostazioni_ascoltatore(self):
        self.impostazioni_ascoltatore = controller_impostazioni()
        # self.home.switch_window.connect(self.show_login_page)
        self.impostazioni_ascoltatore.switch_window_1.connect(self.show_conferma_edit)
        self.impostazioni_ascoltatore.switch_window.connect(self.show_conferma_credenziali)

        if self.check_edit_ascoltatore is True:
            self.EditAscoltatore.close()
            self.check_edit_ascoltatore = False

        if self.check_conferma_credenziali is True:
            self.conferma_credenziali.close()
            self.check_conferma_credenziali = False

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False
        self.check_impostazioni_ascoltatore = True
        self.impostazioni_ascoltatore.show()

    def show_edit_ascoltatore(self):
        self.EditAscoltatore = controller_edit_ascoltatore()
        self.EditAscoltatore.switch_window_1.connect(self.show_impostazioni_ascoltatore)
        self.impostazioni_ascoltatore.close()

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False

        self.check_edit_ascoltatore = True
        self.EditAscoltatore.show()


    """Controller impostazioni artista"""

    def show_impostazioni_artista(self):
        self.impostazioni_artista = controller_impostazioni()
        # self.home.switch_window.connect(self.show_login_page)
        self.impostazioni_artista.switch_window_1.connect(self.show_conferma_edit)
        self.impostazioni_artista.switch_window.connect(self.show_conferma_credenziali)

        if self.check_edit_artista is True:
            self.EditArtista.close()
            self.check_edit_artista = False

        if self.check_conferma_credenziali is True:
            self.conferma_credenziali.close()
            self.check_conferma_credenziali = False

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False

        self.check_impostazioni_artista = True
        self.impostazioni_artista.show()

    def show_edit_artista(self):
        self.EditArtista = controller_edit_artista()
        self.EditArtista.switch_window_1.connect(self.show_impostazioni_artista)
        self.impostazioni_artista.close()

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False

        self.check_edit_artista = True
        self.EditArtista.show()


    """Controller impostazioni etichetta"""

    def show_impostazioni_etichetta(self):
        self.impostazioni_etichetta = controller_impostazioni()
        self.impostazioni_etichetta.switch_window_1.connect(self.show_edit_etichetta)
        self.impostazioni_etichetta.switch_window.connect(self.show_conferma_credenziali)

        if self.check_conferma_credenziali is True:
            self.conferma_credenziali.close()
            self.check_conferma_credenziali = False
        self.check_impostazioni_etichetta = True
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


    """Controlle Player e ricerca canzoni"""

    def show_mostra_tutto(self):
        self.player = controller_mostra_tutto()
        self.check_mostra_tutto = True
        self.player.show()

    def show_mostra_search(self):
        var_search = False
        with open('Canzone.pkl', 'rb') as Dpi:
            MyData = pickle.load(Dpi)

        json_manage = Gestione_json()

        for i in json_manage.get_jsonobject():
            if i["Titolo"] == MyData[0].title() or i["Album"] == MyData[0].title() or i["Artista"] == MyData[0].title():
                self.search = controller_mostra_search(MyData)
                self.check_mostra_search = True
                var_search = True
                self.search.show()
                break

        if not var_search:
            self.pop_message(text="Nessuna corrispondenza trovata.")


    """Controlle Logout"""

    def show_logout(self):
        self.pop_message(text="arrivederci")

        if self.check_verifica_etichetta is True:
            self.check_verifica_etichetta = False

        if self.check_login_page is True:
            self.login.close()
            self.check_login_page = False

        if self.check_newuser_page is True:
            self.newuser.close()
            self.check_newuser_page = False

        if self.check_home_ascoltatore is True:
            self.ascoltatore.close()
            self.check_home_ascoltatore = False

        if self.check_home_artista is True:
            self.artista.close()
            self.check_home_artista = False

        if self.check_home_etichetta is True:
            self.etichetta.close()
            self.check_home_etichetta = False

        if self.check_home_etichetta is True:
            self.etichetta.close()
            self.check_home_etichetta = False

        if self.check_impostazioni_ascoltatore is True:
            self.impostazioni_ascoltatore.close()
            self.check_impostazioni_ascoltatore = False

        if self.check_edit_ascoltatore is True:
            self.EditAscoltatore.close()
            self.check_edit_ascoltatore = False

        if self.check_impostazioni_artista is True:
            self.impostazioni_artista.close()
            self.check_impostazioni_artista = False

        if self.check_edit_artista is True:
            self.EditArtista.close()
            self.check_edit_artista = False

        if self.check_impostazioni_etichetta is True:
            self.impostazioni_etichetta.close()
            self.check_impostazioni_etichetta = False

        if self.check_conferma_credenziali is True:
            self.conferma_credenziali.close()
            self.check_conferma_credenziali= False

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False

        if self.check_mostra_tutto is True:
            self.player.close()
            self.check_mostra_tutto = False

        if self.check_mostra_search is True:
            self.search.close()
            self.check_mostra_search= False

        if self.check_login_page is False:
            self.show_login_page()

    def statistica_top5(self):
        self.g = Gestione_json()
        json_data = self.g.get_jsonobject()
        controller_top = TopFive()
        list = controller_top.json_to_list(json_data)
        Titoli_top5 = []
        i = 0
        while i <= len(list) - 1:
            posi = list.__getitem__(i)
            Titoli_top5.append(self.g.getTitolo_da_Id(posi[0]))
            i = i + 1
        return Titoli_top5


    def statistica_mie_brani_artista(self):
        json_data = self.g.get_jsonobject()
        brani_artista = []
        nome_artista = self.data.return_credenziali()[1].title()+" "+self.data.return_credenziali()[2].title()
        for i in json_data:
            if nome_artista == i["Artista"]:
                brani_artista.append(i["Titolo"])
        return brani_artista





def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login_page()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


