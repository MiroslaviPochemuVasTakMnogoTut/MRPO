from employee import Employee

class Courier(Employee):
    def __init__(self, name, birthdate, phone):
        super().__init__(name, birthdate, phone=phone)
        self.id = None
        self.vehicle_type
        self.vehicle_number
        self.delivery_orders = []
        self.current_location = None

    def assign_order(self, order):
        self.delivery_orders.append(order)

    def unassign_order(self, order):
        self.delivery_orders.remove(order)

    def update_location(self, location):
        self.current_location = location

    def get_delivery_time(self, order, distance):
        # calculate delivery time based on distance and delivery speed
        pass
