import os
import shutil

class Gestione_mp3():


    def Carica_mp3(self, contatoreid, percorsofile):
        if os.path.isfile(percorsofile):
            shutil.copy(percorsofile,
                        "cartella dove verrà spostato il file")  # percorsofile è una stringa che indica dove si trova il file e sarà del tipo C:\\Desktop\\ciao.mp3
            x = contatoreid + ".mp3"
            os.rename("nomefilecanzone.mp3", x)
        else:
            print("il file non esiste")