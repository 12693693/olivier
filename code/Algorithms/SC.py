import random
import matplotlib.pyplot as plt

class SearchC():
    def __init__(self):
        self.existing_cable_dict = {}

    def search_cables(self, house_dict, battery):
        self.cable_list = []

        # set starting point to the location of the house
        self.location_house_x = float(house_dict['location'].split(',')[0])
        self.location_house_y = float(house_dict['location'].split(',')[1])

        # compute distance between the battery and the assigned house
        distance = abs(battery.x - self.location_house_x) + abs(battery.y - self.location_house_y)

        # set starting point to the location of the house
        x_loc = self.location_house_x
        y_loc = self.location_house_y

        # Add these start points to
        house_dict['cables'].append(f'{int(x_loc)},{int(y_loc)}')

        x_list = [x_loc]
        y_list = [y_loc]

        while distance != 0:
            self.step_score_list = []
            self.step_list = []
            self.distance_list = []

            for choice in range(1, 5):

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

    def highest_score(self, step_score_list):
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

        return highest_index


    def set_step(self, highest_index):
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
        house_dict['cables'].append(f'{int(x_loc)},{int(y_loc)}')

        # Add this cable part to the dictionary
        if cable_key not in self.existing_cable_dict:
            self.existing_cable_dict[cable_key] = 1

        return self.existing_cable_dict


    def run_search_2(self, list_with_houses, list_with_batteries):
        '''
        This function uses the previously defined cables function to connect
        to the houses. It adds in a new condition which ensures that if there is
        a choice between cables with the same distance to the house that it choses
        the path along the cable which is already there. This would optimize the
        distance as well as the cost for the cables.
        '''

        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:
                self.search_cables(house_dict, battery)


        return self.cable_list, self.existing_cable_dict
