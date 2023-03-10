import random
import math
from .hill_climber import Hill_Climber

class Simulated_Annealing(Hill_Climber):
    def __init__(self, smartgrid_solution, shared, temperature=1):
        # Use the init of the Hillclimber class
        super().__init__(smartgrid_solution, shared)

        # Starting temperature and current temperature
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

        # Calculate the probability of accepting this new smartgrid
        delta = self.new_costs - self.costs

        # Sometimes you get an error if the (-delta / self.T) is too positive so
        # if that happens make the possibility zero
        try:
            probability = math.exp(-delta / self.T)
        except:
            probability = 0

        # Pull a random number between 0 and 1 and see if we accept the smartgrid
        if random.random() < probability:
            self.smartgrid = new_smartgrid
            self.costs = self.new_costs

        # Update the temperature
        self.update_temperature()
