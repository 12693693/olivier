import random
import matplotlib.pyplot as plt

class Further_Cables():
    def __init__(self):
        self.existing_cable_dict = {}

    def create_step_lists(self, new_distance, distance, step_hash, next_step, next_next_step, step):
        '''
        This function determines the score for each step and their charateristics.
        It then updates the score, step and distance list based on the outcome and
        returns the step_score_list.
        '''

        step_score = 0

        # Determine the score for this step direction
        if new_distance < distance and step_hash in self.existing_cable_dict:
            step_score =+ 2
        if new_distance < distance and step_hash not in self.existing_cable_dict:
            step_score =+ 1
        if new_distance < distance and next_step in self.existing_cable_dict:
            step_score =+ 2
        if new_distance < distance and next_next_step in self.existing_cable_dict:
            step_score =+ 2

        # Add this score, distance and step to the lists.
        self.step_score_list.append(step_score)
        self.step_list.append(step)
        self.distance_list.append(new_distance)

        return self.step_score_list

    def find_highest(self, step_score_list):
        '''
        This function uses the score list to find the highest one in this list.
        If there are multiple instances of this highest score it chooses one random
        and returns this as the highest index. This is later on used to find the
        accompanied distance and step.
        '''

        if self.step_score_list.count(2) > 1:
            list_index_2 = []

            for i in range(len(self.step_score_list)):
                if self.step_score_list[i] == 2:
                    list_index_2.append(i)

            highest_index = random.choice(list_index_2)

        # If there are multiple high scores chose a random one from these high scores.
        elif self.step_score_list.count(1) > 1:
            list_index_1 = []

            for i in range(len(self.step_score_list)):
                if self.step_score_list[i] == 1:
                    list_index_1.append(i)

            highest_index = random.choice(list_index_1)
        else:
            highest_index = self.step_score_list.index(max(self.step_score_list))

        return highest_index

    def further_cables(self, house_dict, battery):
        '''
        This function uses the previously defined cables function to connect
        to the houses. It adds in a new condition which ensures that if there is
        a choice between cables with the same distance to the house that it choses
        the path along the cable which is already there. In addition to the search cables
        this one also looks at the cable may be two steps away.
        This would optimize the distance as well as the cost for the cables.
        '''

        # Intiate the dictionary which will be used later
        self.cable_list = []

        # Set starting point to the location of the house
        self.location_house_x = float(house_dict['location'].split(',')[0])
        self.location_house_y = float(house_dict['location'].split(',')[1])

        # Compute distance between the battery and the assigned house
        distance = abs(battery.x - self.location_house_x) + abs(battery.y - self.location_house_y)

        # Set starting point to the location of the house
        x_loc = self.location_house_x
        y_loc = self.location_house_y

        # Add these start points to the grid list
        house_dict['cables'].append(f'{int(x_loc)},{int(y_loc)}')

        x_list = [x_loc]
        y_list = [y_loc]

        # Initiate and set condition for the while loop
        while distance != 0:
            self.step_score_list = []
            self.step_list = []
            self.distance_list = []

            # Loop over the choices for the steps direction.
            for choice in range(1,5):
                if choice == 1:
                    step_score_1 = 0
                    step_1 = [x_loc, y_loc, (x_loc - 1), y_loc]
                    step_1_hash = tuple(step_1)
                    next_step_1 = tuple([x_loc, y_loc, (x_loc - 2), y_loc])
                    next_next_step_1 = tuple([x_loc, y_loc, (x_loc - 3), y_loc])

                    # Compute the potential new distance with this step
                    new_distance_1 = abs(battery.x - (x_loc - 1)) + abs(battery.y - y_loc)

                    # Add this step to the lists with potential steps
                    self.create_step_lists(new_distance_1, distance, step_1_hash, next_step_1, next_next_step_1, step_1)

                if choice == 2:
                    step_score_2 = 0
                    step_2 = [x_loc, y_loc, (x_loc + 1), y_loc]
                    step_2_hash = tuple(step_2)
                    next_step_2 = tuple([x_loc, y_loc, (x_loc + 2), y_loc])
                    next_next_step_2 = tuple([x_loc, y_loc, (x_loc + 3), y_loc])

                    # Compute the potential new distance with this step
                    new_distance_2 = abs(battery.x - (x_loc + 1)) + abs(battery.y - y_loc)

                    # Add this step to the lists with potential steps
                    self.create_step_lists(new_distance_2, distance, step_2_hash, next_step_2, next_next_step_2, step_2)

                if choice == 3:
                    step_score_3 = 0
                    step_3 = [x_loc, y_loc, x_loc, (y_loc + 1)]
                    step_3_hash = tuple(step_3)
                    next_step_3 = tuple([x_loc, y_loc, x_loc, (y_loc + 2)])
                    next_next_step_3 = tuple([x_loc, y_loc, x_loc, (y_loc + 3)])

                    # Compute the potential new distance with this step
                    new_distance_3 = abs(battery.x - x_loc) + abs(battery.y - (y_loc + 1))

                    # Add this step to the lists with potential steps
                    self.create_step_lists(new_distance_3, distance, step_3_hash, next_step_3, next_next_step_3, step_3)

                if choice == 4:
                    step_score_4 = 0
                    step_4 = [x_loc, y_loc, x_loc, (y_loc - 1)]
                    step_4_hash = tuple(step_4)
                    next_step_4 = tuple([x_loc, y_loc, x_loc, (y_loc - 2)])
                    next_next_step_4 = tuple([x_loc, y_loc, x_loc, (y_loc - 3)])

                    # Compute the potential new distance with this step
                    new_distance_4 = abs(battery.x - x_loc) + abs(battery.y - (y_loc - 1))

                    # Add this step to the lists with potential steps
                    self.create_step_lists(new_distance_4, distance, step_4_hash, next_step_4, next_next_step_4, step_4)


            # Find step with highest score. Choose this step.
            highest_index = self.find_highest(self.step_score_list)

            # Find the step which belongs with the highest score
            for index, highest in enumerate(self.step_score_list):
                cable_key = tuple(self.step_list[highest_index])

            # Find the new distance which belongs with the highest score
            for index, distance in enumerate(self.step_score_list):
                new_distance = self.distance_list[highest_index]

            # Update the distance for this new distance with the step added.
            distance = new_distance

            # Find the x and y location from this cable list.
            x_loc = cable_key[2]
            y_loc = cable_key[3]

            # Add these locations to the grid.
            x_list.append(x_loc)
            y_list.append(y_loc)
            house_dict['cables'].append(f'{int(x_loc)},{int(y_loc)}')

            # Add this cable part to the dictionary
            if cable_key not in self.existing_cable_dict:
                self.existing_cable_dict[cable_key] = 1

    def run_further(self, list_with_houses, list_with_batteries):
        '''
        This functions runs the Further_Cables function on this specific list
        of houses and batteries with these combinations.
        '''

        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:
                self.further_cables(house_dict, battery)

        return self.cable_list, self.existing_cable_dict
