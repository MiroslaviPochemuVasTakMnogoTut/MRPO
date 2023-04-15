class Table:
    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.is_available = True
        self.order = None
        
    def mark_as_available(self):
        self.is_available = True
        self.order = None
    
    def mark_as_unavailable(self, order):
        self.is_available = False
        self.order = order
