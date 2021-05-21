import pickle
import sqlite3

class DataPick(object):


    def put_data(self, nome, password):
        self.nome= nome
        self.password = password
        self.lista=[]
        self.lista.append(self.nome)
        self.lista.append(self.password)
        with open('../Data/Data.pkl', 'wb') as Dpi:
            pickle.dump(self.lista, Dpi)

    def get_data(self):
        with open('../Data/Data.pkl', 'rb') as Dpi:
            MyData = pickle.load(Dpi)
        return MyData

    """ Funzione per la restituzione delle credenziali dell'account presente in questo momento """
    def return_credenziali(self):
        MyData= self.get_data()
        nome = MyData[0]
        pas = MyData[1]
        conn = sqlite3.connect('Data.db')
        cursor = conn.cursor()

        with conn:
            cursor.execute("""SELECT * FROM credentials WHERE username = :first AND password = :last""",  {'first': nome, 'last': pas })
            return cursor.fetchone()
