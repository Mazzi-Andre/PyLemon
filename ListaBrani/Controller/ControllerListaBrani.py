import json
import os
import shutil
from os import path

class ControllerListaBrani():
    def __init__(self, listabrani):
        super(ControllerListaBrani, self).__init__()
        self.model = listabrani()


    def Carica_listabrani(self):
        if os.path.isfile('ListaBrani/data/listabrani.json'):
            with open("data_file.json", "w") as write_file:
                json.dump(self.model, write_file)

        else:
            jsonList = json.dumps(self.model)
            jsonFile = open("listabrani.json", "w")
            jsonFile.write(jsonList)
            jsonFile.close()
            print("fatto")

    def Carica_mp3(self, contatoreid, percorsofile):
        #capire come cazzo si trasferisce un file nella directory desiderata e farlo qui prima del rename
        shutil.copy(percorsofile, "cartella dove verrà spostato il file")  #percorsofile è una stringa che indica dove si trova il file e sarà del tipo C:\\Desktop\\ciao.mp3
        x = contatoreid+".mp3"
        os.rename("nomefilecanzone.mp3", x)

        #da aggiungere try and cath e controlli vari

        #se si vuole possiasmo aggiungere un modo per criptare i file

