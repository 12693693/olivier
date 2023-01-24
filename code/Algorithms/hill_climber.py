from .randomize import Randomize
from .cable_90_degree import Cables
from ..Classes.smartgrid import Smartgrid
import random
import copy

make_cables = Cables()
#my_smartgrid = Smartgrid()


class Hill_Climber():
    def __init__(self, smartgrid_solution):
        self.smartgrid = copy.deepcopy(smartgrid_solution)
        self.costs = self.smartgrid.total_cost

    def fill_new_grid(self, house_dict, battery):

        # fill the grid of the newly added houses
        return make_cables.make_90_degrees_cable(house_dict, battery)


    def switch_two_houses(self, new_smartgrid):
        list_with_batteries = new_smartgrid.battery_list

        # choose two random batteries
        battery_1 = random.choice(list_with_batteries)
        battery_2 = random.choice(list_with_batteries)

        while battery_1 == battery_2:
            battery_2 = random.choice(list_with_batteries)    

        # choose two houses that were assigned to the batteries and remove them
        # and the steps count from the costs
        house_1 = random.choice(battery_1.dict['connected houses'])
        house_2 = random.choice(battery_2.dict['connected houses'])

        battery_1.dict['connected houses'].remove(house_1)
        battery_2.dict['connected houses'].remove(house_2)


        # dit mag nog anders
        self.new_costs = new_smartgrid.total_cost - (len(house_1['grid']) - 1) - (len(house_2['grid']) - 1)
        #self.smartgrid.combined_list[0]['costs shared'] - (len(house_1['grid']) - 1) - (len(house_2['grid']) - 1)

        # reset the grid
        house_1['grid'] = []
        house_2['grid'] = []

        # fill the grid of the houses
        self.steps_house_1 = self.fill_new_grid(house_1, battery_2)
        self.steps_house_2 = self.fill_new_grid(house_2, battery_1)

        # switch the houses and add them to a new battery
        battery_1.dict['connected houses'].append(house_2)
        battery_2.dict['connected houses'].append(house_1)

    def check_solution(self, new_smartgrid):
        #print('oud zonder', self.new_costs)
        self.new_costs += self.steps_house_1 + self.steps_house_2
        #print('nieuw', self.new_costs)

        if self.new_costs <= self.costs:
            self.smartgrid = new_smartgrid
            self.costs = self.new_costs

    def run(self, iterations):
        """
        Runs the hillclimber algorithm for a specific amount of iterations.
        """
        self.iterations = iterations

        for iteration in range(iterations):
            # Nice trick to only print if variable is set to True
            print(f'Iteration {iteration}/{iterations}, current value: {self.costs}')

            # Create a copy of the graph to simulate the change
            new_smartgrid = copy.deepcopy(self.smartgrid)

            self.switch_two_houses(new_smartgrid)

            # Accept it if it is better
            self.check_solution(new_smartgrid)

















        # switch the assigned batteries of the houses

    #Kies een random start state


    #Herhaal:
    #Doe een kleine random aanpassing
#Als de state is verslechterd:
#Maak de aanpassing ongedaan
