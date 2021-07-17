import pickle
import sqlite3

class DataPick(object):

    """---Funzione dell'inserimento nome e password nel file Data.pkl---"""
    def put_data(self, nome, password):
        self.nome= nome
        self.password = password
        self.lista=[]
        self.lista.append(self.nome)
        self.lista.append(self.password)
        with open('Data\Database\Data.pkl', 'wb') as Dpi:
            pickle.dump(self.lista, Dpi)


    """---Funzione di lettura Data.pkl che restituisce nome e password---"""
    def get_data(self):
        with open('Data\Database\Data.pkl', 'rb') as Dpi:
            MyData = pickle.load(Dpi)
        return MyData


    """---Funzione per la restituzione delle credenziali dell'account presente in questo momento---"""
    def return_credenziali(self):
        MyData = self.get_data()
        nome = MyData[0]
        pas = MyData[1]
        conn = sqlite3.connect('Data\Database\Data.db')
        cursor = conn.cursor()
        self.lista= []

        with conn:
            cursor.execute("""SELECT * FROM credentials WHERE username = :first AND password = :last""",
                           {'first': nome, 'last': pas})
            self.lista= cursor.fetchone()
        return self.lista

    """---Funzione della rimozione dell'account utente--- """
    def delete_account(self, nome, pas):
        conn = sqlite3.connect('Data\Database\Data.db')
        cursor = conn.cursor()

        with conn:
            cursor.execute("""DELETE from credentials WHERE username = :first AND password = :last""",
                           {'first': nome, 'last': pas})

    """---Funzione per il cambiamento di tipologia utente---"""
    def update_account(self, newtipo):
        MyData = self.return_credenziali()
        nome = MyData[5]
        pas = MyData[6]
        conn = sqlite3.connect('Data\Database\Data.db')
        cursor = conn.cursor()

        with conn:
            cursor.execute("""UPDATE credentials  SET tipo = :tipo WHERE username = :first AND password = :last""",
                           {'first': nome, 'last': pas, 'tipo': newtipo})


    """---Funzione per il controllo della tipologia utente---"""
    def controlla_login(self):
        MyData = self.return_credenziali()

        tipo_utente = MyData[4]

        if tipo_utente == "ascoltatore" or tipo_utente == "Ascoltatore":
            return 1
        elif tipo_utente == "artista" or tipo_utente == "Artista":
            return 2
        elif tipo_utente == "etichetta" or tipo_utente == "Etichetta":
            return 3

