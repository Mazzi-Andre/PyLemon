import operator

class TopFive():

    def json_to_list(self, json_data):
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

        self.Top5.remove(self.Top5[len(self.Top5)-1]) # ultima posizione rimossa fuor da while perchè qua dentro non veniva rimossa anche
        return self.Top5                              # se la condizione del while era i<=len(self.Top5)-1














