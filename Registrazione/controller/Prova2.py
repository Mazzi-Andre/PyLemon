import sqlite3

class Controller():

    def __init__(self):
        self.conn = sqlite3.connect("employee.db")
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS employees (
                nome text,
                cognome text,
                inirizzo text,
                pay integer
                )""")


    self.c.execute("INSERT INTO employees VALUES ('Corey', 'pippo', 'Schafer', 50000)")
    c.execute("INSERT INTO employees VALUES ('Corey', 'pluto', 'Schafer', 50000)")

    c.execute("SELECT * FROM employees WHERE cognome ='pippo'")

    print(c.fetchall())

    conn.commit()

    conn.close()
