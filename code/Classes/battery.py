class Batteries():
    def __init__(self, capacity, x, y):
        self.capacity = capacity
        self.x = x
        self.y = y
        self.output = 0
        self.color = 'blue'
        self.dict = {'battery location': [self.x, self.y], 'battery capacity': self.capacity, 'connected houses': []}
