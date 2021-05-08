import operator
class TopTen:

    def __init__(self, lista_contatori):
        self.lista_contatori = lista_contatori


    def Calcolo_Top10(self, lista_contatori):
        Top10 = sorted(lista_contatori.items(), key=operator.itemgetter(1))
        i = 10
        for i in Top10:
            Top10.remove(i)
        return Top10













