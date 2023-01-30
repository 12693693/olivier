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
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """

        self.T = self.T - (self.T0 / self.iterations)

        # Exponential would look like this:
        # alpha = 0.99
        # self.T = self.T * alpha

        # where alpha can be any value below 1 but above 0

    def check_solution(self, new_smartgrid):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        self.new_costs += self.steps_house_1 + self.steps_house_2
        #old_value = self.costs

        # Calculate the probability of accepting this new graph
        delta = self.new_costs - self.costs
        probability = math.exp(-delta / self.T)

        # NOTE: Keep in mind that if we want to maximize the value, we use:
        # delta = old_value - new_value

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.smartgrid = new_smartgrid
            self.costs = self.new_costs

        # Update the temperature
        self.update_temperature()
