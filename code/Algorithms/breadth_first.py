import random
import math
import numpy as np
from .search_cables import Search_Cables
import matplotlib.pyplot as plt

make_rest_of_cables = Search_Cables()

class Breadth_first():
    def compute_distance(self, x_battery, y_battery, x_loc, y_loc):
        ''' this function computes the distance between the battery and the starting
        location on the x and y axis '''

        x_distance = int(x_battery) - int(x_loc)
        y_distance = int(y_battery) - int(y_loc)

        return x_distance, y_distance

    def set_locs(self, battery, i):
        ''' this function finds the house dictionary and the location of the
        starting point of the cable, and appends this location in the cables
        dictionary. It also fills the x and y list with the starting point '''

        # initiate list in which to keep track of the x and y coordinates of the cables
        x_list = []
        y_list = []

        # find the house dictionary
        house_dict = battery.dict['houses'][i]

        # find x and y coordinates of the starting point (house location) of the cable
        x_loc = int(house_dict['location'].split(',')[0])
        y_loc = int(house_dict['location'].split(',')[1])

        # save starting point for the cable
        house_dict['cables'].append(f'{x_loc}, {y_loc}')

        # append list with x and y coordinates of the cable starting point
        x_list.append(x_loc)
        y_list.append(y_loc)

        return house_dict, x_loc, y_loc, x_list, y_list

    def create_cables(self, x_distance, y_distance, house_dict):
        ''' this function creates a list with the steps that should be taken
        to form the cable from the house to the battery. It also creates 10
        random cables and saves a list with each possible cable. '''

        steps_list = []

        # create steps list for the steps that should be taken
        if x_distance < 0:
            for i in range(abs(x_distance)):
                steps_list.append('L')
        else:
            for i in range(x_distance):
                steps_list.append('R')

        if y_distance < 0:
            for i in range(abs(y_distance)):
                steps_list.append('D')
        else:
            for i in range(y_distance):
                steps_list.append('U')

        possible_cables = []

        # create 10 cables
        for i in range(10):

            # shuffle the steps in the list randomly
            random.shuffle(steps_list)
            cables_list = []

            # set location back to starting point before creating new cable
            x_loc = int(house_dict['location'].split(',')[0])
            y_loc = int(house_dict['location'].split(',')[1])

            # take the random order of steps
            for step in steps_list:
                if step == 'L':
                    x_loc -= 1
                elif step == 'R':
                    x_loc += 1
                elif step == 'D':
                    y_loc -= 1
                else:
                    y_loc += 1

                # fill list containing steps for one cable
                cables_list.append(f'{x_loc}, {y_loc}')

            # list containing each cable list of steps
            possible_cables.append(cables_list)

            return possible_cables, house_dict

    def distance_to_cable(self, possible_cables, battery):
        ''' this function loops over all possible cables, calculates the distances
        between each house assinged to that battery and the cable. It saves a list
        containing all the shortest distances from the houses to the cable '''

        list_distances_all_cables = []

        # loop over cables
        for cable in possible_cables:
            distance_to_cable_list = []

            # loop over house_dicts
            for house_dict_2 in battery.dict['houses']:
                x_house = int(house_dict_2['location'].split(',')[0])
                y_house = int(house_dict_2['location'].split(',')[1])

                distance = math.inf

                # loop over each step in the grid, and calculate distance between
                # the current house and the cable
                for step in cable:
                    x_loc = float(step.split(', ')[0])
                    y_loc = float(step.split(', ')[1])

                    # calculate current_distance
                    current_distance = abs(x_house - x_loc) + abs(y_house - y_loc)

                    # save the closest distance from the house to the cable
                    if current_distance < distance:
                        distance = current_distance

                # keep track of the shortest distance to the cable
                distance_to_cable_list.append(distance)

            # keep track of the distances for all the cables for one battery
            list_distances_all_cables.append(distance_to_cable_list)


            return list_distances_all_cables

    def choose_best_cable(self, list_distances_all_cables, possible_cables, house_dict, x_list, y_list):
        ''' this function calculates the total distance from the cable to the
        houses that are connected to the same battery, and finds the smallest distance.
        this cable is then chosen as the best cable. Then the steps of the best
        cable are saved to the x and ylist.'''

        lowest_distance = math.inf

        # loop over all possible cables
        for index, cable_distance_list in enumerate(list_distances_all_cables):

            # compute the total distance from the cable to all the other houses
            total_distance = sum(cable_distance_list)

            # when the distance is the smallest, define that cbale as the best cable
            if total_distance < lowest_distance:
                best_cable = possible_cables[index]
                lowest_distance = total_distance
                house_dict['cables'] = best_cable

        # save the seps of the best cable to the x and y list
        for step in best_cable:
            x_loc = float(step.split(', ')[0])
            y_loc = float(step.split(', ')[1])

            x_list.append(x_loc)
            y_list.append(y_loc)

        return x_list, y_list

    def breadth_first_5(self, list_with_houses, list_with_batteries):
        ''' this function executes breadth first algorithm on the first 5 houses
        of each battery. It makes 10 random paths from each house to the battery,
        and then chooses the best path based on the distance from the rest of the
        connected houses to that battery '''

        for battery in list_with_batteries:

            for i in range(5):
                # find the x_loc and y_loc and start the x and y list
                house_dict, x_loc, y_loc, x_list, y_list = self.set_locs(battery, i)

                # compute the distances on the x and y axes
                x_distance, y_distance = self.compute_distance(battery.x, battery.y, x_loc, y_loc)

                # create the 10 cables
                possible_cables, house_dict = self.create_cables(x_distance, y_distance, house_dict)

                # compute distances to the cables
                list_distances_all_cables = self.distance_to_cable(possible_cables, battery)

                # fill the x and y list with the steps of the best cable
                x_list, y_list = self.choose_best_cable(list_distances_all_cables, possible_cables, house_dict, x_list, y_list)




    def run(self, list_with_houses, list_with_batteries):
        ''' this function runs the experiment: it chooses the best cables for the
        first 5 houses per battery, and creates the rest of the cables using
        the search cables algorithm. '''

        self.breadth_first_5(list_with_houses, list_with_batteries)

        for battery in list_with_batteries:
            for house_dict in battery.dict['houses'][5:]:
                make_rest_of_cables.search_cables(house_dict, battery)
