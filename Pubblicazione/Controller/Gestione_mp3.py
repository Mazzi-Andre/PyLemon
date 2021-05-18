import os
import shutil
import json


class Gestione_mp3():
    def __init__(self):
        with open('ContatoreBrani.json', 'r') as j:
            self.json = json.load(j)


    # percorsofile è una stringa che indica dove si trova il file e sarà del tipo C:\\Desktop\\ciao.mp3
    def Carica_mp3(self, percorsofile):
        U = self.json['contatore']
        contatoreid = U.get["valore"]
        if os.path.isfile(percorsofile):
            shutil.copy(percorsofile, 'C:/Users/Stefano/Desktop/Progetti Python/Progetto Esame/CartellaBrani')
            oldfile = percorsofile.split("\ ")
            newfile = contatoreid + ".mp3"
            shutil.move('C:/Users/Stefano/Desktop/Progetti Python/Progetto Esame/CartellaBrani/'+oldfile[oldfile.leg],
                        'C:/Users/Stefano/Desktop/Progetti Python/Progetto Esame/CartellaBrani/' + newfile)
        else:
            print("il file non esiste")

        contatoreid += 1
        Object = {"contatore":{"valore": contatoreid}}
        with open("ContatoreBrani.json", "w") as write_file:
            json.dump(Object, write_file)


    def Elimina_mp3(self, id):
        U = self.json['contatore']
        contatoreid = U.get["valore"]
        contatoreid =-1
        Object = {"contatore": {"valore": contatoreid}}
        with open("ContatoreBrani.json", "w") as write_file:
            json.dump(Object, write_file)
        os.remove('C:/Users/Stefano/Desktop/Progetti Python/Progetto Esame/CartellaBrani/'+id+'.mp3')

