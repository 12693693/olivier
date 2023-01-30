class Batteries():
    def __init__(self, capacity, x, y):
        self.capacity = capacity
        self.x = x
        self.y = y
        self.color = 'blue'
        self.dict = {'location': f'{int(self.x)},{int(self.y)}', 'capacity': self.capacity, 'houses': []}
