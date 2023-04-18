from employee import Employee
from table import Table

class Waiter(Employee):
    def __init__(self, name, birthdate, phone):
        super().__init__(name, birthdate, phone)
        self.tables_served = []

    def serve_table(self, table:Table):
        if table.is_available:
            table.mark_as_unavailable(self)
            self.tables_served.append(table)
            return f"Table {table.number} is now served by {self.name}."
        else:
            return f"Table {table.number} is already served by {table.order.waiter.name}."
