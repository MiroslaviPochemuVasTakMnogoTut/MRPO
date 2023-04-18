import unittest
from model.waiter import Waiter
from model.table import Table
class TestWaiter(unittest.TestCase):

    def test_serve_table_available(self):
        waiter = Waiter("John", "2000-01-01")
        table = Table(1)
        self.assertEqual(waiter.serve_table(table), f"Table {table.number} is now served by {waiter.name}.")

    def test_serve_table_unavailable(self):
        waiter1 = Waiter("John","2000-01-01")
        waiter2 = Waiter("Mike","2000-01-01")
        table = Table(1)
        waiter1.serve_table(table)
        self.assertEqual(waiter2.serve_table(table), f"Table {table.number} is already served by {waiter1.name}.")


    # def test_serve_table(self):
    #     # Arrange
    #     waiter = Waiter('John')
    #     table1 = Table(1)
    #     table2 = Table(2)
    #     # Act
    #     res1 = waiter.serve_table(table1)
    #     res2 = waiter.serve_table(table2)
    #     table1_status = table1.is_available
    #     table2_status = table2.is_available
    #     waiter_tables = waiter.tables_served
    #     # Assert
    #     self.assertEqual(res1, "Table 1 is now served by John.")
    #     self.assertEqual(res2, "Table 2 is now served by John.")
    #     self.assertFalse(table1_status)
    #     self.assertFalse(table2_status)
    #     self.assertEqual(waiter_tables, [table1, table2])
