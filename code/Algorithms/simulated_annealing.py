import random
import math

from .hill_climber import Hill_Climber

class Simulated_Annealing(Hill_Climber):

    def __init__(self, smartgrid_solution, shared, temperature=1):
        # use the init of the Hillclimber class
        super().__init__(smartgrid_solution, shared)

        # starting temperature and current temperature
        self.T0 = temperature
        self.T = temperature


    def update_temperature(self):
        """
        This function implements a linear cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """

        self.T = self.T - (self.T0 / self.iterations)

    def check_solution(self, new_smartgrid):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        self.new_costs = new_smartgrid.get_costs(self.shared)

        # calculate the probability of accepting this new smartgrid
        delta = self.new_costs - self.costs
        print(-delta / self.T)
        probability = math.exp(-delta / self.T)


        # pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.smartgrid = new_smartgrid
            self.costs = self.new_costs

        # update the temperature
        self.update_temperature()
