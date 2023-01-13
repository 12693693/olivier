class Batteries():
    def __init__(self, capacity, x, y):
        self.capacity = capacity
        self.x = x
        self.y = y
        self.output = 0
        self.color = 'blue'
    #
    # def plot_batteries(self):
    #     print(self.x, self.y)
    #     plt.plot(self.x, self.y, 'bo')


#
#     def add_house(self, x, y, maxoutput):
#         # check of de output niet teveel wordt voor de batterij bij het toevoegen van een huis
#         self.output += maxoutput
#         if self.output < self.capacity:
#           # lijntje trekken
#
