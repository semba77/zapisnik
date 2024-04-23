import pyodbc

class Facade:
    def __init__(self, connect):
        self.conn = pyodbc.connect(connect)
        self.cursor = self.conn.cursor()

    def find_all_tasks(self):
        try:
            self.cursor.execute(
            "SELECT udalost.*, typ_udalosti.typ_udalosti FROM udalost INNER JOIN typ_udalosti "
            "ON udalost.id_typu = typ_udalosti.id_typu WHERE typ_udalosti.typ_udalosti = 'ukol' ORDER BY udalost.datum_cas")

            return self.cursor.fetchall()
        except Exception as e:
            print("exeption ocured when reading from database:", e)

    def notebook(self, text):
        try:
            print(1)
            text = text.split(",")
            print(text)
            self.cursor.execute(f"select popis from udalost where popis = {text[0]}")
            myresult = self.cursor.fetchall()
            print("myresult:",myresult)
            print(2)
        except Exception as e:
            print("exeption ocured when reading from database:", e)
        if len(myresult) == 0:
            try:
                print(3)
                self.cursor.execute(f"insert into udalost(popis, datum_cas, id_typu) values ({text[0]}, {text[1]}, {text[2]});")
                print(4)
            except Exception as e:
                print("exeption ocured when uploding to database:", e)
        else:
            print("zaznam již existuje")
    def find_everything_for_date(self, datum):
        try:
            self.cursor.execute(f"SELECT * FROM udalost WHERE CAST(datum_cas AS DATE) = '{datum}'  ORDER BY datum_cas")

            return self.cursor.fetchall()
        except Exception as e:
            print("exeption ocured when reading from database:", e)

    def add_event(self,popis, datum, id_typu):
        try:
            self.cursor.execute(f"INSERT INTO udalost (popis, datum_cas, id_typu) VALUES ('{popis}', '{datum}', {id_typu})")
            self.conn.commit()
        except Exception as e:
            print("exeption ocured when reading from database:", e)
    def del_event(self, event):
        try:
            self.cursor.execute(f"delete from udalost where id_udalosti = {event}")
            self.conn.commit()
        except Exception as e:
            print("exeption ocured when reading from database:", e)


