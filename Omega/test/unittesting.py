import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from src.facade import Facade
import pyodbc
import datetime

class TestFacade(unittest.TestCase):

    def setUp(self):
        self.conn = pyodbc.connect("DRIVER={{SQL Server}};SERVER={};DATABASE=Omega_test;Trusted_Connection=yes;".format("LAPTOP-4E70P610\SQLEXPRESS"))
        self.cursor = self.conn.cursor()
        self.fasade = Facade(self.conn)
    def test_find_all_tasks(self):
        results = list(self.fasade.find_all_tasks())
        self.assertEqual(type(results), list)
        for result in results:
            self.assertEqual(tuple(result),tuple)
            self.assertEqual(len(result),5)

            self.assertEqual(type(result[0]),int)
            self.assertEqual(type(result[1]),str)
            self.assertEqual(type(result[2]),datetime.datetime)
            self.assertEqual(type(result[3]),int)
            self.assertEqual(type(result[4]),str)

    def test_add_event(self, popis, date_time, typ):
        try:
            self.cursor.execute(f"INSERT INTO udalost (popis, datum_cas, id_typu) VALUES ('{popis}', '{date_time}', {typ})")
            self.fasade.conn.commit()

            self.cursor.execute(f"SELECT * FROM udalost WHERE popis = '{popis}'")
            inserted_row = self.cursor.fetchone()
            self.assertIsNotNone(inserted_row)

        except pyodbc.Error as e:
            self.fail("Chyba při vkládání do databáze: " + str(e))



if __name__ == '__main__':
    unittest.main()