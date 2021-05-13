import operator
class TopTen:

    def __init__(self, Top10):
        super(Top10, self).__init__()
        self.model = Top10()


    def Calcolo_Top10(self, dizio_contatori):
        Top10 = sorted(dizio_contatori.items(), key=operator.itemgetter(1))
        i = 10
        for i in Top10:
            Top10.remove(i)
        return Top10

    def get_Top10_by_index(self, index):
        return self.model.Top10[index]












