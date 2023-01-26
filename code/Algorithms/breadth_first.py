import random
class Breadth_first():
    def __init__(self):
        self.x_list = []
        self.y_list = []

    def compute_distance(self, x_battery, y_battery, x_loc, y_loc):
        '''
        this function computes the distance between the battery and the starting
        location on the x and y axis
        '''
        x_distance = x_battery - x_loc
        y_distance = y_battery - y_loc

        return x_distance, y_distance


    def breadth(self, list_with_houses, list_with_batteries):
        # distance y
        steps_list = []
        grid_list = []
        possible_grids = []
        # steps_dict = {'L': 0, 'R': 0, 'U': 0, 'D': 0}

        for battery in list_with_batteries:
            for house_dict in battery.dict['connected houses']:

                # find x and y coordinates for the battery and connected house
                x_loc = house_dict['house location'][0]
                y_loc = house_dict['house location'][1]

                # save starting point for the grid line
                house_dict['grid'].append(f'{x_loc}, {y_loc}')

                # create list with x and y coordinates of the grid line
                x_list = [x_loc]
                y_list = [y_loc]

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

                for i in range(10):
                    # shuffle the steps in the list randomly
                    random.shuffle(steps_list)

                    # take the random order of steps
                    for step in steps_dict:
                        if step == 'L':
                            x_loc -= 1
                        elif step == 'R':
                            x_loc += 1
                        elif step == 'D':
                            y_loc -= 1
                        else:
                            y_loc += 1

                        x_list.append(x_loc)
                        y_list.append(y_loc)

                        # list containing steps for one grid
                        grid_list.append(f'{x_loc}, {y_loc}')

                    # list containing each grids list of steps
                    possible_grids.append(grid_list)

            list_distances_all_grids = []

            # loop over grids
            for grid in possible_grids:
                distance_to_grid_list = []

                # loop over house_dicts
                for house_dict in battery.dict['connected houses']:
                    x_house = house_dict['house location'].split(',')[0]
                    y_house = house_dict['house location'].split(',')[1]

                    distance = 100

                    # loop over each step in the grid, and calculate distance between
                    # the current house and the cable
                    for step in grid:
                        x_loc = step.split(',')[0]
                        y_loc = step.split(',')[1]

                        # calculate current_distance
                        current_distance = abs(x_house - x_loc) + abs(y_house - y_loc)

                        if current_distance < distance:
                            distance = current_distance

                    distance_to_grid_list.append(distance)
                list_distances_all_grids.append(distance_to_grid_list)

            lowest_distance = 100
            for index, grid_distance_list in enumerate(list_distances_all_grids):
                current_distance = sum(grid_distance_list)
                if total_distance < lowest_distance:
                    best_grid = possible_grids[index]
                    lowest_distance = total_distance

            house_dict['grid'] = best_grid












        # make list with corresponding number of -1 or 1,
