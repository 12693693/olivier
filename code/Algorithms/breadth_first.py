import random
import math
import numpy as np
from .search_cables import Search_Cables
import matplotlib.pyplot as plt

make_rest_of_cables = Search_Cables()

class Breadth_first():
    def __init__(self):
        self.x_list = []
        self.y_list = []

    def compute_distance(self, x_battery, y_battery, x_loc, y_loc):
        '''
        this function computes the distance between the battery and the starting
        location on the x and y axis
        '''
        x_distance = int(x_battery) - int(x_loc)
        y_distance = int(y_battery) - int(y_loc)
        # print(x_distance, y_distance)

        return x_distance, y_distance


    def breadth_first_5(self, list_with_houses, list_with_batteries):
        ''' this function executes breadth first algorithm on the first 5 houses
        of each battery. It makes 10 random paths from each house to the battery,
        and then chooses the best path based on the distance from the rest of the
        connected houses to that battery '''

        for battery in list_with_batteries:
            # print('battery')
            for i in range(5):
                x_list = []
                y_list = []
                house_dict = battery.dict['connected houses'][i]
            # for house_dict in battery.dict['connected houses']:
            # house_dict = battery.dict['connected houses'][0]
                steps_list = []

                # find x and y coordinates for the battery and connected house
                x_loc = house_dict['location'][0]
                y_loc = house_dict['location'][1]

                # save starting point for the grid line
                house_dict['cables'].append(f'{x_loc}, {y_loc}')

                # create list with x and y coordinates of the grid line
                x_list.append(x_loc)
                y_list.append(y_loc)

                x_distance, y_distance = self.compute_distance(battery.x, battery.y, x_loc, y_loc)

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

                possible_grids = []

                for i in range(10):
                    # shuffle the steps in the list randomly
                    random.shuffle(steps_list)
                    grid_list = []

                    x_loc = house_dict['house location'][0]
                    y_loc = house_dict['house location'][1]

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
                        grid_list.append(f'{x_loc}, {y_loc}')

                    # list containing each grids list of steps
                    possible_grids.append(grid_list)

                list_distances_all_grids = []

                # loop over grids
                for grid in possible_grids:
                    distance_to_grid_list = []
                    # print(len(grid))
                    # loop over house_dicts
                    for house_dict_2 in battery.dict['connected houses']:
                        x_house = house_dict_2['location'][0]
                        y_house = house_dict_2['location'][1]

                        distance = 100

                        # loop over each step in the grid, and calculate distance between
                        # the current house and the cable
                        for step in grid:
                            x_loc = float(step.split(', ')[0])
                            y_loc = float(step.split(', ')[1])
                            # print('for step in grid')
                            # calculate current_distance
                            current_distance = abs(x_house - x_loc) + abs(y_house - y_loc)
                            # print('current distance')
                            if current_distance < distance:
                                distance = current_distance

                        distance_to_grid_list.append(distance)
                        # print('list of distances for one grid')
                    list_distances_all_grids.append(distance_to_grid_list)
                    # print('total list of distances all grids')

                lowest_distance = math.inf
                for index, grid_distance_list in enumerate(list_distances_all_grids):
                    total_distance = sum(grid_distance_list)
                    if total_distance < lowest_distance:
                        best_grid = possible_grids[index]
                        lowest_distance = total_distance
<<<<<<< HEAD
                        house_dict['grid'] = best_grid

                previous_x = 0
                previous_y = 0

                x_list_scheef = []
                y_list_scheef = []

                for step in best_grid:
                    x_loc = float(step.split(', ')[0])
                    y_loc = float(step.split(', ')[1])

                    if x_loc != previous_x and y_loc != previous_y and previous_x != 0 and previous_y != 0:
                        print('scheef')

                    x_list.append(x_loc)
                    y_list.append(y_loc)
                    # print(x_list, y_list, battery.dict['battery location'])
                    # print(step)

                    # plt.plot(x_list, y_list, 'k--')


                    previous_x = x_loc
                    previous_y = y_loc
                    # plt.figure()
                #
                for (prev_x, prev_y), (next_x, next_y) in zip(zip(x_list[:-1], y_list[:-1]), zip(x_list[1:], y_list[1:])):
                    if abs(prev_x - next_x) + abs(prev_y - next_y) != 1:
                        print(" wtf", (prev_x, prev_y), (next_x, next_y))
                        print(x_list, y_list, house_dict['house location'])



                plt.plot(x_list, y_list, 'k--')
                    # plt.show()

        # plt.show()



=======
                        house_dict['cables'] = np.array(best_grid)
>>>>>>> 62997d2f84dbbfa88b2d33e6d359b8b02a50e6d7
                        # print(np.array(best_grid))
                        # #y
                        # print(np.array(best_grid)[:,1])
                        # #x
                        # print(np.array(best_grid)[:,0])
                        # exit()

            # print(house_dict['grid'])
            # print("HELP", battery.dict['connected houses'])

    def run(self, list_with_houses, list_with_batteries):

        self.breadth_first_5(list_with_houses, list_with_batteries)


        # plt.show()

        for battery in list_with_batteries:
            for house_dict in battery.dict['connected houses'][5:]:
                make_rest_of_cables.search_cables(house_dict, battery)


        # plt.show()

        # print(battery.dict['connected houses'])
















        # make list with corresponding number of -1 or 1,
