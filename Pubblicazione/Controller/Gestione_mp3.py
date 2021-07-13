import os
import shutil
import json
from PyQt5 import QtWidgets

'''Classe responsabile della gestione dei file .mp3 presenti sulla piattaforma'''
class Gestione_mp3():

    '''Nel costruttore vado a leggere il file ContatoreBrani.json'''
    def __init__(self):
        self.verifica_nome_mp3 = True

        with open('ContatoreBrani.json', 'r') as j:
            self.json_contatore = json.load(j)

    '''Pop Up Finestra'''
    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    '''Funzione che, dato il path del file, carica il file sulla piiattaforma'''
    def Carica_mp3(self, percorsofile):
        contatoreid = self.json_contatore["contatore_id"]
        if os.path.isfile(percorsofile):
                shutil.copy(percorsofile, 'Data/mp3')
                oldfile1 = str(percorsofile)
                oldfile2 = oldfile1.replace("[", "")
                oldfile3 = oldfile2.replace("]", "")
                oldfile4 = oldfile3.replace("'", "")
                oldfile5 = oldfile4.split("/")
                nomefile= str(oldfile5[len(oldfile5)-1])
                id=int(contatoreid)
                id = id+1
                newnomefile = str(id) + ".mp3"
                shutil.move('Data/mp3/' + nomefile, 'Data/mp3/' + newnomefile)
                self.json_contatore["contatore_id"] = id
                with open("ContatoreBrani.json", "w") as write_file:
                    json.dump(self.json_contatore, write_file)


    '''Funzione che, dato in input, l'id del brano, lo elimina dalla piattaforma'''
    def Elimina_mp3(self, id):

        try:
            os.remove('Data/mp3/'+str(id)+'.mp3')
            self.pop_message(text="Eliminazione avvenuta con successo.")
            self.pop_message(text="Per vedere gli aggiornamenti rieffettuare l'accesso")
            return True

        except:
            self.pop_message(text="Errore nella rimozione.\n"
                                      "Prova ad effettuare il logout e a riaccedere.")
            return False



