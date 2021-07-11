import os
import shutil
import json
from PyQt5 import QtWidgets


class Gestione_mp3():
    def __init__(self):

        with open('ContatoreBrani.json', 'r') as j:
            self.json_contatore = json.load(j)


    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


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
            newfile = str(id) + ".mp3"
            shutil.move('Data/mp3/' + nomefile, 'Data/mp3/' + newfile)
            self.json_contatore["contatore_id"] = id
            with open("ContatoreBrani.json", "w") as write_file:
                json.dump(self.json_contatore, write_file)

        else:
            print("il file non esiste")


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



