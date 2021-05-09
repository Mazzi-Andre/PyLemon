import sqlite3
from Registrazione.model.Utente import Utente

conn = sqlite3.connect("Utenti.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Utenti (
            nome text,
            cognome text,
            eta integer,
            username text,
            password text,
            email text,
            tipo text
            )""")

u1 = Utente('Andre', 'Mazzi', 20, 'anda00', 'prova', 'cicciopierino', 'artista')

c.execute("INSERT INTO Utenti VALUES ('Andre', 'Mazzi', 20, 'anda00', 'prova', 'cicciopierino', 'artista' )")
#c.execute("INSERT INTO employees VALUES ('Corey', 'pluto', 'Schafer', 50000)")

c.execute("SELECT * FROM Utenti WHERE cognome ='Mazzi'")

result = (c.fetchone())
prova = result
print(result[1])
print(prova[1])

#conn.commit()

conn.close()
