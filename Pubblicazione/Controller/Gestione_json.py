import json


class Gestione_json():

    def __init__(self):
        with open('info_brani.json', 'r') as j:
            self.json_data = json.load(j)

    def carica_brano_su_JSON(self, nome,artista,album,id,contatore):
        oggettobrano = {"Titolo": nome.title(), "Artista": artista.title(), "Album": album.title(), "id": id, "contatore": contatore }
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


    def getTitolo_da_Id(self, id):
        titolo =""
        for i in self.json_data:
            if i["id"] == float(id):
                titolo = i["Titolo"]
        return titolo

    def get_jsonobject(self):
        return self.json_data

