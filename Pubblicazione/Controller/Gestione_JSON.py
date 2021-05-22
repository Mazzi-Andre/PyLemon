
import json


class Gestione_JSON(object):

    def __init__(self):

    '''def lettura(self):
        with open('info_brani.json', 'r') as j:
            json_data = json.load(j)
            return json_data'''
        '''with open('lista_servizi_iniziali') as f:
            lista_servizi_iniziale = json.load(f)'''

    def carica_brano_su_JSON(self, brano):
        oggettobrano = {"Titolo": brano.nome, "Artista": brano.artista, "Album": brano.album, "id": brano.id, "contatore": brano.contatore }
        if self.json_data != None:
            self.json_data[self.json_data.len + 1] = oggettobrano
            with open("info_brani.json.json", "w") as write_file:
                json.dump(self.json_data, write_file)

        else:
            self.json_data = oggettobrano
            with open("info_brani.json.json", "w") as write_file:
                json.dump(self.json_data, write_file)


    #def elimina_brano_su_JSON(self,id):




    def ricerca_id(self, titolo, album):
        U = self.json_data['brani']
        for i in U.len:
            if U[i].get['titolo'] == titolo:
                if U[i].get['album'] == album:
                    ID = U[i].get['id']
        else: ID = 0
        return ID

    def get_jsonobject(self):
        return self.json_data

o=Gestione_JSON()
print(o.lettura())
