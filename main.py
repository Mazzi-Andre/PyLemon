import pickle
import sys

import pygame
from PyQt5 import QtWidgets


from Gestione_Ascolto.Controller.controller_ascolto import controller_mostra_search, controller_mostra_tutto
from Gestione_del_profilo.Controller.Controller_artista import controller_artista
from Gestione_del_profilo.Controller.Controller_ascoltatore import controller_ascoltatore
from Gestione_del_profilo.Controller.Controller_conferma_credenziali import controller_conferma_credenziali
from Gestione_del_profilo.Controller.Controller_conferma_edit import controller_conferma_edit
from Gestione_del_profilo.Controller.Controller_easter_egg import controller_easter_egg
from Gestione_del_profilo.Controller.Controller_edit_artista import controller_edit_artista
from Gestione_del_profilo.Controller.Controller_edit_ascoltatore import controller_edit_ascoltatore
from Gestione_del_profilo.Controller.Controller_impostazioni import controller_impostazioni
from Gestione_del_profilo.Controller.Controller_impostazioni_ascoltatore import controller_impostazioni_ascoltatore
from Gestione_del_profilo.Controller.controller_conferma_eliminazione import controller_conferma_eliminazione
from Gestione_del_profilo.Controller.controller_etichetta import controller_etichetta
from Login.Model.login import DataPick
from Login.controller.controller_login import Login
from Pubblicazione.Controller.Controller_Caricamento_Brano_Etichetta import Controller_Caricamento_Brano_Etichetta
from Pubblicazione.Controller.Controller_Richiesta_nBrani import Controller_Richiesta_nBrani
from Pubblicazione.Controller.Controller_pubblicazione_inizio import controller_pubblicazione_inizio
from Pubblicazione.Controller.Controller_Caricamento_Brano_Artista import Controller_Caricamento_Brano_Artista
from Pubblicazione.Model.pubblicazione_gestione import Gestione_json
from Top5.Controller.ControllerTop5 import TopFive
from Gestione_del_profilo.Controller.Controller_rimozione_brani import controller_rimozioni_brani
from Registrazione.controller.controller_registrazione import Newuser



class Controller():

    def __init__(self):

        '''--variabili per chiusura delle classi--'''

        self.check_login_page = False
        self.check_newuser_page = False
        self.check_home_ascoltatore = False
        self.check_home_artista = False
        self.check_home_etichetta = False
        self.check_pubblicazione_inizio1 = False
        self.check_pubblicazione_brano = False
        self.check_impostazioni_ascoltatore = False
        self.check_edit_ascoltatore = False
        self.check_impostazioni_artista = False
        self.check_edit_artista = False
        self.check_impostazioni_etichetta = False
        self.check_conferma_credenziali = False
        self.check_conferma_edit = False
        self.check_mostra_tutto = False
        self.check_mostra_search = False
        self.check_verifica_etichetta = False
        self.check_richiesta_nBrani1 = False
        self.check_pubblicazione_brano_etichetta1 = False
        self.check_easter_egg = False
        self.check_rimozione_brani = False
        self.check_scelta_rimozione_brano = False

        '''--variabili per funzionamento pubblicazione--'''

        self.check_pubblicazione_brano_artista = False
        self.pippo= 0

        #self.Richiesta_nBrani = Controller_Richiesta_nBrani()
        #self.check_pubblicazione_album = self.Richiesta_nBrani.verifica_album
        self.conta_brani_artista = 0
        self.conta_brani_etichetta = 0

        


    """FINESTRA POP UP"""
    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


    def show_login_page(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_newuser_page)
        self.login.switch_window1.connect(self.show_home_ascoltatore)
        self.login.switch_window2.connect(self.show_home_artista)
        self.login.switch_window3.connect(self.show_home_etichetta)
        if self.check_newuser_page is True:
            self.newuser.close()
            self.check_newuser_page = False

        self.check_login_page = True
        self.login.show()


    def show_newuser_page(self):
        self.newuser = Newuser()
        self.newuser.switch_window.connect(self.show_login_page)
        if self.check_login_page is True:
            self.login.close()
            self.check_login_page = False

        self.check_newuser_page = True
        self.newuser.show()


    """---------------------------------------------------------------------------------------------"""

    """Home PyLemon"""
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
        self.etichetta.switch_window_5.connect(self.show_easter_egg)

        self.check_verifica_etichetta = True

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
        self.check_easter_egg = True
        self.easter.show()


    """---------------------------------------------------------------------------------------------"""

    """Controller pubblicazione"""
    def show_pubblicazione_inizio(self):
        self.pubblicazione_inizio = controller_pubblicazione_inizio()
        self.Richiesta_nBrani = Controller_Richiesta_nBrani()

        if self.check_verifica_etichetta:
            self.pubblicazione_inizio.switch_window_1.connect(self.show_pubblicazione_brano_etichetta)
        else:
            self.pubblicazione_inizio.switch_window_1.connect(self.show_pubblicazione_brano_artista)
        self.pubblicazione_inizio.switch_window_2.connect(self.show_pubblicazione_album)


        if self.check_pubblicazione_brano_artista is True:
            self.Caricamento_Brano_Artista.close()
            self.check_pubblicazione_brano_artista = False

        if self.Richiesta_nBrani.verifica_album is True:
            if self.conta_brani_artista == int(self.nBrani):
                self.Richiesta_nBrani.verifica_album =False


        if self.check_pubblicazione_brano_etichetta1 is True:
            if self.Richiesta_nBrani.verifica_album is True:
                if self.conta_brani_etichetta == int(self.nBrani_etichetta):
                    self.Caricamento_Brano_etichetta.close()
                    self.check_pubblicazione_brano_etichetta1 = False
            else:
                self.Caricamento_Brano_etichetta.close()
                self.check_pubblicazione_brano_etichetta1 = False

        if self.check_richiesta_nBrani1 is True:
            self.Richiesta_nBrani.close()
            self.check_richiesta_nBrani1= False

        self.check_pubblicazione_inizio1 = True
        self.pubblicazione_inizio.show()


    def show_pubblicazione_brano_artista(self):
        self.Richiesta_nBrani = Controller_Richiesta_nBrani()


        if self.check_pubblicazione_inizio1 is True:
            self.pubblicazione_inizio.close()
            self.check_pubblicazione_inizio1 = False

        if self.check_richiesta_nBrani1 is True:
            self.Richiesta_nBrani.close()
            self.check_richiesta_nBrani1 = False

        with open('Data\Database\Album.pkl', 'rb') as Dpi:
            MyData = pickle.load(Dpi)
            print(MyData[0] +' '+ MyData[1])

        if int(MyData[0]) == 0:
            self.verifica_album = False
        else: self.verifica_album = True

        if  int(MyData[0]) > 1:
            self.conta_brani_artista = self.conta_brani_artista + 1
            self.nome_album = MyData[1]
        else: self.nome_album = None

        self.Caricamento_Brano_Artista = Controller_Caricamento_Brano_Artista(self.verifica_album, self.nome_album)

        self.Caricamento_Brano_Artista.switch_window_1.connect(self.show_pubblicazione_inizio)
        self.Caricamento_Brano_Artista.switch_window_3.connect(self.show_pubblicazione_brano_artista)

        if  int(MyData[0]) > 0:
            if self.conta_brani_artista == int(MyData[0]):
                self.Richiesta_nBrani.put_data_brani('0','0')
                self.conta_brani_artista = 0
                self.Caricamento_Brano_Artista.controllo_fine_album = True
            else:
                self.Caricamento_Brano_Artista.controllo_fine_album = False

        if int(MyData[0]) > 0:
            self.Caricamento_Brano_Artista.switch_window_2.connect(self.show_pubblicazione_album)
        else: self.Caricamento_Brano_Artista.switch_window_2.connect(self.show_pubblicazione_inizio)

        self.check_pubblicazione_brano_artista = True
        self.Caricamento_Brano_Artista.show()



    def show_pubblicazione_brano_etichetta(self):
        self.Richiesta_nBrani = Controller_Richiesta_nBrani()

        if self.check_richiesta_nBrani1 is True:
            self.Richiesta_nBrani.close()
            self.check_richiesta_nBrani1 = False

        if self.check_pubblicazione_inizio1 is True:
            self.pubblicazione_inizio.close()
            self.check_pubblicazione_inizio1 = False

        with open('Data\Database\Album.pkl', 'rb') as Dpi:
            MyData = pickle.load(Dpi)
            print(MyData[0] +' '+ MyData[1])

        if int(MyData[0]) == 0:
            self.verifica_album = False
        else: self.verifica_album = True

        if  int(MyData[0]) > 1:
            self.conta_brani_etichetta = self.conta_brani_etichetta + 1
            self.nome_album = MyData[1]
        else: self.nome_album = None

        '''if self.Richiesta_nBrani.verifica_album:
            self.conta_brani_etichetta = self.conta_brani_etichetta + 1
            self.nome_album_etichetta = self.Richiesta_nBrani.album_name
            self.nBrani_etichetta = self.Richiesta_nBrani.nBrani
        else: self.nome_album_etichetta = None'''

        self.Caricamento_Brano_etichetta = Controller_Caricamento_Brano_Etichetta(self.Richiesta_nBrani.verifica_album, self.nome_album_etichetta)
        self.Caricamento_Brano_etichetta.switch_window_1.connect(self.show_pubblicazione_brano_etichetta)
        self.Caricamento_Brano_etichetta.switch_window_2.connect(self.show_pubblicazione_inizio)

        if  int(MyData[0]) > 0:
            if self.conta_brani_etichetta == int(MyData[0]):
                self.Richiesta_nBrani.put_data_brani('0','0')
                self.conta_brani_etichetta = 0
                self.Caricamento_Brano_etichetta.controllo_fine_album = True
            else:
                self.Caricamento_Brano_etichetta.controllo_fine_album = False

        if int(MyData[0]) > 0:
            self.Caricamento_Brano_etichetta.switch_window_2.connect(self.show_pubblicazione_album)
        else: self.Caricamento_Brano_etichetta.switch_window_2.connect(self.show_pubblicazione_inizio)


        '''if self.Richiesta_nBrani.verifica_album is True:
            if self.conta_brani_etichetta <= self.nBrani_etichetta:
                self.check_pubblicazione_brano_etichetta1 = True
                if self.conta_brani_etichetta == self.nBrani_etichetta:
                    self.Caricamento_Brano_etichetta.btn_Pubblica.clicked.connect(self.show_pubblicazione_inizio)
                self.Caricamento_Brano_etichetta.show()
        else:
            self.check_pubblicazione_brano_etichetta1 = True
            self.Caricamento_Brano_etichetta.btn_Pubblica.clicked.connect(self.show_pubblicazione_inizio)'''
        self.Caricamento_Brano_etichetta.show()






    def show_pubblicazione_album(self):
        self.Richiesta_nBrani = Controller_Richiesta_nBrani()

        if self.check_pubblicazione_inizio1 is True:
            self.pubblicazione_inizio.close()
            self.check_pubblicazione_inizio1 = False

        if self.check_verifica_etichetta:
            self.Richiesta_nBrani.switch_window.connect(self.show_pubblicazione_brano_etichetta)
        else:
            self.Richiesta_nBrani.switch_window.connect(self.show_pubblicazione_brano_artista)
        self.Richiesta_nBrani.switch_window_2.connect(self.show_pubblicazione_inizio)

        if self.check_pubblicazione_brano_artista is True:
            self.Caricamento_Brano_Artista.close()
            self.check_pubblicazione_brano_artista = False

        self.check_richiesta_nBrani1 = True
        self.Richiesta_nBrani.show()



    """---------------------------------------------------------------------------------------------"""


    """Controller impostazioni ascoltatore"""
    def show_impostazioni_ascoltatore(self):
        self.impostazioni_ascoltatore = controller_impostazioni_ascoltatore()
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
        self.EditAscoltatore.btn_Artista.clicked.connect(self.show_logout)
        self.EditAscoltatore.btn_Etichetta.clicked.connect(self.show_logout)

        self.impostazioni_ascoltatore.close()

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False

        self.check_edit_ascoltatore = True
        self.EditAscoltatore.show()


    """Controller impostazioni artista"""

    def show_impostazioni_artista(self):
        self.impostazioni_artista = controller_impostazioni()
        self.impostazioni_artista.switch_window_1.connect(self.show_conferma_edit)
        self.impostazioni_artista.switch_window.connect(self.show_conferma_credenziali)
        self.impostazioni_artista.switch_window_2.connect(self.show_rimozione_brani)

        if self.check_edit_artista is True:
            self.EditArtista.close()
            self.check_edit_artista = False

        if self.check_conferma_credenziali is True:
            self.conferma_credenziali.close()
            self.check_conferma_credenziali = False

        if self.check_conferma_edit is True:
            self.conferma_edit.close()
            self.check_conferma_edit = False

        if self.check_scelta_rimozione_brano is True:
            self.rimuovi.close()
            self.check_scelta_rimozione_brano = False

        if self.check_rimozione_brani is True:
            self.controlla_eliminazione.close()
            self.check_rimozione_brani = False

        self.check_impostazioni_artista = True
        self.impostazioni_artista.show()

    def show_edit_artista(self):
        self.EditArtista = controller_edit_artista()
        self.EditArtista.switch_window_1.connect(self.show_impostazioni_artista)
        self.EditArtista.btn_Ascoltatore.clicked.connect(self.show_logout)
        self.EditArtista.btn_Etichetta.clicked.connect(self.show_logout)
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


    """Controller conferma eliminazione universale"""

    def show_conferma_credenziali(self):
        self.conferma_credenziali = controller_conferma_credenziali()
        self.conferma_credenziali.switch_window_1.connect(self.show_impostazioni_ascoltatore)
        self.conferma_credenziali.switch_window_2.connect(self.show_impostazioni_artista)
        self.conferma_credenziali.switch_window_3.connect(self.show_impostazioni_etichetta)

        self.conferma_credenziali.btn_Ok.clicked.connect(self.show_logout)
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

    def show_rimozione_brani(self):
        self.controlla_eliminazione = controller_conferma_eliminazione()
        self.controlla_eliminazione.switch_window_1.connect(self.show_impostazioni_artista)
        self.controlla_eliminazione.switch_window_2.connect(self.show_scelta_rimozione_brano)

        self.check_rimozione_brani = True
        self.controlla_eliminazione.show()

    def show_scelta_rimozione_brano(self):
        self.rimuovi = controller_rimozioni_brani()
        self.rimuovi.switch_window_1.connect(self.show_impostazioni_artista)

        if self.check_rimozione_brani is True:
            self.controlla_eliminazione.close()
            self.check_rimozione_brani = True

        if self.check_impostazioni_artista is True:
            self.impostazioni_artista.close()
            self.check_impostazioni_artista = True

        self.check_scelta_rimozione_brano = True
        self.rimuovi.show()



    """Controller Player e ricerca canzoni"""

    def show_mostra_tutto(self):
        self.player = controller_mostra_tutto()
        self.check_mostra_tutto = True
        self.player.show()

    def show_mostra_search(self):
        var_search = False
        with open('Data\Database\Canzone.pkl', 'rb') as Dpi:
            MyData = pickle.load(Dpi)

        if MyData[0]:
            json_manage = Gestione_json()

            for i in json_manage.get_jsonobject():
                if i["Titolo"] == MyData[0].title() or i["Album"] == MyData[0].title() or i["Artista"] == MyData[0].title():
                    self.search = controller_mostra_search(MyData)
                    self.check_mostra_search = True
                    var_search = True
                    self.search.show()
                    break

        else:   self.pop_message(text="Immetti il nome di un brano, di un album o di un artista.")

        if not var_search and MyData[0]:
            self.pop_message(text="Non ho trovato nessun risultato.")


    """Controlle Logout"""

    def show_logout(self):
        self.pop_message(text="Arrivederci")

        if self.check_verifica_etichetta is True:
            self.etichetta.close()
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
            pygame.mixer.init()
            self.player.close()
            self.check_mostra_tutto = False

        if self.check_mostra_search is True:
            pygame.mixer.init()
            self.search.close()
            self.check_mostra_search= False

        if self.check_easter_egg is True:
            self.easter.close()
            self.check_easter_egg = False

        if self.check_rimozione_brani is True:
            self.controlla_eliminazione.close()
            self.check_rimozione_brani = False

        if self.check_scelta_rimozione_brano is True:
            self.rimuovi.close()
            self.check_scelta_rimozione_brano = False

        if self.check_richiesta_nBrani1 is True:
            self.Richiesta_nBrani.close()
            self.check_richiesta_nBrani1= False

        if self.check_pubblicazione_brano_artista is True:
            self.Caricamento_Brano_Artista.close()
            self.check_pubblicazione_brano_artista = False

        if self.check_pubblicazione_brano_etichetta1 is True:
            self.Caricamento_Brano_etichetta.close()
            self.check_pubblicazione_brano_etichetta1 = False

        if self.check_pubblicazione_inizio1 is True:
            self.pubblicazione_inizio.close()
            self.check_pubblicazione_inizio1 = False

        if self.check_login_page is False:
            self.show_login_page()

    def statistica_top5(self):
        self.g = Gestione_json()
        json_data = self.g.get_jsonobject()
        controller_top = TopFive()
        sort_conta = controller_top.sort_lista_contatori(json_data)
        Titoli_top5 = []
        for i in sort_conta:
            for j in json_data:
                if i==j["contatore"]:
                    Titoli_top5.append(j["Titolo"])
                    break

        return Titoli_top5


    def statistica_mie_brani_artista(self):
        self.data = DataPick()
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


