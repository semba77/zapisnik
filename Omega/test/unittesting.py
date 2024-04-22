import unittest
from unittest.mock import Mock
from src.facade import Facade
import src.change_UI4F

class TestFacade(unittest.TestCase):

    def setUp(self):
        self.mock_conn = Mock()
        self.mock_cursor = Mock()
        self.mock_conn.cursor.return_value = self.mock_cursor
        self.facade = Facade(host="LAPTOP-4E70P610\SQLEXPRESS", database="Omega")
        self.facade.conn = self.mock_conn

    def test_find_all_tasks(self):

        expected_result = [('task1', '2024-04-21 09:00:00'), ('task2', '2024-04-22 10:00:00')]
        self.mock_cursor.fetchall.return_value = expected_result

        result = self.facade.find_all_tasks()

        self.mock_cursor.execute.assert_called_once_with(
            "SELECT udalost.*, typ_udalosti.typ_udalosti FROM udalost INNER JOIN typ_udalosti "
            "ON udalost.id_typu = typ_udalosti.id_typu WHERE typ_udalosti.typ_udalosti = 'ukol' ORDER BY udalost.datum_cas")

        self.assertEqual(result, expected_result)



if __name__ == '__main__':
    unittest.main()