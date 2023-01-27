locationclass Batteries():
    def __init__(self, capacity, x, y):
        self.capacity = capacity
        self.x = x
        self.y = y
        self.color = 'blue'
        self.dict = {'location': [self.x, self.y], 'capacity': self.capacity, 'houses': []}
