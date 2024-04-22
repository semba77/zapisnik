import pyodbc
import change_UI4F

class Facade:
    def __init__(self, server, user, password):
        self.conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE=Omega;UID="+user+";PWD="+password)
        self.cursor = self.conn.cursor()

    def find_all_tasks(self):
        try:
            self.cursor.execute(
            "SELECT udalost.*, typ_udalosti.typ_udalosti FROM udalost INNER JOIN typ_udalosti "
            "ON udalost.id_typu = typ_udalosti.id_typu WHERE typ_udalosti.typ_udalosti = 'ukol' ORDER BY udalost.datum_cas")

            return self.cursor.fetchall()
        except Exception as e:
            print("exeption ocured when reading from database:", e)

    def notebook(self):
        pass

    def find_everything_for_date(self, datum):
        try:
            self.cursor.execute(f"SELECT * FROM udalost WHERE CAST(datum_cas AS DATE) = '{datum}'  ORDER BY datum_cas")

            return self.cursor.fetchall()
        except Exception as e:
            print("exeption ocured when reading from database:", e)

    def add_event(self,popis, datum, id_typu):
        try:
            self.cursor.execute(f"INSERT INTO udalost (popis, datum_cas, id_typu) VALUES ('{popis}', '{datum}', {id_typu})")
        except Exception as e:
            print("exeption ocured when reading from database:", e)


