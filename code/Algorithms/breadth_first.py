import random
import math
import numpy as np
from .search_cables import Search_Cables
import matplotlib.pyplot as plt

make_rest_of_cables = Search_Cables()

class Breadth_first():


    def compute_distance(self, x_battery, y_battery, x_loc, y_loc):
        '''
        this function computes the distance between the battery and the starting
        location on the x and y axis
        '''
        x_distance = int(x_battery) - int(x_loc)
        y_distance = int(y_battery) - int(y_loc)


        return x_distance, y_distance

    def set_locs(self, battery, i):
        ''' this function finds the house dictionary and the location of the
        starting point of the cable, and appends this location in the cables
        dictionary. It also computes the distance on the x an '''

        x_list = []
        y_list = []
        house_dict = battery.dict['houses'][i]

        # for house_dict in battery.dict['connected houses']:
        # house_dict = battery.dict['connected houses'][0]
        # steps_list = []

        # find x and y coordinates for the battery and connected house
        x_loc = int(house_dict['location'].split(',')[0])
        y_loc = int(house_dict['location'].split(',')[1])

        # save starting point for the grid line
        house_dict['cables'].append(f'{x_loc}, {y_loc}')

        # create list with x and y coordinates of the grid line
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

                # x_list.append(x_loc)
                # y_list.append(y_loc)

                # list containing steps for one grid
                cables_list.append(f'{x_loc}, {y_loc}')

            # list containing each grids list of steps
            possible_cables.append(cables_list)

            return possible_cables, house_dict

    def distance_to_cable(self, possible_cables, battery):
        ''' this function loops over all possible cables, calculates the distances
        between each house assinged to that battery and the cable. It saves a list
        containing all the (shortest) distances from the houses to the cable '''
        list_distances_all_cables = []

        # loop over grids
        for cable in possible_cables:
            distance_to_cable_list = []
            # print(len(grid))
            # loop over house_dicts
            for house_dict_2 in battery.dict['houses']:
                x_house = int(house_dict_2['location'].split(',')[0])
                y_house = int(house_dict_2['location'].split(',')[1])

                distance = 100

                # loop over each step in the grid, and calculate distance between
                # the current house and the cable
                for step in cable:
                    x_loc = float(step.split(', ')[0])
                    y_loc = float(step.split(', ')[1])

                    # print('for step in grid')
                    # calculate current_distance
                    current_distance = abs(x_house - x_loc) + abs(y_house - y_loc)
                    # print('current distance')
                    if current_distance < distance:
                        distance = current_distance

                distance_to_cable_list.append(distance)
                # print('list of distances for one grid')
            list_distances_all_cables.append(distance_to_cable_list)
            # print('total list of distances all grids')

            return list_distances_all_cables

    def choose_best_cable(self, list_distances_all_cables, possible_cables, house_dict, x_list, y_list):

        lowest_distance = math.inf
        for index, cable_distance_list in enumerate(list_distances_all_cables):
            total_distance = sum(cable_distance_list)

            if total_distance < lowest_distance:
                best_grid = possible_cables[index]
                lowest_distance = total_distance
                house_dict['cables'] = best_grid

        # previous_x = 0
        # previous_y = 0
        #
        # x_list_scheef = []
        # y_list_scheef = []

        for step in best_grid:
            x_loc = float(step.split(', ')[0])
            y_loc = float(step.split(', ')[1])

            # if x_loc != previous_x and y_loc != previous_y and previous_x != 0 and previous_y != 0:
            #     print('scheef')

            x_list.append(x_loc)
            y_list.append(y_loc)

        return x_list, y_list

    def breadth_first_5(self, list_with_houses, list_with_batteries):
        ''' this function executes breadth first algorithm on the first 5 houses
        of each battery. It makes 10 random paths from each house to the battery,
        and then chooses the best path based on the distance from the rest of the
        connected houses to that battery '''

        for battery in list_with_batteries:
            # print('battery')
            for i in range(5):
                house_dict, x_loc, y_loc, x_list, y_list = self.set_locs(battery, i)
                x_distance, y_distance = self.compute_distance(battery.x, battery.y, x_loc, y_loc)
                possible_cables, house_dict = self.create_cables(x_distance, y_distance, house_dict)
                list_distances_all_cables = self.distance_to_cable(possible_cables, battery)
                x_list, y_list = self.choose_best_cable(list_distances_all_cables, possible_cables, house_dict, x_list, y_list)

                    # print(x_list, y_list, battery.dict['battery location'])
                    # print(step)

                    # plt.plot(x_list, y_list, 'k--')


                #     previous_x = x_loc
                #     previous_y = y_loc
                #     # plt.figure()
                # #
                # for (prev_x, prev_y), (next_x, next_y) in zip(zip(x_list[:-1], y_list[:-1]), zip(x_list[1:], y_list[1:])):
                #     if abs(prev_x - next_x) + abs(prev_y - next_y) != 1:
                #         print(" wtf", (prev_x, prev_y), (next_x, next_y))
                #         print(x_list, y_list, house_dict['house location'])

                plt.plot(x_list, y_list, 'k--')
                    # plt.show()

        # plt.show()

                        # house_dict['cables'] = np.array(best_grid)


    def run(self, list_with_houses, list_with_batteries):

        self.breadth_first_5(list_with_houses, list_with_batteries)

        # plt.show()

        for battery in list_with_batteries:
            for house_dict in battery.dict['houses'][5:]:
                make_rest_of_cables.search_cables(house_dict, battery)


        # plt.show()

        # print(battery.dict['connected houses'])
















        # make list with corresponding number of -1 or 1,
