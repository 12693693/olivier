from .randomize import Randomize
import random
import copy

class Hill_Climber():
    def __init__(self, smartgrid_solution):
        self.smartgrid = copy.deepcopy(smartgrid_solution)

    def fill_new_grid(self, house_dict, battery):

        # fill the grid of the newly added houses


    def switch_two_houses(self, list_with_batteries):

        # choose two random batteries
        battery_1 = random.choice(list_with_batteries)
        battery_2 = random.choice(list_with_batteries)

        # choose two houses that were assigned to the batteries
        house_1 = random.choice(battery_1.dict['connected houses'])
        house_2 = random.choice(battery_2.dict['connected houses'])

        # reset the grid
        house_1['grid'] = []
        house_2['grid'] = []

        # fill the grid of the houses
        house_1['grid'] = fill_new_grid(house_1, battery_2)
        house_2['grid'] = fill_new_grid(house_2, battery_1)

        # switch the houses and add them to a new battery
        battery_1.dict['connected houses'].append(house_2)
        battery_2.dict['connected houses'].append(house_1)












        # switch the assigned batteries of the houses

    #Kies een random start state


    #Herhaal:
    #Doe een kleine random aanpassing
#Als de state is verslechterd:
#Maak de aanpassing ongedaan
