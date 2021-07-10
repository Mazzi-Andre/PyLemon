import json

from Pubblicazione.Controller.Gestione_mp3 import Gestione_mp3

'''Classe responsabile della gestione del file info_brani.json'''
class Gestione_json():


    '''Nel costruttore si esegue la lettura del file memorizzandola nell'attributo json_data'''
    def __init__(self):

        with open('info_brani.json', 'r') as j:
            self.json_data = json.load(j)


    '''Metodo che aggiunge coppie chiave-valore all'interno dell'attributo json_data(usato nell'attività di pubblicazione).
       A questo punto si esegue la sovrascttura del file con i dati aggiornati'''
    def carica_brano_su_JSON(self, nome,artista,album,id,contatore):
        oggettobrano = {"Titolo": nome.title(), "Artista": artista.title(), "Album": album.title(), "id": id, "contatore": contatore }
        if self.json_data != None:

            self.json_data.append(oggettobrano)
            with open("info_brani.json", "w") as write_file:
                json.dump(self.json_data, write_file)

        else:
            self.json_data = oggettobrano
            with open("info_brani.json", "w") as write_file:
                json.dump(self.json_data, write_file)


    '''Metodo che ritorna l'id corrispondente di un brano dati titolo e album'''
    def ricerca_id(self, titolo, album):
        U = self.json_data
        for i in U:
            if (i["Titolo"] == titolo) and (i["Album"] == album):
                ID = i["id"]
        return ID



    '''Metodo che incrementa il valore della chiave CONTATORE a seguito di riproduzioni musicali.
       Sovrascittura del file per il suo aggiornamento'''
    def incremento_conta(self, titolo, album):
        data = self.json_data
        posi = 0
        for i in data:
            posi =posi + 1
            if (i["Titolo"] == titolo) and (i["Album"] == album):
                i["contatore"] += 1.0
                data[posi-1] = i
                break

        with open("info_brani.json", "w") as write_file:
            json.dump(data, write_file)



    '''Metodo ritorna l'id corrispondente ad un titolo di un brano.
       Utilizzato per la statistica I MIEI BRANI'''
    def getTitolo_da_Id(self, id):
        titolo =""
        for i in self.json_data:
            if i["id"] == float(id):
                titolo = i["Titolo"]
        return titolo



    def elimina_object(self, nome_artista, titolo_brano):
        for i in self.json_data:
            if nome_artista==i["Artista"] and titolo_brano==i["Titolo"]:
                mp3 = Gestione_mp3()
                id = self.ricerca_id(i["Titolo"], i["Album"])
                mp3.Elimina_mp3(id)
                if i is self.json_data[len(self.json_data)-1]:
                    self.decrementa_conta_id()

                self.json_data.remove(i)
                with open("info_brani.json", "w") as write_file:
                    json.dump(self.json_data, write_file)
                break




    def decrementa_conta_id(self):
        with open('ContatoreBrani.json', 'r') as j:
            self.json_conta_id = json.load(j)

        self.json_conta_id["contatore_id"] = self.json_conta_id["contatore_id"] - 1
        with open("ContatoreBrani.json", "w") as write_file:
            json.dump(self.json_conta_id, write_file)






    '''Metodo che ritorna l'attributo json_data'''
    def get_jsonobject(self):
        return self.json_data