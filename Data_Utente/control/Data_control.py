import pickle
import sqlite3

class DataPick(object):


    def put_data(self, nome, password):
        self.nome= nome
        self.password = password
        self.lista=[]
        self.lista.append(self.nome)
        self.lista.append(self.password)
        with open('Data.pkl', 'wb') as Dpi:
            pickle.dump(self.lista, Dpi)

    def get_data(self):
        with open('Data.pkl', 'rb') as Dpi:
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

    """ Funzione per la restituzione delle credenziali dell'account presente in questo momento """

    def return_credenziali(self):
        MyData = self.get_data()
        nome = MyData[0]
        pas = MyData[1]
        conn = sqlite3.connect('Data.db')
        cursor = conn.cursor()
        self.lista= []

        with conn:
            cursor.execute("""SELECT * FROM credentials WHERE username = :first AND password = :last""",
                           {'first': nome, 'last': pas})
            self.lista= cursor.fetchone()
            return self.lista

    """ DA TESTARE IL FUNZIONAMENTO """
    def delete_acount(self):
        MyData = self.get_data()
        nome = MyData[0]
        pas = MyData[1]
        conn = sqlite3.connect('Data.db')
        cursor = conn.cursor()

        with conn:
            cursor.execute("""DELETE * FROM credentials WHERE username = :first AND password = :last""",
                           {'first': nome, 'last': pas})

    """ DA TESTARE IL FUNZIONAMENTO """
    def update_account(self, newtipo):
        MyData = self.get_data()
        nome = MyData[0]
        pas = MyData[1]
        conn = sqlite3.connect('Data.db')
        cursor = conn.cursor()

        with conn:
            cursor.execute("""UPDATE credentials  SET tipo = :tipo WHERE username = :first AND password = :last""",
                           {'first': nome, 'last': pas, 'tipo': newtipo})