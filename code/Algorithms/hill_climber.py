from .randomize import Randomize
from .cable_90_degree import Cables_90
from .random_try import Cables
from .search_cables import Search_Cables
from ..Classes.smartgrid import Smartgrid
import random
import copy

cable_90_degree = Cables_90()
cable_random = Cables()
search_cables = Search_Cables()


class Hill_Climber():
    def __init__(self, smartgrid_solution, shared):
        self.smartgrid = copy.deepcopy(smartgrid_solution)
        self.shared = shared

        self.costs = self.smartgrid.get_costs(self.shared)


    def fill_new_grid(self, house_dict, battery, function):

        function_dict = {'cable_90_degree.make_90_degrees_cables(houses, batteries)': 'cable_90_degree.make_90_degrees_cable(house_dict, battery)', 'cable_random.random_try(houses, batteries)': 'cable_random.random_try(house_dict, battery)', 'search_cables.run_search(houses, batteries)' : 'search_cables.search_cables(house_dict, battery)'}
        #print('function', function_dict[function])
        # fill the grid of the newly added houses

        #print(house_dict, battery)

        #print(eval(function_dict[function]))
        #print(cable_90_degree.make_90_degrees_cable(house_dict, battery))
        return eval(function_dict[function])

    def check_capacity(self, battery_1, battery_2, house_1, house_2):
        if battery_1.capacity + house_1['output'] - house_2['output'] >= 0 and battery_2.capacity + house_2['output'] - house_1['output'] >= 0:

            return True

        else:
            return False

    def choose_battery_and_houses(self, list_with_batteries):

        # choose two random batteries
        self.battery_1 = random.choice(list_with_batteries)
        self.battery_2 = random.choice(list_with_batteries)

        while self.battery_1 == self.battery_2:
            self.battery_2 = random.choice(list_with_batteries)

        # choose two houses that were assigned to the batteries and remove them
        # and the steps count from the costs
        self.house_1 = random.choice(self.battery_1.dict['houses'])
        self.house_2 = random.choice(self.battery_2.dict['houses'])


    def switch_two_houses(self, new_smartgrid, function):
        list_with_batteries = new_smartgrid.battery_list

        self.choose_battery_and_houses(list_with_batteries)

        #print(house_1)
        #print(self.check_capacity(self.battery_1, self.battery_2, self.house_1, self.house_2))
        while self.check_capacity(self.battery_1, self.battery_2, self.house_1, self.house_2) == False:
            #print(self.check_capacity(self.battery_1, self.battery_2, self.house_1, self.house_2))
            self.choose_battery_and_houses(list_with_batteries)

        else:
            #print(self.check_capacity(self.battery_1, self.battery_2, self.house_1, self.house_2))
            self.battery_1.dict['houses'].remove(self.house_1)
            self.battery_2.dict['houses'].remove(self.house_2)


            # dit mag nog anders
            self.new_costs = new_smartgrid.total_cost - (len(self.house_1['cables']) - 1) - (len(self.house_2['cables']) - 1)
            #self.smartgrid.combined_list[0]['costs shared'] - (len(house_1['grid']) - 1) - (len(house_2['grid']) - 1)

            # reset the grid
            self.house_1['cables'] = []
            self.house_2['cables'] = []

            # fill the grid of the houses
            # string_function_1 = f'{self.fill_new_grid(function)}({self.house_1}, {self.battery_2})'
            # print('string', string_function_1)
            # self.steps_house_1 = eval(string_function_1)
            # string_function_2 = self.fill_new_grid(self.house_2, self.battery_1, function)
            # self.steps_house_2 = eval(string_function_2)

            self.steps_house_1 = self.fill_new_grid(self.house_1, self.battery_2, function)
            self.steps_house_2 = self.fill_new_grid(self.house_2, self.battery_1, function)

            # switch the houses and add them to a new battery
            self.battery_1.dict['houses'].append(self.house_2)
            self.battery_2.dict['houses'].append(self.house_1)

    def check_solution(self, new_smartgrid):
        #print('oud zonder', self.new_costs)
        self.new_costs = new_smartgrid.get_costs(self.shared)
        #print('nieuw', self.new_costs)

        if self.new_costs <= self.costs:
            self.smartgrid = new_smartgrid
            self.costs = self.new_costs

    def run(self, iterations, function):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.costs}')

            # Create a copy of the graph to simulate the change
            new_smartgrid = copy.deepcopy(self.smartgrid)

            self.switch_two_houses(new_smartgrid, function)
            #print('na switchen')

            # Accept it if it is better
            self.check_solution(new_smartgrid)

















        # switch the assigned batteries of the houses

    #Kies een random start state


    #Herhaal:
    #Doe een kleine random aanpassing
#Als de state is verslechterd:
#Maak de aanpassing ongedaan
