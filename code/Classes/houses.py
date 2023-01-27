class Houses():
    def __init__(self, x, y, maxoutput):
        self.maxoutput = maxoutput
        self.x = x
        self.y = y
        self.color = 'red'
        self.dict = {'location': [self.x, self.y], 'output': self.maxoutput, 'cables': []}
