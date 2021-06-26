import json


class Gestione_json():

    def __init__(self):
        with open('info_brani.json', 'r') as j:
            self.json_data = json.load(j)


    '''def scrittura(self):
        with open("prova.Json", "w") as write_file:
            json.dump(self.oggetto, write_file)
        print("fatto")
        print(self.oggetto)'''  #manteniamo "carica_brano_su_JSON" ?

    def carica_brano_su_JSON(self, nome,artista,album,id,contatore):
        oggettobrano = {"Titolo": nome, "Artista": artista, "Album": album, "id": id, "contatore": contatore }
        if self.json_data != None:
            i=len(self.json_data)

            self.json_data.append(oggettobrano)
            with open("info_brani.json", "w") as write_file:
                json.dump(self.json_data, write_file)

        else:
            self.json_data = oggettobrano
            with open("info_brani.json", "w") as write_file:
                json.dump(self.json_data, write_file)

    def ricerca_id(self, titolo, album):
        U = self.json_data
        for i in U:
            if (i["Titolo"] == titolo) and (i["Album"] == album):
                ID = i["id"]
        return ID


    def get_jsonobject(self):
        return self.json_data

