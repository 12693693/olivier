import argparse
import pandas as pd
import matplotlib.pyplot as plt
import random
import copy
import json
from .houses import Houses
from .battery import Batteries
import os

class Smartgrid():
    def __init__(self, houses_df, batteries_df):

        self.houses_and_batteries = []
        # self.houses_list_per_batterie = []
        # self.battery_dict = {}
        self.district_cost_dict = {}
        self.combined_list = []
        self.add_houses_and_batteries(houses_df, batteries_df)
        #self.add_batteries(batteries_df)
        #self.add_houses(houses_df)


        # self.costs()
        # self.district_name()
        # self.create_district_dict()
        # self.make_output()
        #
        #
        # #self.assign_house_random() # CHECK
        # #self.make_cables()
        #
        #
        #
        # self.draw_plot()

    @classmethod
    def from_file(cls, houses_csv, batteries_csv):
        """
        This function loads the villages and saves them as dataframes
        """
        print('in classmethod')

        df_houses = pd.read_csv(houses_csv)
        df_batteries = pd.read_csv(batteries_csv)

        # create and fill lists of seperate coordinates for the batteries
        x_list = []
        y_list = []

        for index, row in df_batteries.iterrows():
            x = row[0].split(',')[0]
            y = row[0].split(',')[1]

            x_list.append(int(x))
            y_list.append(int(y))

        # modify the dataframe to add the lists and remove unnecessary columns
        df_batteries['x'] = x_list
        df_batteries['y'] = y_list
        df_batteries = df_batteries.drop('positie', axis=1)

        return Smartgrid(df_houses, df_batteries)


    def add_houses_and_batteries(self, houses_df, batteries_df):
        """
        This function creates a list with all battery instances as objects and
        adds them to a combined list of houses and batteries.
        """
        # create list in which to store the batteries
        self.battery_list = []
        self.house_list = []

        # create battery instances and saves them in a battery list and in
        # houses and batteries list
        for index, row in batteries_df.iterrows():
            battery = Batteries(row[0], row[1], row[2])
            self.houses_and_batteries.append(battery)
            self.battery_list.append(battery)


        # add house instances to the batteries and houses list and in the
        # houses list
        for index, row in houses_df.iterrows():
            house = Houses(row[0], row[1], row[2])
            self.houses_and_batteries.append(house)
            self.house_list.append(house)


        return self.house_list, self.battery_list

    # def add_batteries(self, batteries_df):
    #     """
    #     This function creates a list with all battery instances as objects and
    #     adds them to a combined list of houses and batteries.
    #     """
    #     # create list in which to store the batteries
    #     self.battery_list = []
    #
    #     # create battery instances and saves them in a battery list and in
    #     # houses and batteries list
    #     for index, row in batteries_df.iterrows():
    #         battery = Batteries(row[0], row[1], row[2])
    #         self.houses_and_batteries.append(battery)
    #         self.battery_list.append(battery)
    #
    #     return self.battery_list
    #
    #
    #
    #
    # def add_houses(self, houses_df):
    #     """
    #     This function creates a list with all house instances as objects and
    #     adds them to a combined list of houses and batteries.
    #     """
    #     # create list in which to store houses
    #     self.house_list = []
    #
    #     # add house instances to the batteries and houses list and in the
    #     # houses list
    #     for index, row in houses_df.iterrows():
    #         house = Houses(row[0], row[1], row[2])
    #         self.houses_and_batteries.append(house)
    #         self.house_list.append(house)
    #
    #     return self.house_list

    def draw_plot(self):
        """
        This function draws a plot of the houses and batteries in the village.
        """
        # create lists in which to store the information for the plot
        pos_x_list = []
        pos_y_list = []
        color_list = []
        shape_list = []

        # find x and y coordinates and the color of the thing to be plotted
        for thing in self.houses_and_batteries:
            pos_x_list.append(thing.x)
            pos_y_list.append(thing.y)
            color_list.append(thing.color)

        # plot all houses and batteries
        plt.scatter(pos_x_list, pos_y_list, color=color_list, marker='s', s=40)
        plt.show()
        plt.clf()

    #
    # def assign_house(self):
    #     for house in self.house_list:
    #         assign_house_not_random()


    # def assign_house_random(self):
    #     """
    #     This function assigns the houses to a randomly selected battery.
    #     """
    #     # randomly assign a battery to each house
    #     for house in self.house_list:
    #         assigned_battery = random.choice(self.battery_list)
    #
    #         # create copy of the battery list for later
    #         new_battery_list = copy.copy(self.battery_list)
    #
    #         # if the house doesn't fit the battery anymore, choose another battery
    #         while house.maxoutput > assigned_battery.capacity:
    #
    #             # make copy of battery_list and remove the full battery
    #             new_battery_list = copy.copy(new_battery_list)
    #             new_battery_list.remove(assigned_battery)
    #
    #             if len(new_battery_list) > 0:
    #                 # choose another battery
    #                 assigned_battery = random.choice(new_battery_list)
    #             else:
    #                 print('no battery left')
    #                 break
    #
    #         # adjust the capacity of the battery
    #         assigned_battery.capacity -= house.maxoutput
    #
    #         # save the dictionary of the house in the list of houses for that battery
    #         assigned_battery.dict['houses'].append(house.dict)
    #
    # def make_cables(self):
    #     """
    #     This function computes and plots the grid lines. It also keeps track of
    #     the individual steps within the grid. It then saves the individual
    #     coordinates in a new list.
    #     """
    #     self.steps_count = 0
    #     # loop over batteries and the houses that are connected to that battery
    #     for battery in self.battery_list:
    #         for house_dict in battery.dict['houses']:
    #
    #             # find x and y coordinates for the battery and connected house
    #             location_house_x = house_dict['location'][0]
    #             location_house_y = house_dict['location'][1]
    #             location_battery_x = battery.dict['location'][0]
    #             location_battery_y = battery.dict['location'][1]
    #
    #             x_list = [location_house_x, location_battery_x, location_battery_x]
    #             y_list = [location_house_y, location_house_y, location_battery_y]
    #             plt.plot(x_list, y_list, 'k--')
    #
    #             # create starting point for creating the grid line
    #             x_loc = location_house_x
    #             y_loc = location_house_y
    #
    #             # compute distance to use as a constraint for choosing which way
    #             # to move on the grid line
    #             distance_x = location_house_x - location_battery_x
    #             distance_y = location_house_y - location_battery_y
    #
    #             # take steps until the correct x coordinate is reached
    #             # and keep track of the steps
    #             while x_loc != location_battery_x:
    #                 if distance_x > 0:
    #                     x_loc -= 1
    #                 else:
    #                     x_loc += 1
    #                 self.steps_count += 1
    #
    #                 # save the individual steps in the grid list in the dictionary of the house
    #                 house_dict['grid'].append(f'{x_loc}, {y_loc}')
    #
    #             # take steps until the correct y coordinate is reached
    #             # and keep track of the grid line
    #             while y_loc != location_battery_y:
    #                 if distance_y > 0:
    #                     y_loc -= 1
    #                 else:
    #                     y_loc += 1
    #                 self.steps_count += 1
    #
    #                 # save the individual steps in the grid list in the dictionary of the house
    #                 house_dict['grid'].append(f'{x_loc}, {y_loc}')

    # def costs_own(self, steps_count):
    #     '''
    #     This function computes the total cost for the district if the cables are
    #     not shared.
    #     '''
    #
    #     self.battery_costs = len(self.battery_list) * 5000
    #     cable_costs = 0
    #
    #     for battery in self.battery_list:
    #         for house_dict in battery.dict['houses']:
    #             cable_costs += (len(house_dict['cables']) - 1) * 9
    #
    #     # cable_costs = steps_count * 9
    #
    #     self.total_cost = self.battery_costs + cable_costs
    #     #print(self.total_cost, 'aangemaakte costs')

    def get_costs(self, shared):
        '''
        This function computes the total cost for the district if the cables are
        shared.
        '''
        steps_set = set()
        steps_list = []

        #self.costs_own(10)
        #cable_costs = 0
        #print(self.total_cost)
        cable_segments = []

        for battery in self.battery_list:
            for house_dict in battery.dict['houses']:

                for cable_a, cable_b in zip(house_dict["cables"][:-1], house_dict["cables"][1:]):
                    cable_segments.append((cable_a, cable_b, battery))

        if shared == 'yes':
             cable_segments = list(set(cable_segments))

        cable_costs = 9 * len(cable_segments)
        battery_costs = 5000 * len(self.battery_list)
        self.total_cost = cable_costs + battery_costs
        print(self.total_cost, 'total costs')

        return self.total_cost


    def district_name(self):
        '''
        This function takes a users input as name for the district.
        '''

        self.district_name = input("What district are you using?: ")

    def make_f_string(self):
        for battery in self.battery_list:
            battery.dict['location'] = f'{int(battery.x)},{int(battery.y)}'

            for house_dict in battery.dict['houses']:
                location_x = house_dict['location'][0]
                location_y = house_dict['location'][1]

                house_dict['location'] = f'{int(location_x)},{int(location_y)}'
                #print(house_dict['location'])

    def create_district_dict(self, district, shared='yes'):
        '''
        This function combines the district name and costs in one dictionary.
        '''

        self.district_cost_dict['district'] = int(district)
        if shared == 'yes':
            self.district_cost_dict['costs-shared'] = self.total_cost
        else:
            self.district_cost_dict['costs-own'] = self.total_cost

    def make_output(self, district, shared):
        '''
        This function creates the final list with all information
        '''


        #self.make_f_string()
        # if shared == 'yes':
        #     self.costs_shared()
        # else:
        #     self.costs_own(10)
        costs = self.get_costs(shared)
        print('costs in output', costs)
        self.create_district_dict(district, shared)



        self.combined_list.append(self.district_cost_dict)

        for battery in self.battery_list:
            self.combined_list.append(battery.dict)

        json_list = json.dumps(self.combined_list)

        cur_path = os.path.dirname(__file__)

        with open(cur_path + '/../../resultaten/output.json', 'w') as outfile:
            outfile.write(json_list)


        return self.combined_list






cables_list = [] # CHECK!!!
house_dict = {} # location, output and cables of each house CHECK!!!
houses_list_per_battery = [] # the houses that are connected to that battery CHECK!!
battery_dict = {} #location, capacity and houses that are connected CHECK!!
district_cost_dict = {} # what district and cost
main_list = [] #battery_dict and district_cost_dict
