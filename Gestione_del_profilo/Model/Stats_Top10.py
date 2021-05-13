import operator
class TopTen:

    def __init__(self, dizio_contatori):
        self.dizio_contatori = dizio_contatori


    def Calcolo_Top10(self, dizio_contatori):
        Top10 = sorted(dizio_contatori.items(), key=operator.itemgetter(1))
        i = 10
        for i in Top10:
            Top10.remove(i)
        return Top10












