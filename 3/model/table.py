class Table:
    def __init__(self, number: int):
        self.id = None
        self.number = number
        self.capacity = 4
        self.is_available = True
        self.waiter :str= ''
        
    def mark_as_available(self):
        self.is_available = True
        self.order = None
    
    def mark_as_unavailable(self, waiter):
        self.is_available = False
        self.waiter = waiter

    def __eq__(self, other):
        if not isinstance(other, Table):
            return False
        return self.number == other.number and self.capacity == other.capacity