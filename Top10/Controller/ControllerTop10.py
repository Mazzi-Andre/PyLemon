import operator
class TopTen():

    def json_to_list(self,json_data):
        appoggio = {}
        dizio = {}
        for i in range(len(json_data)):
            posizione = json_data[i]
            appoggio = {str(i+1) : posizione["contatore"]}
            dizio = {**dizio, **appoggio}
        self.Top5 = sorted(dizio.items(), key=operator.itemgetter(1))
        i = 5
        if len(self.Top5) > 5:
            for i in self.Top5:
                self.Top5.remove(i)
        return self.Top5

    '''def get_Top10_by_index(self, index):
        return self.Top5[index]'''











