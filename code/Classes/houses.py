class Houses():
    def __init__(self, x, y, maxoutput):
        self.maxoutput = maxoutput
        self.x = x
        self.y = y
        self.color = 'red'
        self.dict = {'house location': [self.x, self.y], 'house output': self.maxoutput, 'grid': []}
