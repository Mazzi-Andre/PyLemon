import pickle

class DataPick(object):

    def put_data(self, nome, password):
        self.nome= nome
        self.password = password
        self.lista=[]
        self.lista.append(self.nome)
        self.lista.append(self.password)
        with open('Data.pkl' , 'wb') as Dpi:
            pickle.dump(self.lista, Dpi)

    def get_data(self):
        with open('Data.pkl', 'rb') as Dpi:
            MyData = pickle.load(Dpi)
        return MyData