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

    def add_houses_and_batteries(self, houses_df, batteries_df):
        """
        This function creates a list with all battery instances as objects and
        adds them to a combined list of houses and batteries.
        """
        # Create list in which to store the batteries
        self.battery_list = []
        self.house_list = []

        # Create battery instances and saves them in a battery list and in
        # houses and batteries list
        for index, row in batteries_df.iterrows():
            battery = Batteries(row[0], row[1], row[2])
            self.houses_and_batteries.append(battery)
            self.battery_list.append(battery)

        # Add house instances to the batteries and houses list and in the
        # houses list
        for index, row in houses_df.iterrows():
            house = Houses(row[0], row[1], row[2])
            self.houses_and_batteries.append(house)
            self.house_list.append(house)


        return self.house_list, self.battery_list

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

    def create_district_dict(self, district, shared='yes'):
        '''
        This function combines the district name and costs in one dictionary.
        '''

        # Add the district number to the dictionary
        self.district_cost_dict['district'] = int(district)

        # Add the correct title and the total costs
        if shared == 'yes':
            self.district_cost_dict['costs-shared'] = self.total_cost
        else:
            self.district_cost_dict['costs-own'] = self.total_cost

    def make_output(self, district, shared):
        '''
        This function creates the final list with all information.
        '''

        # Calculate the costs and create the first dictionary of the district
        costs = self.get_costs(shared)
        self.create_district_dict(district, shared)

        self.combined_list = []
        self.combined_list.append(self.district_cost_dict)

        # Add each battery list to the combined list
        for battery in self.battery_list:
            self.combined_list.append(battery.dict)

        # Make a json file and add it to the output in the correct path
        json_list = json.dumps(self.combined_list)
        cur_path = os.path.dirname(__file__)
        with open(cur_path + '/../../resultaten/output.json', 'w') as outfile:
            outfile.write(json_list)
