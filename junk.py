# ============== Breadth first ==============
import random
import math
import numpy as np
from .search_cables import Search_Cables

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

        return x_distance, y_distance


    def breadth_first_5(self, list_with_houses, list_with_batteries):
        ''' this function executes breadth first algorithm on the first 5 houses
        of each battery. It makes 10 random paths from each house to the battery,
        and then chooses the best path based on the distance from the rest of the
        connected houses to that battery '''

        for battery in list_with_batteries:

            for i in range(5):
                house_dict = battery.dict['connected houses'][i]

                steps_list = []

                # find x and y coordinates for the battery and connected house
                x_loc = house_dict['location'][0]
                y_loc = house_dict['location'][1]

                # save starting point for the grid line
                house_dict['cables'].append(f'{x_loc}, {y_loc}')

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

                possible_grids = []

                for i in range(10):
                    # shuffle the steps in the list randomly
                    random.shuffle(steps_list)
                    grid_list = []

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

                        x_list.append(x_loc)
                        y_list.append(y_loc)

                        # list containing steps for one grid
                        grid_list.append([x_loc, y_loc])

                    # list containing each grids list of steps
                    possible_grids.append(grid_list)

                list_distances_all_grids = []

                # loop over grids
                for grid in possible_grids:
                    distance_to_grid_list = []
                    # loop over house_dicts
                    for house_dict_2 in battery.dict['connected houses']:
                        x_house = house_dict_2['location'][0]
                        y_house = house_dict_2['location'][1]

                        distance = 100

                        # loop over each step in the grid, and calculate distance between
                        # the current house and the cable
                        for step in grid:
                            x_loc = step[0]
                            y_loc = step[1]

                            # calculate current_distance
                            current_distance = abs(x_house - x_loc) + abs(y_house - y_loc)
                            if current_distance < distance:
                                distance = current_distance

                        distance_to_grid_list.append(distance)
                    list_distances_all_grids.append(distance_to_grid_list)

                lowest_distance = math.inf
                for index, grid_distance_list in enumerate(list_distances_all_grids):
                    total_distance = sum(grid_distance_list)
                    if total_distance < lowest_distance:
                        best_grid = possible_grids[index]
                        lowest_distance = total_distance
                        house_dict['cables'] = np.array(best_grid)


    def run(self, list_with_houses, list_with_batteries):

        self.breadth_first_5(list_with_houses, list_with_batteries)

        for battery in list_with_batteries:
            for house_dict in battery.dict['connected houses'][5:]:
                make_rest_of_cables.search_cables(house_dict, battery)

        print(battery.dict['connected houses'])



# ========= Cable 90 degrees ==============
import matplotlib.pyplot as plt
class Cables_90():

    def get_location(self, dictionary_of_house):
        self.location_house_x = dictionary_of_house['location'][0]
        self.location_house_y = dictionary_of_house['location'][1]

    def plot_cable_90(self, loc_house_x, loc_house_y, battery):
        x_list = [loc_house_x, battery.x, battery.x]
        y_list = [loc_house_y, loc_house_y, battery.y]
        plt.plot(x_list, y_list, 'k--')

    def make_lines_90(self, dictionary_of_house, battery):
        step_count = 0

        # create starting point for creating the grid line
        # and add the starting point to the grid dictionary
        x_loc = self.location_house_x
        y_loc = self.location_house_y
        dictionary_of_house['cables'].append(f'{x_loc}, {y_loc}')

        # compute distance to use as a constraint for choosing which way
        # to move on the grid line

        distance_x = self.location_house_x - battery.x
        distance_y = self.location_house_y - battery.y

        # take steps until the correct x coordinate is reached
        # and keep track of the steps
        while x_loc != battery.x:
            if distance_x > 0:
                x_loc -= 1
            else:
                x_loc += 1
            step_count += 1

            # save the individual steps in the grid list in the dictionary of the house
            dictionary_of_house['cables'].append(f'{x_loc}, {y_loc}')

        # take steps until the correct y coordinate is reached
        # and keep track of the grid line
        while y_loc != battery.y:
            if distance_y > 0:
                y_loc -= 1
            else:
                y_loc += 1
            step_count += 1

            # save the individual steps in the grid list in the dictionary of the house
            dictionary_of_house['cables'].append(f'{x_loc}, {y_loc}')

        return step_count

    def make_90_degrees_cable(self, dictionary_of_house, battery):
        self.get_location(dictionary_of_house)
        self.plot_cable_90(self.location_house_x, self.location_house_y, battery)
        step_count = self.make_lines_90(dictionary_of_house, battery)

        return step_count


    def make_90_degrees_cables(self, list_with_houses, list_with_batteries):
        """
        This function computes and plots the grid lines. It also keeps track of
        the individual steps within the grid. It then saves the individual
        coordinates in a new list.
        """
        steps_count = 0


        # loop over batteries and the houses that are connected to that battery
        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:
                steps_count += self.make_90_degrees_cable(house_dict, battery)




                # # find x and y coordinates for the battery and connected house
                # self.get_location(house_dict)
                # self.plot_cable(self.location_house_x, self.location_house_y, battery)

                # # extra
                # location_house_x = house_dict['location'][0]
                # location_house_y = house_dict['location'][1]
                # location_battery_x = battery.dict['location'][0]
                # location_battery_y = battery.dict['location'][1]


                # x_list = [location_house_x, battery.x, battery.x]
                # y_list = [location_house_y, location_house_y, battery.y]
                # plt.plot(x_list, y_list, 'k--')

                # # create starting point for creating the grid line
                # # and add the starting point to the grid dictionary
                # x_loc = self.location_house_x
                # y_loc = self.location_house_y
                # house_dict['grid'].append(f'{x_loc}, {y_loc}')
                #
                # # compute distance to use as a constraint for choosing which way
                # # to move on the grid line
                #
                #
                # distance_x = self.location_house_x - battery.x
                # distance_y = self.location_house_y - battery.y
                #
                # # take steps until the correct x coordinate is reached
                # # and keep track of the steps
                # while x_loc != battery.x:
                #     if distance_x > 0:
                #         x_loc -= 1
                #     else:
                #         x_loc += 1
                #     self.steps_count += 1
                #
                #     # save the individual steps in the grid list in the dictionary of the house
                #     house_dict['grid'].append(f'{x_loc}, {y_loc}')
                #
                # # take steps until the correct y coordinate is reached
                # # and keep track of the grid line
                # while y_loc != battery.y:
                #     if distance_y > 0:
                #         y_loc -= 1
                #     else:
                #         y_loc += 1
                #     self.steps_count += 1
                #
                #     # save the individual steps in the grid list in the dictionary of the house
                #     house_dict['grid'].append(f'{x_loc}, {y_loc}')

        #plt.show()
        return steps_count

# ==================== Cables =============
class Cables_90():

    def make_90_degrees_cables(self, list_with_houses, list_with_batteries):
        """
        This function computes and plots the grid lines. It also keeps track of
        the individual steps within the grid. It then saves the individual
        coordinates in a new list.
        """
        self.steps_count = 0

        # loop over batteries and the houses that are connected to that battery
        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:

                # find x and y coordinates for the battery and connected house
                location_house_x = house_dict['location'][0]
                location_house_y = house_dict['location'][1]
                location_battery_x = battery.dict['location'][0]
                location_battery_y = battery.dict['location'][1]

                x_list = [location_house_x, location_battery_x, location_battery_x]
                y_list = [location_house_y, location_house_y, location_battery_y]
                plt.plot(x_list, y_list, 'k--')

                # create starting point for creating the grid line
                x_loc = location_house_x
                y_loc = location_house_y
#--------------------------------------------
                # compute distance to use as a constraint for choosing which way
                # to move on the grid line
                distance_x = location_house_x - location_battery_x
                distance_y = location_house_y - location_battery_y

                # take steps until the correct x coordinate is reached
                # and keep track of the steps
                while x_loc != location_battery_x:
                    if distance_x > 0:
                        x_loc -= 1
                    else:
                        x_loc += 1
                    self.steps_count += 1

                    # save the individual steps in the grid list in the dictionary of the house
                    house_dict['cables'].append(f'{x_loc}, {y_loc}')

                # take steps until the correct y coordinate is reached
                # and keep track of the grid line
                while y_loc != location_battery_y:
                    if distance_y > 0:
                        y_loc -= 1
                    else:
                        y_loc += 1
                    self.steps_count += 1

                    # save the individual steps in the grid list in the dictionary of the house
                    house_dict['cables'].append(f'{x_loc}, {y_loc}')


# ================ Further Back up ===============


import random
import matplotlib.pyplot as plt

class Further_Cables():
    def further_cables(self, list_with_houses, list_with_batteries):
        '''
        This function uses the previously defined cables function to connect
        to the houses. It adds in a new condition which ensures that if there is
        a choice between cables with the same distance to the house that it choses
        the path along the cable which is already there. In addition to the search cables
        this one also looks at the cable may be two steps away.
        This would optimize the distance as well as the cost for the cables.
        '''

        self.existing_cable_dict = {}
        self.steps_count = 0

        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:
                self.cable_list = []

                # set starting point to the location of the house
                location_house_x = house_dict['location'][0]
                location_house_y = house_dict['location'][1]

                # compute distance between the battery and the assigned house
                distance = abs(battery.x - location_house_x) + abs(battery.y - location_house_y)

                # set starting point to the location of the house
                x_loc = location_house_x
                y_loc = location_house_y

                house_dict['cables'].append(f'{x_loc}, {y_loc}')

                x_list = [x_loc]
                y_list = [y_loc]

                while distance != 0:
                    self.step_score_list = []
                    self.step_list = []
                    self.distance_list = []

                    for choice in range(1,5):
                        if choice == 1:
                            step_score_1 = 0
                            step_1 = [x_loc, y_loc, (x_loc - 1), y_loc]
                            step_1_hash = tuple(step_1)

                            #compute the potential new distance with this stap
                            new_distance_1 = abs(battery.x - (x_loc - 1)) + abs(battery.y - y_loc)

                            if new_distance_1 < distance and step_1_hash in self.existing_cable_dict:
                                step_score_1 = 2
                            if new_distance_1 < distance and step_1_hash not in self.existing_cable_dict:
                                step_score_1 = 1
                            if new_distance_1 < distance and (step_1_hash[2] + 1) in self.existing_cable_dict:
                                step_score_1 = 2
                            if new_distance_1 < distance and (step_1_hash[2] + 2) in self.existing_cable_dict:
                                step_score_1 = 2
                            self.step_score_list.append(step_score_1)
                            self.step_list.append(step_1)
                            self.distance_list.append(new_distance_1)

                        if choice == 2:
                            step_score_2 = 0
                            step_2 = [x_loc, y_loc, (x_loc + 1), y_loc]
                            step_2_hash = tuple(step_2)

                            #compute the potential new distance with this stap
                            new_distance_2 = abs(battery.x - (x_loc + 1)) + abs(battery.y - y_loc)

                            if new_distance_2 < distance and step_2_hash in self.existing_cable_dict:
                                step_score_2 = 2
                            if new_distance_2 < distance and step_2_hash not in self.existing_cable_dict:
                                step_score_2 = 1
                            if new_distance_1 < distance and (step_2_hash[2] - 1) in self.existing_cable_dict:
                                step_score_2 = 2
                            if new_distance_1 < distance and (step_2_hash[2] - 2) in self.existing_cable_dict:
                                step_score_2 = 2

                            self.step_score_list.append(step_score_2)
                            self.step_list.append(step_2)
                            self.distance_list.append(new_distance_2)

                        if choice == 3:
                            step_score_3 = 0
                            step_3 = [x_loc, y_loc, x_loc, (y_loc + 1)]
                            step_3_hash = tuple(step_3)

                            #compute the potential new distance with this stap
                            new_distance_3 = abs(battery.x - x_loc) + abs(battery.y - (y_loc + 1))

                            if new_distance_3 < distance and step_3_hash in self.existing_cable_dict:
                                step_score_3 = 2
                            if new_distance_3 < distance and step_3_hash not in self.existing_cable_dict:
                                step_score_3 = 1
                            if new_distance_3 < distance and (step_3_hash[3] + 1) in self.existing_cable_dict:
                                step_score_3 = 2
                            if new_distance_3 < distance and (step_3_hash[3] + 2) in self.existing_cable_dict:
                                step_score_3 = 2

                            self.step_score_list.append(step_score_3)
                            self.step_list.append(step_3)
                            self.distance_list.append(new_distance_3)

                        if choice == 4:
                            step_score_4 = 0
                            step_4 = [x_loc, y_loc, x_loc, (y_loc - 1)]
                            step_4_hash = tuple(step_4)

                            #compute the potential new distance with this stap
                            new_distance_4 = abs(battery.x - x_loc) + abs(battery.y - (y_loc - 1))

                            # Add score to each step based on it's characteristics
                            if new_distance_4 < distance and step_4_hash in self.existing_cable_dict:
                                step_score_4 = 2
                            if new_distance_4 < distance and step_4_hash not in self.existing_cable_dict:
                                step_score_4 = 1
                            if new_distance_4 < distance and (step_4_hash[3] - 1) in self.existing_cable_dict:
                                step_score_4 = 2
                            if new_distance_4 < distance and (step_4_hash[3] - 2) in self.existing_cable_dict:
                                step_score_4 = 2

                            self.step_score_list.append(step_score_4)
                            self.step_list.append(step_4)
                            self.distance_list.append(new_distance_4)


                    # find step with highest score
                    if self.step_score_list.count(2) > 1:
                        list_index_2 = []

                        for i in range(len(self.step_score_list)):
                            if self.step_score_list[i] == 2:
                                list_index_2.append(i)

                        highest_index = random.choice(list_index_2)
                    elif self.step_score_list.count(1) > 1:
                        list_index_1 = []

                        for i in range(len(self.step_score_list)):
                            if self.step_score_list[i] == 1:
                                list_index_1.append(i)

                        highest_index = random.choice(list_index_1)
                    else:
                        highest_index = self.step_score_list.index(max(self.step_score_list))

                    # find the step which belongs with the highest score
                    for index, highest in enumerate(self.step_score_list):
                        cable_key = tuple(self.step_list[highest_index])

                        #find the new distance which belongs with the highest score
                    for index, distance in enumerate(self.step_score_list):
                        new_distance = self.distance_list[highest_index]

                    distance = new_distance

                    x_loc = cable_key[2]
                    y_loc = cable_key[3]

                    x_list.append(x_loc)
                    y_list.append(y_loc)
                    house_dict['cables'].append(f'{x_loc}, {y_loc}')

                    # Add this list to the dictionary
                    if cable_key not in self.existing_cable_dict:
                        self.existing_cable_dict[cable_key] = 1

                plt.plot(x_list, y_list, 'k--')

            print(count)

        return self.steps_count, self.cable_list, self.existing_cable_dict


# =================== further Cables =================



import random
import matplotlib.pyplot as plt

class Further_Cables():
    def __init__(self):
        self.existing_cable_dict = {}

    def further_cables(self, house_dict, battery):
        self.cable_list = []
        # set starting point to the location of the house
        self.location_house_x = float(dictionary_of_house['location'].split(',')[0])
        self.location_house_y = float(dictionary_of_house['location'].split(',')[1])

        # compute distance between the battery and the assigned house
        distance = abs(battery.x - self.location_house_x) + abs(battery.y - self.location_house_y)

        # set starting point to the location of the house
        x_loc = self.location_house_x
        y_loc = self.location_house_y

        # Add these start points to
        house_dict['cables'].append(f'{int(x_loc)}, {int(y_loc)}')

        x_list = [x_loc]
        y_list = [y_loc]

        while distance != 0:
            self.step_score_list = []
            self.step_list = []
            self.distance_list = []

            for choice in range(1,5):
                if choice == 1:
                    step_score_1 = 0
                    step_1 = [x_loc, y_loc, (x_loc - 1), y_loc]
                    step_1_hash = tuple(step_1)

                    #compute the potential new distance with this stap
                    new_distance_1 = abs(battery.x - (x_loc - 1)) + abs(battery.y - y_loc)

                    if new_distance_1 < distance and step_1_hash in self.existing_cable_dict:
                        step_score_1 = 2
                    if new_distance_1 < distance and step_1_hash not in self.existing_cable_dict:
                        step_score_1 = 1
                    if new_distance_1 < distance and (step_1_hash[2] + 1) in self.existing_cable_dict:
                        step_score_1 = 2
                    if new_distance_1 < distance and (step_1_hash[2] + 2) in self.existing_cable_dict:
                        step_score_1 = 2

                    self.step_score_list.append(step_score_1)
                    self.step_list.append(step_1)
                    self.distance_list.append(new_distance_1)

                if choice == 2:
                    step_score_2 = 0
                    step_2 = [x_loc, y_loc, (x_loc + 1), y_loc]
                    step_2_hash = tuple(step_2)

                    #compute the potential new distance with this stap
                    new_distance_2 = abs(battery.x - (x_loc + 1)) + abs(battery.y - y_loc)

                    if new_distance_2 < distance and step_2_hash in self.existing_cable_dict:
                        step_score_2 = 2
                    if new_distance_2 < distance and step_2_hash not in self.existing_cable_dict:
                        step_score_2 = 1
                    if new_distance_1 < distance and (step_2_hash[2] - 1) in self.existing_cable_dict:
                        step_score_2 = 2
                    if new_distance_1 < distance and (step_2_hash[2] - 2) in self.existing_cable_dict:
                        step_score_2 = 2

                    self.step_score_list.append(step_score_2)
                    self.step_list.append(step_2)
                    self.distance_list.append(new_distance_2)

                if choice == 3:
                    step_score_3 = 0
                    step_3 = [x_loc, y_loc, x_loc, (y_loc + 1)]
                    step_3_hash = tuple(step_3)

                    #compute the potential new distance with this stap
                    new_distance_3 = abs(battery.x - x_loc) + abs(battery.y - (y_loc + 1))

                    if new_distance_3 < distance and step_3_hash in self.existing_cable_dict:
                        step_score_3 = 2
                    if new_distance_3 < distance and step_3_hash not in self.existing_cable_dict:
                        step_score_3 = 1
                    if new_distance_3 < distance and (step_3_hash[3] + 1) in self.existing_cable_dict:
                        step_score_3 = 2
                    if new_distance_3 < distance and (step_3_hash[3] + 2) in self.existing_cable_dict:
                        step_score_3 = 2


                    self.step_score_list.append(step_score_3)
                    self.step_list.append(step_3)
                    self.distance_list.append(new_distance_3)

                if choice == 4:
                    step_score_4 = 0
                    step_4 = [x_loc, y_loc, x_loc, (y_loc - 1)]
                    step_4_hash = tuple(step_4)

                    #compute the potential new distance with this stap
                    new_distance_4 = abs(battery.x - x_loc) + abs(battery.y - (y_loc - 1))

                    # Add score to each step based on it's characteristics
                    if new_distance_4 < distance and step_4_hash in self.existing_cable_dict:
                        step_score_4 = 2
                    if new_distance_4 < distance and step_4_hash not in self.existing_cable_dict:
                        step_score_4 = 1
                    if new_distance_4 < distance and (step_4_hash[3] - 1) in self.existing_cable_dict:
                        step_score_4 = 2
                    if new_distance_4 < distance and (step_4_hash[3] - 2) in self.existing_cable_dict:
                        step_score_4 = 2

                    self.step_score_list.append(step_score_4)
                    self.step_list.append(step_4)
                    self.distance_list.append(new_distance_4)


            # find step with highest score
            if self.step_score_list.count(2) > 1:
                list_index_2 = []

                for i in range(len(self.step_score_list)):
                    if self.step_score_list[i] == 2:
                        list_index_2.append(i)

                highest_index = random.choice(list_index_2)
            elif self.step_score_list.count(1) > 1:
                list_index_1 = []

                for i in range(len(self.step_score_list)):
                    if self.step_score_list[i] == 1:
                        list_index_1.append(i)

                highest_index = random.choice(list_index_1)
            else:
                highest_index = self.step_score_list.index(max(self.step_score_list))

            # Find the step which belongs with the highest score
            for index, highest in enumerate(self.step_score_list):
                cable_key = tuple(self.step_list[highest_index])

            # Find the new distance which belongs with the highest score
            for index, distance in enumerate(self.step_score_list):
                new_distance = self.distance_list[highest_index]
            # Update the new distance
            distance = new_distance

            x_loc = cable_key[2]
            y_loc = cable_key[3]

            x_list.append(x_loc)
            y_list.append(y_loc)
            house_dict['cables'].append(f'{int(x_loc)}, {int(y_loc)}')

            # Add this cable part to the dictionary
            if cable_key not in self.existing_cable_dict:
                self.existing_cable_dict[cable_key] = 1

        plt.plot(x_list, y_list, 'k--')

    def run_further(self, list_with_houses, list_with_batteries):
        '''
        This function uses the previously defined cables function to connect
        to the houses. It adds in a new condition which ensures that if there is
        a choice between cables with the same distance to the house that it choses
        the path along the cable which is already there. This would optimize the
        distance as well as the cost for the cables.
        '''

        self.steps_count = 0

        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:
                self.further_cables(house_dict, battery)


        return self.steps_count, self.cable_list, self.existing_cable_dict


# ================= Further Try ===============


import random
import matplotlib.pyplot as plt

class Further_Cables():
    def __init__(self):
        self.existing_cable_dict = {}

    def further_cables(self, house_dict, battery):
        self.cable_list = []
        # set starting point to the location of the house
        self.location_house_x = dictionary_of_house['location'][0]
        self.location_house_y = dictionary_of_house['location'][1]
        # location_house_x = house_dict['location'][0]
        # location_house_y = house_dict['location'][1]

        # compute distance between the battery and the assigned house
        distance = abs(battery.x - self.location_house_x) + abs(battery.y - self.location_house_y)

        # set starting point to the location of the house
        x_loc = self.location_house_x
        y_loc = self.location_house_y

        # Add these start points to the grid list.
        house_dict['cables'].append(f'{x_loc}, {y_loc}')

        x_list = [x_loc]
        y_list = [y_loc]

        # Set condition to make sure it moves untill the battery and create lists.
        while distance != 0:
            self.step_score_list = []
            self.step_list = []
            self.distance_list = []

            # Create the steps for each direction
            for choice in range(1,5):
                if choice == 1:
                    step_score_1 = 0
                    step_1 = [x_loc, y_loc, (x_loc - 1), y_loc]
                    step_1_hash = tuple(step_1)

                    #compute the potential new distance with this stap
                    new_distance_1 = abs(battery.x - (x_loc - 1)) + abs(battery.y - y_loc)

                    # Define the scores for each step.
                    if new_distance_1 < distance and step_1_hash in self.existing_cable_dict:
                        step_score_1 = 2
                    if new_distance_1 < distance and step_1_hash not in self.existing_cable_dict:
                        step_score_1 = 1

                    # Update the lists with the information if this step
                    self.step_score_list.append(step_score_1)
                    self.step_list.append(step_1)
                    self.distance_list.append(new_distance_1)

                if choice == 2:
                    step_score_2 = 0
                    step_2 = [x_loc, y_loc, (x_loc + 1), y_loc]
                    step_2_hash = tuple(step_2)

                    #compute the potential new distance with this stap
                    new_distance_2 = abs(battery.x - (x_loc + 1)) + abs(battery.y - y_loc)

                    # Define and add score to each step based on it's characteristics
                    if new_distance_2 < distance and step_2_hash in self.existing_cable_dict:
                        step_score_2 = 2
                    if new_distance_2 < distance and step_2_hash not in self.existing_cable_dict:
                        step_score_2 = 1

                    # Update the lists with the information if this step
                    self.step_score_list.append(step_score_2)
                    self.step_list.append(step_2)
                    self.distance_list.append(new_distance_2)

                if choice == 3:
                    step_score_3 = 0
                    step_3 = [x_loc, y_loc, x_loc, (y_loc + 1)]
                    step_3_hash = tuple(step_3)

                    #compute the potential new distance with this stap
                    new_distance_3 = abs(battery.x - x_loc) + abs(battery.y - (y_loc + 1))

                    # Define and add score to each step based on it's characteristics
                    if new_distance_3 < distance and step_3_hash in self.existing_cable_dict:
                        step_score_3 = 2
                    if new_distance_3 < distance and step_3_hash not in self.existing_cable_dict:
                        step_score_3 = 1

                    # Update the lists with the information if this step
                    self.step_score_list.append(step_score_3)
                    self.step_list.append(step_3)
                    self.distance_list.append(new_distance_3)

                if choice == 4:
                    step_score_4 = 0
                    step_4 = [x_loc, y_loc, x_loc, (y_loc - 1)]
                    step_4_hash = tuple(step_4)

                    #compute the potential new distance with this stap
                    new_distance_4 = abs(battery.x - x_loc) + abs(battery.y - (y_loc - 1))

                    # Define and add score to each step based on it's characteristics
                    if new_distance_4 < distance and step_4_hash in self.existing_cable_dict:
                        step_score_4 = 2
                    if new_distance_4 < distance and step_4_hash not in self.existing_cable_dict:
                        step_score_4 = 1

                    # Update the lists with the information if this step
                    self.step_score_list.append(step_score_4)
                    self.step_list.append(step_4)
                    self.distance_list.append(new_distance_4)


            # Find step with highest score
            if self.step_score_list.count(2) > 1:
                list_index_2 = []

                for i in range(len(self.step_score_list)):
                    if self.step_score_list[i] == 2:
                        list_index_2.append(i)

                highest_index = random.choice(list_index_2)
            elif self.step_score_list.count(1) > 1:
                list_index_1 = []

                for i in range(len(self.step_score_list)):
                    if self.step_score_list[i] == 1:
                        list_index_1.append(i)

                highest_index = random.choice(list_index_1)
            else:
                highest_index = self.step_score_list.index(max(self.step_score_list))

            # Find the step which belongs with the highest score.
            for index, highest in enumerate(self.step_score_list):
                cable_key = tuple(self.step_list[highest_index])

            # Find the new distance which belongs with the highest score.
            for index, distance in enumerate(self.step_score_list):
                new_distance = self.distance_list[highest_index]

            # Update the new distance.
            distance = new_distance

            # Add the new location to the grid list.
            x_loc = cable_key[2]
            y_loc = cable_key[3]

            x_list.append(x_loc)
            y_list.append(y_loc)
            house_dict['cables'].append(f'{x_loc}, {y_loc}')

            # Add this cable part to the cable dictionary
            if cable_key not in self.existing_cable_dict:
                self.existing_cable_dict[cable_key] = 1

        plt.plot(x_list, y_list, 'k--')

    def run_further(self, list_with_houses, list_with_batteries):
        '''
        This function uses the previously defined cables function to connect
        to the houses. It adds in a new condition which ensures that if there is
        a choice between cables with the same distance to the house that it choses
        the path along the cable which is already there. This would optimize the
        distance as well as the cost for the cables.
        '''

        self.steps_count = 0


        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:
                self.further_cables(house_dict, battery)

        return self.steps_count, self.cable_list, self.existing_cable_dict



# ===================== GREEDY ========================


import math
def sort_houses(list_with_houses):
    """
    This function sorts the houses based on the maximum output
    """
    new_list_with_houses = sorted(list_with_houses, key=lambda x:x.maxoutput, reverse=True)
    return new_list_with_houses

class Greedy():
    def assign_closest_battery(self, list_with_houses, list_with_batteries):
        """
        This function assign a house to the closest battery that still has capacity
        """

        # sort the houses based on the maximum capacity
        list_with_houses_sorted = sort_houses(list_with_houses)

        for house in list_with_houses_sorted:
            #print('new house')
            #print('output', house.maxoutput)

            # set distance to infinity
            closest_distance = math.inf

            for battery in list_with_batteries:
                #print(battery.capacity)

                # calculate distance to each battery
                distance = abs((battery.x - house.x) + (battery.y - house.y))

                # assign the house closest battery that still has enough capacity
                if distance < closest_distance and house.maxoutput < battery.capacity:
                    closest_distance = distance
                    assigned_battery = battery

            # adjust the capacity of the battery
            assigned_battery.capacity -= house.maxoutput
            #print(assigned_battery.x, assigned_battery.capacity)

            # save the dictionary of the house in the list of houses for that battery
            assigned_battery.dict['houses'].append(house.dict)




# ======================= HILL CLIMBER ==================


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
    def __init__(self, smartgrid_solution):
        self.smartgrid = copy.deepcopy(smartgrid_solution)
        self.costs = self.smartgrid.total_cost

    def fill_new_grid(self, house_dict, battery, function):

        # fill the grid of the newly added houses
        fill_string =f'{function}({house_dict}, {battery})'
        return fill_string

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
            self.new_costs = new_smartgrid.total_cost - (len(self.house_1['grid']) - 1) - (len(self.house_2['grid']) - 1)
            #self.smartgrid.combined_list[0]['costs shared'] - (len(house_1['grid']) - 1) - (len(house_2['grid']) - 1)

            # reset the grid
            self.house_1['grid'] = []
            self.house_2['grid'] = []

            # fill the grid of the houses
            string_function_1 = self.fill_new_grid(self.house_1, self.battery_2, function)
            self.steps_house_1 = eval(string_function_1)
            string_function_2 = self.fill_new_grid(self.house_2, self.battery_1, function)
            self.steps_house_2 = eval(string_function_2)

            # switch the houses and add them to a new battery
            self.battery_1.dict['houses'].append(self.house_2)
            self.battery_2.dict['houses'].append(self.house_1)

    def check_solution(self, new_smartgrid):
        #print('oud zonder', self.new_costs)
        self.new_costs += self.steps_house_1 + self.steps_house_2
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



# ================ LOCATION .PY ==================


def get_location():
    for battery in list_with_batteries:
        for house_dict in battery.dict['houses']:


            # find x and y coordinates for the battery and connected house
            location_house_x = house_dict['location'][0]
            location_house_y = house_dict['location'][1]
            location_battery_x = battery.dict['location'][0]
            location_battery_y = battery.dict['location'][1]

            # compute distance between the battery and the assigned house
            distance = abs((location_battery_x - location_house_x) + (location_battery_y - location_house_y))

            # set starting point to the location of the house
            x_loc = location_house_x
            y_loc = location_house_y

            x_list = [x_loc]
            y_list = [y_loc]




# ================== RANDOM _ TRY .PY =============
import random
import matplotlib.pyplot as plt

class Cables():
    def __init__(self):
        self.x_list = []
        self.y_list = []

    def compute_distance(self, x_battery, y_battery, x_loc, y_loc):
        '''
        This function calculates the distance between location of the battery
        and current location on grid line
        '''

        distance = abs(x_battery - x_loc) + abs(y_battery - y_loc)

        return distance

    def random_try(self, list_with_houses, list_with_batteries):
        '''
        This function is an algorithm that connects the houses to the batteries
        by taking a random step, evaluating if this step is closer to the battery
        and repeating the process
        '''

        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:

                # find x and y coordinates for the battery and connected house
                x_loc = house_dict['location'][0]
                y_loc = house_dict['location'][1]

    def save_step(self, old_distance, new_distance, house_dict, x_loc, y_loc):
        '''
        in this function a new distance is set, and the step is saved to the grid lists
        '''

        distance = new_distance

        # save the individual steps in the grid list in the dictionary of the house
        house_dict['cables'].append(f'{int(x_loc)},{int(y_loc)}')

        self.x_list.append(x_loc)
        self.y_list.append(y_loc)

        return distance


    def try_steps(self, x_battery, y_battery, x_loc, y_loc, distance, house_dict):
        '''
        This function takes a starting point and a battery location, and repeatedly
        takes steps in random directions, checks if this random step improved
        the state. If so, the step is taken, if not, the step is reset.
        '''

        # compute distance between the battery and the assigned house
        # distance = self.compute_distance(x_battery, y_battery, x_loc, y_loc)
        while distance != 0:
            choice = random.randint(1, 4)

            # take a step left
            if choice == 1:
                x_loc -= 1

                # compute new distance between the new point and the battery
                new_distance = self.compute_distance(x_battery, y_battery, x_loc, y_loc)

                # if the new point is closer to the battery location, take the step
                if new_distance < distance:
                    distance = self.save_step(distance, new_distance, house_dict, x_loc, y_loc)

                # if the new point is not closer to the battery location,
                # reset the step
                else:
                    x_loc += 1

            # take a step right
            elif choice == 2:
                x_loc += 1

                # compute new distance between the new point and the battery
                new_distance = self.compute_distance(x_battery, y_battery, x_loc, y_loc)

                # if the new point is closer to the battery location, take the step
                if new_distance < distance:
                    distance = self.save_step(distance, new_distance, house_dict, x_loc, y_loc)

                # if the new point is not closer to the battery location,
                # reset the step
                else:
                    x_loc -= 1

            # take a step up
            elif choice == 3:
                y_loc += 1

                # compute new distance between the new point and the battery
                new_distance = self.compute_distance(x_battery, y_battery, x_loc, y_loc)

                # if the new point is closer to the battery location, take the step
                if new_distance < distance:
                    distance = self.save_step(distance, new_distance, house_dict, x_loc, y_loc)

                # if the new point is not closer to the battery location,
                # reset the step
                else:
                    y_loc -= 1

            # take a step down
            else:
                y_loc -= 1

                # compute new distance between the new point and the battery
                new_distance = self.compute_distance(x_battery, y_battery, x_loc, y_loc)
                # if the new point is closer to the battery location, take the step
                if new_distance < distance:
                    distance = self.save_step(distance, new_distance, house_dict, x_loc, y_loc)

                # if the new point is not closer to the battery location,
                # reset the step
                else:
                    y_loc += 1


    def random_try(self, list_with_houses, list_with_batteries):
        '''
        This function is an algorithm that connects the houses to the batteries
        by taking a random step, evaluating if this step is closer to the battery
        and repeating the process
        '''

        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:

                # find x and y coordinates for the battery and connected house
                x_loc = house_dict['location'][0]
                y_loc = house_dict['location'][1]

                # save starting point for the grid line
                house_dict['cables'].append(f'{int(x_loc)},{int(y_loc)}')

                # create list with x and y coordinates of the grid line
                self.x_list = [x_loc]
                self.y_list = [y_loc]

                distance = self.compute_distance(battery.x, battery.y, x_loc, y_loc)

                self.try_steps(battery.x, battery.y, x_loc, y_loc, distance, house_dict)

                plt.plot(self.x_list, self.y_list, 'k--')



# ============== RANDOMIZE,PY =============

#from .Classes.smartgrid import Smartgrid
import random
import copy

class Randomize():
    def assign_house_random(self, list_with_houses, list_with_batteries):
        """
        This function assigns the houses to a randomly selected battery.
        """

        # set valid_option to False so it will enter the while loop
        valid_option = False

        # make a copy of the list with batteries to save the capacities
        batteries_copy = copy.deepcopy(list_with_batteries)

        # assign all of the houses to a battery
        # do this untill every house is assigned to a battery that has enough capacity
        while valid_option == False:
            #print('in while')

            # reset the capacities and empty the houses
            for i in range(len(list_with_batteries)):
                list_with_batteries[i].capacity = batteries_copy[i].capacity
                list_with_batteries[i].dict['houses'] = []

            # for i in range(len(list_with_houses)):
            #     list_with_houses[i].dict['grid'] = []
                #print(list_with_batteries[i].dict['houses'])

            #print('na batteries reset')

            # set valid_option to true so if all houses are assigned to a battery
            # that has enough capacity it will leave the while loop
            valid_option = True

            # randomly assign a battery to each house
            for house in list_with_houses:
                #print('huizen vullen')

                # choose a battery of the list_with_batteries
                assigned_battery = random.choice(list_with_batteries)

                # create copy of the battery list for later
                remaining_batteries = copy.copy(list_with_batteries)

                # if the house doesn't fit the battery anymore, choose another battery
                while house.maxoutput > assigned_battery.capacity:
                    #print(assigned_battery.capacity)

                    # remove the full battery of the remaining_batteries
                    remaining_batteries.remove(assigned_battery)

                    if len(remaining_batteries) > 0:
                        # choose another battery if there are any still availeble
                        assigned_battery = random.choice(remaining_batteries)
                    else:
                        # go further with the previous assigned battery that is
                        # already full, but set the valid option to false so it
                        # will run through the while loop again
                        valid_option = False
                        #print('hij is vals')
                        break

                # adjust the capacity of the battery
                assigned_battery.capacity -= house.maxoutput

                # save the dictionary of the house in the list of houses for that battery
                assigned_battery.dict['houses'].append(house.dict)





# ============= SEARCH CABLES ==============



import random
import matplotlib.pyplot as plt

class Search_Cables():
    def __init__(self):
        self.existing_cable_dict = {}

    def search_cables(self, house_dict, battery):
        self.cable_list = []

        # set starting point to the location of the house
        self.location_house_x = float(dictionary_of_house['location'].split(',')[0])
        self.location_house_y = float(dictionary_of_house['location'].split(',')[1])
        # compute distance between the battery and the assigned house
        distance = abs(battery.x - self.location_house_x) + abs(battery.y - self.location_house_y)

        # set starting point to the location of the house
        x_loc = self.location_house_x
        y_loc = self.location_house_y

        # Add these start points to
        house_dict['cables'].append(f'{int(x_loc)}, {int(y_loc)}')

        x_list = [x_loc]
        y_list = [y_loc]

        while distance != 0:
            self.step_score_list = []
            self.step_list = []
            self.distance_list = []

            for choice in range(1,5):
                if choice == 1:
                    step_score_1 = 0
                    step_1 = [x_loc, y_loc, (x_loc - 1), y_loc]
                    step_1_hash = tuple(step_1)

                    #compute the potential new distance with this stap
                    new_distance_1 = abs(battery.x - (x_loc - 1)) + abs(battery.y - y_loc)

                    if new_distance_1 < distance and step_1_hash in self.existing_cable_dict:
                        step_score_1 = 2
                    if new_distance_1 < distance and step_1_hash not in self.existing_cable_dict:
                        step_score_1 = 1

                    self.step_score_list.append(step_score_1)
                    self.step_list.append(step_1)
                    self.distance_list.append(new_distance_1)

                if choice == 2:
                    step_score_2 = 0
                    step_2 = [x_loc, y_loc, (x_loc + 1), y_loc]
                    step_2_hash = tuple(step_2)

                    #compute the potential new distance with this stap
                    new_distance_2 = abs(battery.x - (x_loc + 1)) + abs(battery.y - y_loc)

                    if new_distance_2 < distance and step_2_hash in self.existing_cable_dict:
                        step_score_2 = 2
                    if new_distance_2 < distance and step_2_hash not in self.existing_cable_dict:
                        step_score_2 = 1

                    self.step_score_list.append(step_score_2)
                    self.step_list.append(step_2)
                    self.distance_list.append(new_distance_2)

                if choice == 3:
                    step_score_3 = 0
                    step_3 = [x_loc, y_loc, x_loc, (y_loc + 1)]
                    step_3_hash = tuple(step_3)

                    #compute the potential new distance with this stap
                    new_distance_3 = abs(battery.x - x_loc) + abs(battery.y - (y_loc + 1))

                    if new_distance_3 < distance and step_3_hash in self.existing_cable_dict:
                        step_score_3 = 2
                    if new_distance_3 < distance and step_3_hash not in self.existing_cable_dict:
                        step_score_3 = 1

                    self.step_score_list.append(step_score_3)
                    self.step_list.append(step_3)
                    self.distance_list.append(new_distance_3)

                if choice == 4:
                    step_score_4 = 0
                    step_4 = [x_loc, y_loc, x_loc, (y_loc - 1)]
                    step_4_hash = tuple(step_4)

                    #compute the potential new distance with this stap
                    new_distance_4 = abs(battery.x - x_loc) + abs(battery.y - (y_loc - 1))

                    # Add score to each step based on it's characteristics
                    if new_distance_4 < distance and step_4_hash in self.existing_cable_dict:
                        step_score_4 = 2
                    if new_distance_4 < distance and step_4_hash not in self.existing_cable_dict:
                        step_score_4 = 1

                    self.step_score_list.append(step_score_4)
                    self.step_list.append(step_4)
                    self.distance_list.append(new_distance_4)


            # find step with highest score
            if self.step_score_list.count(2) > 1:
                list_index_2 = []

                for i in range(len(self.step_score_list)):
                    if self.step_score_list[i] == 2:
                        list_index_2.append(i)

                highest_index = random.choice(list_index_2)
            elif self.step_score_list.count(1) > 1:
                list_index_1 = []

                for i in range(len(self.step_score_list)):
                    if self.step_score_list[i] == 1:
                        list_index_1.append(i)

                highest_index = random.choice(list_index_1)
            else:
                highest_index = self.step_score_list.index(max(self.step_score_list))

            # Find the step which belongs with the highest score
            for index, highest in enumerate(self.step_score_list):
                cable_key = tuple(self.step_list[highest_index])

            # Find the new distance which belongs with the highest score
            for index, distance in enumerate(self.step_score_list):
                new_distance = self.distance_list[highest_index]
            # Update the new distance
            distance = new_distance

            x_loc = cable_key[2]
            y_loc = cable_key[3]

            x_list.append(x_loc)
            y_list.append(y_loc)
            house_dict['cables'].append(f'{int(x_loc)}, {int(y_loc)}')

            # Add this cable part to the dictionary
            if cable_key not in self.existing_cable_dict:
                self.existing_cable_dict[cable_key] = 1

        plt.plot(x_list, y_list, 'k--')

    def run_search(self, list_with_houses, list_with_batteries):
        '''
        This function uses the previously defined cables function to connect
        to the houses. It adds in a new condition which ensures that if there is
        a choice between cables with the same distance to the house that it choses
        the path along the cable which is already there. This would optimize the
        distance as well as the cost for the cables.
        '''

        self.steps_count = 0

        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:
                self.search_cables(house_dict, battery)


        return self.steps_count, self.cable_list, self.existing_cable_dict




# =========== SIMULATED ANNEALING ============



import random
import math

from .hill_climber import Hill_Climber

class Simulated_Annealing(Hill_Climber):

    def __init__(self, smartgrid_solution, temperature=1):
        # Use the init of the Hillclimber class
        super().__init__(smartgrid_solution)

        # Starting temperature and current temperature
        self.T0 = temperature
        self.T = temperature


    def update_temperature(self):
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """

        self.T = self.T - (self.T0 / self.iterations)

        # Exponential would look like this:
        # alpha = 0.99
        # self.T = self.T * alpha

        # where alpha can be any value below 1 but above 0

    def check_solution(self, new_smartgrid):
        """
        Checks and accepts better solutions than the current solution.
        Also sometimes accepts solutions that are worse, depending on the current
        temperature.
        """
        self.new_costs += self.steps_house_1 + self.steps_house_2
        #old_value = self.costs

        # Calculate the probability of accepting this new graph
        delta = self.new_costs - self.costs
        probability = math.exp(-delta / self.T)

        # NOTE: Keep in mind that if we want to maximize the value, we use:
        # delta = old_value - new_value

        # Pull a random number between 0 and 1 and see if we accept the graph!
        if random.random() < probability:
            self.smartgrid = new_smartgrid
            self.costs = self.new_costs

        # Update the temperature
        self.update_temperature()




# ====================== VISUALIZE ==============
import os
import json
import matplotlib.pyplot as plt

def visualise():
    cur_path = os.path.dirname(__file__)

    with open(cur_path + '/../../resultaten/output.json', 'r') as file:
        data_list = json.load(file)
        print(data_list)

    position_x_list = []
    position_y_list = []
    color_list = []
    grid_color_list = ['m', 'c', 'g', 'tab:orange', 'tab:brown']

    i = 0
    plt.clf()

    for battery in data_list[1:]:
        position_x_list.append(int(battery['location'].split(',')[0]))
        position_y_list.append(int(battery['location'].split(',')[1]))
        color_list.append('blue')

        color = grid_color_list[i]
        i += 1

        for house in battery['houses']:
            position_x_list.append(int(house['location'].split(',')[0]))
            position_y_list.append(int(house['location'].split(',')[1]))
            color_list.append('red')

            cables_x_list = []
            cables_y_list = []
            for cable in house['cables']:
                cables_x_list.append(int(cable.split(',')[0]))
                cables_y_list.append(int(cable.split(',')[1]))
            plt.plot(cables_x_list, cables_y_list, linestyle='dashed', color=color)


    plt.scatter(position_x_list, position_y_list, color=color_list, marker='s', s=60)
    plt.show()
    plt.clf()




# ============== MAIN.PY ============




import argparse
import pandas as pd
import random
import copy
import seaborn as sns
import matplotlib.pyplot as plt
from code.Classes.smartgrid import Smartgrid
from code.Algorithms.randomize import Randomize
from code.Algorithms.cable_90_degree import Cables_90
from code.Algorithms.random_try import Cables
from code.Algorithms.greedy import Greedy
from code.Algorithms.search_cables import Search_Cables
from code.Algorithms.hill_climber import Hill_Climber
from code.Algorithms.simulated_annealing import Simulated_Annealing
from code.Algorithms.breadth_first import Breadth_first
from code.Algorithms.further_cables import Further_Cables
#from code.Algorithms.breadth_first import Breadth_first

# dit moet eigenlijk in classmethod
def load_df(houses_csv, batteries_csv):
    """
    This function loads the villages and saves them as dataframes
    """
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


    return df_houses, df_batteries

if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "adding houses to batteries")

    # Adding arguments
    #parser.add_argument("output", help = "output file (csv)")
    parser.add_argument("input_houses", help="houses file")
    parser.add_argument("input_batteries", help="batteries_file")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    df_houses, df_batteries = load_df(args.input_houses, args.input_batteries)
    my_smartgrid = Smartgrid(df_houses, df_batteries)

    #my_smartgrid = Smartgrid.from_file(args.input_houses, args.input_batteries)

    houses, batteries = my_smartgrid.add_houses_and_batteries(df_houses, df_batteries)
    #print(houses, batteries)

    # # ----------------- random houses and 90 degrees cables-----------------------
    # create class objects to work with
    random_algo = Randomize()
    greedy_algo = Greedy()
    cable_90_degree = Cables_90()
    cable_random = Cables()
    #cable_breadth = Breadth_first()

    search_cables = Search_Cables()
    cable_breadth = Breadth_first()
    further_cables = Further_Cables()


    # prompt the user to give the district number
    my_smartgrid.district_name()

    # batteries_filled = copy.deepcopy(batteries)
    # houses_filled = copy.deepcopy(houses)

# ----------------------loop with greedy and breadth
    # list_with_costs_greedy_breadth = []
    #
    # for i in range(100):


    # -------------------- loop with random and 90 degrees ----------
    # create list in which to store the costs of this algorithm combination
    # list_with_costs_random_90 = []
    #
    # for i in range(100):
    #

    #     # create battery and houses list of the smartgrid, by making deepcopies
    #     my_smartgrid.battery_list = copy.deepcopy(batteries)
    #     my_smartgrid.houses_list = copy.deepcopy(houses)
    #

    #     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     cable_breadth.breadth(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     my_smartgrid.costs_shared()
    #     my_smartgrid.create_district_dict()
    #     list = my_smartgrid.make_output()
    #     list_with_costs_greedy_breadth.append(list[0]['costs shared'])
    # my_smartgrid.draw_plot()
    #
    # series_with_costs_greedy_breadth = pd.Series(list_with_costs_random_90)
    # print(series_with_costs_greedy_breadth)
    #
    # # plot the distribution of costs for this algorithm
    # plt.clf()
    # plt.title('houses greedy assigned with breadth first cables')
    # sns.histplot(data=series_with_costs_greedy_breadth)
    # plt.show()

    #     # assign the houses with the random algorithm
    #     random_algo.assign_house_random(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # lay the cables with the 90 degrees algorithm
    #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # calculate the costs of the grid
    #     my_smartgrid.costs_shared()
    #
    #     # make sure the output is made
    #     my_smartgrid.create_district_dict()
    #     list = my_smartgrid.make_output()
    #
    #     # append the cost to the list of costs for this combination of algorithms
    #     list_with_costs_random_90.append(list[0]['costs shared'])
    #     print('costs', list[0]['costs shared'])
    #     print(f'{i}/1000')
    #
    # # draw a smartgrid of this combination of algorithms to demonstrate
    # my_smartgrid.draw_plot()
    #
    #
    # # create series of the costs of the algorithm to plot
    # series_with_costs_random_90 = pd.Series(list_with_costs_random_90)
    # print(series_with_costs_random_90)
    #
    # # plot the distribution of costs for this algorithm
    # plt.clf()
    # plt.title('houses random assigned with 90 degree cables')
    # sns.histplot(data=series_with_costs_random_90)
    # plt.show()


#----------------------------loop with greedy and 90 degrees -------------------
# kan voor beide dus!
    # create list in which to keep track of the costs for this combination of algorithms
    # list_with_costs_greedy_90 = []
    #
    # for i in range(100):
    #
    #     # create battery and houses list of the smartgrid, by making deepcopies
    #     my_smartgrid.battery_list = copy.deepcopy(batteries)
    #     my_smartgrid.houses_list = copy.deepcopy(houses)
    #
    #     # assign the houses with the greedy algorithm
    #     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # lay the cables with the 90 degrees algorithm
    #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # calculate the costs
    #     my_smartgrid.costs_shared()
    #
    #     # create output
    #     my_smartgrid.create_district_dict()
    #     list = my_smartgrid.make_output()
    #
    #     # append costs to the list of costs for this combination of algorithms
    #     list_with_costs_greedy_90.append(list[0]['costs shared'])
    #
    #     print('costs', list[0]['costs shared'])
    #     print(f'{i}/1000')
    #
    # # create plot of smartgrid for demonstration
    # my_smartgrid.draw_plot()
    #
    # # make series to plot later
    # series_with_costs_greedy_90 = pd.Series(list_with_costs_greedy_90)
    # print(series_with_costs_greedy_90)
    #
    # # plot the distribution of costs
#     plt.clf()
#     plt.title('houses assigned with greedy and 90 degree cables')
#     sns.histplot(data=series_with_costs_greedy_90)
#     plt.show()
#
# #------------------------- loop with hillclimber and 90 degrees ----------------

    # # create list in which to store the costs of this combination of algorithms
    # list_with_costs_hillclimber_90 = []
    # for i in range(100):
    #
    #     # create deepcopy to ensure that filling the grid lists is correct
    #     my_smartgrid_filled = copy.deepcopy(my_smartgrid)
    #
    #     # create battery and houses list by making deepcopies
    #     my_smartgrid_filled.battery_list = copy.deepcopy(batteries)
    #     my_smartgrid_filled.house_list = copy.deepcopy(houses)
    #
    #     # connect the houses using the random algorithm
    #     random_algo.assign_house_random(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
    #
    #     # lay the cables using the 90 degree algorithm
    #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
    #
    #     # calculate the costs
    #     my_smartgrid_filled.costs_shared()
    #
    #     # initiate hill climber
    #     random_hill_climber = Hill_Climber(my_smartgrid_filled)
    #     random_hill_climber.run(500)
    #
    #     # create output
    #     my_smartgrid_filled.create_district_dict()
    #     list = my_smartgrid_filled.make_output()
    #
    #     # append cost to the list with costs for this algorithm combination
    #     list_with_costs_hillclimber_90.append(list[0]['costs shared'])
    #
    #     print('costs', list[0]['costs shared'])
    #     print(f'{i}/1000')
    #
    # # plot the smartgrid for demonstration
    # my_smartgrid.draw_plot()
    #
    # # create series to plot later
    # series_with_costs_hillclimber_90 = pd.Series(list_with_costs_hillclimber_90)
    # print(series_with_costs_hillclimber_90)
    #
    # # plot the distribution of costs for this algorithm combination
    # plt.clf()
    # plt.title('houses assigned with hillclimber and cables 90 degrees')
    # sns.histplot(data=series_with_costs_hillclimber_90)
    # plt.show()


# -----------------------------------------------------------------------------
# list_with_costs_greedy_breadth = []
#
# for i in range(100):
#     # create battery and houses list of the smartgrid, by making deepcopies
#     my_smartgrid.battery_list = copy.deepcopy(batteries)
#     my_smartgrid.houses_list = copy.deepcopy(houses)
#
#     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     cable_breadth.breadth(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     my_smartgrid.costs_shared()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     list_with_costs_greedy_breadth.append(list[0]['costs shared'])
# my_smartgrid.draw_plot()
#
# series_with_costs_greedy_breadth = pd.Series(list_with_costs_random_90)
# print(series_with_costs_greedy_breadth)
#
# # plot the distribution of costs for this algorithm
# plt.clf()
# plt.title('houses greedy assigned with breadth first cables')
# sns.histplot(data=series_with_costs_greedy_breadth)
# plt.show()
#
# list_with_costs_greedy_breadth = []
#
#
# for i in range(100):
#     # create battery and houses list of the smartgrid, by making deepcopies
#     my_smartgrid.battery_list = copy.deepcopy(batteries)
#     my_smartgrid.houses_list = copy.deepcopy(houses)
#
#     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     cable_breadth.breadth(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     my_smartgrid.costs_shared()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     list_with_costs_greedy_breadth.append(list[0]['costs shared'])
# my_smartgrid.draw_plot()
#
# series_with_costs_greedy_breadth = pd.Series(list_with_costs_random_90)
# print(series_with_costs_greedy_breadth)
#
# # plot the distribution of costs for this algorithm
# plt.clf()
# plt.title('houses greedy assigned with breadth first cables')
# sns.histplot(data=series_with_costs_greedy_breadth)
# plt.show()
# >>>>>>> 194b396a835e32ec32e5925805c01e3b3a8b6e5d
#     # -------------------- loop with random and 90 degrees ----------
# #     # create list in which to store the costs of this algorithm combination
#     list_with_costs_random_90 = []
#
#     for i in range(100):
#
#         # create battery and houses list of the smartgrid, by making deepcopies
#         my_smartgrid.battery_list = copy.deepcopy(batteries)
#         my_smartgrid.houses_list = copy.deepcopy(houses)
#
#         # assign the houses with the random algorithm
#         random_algo.assign_house_random(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # lay the cables with the 90 degrees algorithm
#         step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # calculate the costs of the grid
#         my_smartgrid.costs_shared()
#
#         # make sure the output is made
#         my_smartgrid.create_district_dict()
#         list = my_smartgrid.make_output()
#
#         # append the cost to the list of costs for this combination of algorithms
#         list_with_costs_random_90.append(list[0]['costs shared'])
#         print('costs', list[0]['costs shared'])
#         print(f'{i}/1000')
#
#     # draw a smartgrid of this combination of algorithms to demonstrate
#     my_smartgrid.draw_plot()
#
#
#     # create series of the costs of the algorithm to plot
#     series_with_costs_random_90 = pd.Series(list_with_costs_random_90)
#     print(series_with_costs_random_90)
#
#     # plot the distribution of costs for this algorithm
#     plt.clf()
#     plt.title('houses random assigned with 90 degree cables')
#     sns.histplot(data=series_with_costs_random_90)
#     plt.show()
#
#
# #----------------------------loop with greedy and 90 degrees -------------------
# # kan voor beide dus!
#     # create list in which to keep track of the costs for this combination of algorithms
#     list_with_costs_greedy_90 = []
#
#     for i in range(100):
#
#         # create battery and houses list of the smartgrid, by making deepcopies
#         my_smartgrid.battery_list = copy.deepcopy(batteries)
#         my_smartgrid.houses_list = copy.deepcopy(houses)
#
#         # assign the houses with the greedy algorithm
#         greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # lay the cables with the 90 degrees algorithm
#         step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # calculate the costs
#         my_smartgrid.costs_shared()
#
#         # create output
#         my_smartgrid.create_district_dict()
#         list = my_smartgrid.make_output()
#
#         # append costs to the list of costs for this combination of algorithms
#         list_with_costs_greedy_90.append(list[0]['costs shared'])
#
#         print('costs', list[0]['costs shared'])
#         print(f'{i}/1000')
#
#     # create plot of smartgrid for demonstration
#     my_smartgrid.draw_plot()
#
#     # make series to plot later
#     series_with_costs_greedy_90 = pd.Series(list_with_costs_greedy_90)
#     print(series_with_costs_greedy_90)
#
#     # plot the distribution of costs
#     plt.clf()
#     plt.title('houses assigned with greedy and 90 degree cables')
#     sns.histplot(data=series_with_costs_greedy_90)
#     plt.show()
#
# #------------------------- loop with hillclimber and 90 degrees ----------------
#
#     # # create list in which to store the costs of this combination of algorithms
#     # list_with_costs_hillclimber_90 = []
#     # for i in range(100):
#     #
#     #     # create deepcopy to ensure that filling the grid lists is correct
#     #     my_smartgrid_filled = copy.deepcopy(my_smartgrid)
#     #
#     #     # create battery and houses list by making deepcopies
#     #     my_smartgrid_filled.battery_list = copy.deepcopy(batteries)
#     #     my_smartgrid_filled.house_list = copy.deepcopy(houses)
#     #
#     #     # connect the houses using the random algorithm
#     #     random_algo.assign_house_random(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
#     #
#     #     # lay the cables using the 90 degree algorithm
#     #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
#     #
#     #     # calculate the costs
#     #     my_smartgrid_filled.costs_shared()
#     #
#     #     # initiate hill climber
#     #     random_hill_climber = Hill_Climber(my_smartgrid_filled)
#     #     random_hill_climber.run(500)
#     #
#     #     # create output
#     #     my_smartgrid_filled.create_district_dict()
#     #     list = my_smartgrid_filled.make_output()
#     #
#     #     # append cost to the list with costs for this algorithm combination
#     #     list_with_costs_hillclimber_90.append(list[0]['costs shared'])
#     #
#     #     print('costs', list[0]['costs shared'])
#     #     print(f'{i}/1000')
#     #
#     # # plot the smartgrid for demonstration
#     # my_smartgrid.draw_plot()
#     #
#     # # create series to plot later
#     # series_with_costs_hillclimber_90 = pd.Series(list_with_costs_hillclimber_90)
#     # print(series_with_costs_hillclimber_90)
#     #
#     # # plot the distribution of costs for this algorithm combination
#     # plt.clf()
#     # plt.title('houses assigned with hillclimber and cables 90 degrees')
#     # sns.histplot(data=series_with_costs_hillclimber_90)
#     # plt.show()
#
# # -----------------------------------------------------------------------------

    # random_algo = Randomize()
    # random_algo.assign_house_random(houses, batteries)
    #
    # cable_90_degree = Cables_90()
    # step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
    #
    # #my_smartgrid.draw_plot()
    # my_smartgrid.costs_shared()
    # #my_smartgrid.district_name()
    # my_smartgrid.make_f_string()
    # my_smartgrid.create_district_dict()
    # list = my_smartgrid.make_output()
    # #print(list)
    # #print('costs', list[0]['costs shared'])

# # ------------------------greedy & random-try ---------------------------------
#     # create list in which to store the costs for this combination of algorithms
#     list_with_costs_greedy_random_try = []
#
#     for i in range(100):
#
#         # create battery and houses list by making a deepcopy
#         my_smartgrid.battery_list = copy.deepcopy(batteries)
#         my_smartgrid.houses_list = copy.deepcopy(houses)
#
#         # connect houses to batteries using the greedy algorithm
#         greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # lay cables using the random try algorithm
#         count = cable_random.random_try(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # calculate costs
#         my_smartgrid.costs_shared()
#
#         # create output
#         my_smartgrid.create_district_dict()
#         list = my_smartgrid.make_output()
#
#         # append cost to list with costs for this algorithm combination
#         list_with_costs_greedy_random_try.append(list[0]['costs shared'])
#
#         print('costs', list[0]['costs shared'])
#         print(f'{i}/500')
#
#     # draw smartgrid for demonstration
#     my_smartgrid.draw_plot()
#
#     # create series to plot later
#     series_with_costs_greedy_random_try = pd.Series(list_with_costs_greedy_random_try)
#     print(series_with_costs_greedy_random_try)
#
#     # plot the distribution of costs for this algorithm combination
#     plt.clf()
#     plt.title('houses assigned with greedy, cables with random-try')
#     sns.histplot(data=series_with_costs_greedy_random_try)
#     plt.show()
#
# #------------------------print lists of costs ------------------------
# print(series_with_costs_greedy_90.describe())
# print(series_with_costs_random_90.describe())
# # print(series_with_costs_hillclimber_90.describe())
# print(series_with_costs_greedy_random_try.describe())
#
# mean_greedy_90 = series_with_costs_greedy_90.mean()
# mean_random_90 = series_with_costs_random_90.mean()
# mean_greedy_random_try = series_with_costs_greedy_random_try.mean()
#
# dict_means = {'algorithm':['greedy, 90 degrees', 'random, 90 degrees', 'greedy, random try'], 'means':[mean_greedy_90, mean_random_90, mean_greedy_random_try]}
# df_means = pd.DataFrame(dict_means)
# plt.clf()
# df_means.plot.bar(x='algorithm', y='means')
# plt.show()
#------------------------- search cables --------------------------
#
# list_with_costs_greedy_search = []
#
# for i in range(1):
#
#     # create battery and houses list by making a deepcopy
#     my_smartgrid.battery_list = copy.deepcopy(batteries)
#     my_smartgrid.houses_list = copy.deepcopy(houses)
#
#     # connect houses to batteries using the greedy algorithm
#     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     # lay cables using the random try algorithm
#     count = search_cables.run(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     # calculate costs
#     my_smartgrid.costs_shared()
#
#     # create output
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#
#     # append cost to list with costs for this algorithm combination
#     list_with_costs_greedy_search.append(list[0]['costs shared'])
#
#     print('costs', list[0]['costs shared'])
#     print(f'{i}/500')
#
# # draw smartgrid for demonstration
# my_smartgrid.draw_plot()
#
# # create series to plot later
# series_with_costs_greedy_search = pd.Series(list_with_costs_greedy_search)
# print(series_with_costs_greedy_search)
#
# #plot the distribution of costs for this algorithm combination
# plt.clf()
# plt.title('houses assigned with greedy, cables with search')
# sns.histplot(data=series_with_costs_greedy_search)
# plt.show()
#
# # print(series_with_costs_greedy_90.describe())
# # print(series_with_costs_random_90.describe())
# # print(series_with_costs_hillclimber_90.describe())
# print(series_with_costs_greedy_search.describe())
#
# # mean_greedy_90 = series_with_costs_greedy_90.mean()
# # mean_random_90 = series_with_costs_random_90.mean()
# #mean_greedy_random_try = series_with_costs_greedy_random_try.mean()
# mean_greedy_search = series_with_costs_greedy_search.mean()
#
# dict_means = {'algorithm':['greedy, search cables'], 'means':[mean_greedy_search]}
# df_means = pd.DataFrame(dict_means)
# plt.clf()
# df_means.plot.bar(x='algorithm', y='means')
# plt.show()



# _______________________________FURTHER try:
#
# list_with_costs_further_ = []
#
# for i in range(1):
#
#     # create battery and houses list by making a deepcopy
#     my_smartgrid.battery_list = copy.deepcopy(batteries)
#     my_smartgrid.houses_list = copy.deepcopy(houses)
#
#     # connect houses to batteries using the greedy algorithm
#     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     # lay cables using the random try algorithm
#     count = further_try.run_further(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     # calculate costs
#     my_smartgrid.costs_shared()
#
#     # create output
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#
#     # append cost to list with costs for this algorithm combination
#     list_with_costs_further_try.append(list[0]['costs shared'])
#
#     print('costs', list[0]['costs shared'])
#     print(f'{i}/500')
#
# # draw smartgrid for demonstration
# my_smartgrid.draw_plot()
#
# # create series to plot later
# series_with_costs_greedy_further_try = pd.Series(list_with_costs_further_try)
# print(series_with_costs_greedy_further_try)
#
# #plot the distribution of costs for this algorithm combination
# plt.clf()
# plt.title('houses assigned with greedy, cables with search')
# sns.histplot(data=series_with_costs_greedy_further_try)
# plt.show()
#
# # print(series_with_costs_greedy_90.describe())
# # print(series_with_costs_random_90.describe())
# # print(series_with_costs_hillclimber_90.describe())
# print(series_with_costs_greedy_further_try.describe())
#
# # mean_greedy_90 = series_with_costs_greedy_90.mean()
# # mean_random_90 = series_with_costs_random_90.mean()
# #mean_greedy_random_try = series_with_costs_greedy_random_try.mean()
# mean_greedy_further_try = series_with_costs_greedy_further_try.mean()
#
# dict_means = {'algorithm':['greedy, search cables'], 'means':[mean_greedy_further_try]}
# df_means = pd.DataFrame(dict_means)
# plt.clf()
# df_means.plot.bar(x='algorithm', y='means')
# plt.show()
# #------------------------print lists of costs ------------------------
# print(series_with_costs_greedy_90.describe())
# print(series_with_costs_random_90.describe())
# # print(series_with_costs_hillclimber_90.describe())
# print(series_with_costs_greedy_random_try.describe())
#
# mean_greedy_90 = series_with_costs_greedy_90.mean()
# mean_random_90 = series_with_costs_random_90.mean()
# mean_greedy_random_try = series_with_costs_greedy_random_try.mean()
#
# dict_means = {'algorithm':['greedy, 90 degrees', 'random, 90 degrees', 'greedy, random try'], 'means':[mean_greedy_90, mean_random_90, mean_greedy_random_try]}
# df_means = pd.DataFrame(dict_means)
# plt.clf()
# df_means.plot.bar(x='algorithm', y='means')
# plt.show()

    #---------------- Search cables ---------------------------------------------

#
#     random_algo = Randomize()
#     random_algo.assign_house_random(my_smartgrid.house_list, my_smartgrid.battery_list)
#
#     cable_search = Search_Cables()
#     step_count, cable_list, existing_cable_dict = cable_search.search_cables(my_smartgrid.house_list, my_smartgrid.battery_list)
#
#     my_smartgrid.draw_plot()
#     my_smartgrid.costs(step_count)
#     # my_smartgrid.district_name()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     #print(list)
# # print('costs', list[0]['costs shared'])
#     print(cable_list)
#
# #     self.assign_house_random() # CHECK
# self.make_cables()

    #---------------- FURTHER CABLES ---------------------------------------------

        # random_algo = Randomize()
        # random_algo.assign_house_random(my_smartgrid.house_list, my_smartgrid.battery_list)
        #
        # further_cable_search = Further_Cables()
        # step_count, cable_list, existing_cable_dict = further_cable_search.further_cables(my_smartgrid.house_list, my_smartgrid.battery_list)
        #
        # my_smartgrid.draw_plot()
        # my_smartgrid.costs_shared()
        # # my_smartgrid.district_name()
        # my_smartgrid.create_district_dict()
        # list = my_smartgrid.make_output()
        # #print(list)
        # print('costs', list[0]['costs shared'])
        # print(cable_list)
#____________________________________________________________________

# kan voor beide dus!
    # create list in which to keep track of the costs for this combination of algorithms
    list_with_costs_further = []

    for i in range(200):

        # create battery and houses list of the smartgrid, by making deepcopies
        my_smartgrid.battery_list = copy.deepcopy(batteries)
        my_smartgrid.houses_list = copy.deepcopy(houses)

        # assign the houses with the greedy algorithm
        greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)

        # lay the cables with the 90 degrees algorithm
        step_count = further_cables.run_further(my_smartgrid.houses_list, my_smartgrid.battery_list)

        # calculate the costs
        my_smartgrid.costs_shared()

        # create output
        my_smartgrid.create_district_dict()
        list = my_smartgrid.make_output()

        # append costs to the list of costs for this combination of algorithms
        list_with_costs_further.append(list[0]['costs shared'])

        print('costs', list[0]['costs shared'])
        print(f'{i}/1000')

    # create plot of smartgrid for demonstration
    my_smartgrid.draw_plot()

    # make series to plot later
    series_with_costs_further = pd.Series(list_with_costs_further)
    print(series_with_costs_further)

    # plot the distribution of costs
    plt.clf()
    plt.title('houses assigned with greedy and further search algorithm')
    sns.histplot(data=series_with_costs_further)
    plt.show()


    # print(series_with_costs_greedy_90.describe())
    # print(series_with_costs_random_90.describe())
    # print(series_with_costs_hillclimber_90.describe())
    print(series_with_costs_further.describe())

    # mean_greedy_90 = series_with_costs_greedy_90.mean()
    # mean_random_90 = series_with_costs_random_90.mean()
    #mean_greedy_random_try = series_with_costs_greedy_random_try.mean()
    mean_greedy_further = series_with_costs_further.mean()

    dict_means = {'algorithm':['greedy, further cables'], 'means':[mean_greedy_further]}
    df_means = pd.DataFrame(dict_means)
    plt.clf()
    df_means.plot.bar(x='algorithm', y='means')
    plt.show()






    #---------------- hill climber ---------------------------------------------
#     random_algo = Randomize()
#     random_algo.assign_house_random(houses, batteries)
#
#     cable_90_degree = Cables_90()
#     step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
#
#     my_smartgrid.draw_plot()
#     my_smartgrid.costs_shared()
#     #my_smartgrid.district_name()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     #print(list)
# # print('costs', list[0]['costs shared'])
#     #print(existing_cable_dict)
#     #print(cable_list)
#
#
#
#     random_hill_climber = Hill_Climber(my_smartgrid)
#     random_hill_climber.run(2000)

    #---------------- simulated annealing ---------------------------------------------
#     random_algo = Randomize()
#     random_algo.assign_house_random(houses, batteries)
#
#     cable_90_degree = Cables_90()
#     step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
#
#     my_smartgrid.draw_plot()
#     my_smartgrid.costs_shared()
#     #my_smartgrid.district_name()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     #print(list)
# # print('costs', list[0]['costs shared'])
#     #print(existing_cable_dict)
#     #print(cable_list)
#
#
#
#     random_sa = Simulated_Annealing(my_smartgrid, temperature=200)
#     random_sa.run(2000)




# ========================== MAIN.SCHOON.PY =================

import argparse
import pandas as pd
import random
import copy
import seaborn as sns
import matplotlib.pyplot as plt
from code.Classes.smartgrid import Smartgrid
from code.Algorithms.randomize import Randomize
from code.Algorithms.cable_90_degree import Cables_90
from code.Algorithms.random_try import Cables
from code.Algorithms.greedy import Greedy
from code.Algorithms.search_cables import Search_Cables
from code.Algorithms.hill_climber import Hill_Climber
from code.Algorithms.simulated_annealing import Simulated_Annealing
from code.Algorithms.further_cables import Further_Cables

from code.Visualisation import Visualize as vis
#from code.Algorithms.breadth_first import Breadth_first

# dit moet eigenlijk in classmethod
def load_df(houses_csv, batteries_csv):
    """
    This function loads the villages and saves them as dataframes
    """
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


    return df_houses, df_batteries

if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "adding houses to batteries")

    # Adding arguments
    #parser.add_argument("output", help = "output file (csv)")
    #parser.add_argument("input_houses", help="houses file")
    #parser.add_argument("input_batteries", help="batteries_file")
    parser.add_argument("district", help = "district")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    df_houses, df_batteries = load_df(f'Huizen&Batterijen/district_{args.district}/district-{args.district}_houses.csv', f'Huizen&Batterijen/district_{args.district}/district-{args.district}_batteries.csv')
    my_smartgrid = Smartgrid(df_houses, df_batteries)

    #my_smartgrid = Smartgrid.from_file(args.input_houses, args.input_batteries)

    houses, batteries = my_smartgrid.add_houses_and_batteries(df_houses, df_batteries)
    #print(houses, batteries)


    # # ----------------- random houses and 90 degrees cables-----------------------
    # create class objects to work with
    random_algo = Randomize()
    greedy_algo = Greedy()
    cable_90_degree = Cables_90()
    cable_random = Cables()
    search_cables = Search_Cables()
    further_cables = Further_Cables()



    #cable_breadth = Breadth_first()

    # prompt the user to give the district number
    #my_smartgrid.district_name()

    # -----------------------------------------------------------------------------------

    connections_input = input('What algorithm do you want to use for the connections?: ')
    cables_input = input('What algorithm do you want to use for the cables?: ')
    shared_input = input('Do you want to share the cables?: ')


    connections_dict = {'random': 'random_algo.assign_house_random(houses, batteries)', 'greedy' : 'greedy_algo.assign_closest_battery(houses, batteries)', 'hillclimber' : 'random_hill_climber', 'simulated annealing': 'random_sa'}
    cables_dict = {'90 degrees': 'cable_90_degree.make_90_degrees_cables(houses, batteries)', 'random' : 'cable_random.random_try(houses, batteries)', 'search cables' : 'search_cables.run_search(houses, batteries)', 'further cables': 'further_cables.run_further(houses, batteries)'}

    # eval(connections_dict[connections_input])
    # eval(cables_dict[cables_input])
    #
    # list = my_smartgrid.make_output(args.district, shared_input)
    # print(my_smartgrid.total_cost)


    # -------------------------------------------------------------------------------------

    if connections_input == 'hillclimber' or connections_input == 'simulated annealing':
        random_algo.assign_house_random(houses, batteries)

        eval(cables_dict[cables_input])

        list = my_smartgrid.make_output(args.district, shared_input)
        print(my_smartgrid.total_cost)



        function = cables_dict[cables_input].split('(')[0]
        print(function)




        random_hill_climber = Hill_Climber(my_smartgrid)
        random_sa = Simulated_Annealing(my_smartgrid, temperature=200)


        eval(connections_dict[connections_input]).run(2000, function)


        list = my_smartgrid.make_output(args.district, shared_input)
        print(my_smartgrid.total_cost)






        #
        #     my_smartgrid.draw_plot()
        #     my_smartgrid.costs_shared()
        #     #my_smartgrid.district_name()
        #     my_smartgrid.create_district_dict()
        #     list = my_smartgrid.make_output()
        #     #print(list)
        # # print('costs', list[0]['costs shared'])
        #     #print(existing_cable_dict)
        #     #print(cable_list)
        #
        #
        #
        #     random_hill_climber = Hill_Climber(my_smartgrid)
        #     random_hill_climber.run(2000)


    else:
        eval(connections_dict[connections_input])
        eval(cables_dict[cables_input])

        list = my_smartgrid.make_output(args.district, shared_input)
        print(my_smartgrid.total_cost)

        vis.visualise()





    # batteries_filled = copy.deepcopy(batteries)
    # houses_filled = copy.deepcopy(houses)

    # -------------------- loop with random and 90 degrees ----------
    # # create list in which to store the costs of this algorithm combination
    # list_with_costs_random_90 = []
    #
    # for i in range(100):
    #
    #     # create battery and houses list of the smartgrid, by making deepcopies
    #     my_smartgrid.battery_list = copy.deepcopy(batteries)
    #     my_smartgrid.houses_list = copy.deepcopy(houses)
    #
    #     # assign the houses with the random algorithm
    #     random_algo.assign_house_random(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # lay the cables with the 90 degrees algorithm
    #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # calculate the costs of the grid
    #     my_smartgrid.costs_shared()
    #
    #     # make sure the output is made
    #     my_smartgrid.create_district_dict()
    #     list = my_smartgrid.make_output()
    #
    #     # append the cost to the list of costs for this combination of algorithms
    #     list_with_costs_random_90.append(list[0]['costs shared'])
    #     print('costs', list[0]['costs shared'])
    #     print(f'{i}/1000')
    #
    # # draw a smartgrid of this combination of algorithms to demonstrate
    # my_smartgrid.draw_plot()
    #
    #
    # # create series of the costs of the algorithm to plot
    # series_with_costs_random_90 = pd.Series(list_with_costs_random_90)
    # print(series_with_costs_random_90)
    #
    # # plot the distribution of costs for this algorithm
    # plt.clf()
    # plt.title('houses random assigned with 90 degree cables')
    # sns.histplot(data=series_with_costs_random_90)
    # plt.show()
    #

#----------------------------loop with greedy and 90 degrees -------------------
# kan voor beide dus!
    # create list in which to keep track of the costs for this combination of algorithms
    # list_with_costs_greedy_90 = []
    #
    # for i in range(100):
    #
    #     # create battery and houses list of the smartgrid, by making deepcopies
    #     my_smartgrid.battery_list = copy.deepcopy(batteries)
    #     my_smartgrid.houses_list = copy.deepcopy(houses)
    #
    #     # assign the houses with the greedy algorithm
    #     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # lay the cables with the 90 degrees algorithm
    #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # calculate the costs
    #     my_smartgrid.costs_shared()
    #
    #     # create output
    #     my_smartgrid.create_district_dict()
    #     list = my_smartgrid.make_output()
    #
    #     # append costs to the list of costs for this combination of algorithms
    #     list_with_costs_greedy_90.append(list[0]['costs shared'])
    #
    #     print('costs', list[0]['costs shared'])
    #     print(f'{i}/1000')
    #
    # # create plot of smartgrid for demonstration
    # my_smartgrid.draw_plot()
    #
    # # make series to plot later
    # series_with_costs_greedy_90 = pd.Series(list_with_costs_greedy_90)
    # print(series_with_costs_greedy_90)
    #
    # # plot the distribution of costs
    # plt.clf()
    # plt.title('houses assigned with greedy and 90 degree cables')
    # sns.histplot(data=series_with_costs_greedy_90)
    # plt.show()
#
# #------------------------- loop with hillclimber and 90 degrees ----------------

    # # create list in which to store the costs of this combination of algorithms
    # list_with_costs_hillclimber_90 = []
    # for i in range(100):
    #
    #     # create deepcopy to ensure that filling the grid lists is correct
    #     my_smartgrid_filled = copy.deepcopy(my_smartgrid)
    #
    #     # create battery and houses list by making deepcopies
    #     my_smartgrid_filled.battery_list = copy.deepcopy(batteries)
    #     my_smartgrid_filled.house_list = copy.deepcopy(houses)
    #
    #     # connect the houses using the random algorithm
    #     random_algo.assign_house_random(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
    #
    #     # lay the cables using the 90 degree algorithm
    #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
    #
    #     # calculate the costs
    #     my_smartgrid_filled.costs_shared()
    #
    #     # initiate hill climber
    #     random_hill_climber = Hill_Climber(my_smartgrid_filled)
    #     random_hill_climber.run(500)
    #
    #     # create output
    #     my_smartgrid_filled.create_district_dict()
    #     list = my_smartgrid_filled.make_output()
    #
    #     # append cost to the list with costs for this algorithm combination
    #     list_with_costs_hillclimber_90.append(list[0]['costs shared'])
    #
    #     print('costs', list[0]['costs shared'])
    #     print(f'{i}/1000')
    #
    # # plot the smartgrid for demonstration
    # my_smartgrid.draw_plot()
    #
    # # create series to plot later
    # series_with_costs_hillclimber_90 = pd.Series(list_with_costs_hillclimber_90)
    # print(series_with_costs_hillclimber_90)
    #
    # # plot the distribution of costs for this algorithm combination
    # plt.clf()
    # plt.title('houses assigned with hillclimber and cables 90 degrees')
    # sns.histplot(data=series_with_costs_hillclimber_90)
    # plt.show()


# -----------------------------------------------------------------------------
    # list_with_costs_greedy_breadth = []
    #
    # for i in range(100):
    #     # create battery and houses list of the smartgrid, by making deepcopies
    #     my_smartgrid.battery_list = copy.deepcopy(batteries)
    #     my_smartgrid.houses_list = copy.deepcopy(houses)
    #
    #     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     cable_breadth.breadth(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     my_smartgrid.costs_shared()
    #     my_smartgrid.create_district_dict()
    #     list = my_smartgrid.make_output()
    #     list_with_costs_greedy_breadth.append(list[0]['costs shared'])
    # my_smartgrid.draw_plot()
    #
    # series_with_costs_greedy_breadth = pd.Series(list_with_costs_random_90)
    # print(series_with_costs_greedy_breadth)
    #
    # # plot the distribution of costs for this algorithm
    # plt.clf()
    # plt.title('houses greedy assigned with breadth first cables')
    # sns.histplot(data=series_with_costs_greedy_breadth)
    # plt.show()
    # -------------------- loop with random and 90 degrees ----------
#     # create list in which to store the costs of this algorithm combination
#     list_with_costs_random_90 = []
#
#     for i in range(100):
#
#         # create battery and houses list of the smartgrid, by making deepcopies
#         my_smartgrid.battery_list = copy.deepcopy(batteries)
#         my_smartgrid.houses_list = copy.deepcopy(houses)
#
#         # assign the houses with the random algorithm
#         random_algo.assign_house_random(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # lay the cables with the 90 degrees algorithm
#         step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # calculate the costs of the grid
#         my_smartgrid.costs_shared()
#
#         # make sure the output is made
#         my_smartgrid.create_district_dict()
#         list = my_smartgrid.make_output()
#
#         # append the cost to the list of costs for this combination of algorithms
#         list_with_costs_random_90.append(list[0]['costs shared'])
#         print('costs', list[0]['costs shared'])
#         print(f'{i}/1000')
#
#     # draw a smartgrid of this combination of algorithms to demonstrate
#     my_smartgrid.draw_plot()
#
#
#     # create series of the costs of the algorithm to plot
#     series_with_costs_random_90 = pd.Series(list_with_costs_random_90)
#     print(series_with_costs_random_90)
#
#     # plot the distribution of costs for this algorithm
#     plt.clf()
#     plt.title('houses random assigned with 90 degree cables')
#     sns.histplot(data=series_with_costs_random_90)
#     plt.show()
#
#
# #----------------------------loop with greedy and 90 degrees -------------------
# # kan voor beide dus!
#     # create list in which to keep track of the costs for this combination of algorithms
#     list_with_costs_greedy_90 = []
#
#     for i in range(100):
#
#         # create battery and houses list of the smartgrid, by making deepcopies
#         my_smartgrid.battery_list = copy.deepcopy(batteries)
#         my_smartgrid.houses_list = copy.deepcopy(houses)
#
#         # assign the houses with the greedy algorithm
#         greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # lay the cables with the 90 degrees algorithm
#         step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # calculate the costs
#         my_smartgrid.costs_shared()
#
#         # create output
#         my_smartgrid.create_district_dict()
#         list = my_smartgrid.make_output()
#
#         # append costs to the list of costs for this combination of algorithms
#         list_with_costs_greedy_90.append(list[0]['costs shared'])
#
#         print('costs', list[0]['costs shared'])
#         print(f'{i}/1000')
#
#     # create plot of smartgrid for demonstration
#     my_smartgrid.draw_plot()
#
#     # make series to plot later
#     series_with_costs_greedy_90 = pd.Series(list_with_costs_greedy_90)
#     print(series_with_costs_greedy_90)
#
#     # plot the distribution of costs
#     plt.clf()
#     plt.title('houses assigned with greedy and 90 degree cables')
#     sns.histplot(data=series_with_costs_greedy_90)
#     plt.show()
#
# #------------------------- loop with hillclimber and 90 degrees ----------------
#
#     # # create list in which to store the costs of this combination of algorithms
#     # list_with_costs_hillclimber_90 = []
#     # for i in range(100):
#     #
#     #     # create deepcopy to ensure that filling the grid lists is correct
#     #     my_smartgrid_filled = copy.deepcopy(my_smartgrid)
#     #
#     #     # create battery and houses list by making deepcopies
#     #     my_smartgrid_filled.battery_list = copy.deepcopy(batteries)
#     #     my_smartgrid_filled.house_list = copy.deepcopy(houses)
#     #
#     #     # connect the houses using the random algorithm
#     #     random_algo.assign_house_random(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
#     #
#     #     # lay the cables using the 90 degree algorithm
#     #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
#     #
#     #     # calculate the costs
#     #     my_smartgrid_filled.costs_shared()
#     #
#     #     # initiate hill climber
#     #     random_hill_climber = Hill_Climber(my_smartgrid_filled)
#     #     random_hill_climber.run(500)
#     #
#     #     # create output
#     #     my_smartgrid_filled.create_district_dict()
#     #     list = my_smartgrid_filled.make_output()
#     #
#     #     # append cost to the list with costs for this algorithm combination
#     #     list_with_costs_hillclimber_90.append(list[0]['costs shared'])
#     #
#     #     print('costs', list[0]['costs shared'])
#     #     print(f'{i}/1000')
#     #
#     # # plot the smartgrid for demonstration
#     # my_smartgrid.draw_plot()
#     #
#     # # create series to plot later
#     # series_with_costs_hillclimber_90 = pd.Series(list_with_costs_hillclimber_90)
#     # print(series_with_costs_hillclimber_90)
#     #
#     # # plot the distribution of costs for this algorithm combination
#     # plt.clf()
#     # plt.title('houses assigned with hillclimber and cables 90 degrees')
#     # sns.histplot(data=series_with_costs_hillclimber_90)
#     # plt.show()
#
# # -----------------------------------------------------------------------------
    #
    # #random_algo = Randomize()
    # random_algo.assign_house_random(houses, batteries)
    #
    # cable_90_degree = Cables_90()
    # step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
    #
    # #my_smartgrid.draw_plot()
    # my_smartgrid.costs_shared()
    # #my_smartgrid.district_name()
    # my_smartgrid.make_f_string()
    # my_smartgrid.create_district_dict()
    # list = my_smartgrid.make_output()
    # #print(list)
    # #print('costs', list[0]['costs shared'])





    # #random_algo = Randomize()
    # greedy_algo.assign_closest_battery(houses, batteries)
    #
    # cable_90_degree = Cables_90()
    # step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
    #
    # # #my_smartgrid.draw_plot()
    # # my_smartgrid.costs_shared()
    # # #my_smartgrid.district_name()
    # # my_smartgrid.make_f_string()
    # # my_smartgrid.create_district_dict()
    # list = my_smartgrid.make_output()
    # #print(list)
    # #print('costs', list[0]['costs shared'])

# # ------------------------greedy & random-try ---------------------------------
#     # create list in which to store the costs for this combination of algorithms
#     list_with_costs_greedy_random_try = []
#
#     for i in range(100):
#
#         # create battery and houses list by making a deepcopy
#         my_smartgrid.battery_list = copy.deepcopy(batteries)
#         my_smartgrid.houses_list = copy.deepcopy(houses)
#
#         # connect houses to batteries using the greedy algorithm
#         greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # lay cables using the random try algorithm
#         count = cable_random.random_try(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # calculate costs
#         my_smartgrid.costs_shared()
#
#         # create output
#         my_smartgrid.create_district_dict()
#         list = my_smartgrid.make_output()
#
#         # append cost to list with costs for this algorithm combination
#         list_with_costs_greedy_random_try.append(list[0]['costs shared'])
#
#         print('costs', list[0]['costs shared'])
#         print(f'{i}/500')
#
#     # draw smartgrid for demonstration
#     my_smartgrid.draw_plot()
#
#     # create series to plot later
#     series_with_costs_greedy_random_try = pd.Series(list_with_costs_greedy_random_try)
#     print(series_with_costs_greedy_random_try)
#
#     # plot the distribution of costs for this algorithm combination
#     plt.clf()
#     plt.title('houses assigned with greedy, cables with random-try')
#     sns.histplot(data=series_with_costs_greedy_random_try)
#     plt.show()
#
# #------------------------print lists of costs ------------------------
# print(series_with_costs_greedy_90.describe())
# print(series_with_costs_random_90.describe())
# # print(series_with_costs_hillclimber_90.describe())
# print(series_with_costs_greedy_random_try.describe())
#
# mean_greedy_90 = series_with_costs_greedy_90.mean()
# mean_random_90 = series_with_costs_random_90.mean()
# mean_greedy_random_try = series_with_costs_greedy_random_try.mean()
#
# dict_means = {'algorithm':['greedy, 90 degrees', 'random, 90 degrees', 'greedy, random try'], 'means':[mean_greedy_90, mean_random_90, mean_greedy_random_try]}
# df_means = pd.DataFrame(dict_means)
# plt.clf()
# df_means.plot.bar(x='algorithm', y='means')
# plt.show()
#------------------------- search cables --------------------------


# list_with_costs_greedy_random_try = []
#
# for i in range(100):
#
#     # create battery and houses list by making a deepcopy
#     my_smartgrid.battery_list = copy.deepcopy(batteries)
#     my_smartgrid.houses_list = copy.deepcopy(houses)
#
#     # connect houses to batteries using the greedy algorithm
#     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     # lay cables using the random try algorithm
#     count = cable_random.search_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     # calculate costs
#     my_smartgrid.costs_shared()
#
#     # create output
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#
#     # append cost to list with costs for this algorithm combination
#     list_with_costs_greedy_random_try.append(list[0]['costs shared'])
#
#     print('costs', list[0]['costs shared'])
#     print(f'{i}/500')
#
# # draw smartgrid for demonstration
# my_smartgrid.draw_plot()
#
# # create series to plot later
# series_with_costs_greedy_random_try = pd.Series(list_with_costs_greedy_random_try)
# print(series_with_costs_greedy_random_try)
#
# # plot the distribution of costs for this algorithm combination
# plt.clf()
# plt.title('houses assigned with greedy, cables with random-try')
# sns.histplot(data=series_with_costs_greedy_random_try)
# plt.show()
#
# #------------------------print lists of costs ------------------------
# print(series_with_costs_greedy_90.describe())
# print(series_with_costs_random_90.describe())
# # print(series_with_costs_hillclimber_90.describe())
# print(series_with_costs_greedy_random_try.describe())
#
# mean_greedy_90 = series_with_costs_greedy_90.mean()
# mean_random_90 = series_with_costs_random_90.mean()
# mean_greedy_random_try = series_with_costs_greedy_random_try.mean()
#
# dict_means = {'algorithm':['greedy, 90 degrees', 'random, 90 degrees', 'greedy, random try'], 'means':[mean_greedy_90, mean_random_90, mean_greedy_random_try]}
# df_means = pd.DataFrame(dict_means)
# plt.clf()
# df_means.plot.bar(x='algorithm', y='means')
# plt.show()


    #---------------- hill climber ---------------------------------------------
#     random_algo = Randomize()
#     random_algo.assign_house_random(houses, batteries)
#
#     cable_90_degree = Cables_90()
#     step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
#
#     my_smartgrid.draw_plot()
#     my_smartgrid.costs_shared()
#     #my_smartgrid.district_name()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     #print(list)
# # print('costs', list[0]['costs shared'])
#     #print(existing_cable_dict)
#     #print(cable_list)
#
#
#
#     random_hill_climber = Hill_Climber(my_smartgrid)
#     random_hill_climber.run(2000)

    #---------------- simulated annealing ---------------------------------------------
#     random_algo = Randomize()
#     random_algo.assign_house_random(houses, batteries)
#
#     cable_90_degree = Cables_90()
#     step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
#
#     my_smartgrid.draw_plot()
#     my_smartgrid.costs_shared()
#     #my_smartgrid.district_name()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     #print(list)
# # print('costs', list[0]['costs shared'])
#     #print(existing_cable_dict)
#     #print(cable_list)
#
#
#
#     random_sa = Simulated_Annealing(my_smartgrid, temperature=200)
#     random_sa.run(2000)
