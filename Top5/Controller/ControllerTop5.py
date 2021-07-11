
class TopFive():

    def sort_lista_contatori(self, json_data):
        lista_contatori = []
        j = 0
        for i in json_data:
            lista_contatori.append(i["contatore"])
            if j>0:
                if lista_contatori[j-1] == lista_contatori[j]:
                    lista_contatori.pop(j)
            if j<len(lista_contatori):
                j = j+1
        lista_contatori.sort()
        lista_contatori.reverse()

        return lista_contatori












        dizio = {}
        for i in range(len(json_data)):
            posizione = json_data[i]
            appoggio = {str(i + 1): posizione["contatore"]}
            dizio = {**dizio, **appoggio}
        self.Top5 = sorted(dizio.items(), key=operator.itemgetter(1))
        self.Top5.reverse()

        if len(self.Top5) > 5:
            i = 5
            while i < (len(self.Top5)):
                self.Top5.remove(self.Top5[i])
                i = i + 1

        self.Top5.remove(self.Top5[len(self.Top5)-1])
        return self.Top5