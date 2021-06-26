import os
import shutil
import json


class Gestione_mp3():
    def __init__(self):

        with open('ContatoreBrani.json', 'r') as j:
            self.json_contatore = json.load(j)


    # percorsofile è una stringa che indica dove si trova il file e sarà del tipo C:\\Desktop\\ciao.mp3
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

        #contatoreid += 1
        #Object = {"contatore":{"valore": contatoreid}}
        #with open("ContatoreBrani.json", "w") as write_file:
            #json.dump(Object, write_file)


    def Elimina_mp3(self, id):
        U = self.json['contatore']
        contatoreid = U.get["valore"]
        Object = {"contatore": {"valore": contatoreid}}
        with open("../../ContatoreBrani.json", "w") as write_file:
            json.dump(Object, write_file)
        os.remove('C:/Users/Stefano/Desktop/Progetti Python/Progetto Esame/CartellaBrani/'+id+'.mp3')



