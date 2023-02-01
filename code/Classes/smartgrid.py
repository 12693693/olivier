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
        self.district_cost_dict = {}
        self.combined_list = []
        self.batteries_list = []
        self.houses_list = []
        self.add_houses_and_batteries(houses_df, batteries_df)
    #
    # @classmethod
    # def from_file(cls, houses_csv, batteries_csv):
    #     """
    #     This function loads the villages and saves them as dataframes
    #     """
    #     print('in classmethod')
    #
    #     df_houses = pd.read_csv(houses_csv)
    #     df_batteries = pd.read_csv(batteries_csv)
    #
    #     # create and fill lists of seperate coordinates for the batteries
    #     x_list = []
    #     y_list = []
    #
    #     for index, row in df_batteries.iterrows():
    #         x = row[0].split(',')[0]
    #         y = row[0].split(',')[1]
    #
    #         x_list.append(int(x))
    #         y_list.append(int(y))
    #
    #     # modify the dataframe to add the lists and remove unnecessary columns
    #     df_batteries['x'] = x_list
    #     df_batteries['y'] = y_list
    #     df_batteries = df_batteries.drop('positie', axis=1)
    #
    #     return Smartgrid(df_houses, df_batteries)


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
    #
    # def draw_plot(self):
    #     """
    #     This function draws a plot of the houses and batteries in the village.
    #     """
    #     # create lists in which to store the information for the plot
    #     pos_x_list = []
    #     pos_y_list = []
    #     color_list = []
    #     shape_list = []
    #
    #     # find x and y coordinates and the color of the thing to be plotted
    #     for thing in self.houses_and_batteries:
    #         pos_x_list.append(thing.x)
    #         pos_y_list.append(thing.y)
    #         color_list.append(thing.color)
    #
    #     # plot all houses and batteries
    #     plt.scatter(pos_x_list, pos_y_list, color=color_list, marker='s', s=40)
    #     plt.show()
    #     plt.clf()

    def get_costs(self, shared):
        '''
        This function computes the total cost for the district.
        '''
        cable_segments = []

        for battery in self.battery_list:
            for house_dict in battery.dict['houses']:

                # make a tuple for every pair consequitive cable segments for
                # each battery and add them to a list
                for cable_a, cable_b in zip(house_dict["cables"][:-1], house_dict["cables"][1:]):
                    cable_segments.append((cable_a, cable_b, battery))

        # remove duplicates if you want to share the cable costs
        if shared == 'yes':
             cable_segments = list(set(cable_segments))

        # calculate the total costs
        cable_costs = 9 * len(cable_segments)
        battery_costs = 5000 * len(self.battery_list)
        self.total_cost = cable_costs + battery_costs

        return self.total_cost


    # def district_name(self):
    #     '''
    #     This function takes a users input as name for the district.
    #     '''
    #
    #     self.district_name = input("What district are you using?: ")

    # def make_f_string(self):
    #     for battery in self.battery_list:
    #         battery.dict['location'] = f'{int(battery.x)},{int(battery.y)}'
    #
    #         for house_dict in battery.dict['houses']:
    #             location_x = house_dict['location'][0]
    #             location_y = house_dict['location'][1]
    #
    #             house_dict['location'] = f'{int(location_x)},{int(location_y)}'

    def create_district_dict(self, district, shared='yes'):
        '''
        This function combines the district name and costs in one dictionary.
        '''

        # add the district number to the dictionary
        self.district_cost_dict['district'] = int(district)

        # add the correct title and the total costs
        if shared == 'yes':
            self.district_cost_dict['costs-shared'] = self.total_cost
        else:
            self.district_cost_dict['costs-own'] = self.total_cost

    def make_output(self, district, shared):
        '''
        This function creates the final list with all information
        '''

        # calculate the costs and create the first dictionary of the district
        costs = self.get_costs(shared)
        self.create_district_dict(district, shared)


        self.combined_list = []
        self.combined_list.append(self.district_cost_dict)

        # add each battery list to the combined list
        for battery in self.battery_list:
            self.combined_list.append(battery.dict)

        # make a json file and add it to the output in the correct path
        json_list = json.dumps(self.combined_list)
        cur_path = os.path.dirname(__file__)
        with open(cur_path + '/../../resultaten/output.json', 'w') as outfile:
            outfile.write(json_list)


        return self.combined_list
