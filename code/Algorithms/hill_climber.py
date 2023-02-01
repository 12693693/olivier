from .random_connection import Randomize
from .cable_90_degree import Cables_90
from .random_cables import Cables
from .search_cables import Search_Cables
from .further_cables import Further_Cables
from ..Classes.smartgrid import Smartgrid
import random
import copy
import matplotlib.pyplot as plt

cable_90_degree = Cables_90()
cable_random = Cables()
search_cables = Search_Cables()
cable_further = Further_Cables()

class Hill_Climber():
    """
    The HillClimber class that switches a two random houses in the smartgrid.
    Each improvement or equivalent solution is kept for the next iteration.
    """

    def __init__(self, smartgrid_solution, shared):
        self.smartgrid = copy.deepcopy(smartgrid_solution)
        self.shared = shared

        self.costs = self.smartgrid.get_costs(self.shared)

    def fill_new_grid(self, house_dict, battery, function):
        """
        This function returns the function that is used for the laying the cables.
        """

        # Make a dictionary of every possible algoritm that can be used
        function_dict = {'cable_90_degree.make_90_degrees_cables(houses_list, batteries_list)': 'cable_90_degree.make_90_degrees_cable(house_dict, battery)', 'cable_random.run(houses_list, batteries_list)': 'cable_random.random_try(house_dict, battery)', 'search_cables.run_search(houses_list, batteries_list)' : 'search_cables.search_cables(house_dict, battery)', 'further_cables.run_further(houses_list, batteries_list)' : 'cable_further.further_cables(house_dict, battery)' }

        return eval(function_dict[function])

    def check_capacity(self, battery_1, battery_2, house_1, house_2):
        """
        This function returns if it is possible to change the houses without
        exceeding the battery capacity.
        """

        if battery_1.capacity + house_1['output'] - house_2['output'] >= 0 and battery_2.capacity + house_2['output'] - house_1['output'] >= 0:
            return True

        else:
            return False

    def choose_battery_and_houses(self, list_with_batteries):
        """
        This function chooses two houses that are going to be switched
        """

        # Choose two random batteries
        self.battery_1 = random.choice(list_with_batteries)
        self.battery_2 = random.choice(list_with_batteries)

        # Choose another battery if they are the same
        while self.battery_1 == self.battery_2:
            self.battery_2 = random.choice(list_with_batteries)

        # Choose two houses that were assigned to the batteries
        self.house_1 = random.choice(self.battery_1.dict['houses'])
        self.house_2 = random.choice(self.battery_2.dict['houses'])

    def switch_two_houses(self, new_smartgrid, function):
        """
        This function switches two houses and lays the new cables.
        """

        list_with_batteries = new_smartgrid.battery_list

        # Choose houses that are going to be switched
        self.choose_battery_and_houses(list_with_batteries)

        # Choose other houses if switching them exceeds the battery capacity
        while self.check_capacity(self.battery_1, self.battery_2, self.house_1, self.house_2) == False:
            self.choose_battery_and_houses(list_with_batteries)

        # Change the capacities of the batteries
        self.battery_1.capacity += (self.house_1['output'] - self.house_2['output'])
        self.battery_2.capacity += (self.house_2['output'] - self.house_1['output'])

        # Remove the houses from the batteries
        self.battery_1.dict['houses'].remove(self.house_1)
        self.battery_2.dict['houses'].remove(self.house_2)

        # Reset the cables
        self.house_1['cables'] = []
        self.house_2['cables'] = []

        # Add the houses to the other battery
        self.battery_1.dict['houses'].append(self.house_2)
        self.battery_2.dict['houses'].append(self.house_1)

        # Make new paths of cables using the cable algorithm that you choose
        self.fill_new_grid(self.house_1, self.battery_2, function)
        self.fill_new_grid(self.house_2, self.battery_1, function)

    def check_solution(self, new_smartgrid):
        """
        Checks and accepts better solutions than the current solution.
        """

        self.new_costs = new_smartgrid.get_costs(self.shared)

        # Accepts if the solution costs less
        if self.new_costs <= self.costs:
            self.smartgrid = new_smartgrid
            self.costs = self.new_costs

    def run(self, iterations, function):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """

        self.iterations = iterations
        cost_list = []

        for iteration in range(iterations):
            print(f'Iteration {iteration}/{iterations}, current value: {self.costs}')

            # Add the costs to cost_list (to later make an average)
            cost_list.append(self.costs)

            # Create a copy of the smartgrid to simulate the change
            new_smartgrid = copy.deepcopy(self.smartgrid)

            self.switch_two_houses(new_smartgrid, function)

            # Accept it if it is better
            self.check_solution(new_smartgrid)

            # for battery in self.smartgrid.battery_list:
            #     print(battery.capacity)

        return self.smartgrid, cost_list
