import json
import os
from Brani.Model.Brano import Brano


class Gestione_JSON():

    def __init__(self):
        with open('ListaBrani.json', 'r') as j:
            self.json_data = json.load(j)


    def carica_brano_su_JSON(self, brano):
        oggettobrano = {"titolo": brano.nome, "artista": brano.artista, "album": brano.album, "id": brano.id, "contatore": brano.contatore }
        if self.json_data != None:
            self.json_data[self.json_data.len + 1] = oggettobrano
            with open("ListaBrani.json", "w") as write_file:
                json.dump(self.json_data, write_file)

        else:
            self.json_data = oggettobrano
            with open("ListaBrani.json", "w") as write_file:
                json.dump(self.json_data, write_file)


    def elimina_brano_su_JSON(self,id):




    def ricerca_id(self, titolo, album):
        U = self.json_data['brani']
        for i in U.len:
            if U[i].get['titolo'] == titolo:
                if U[i].get['album'] == album:
                    ID = U[i].get['id']
        else: ID = 0
        return ID
