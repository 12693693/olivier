import matplotlib.pyplot as plt
class Cables_90():

    def get_location(self, dictionary_of_house):
        #print(dictionary_of_house['location'].split(',')[0])
        #print(dictionary_of_house['location'])
        self.location_house_x = float(dictionary_of_house['location'].split(',')[0])
        self.location_house_y = float(dictionary_of_house['location'].split(',')[1])

    def plot_cable_90(self, loc_house_x, loc_house_y, battery):
        x_list = [loc_house_x, battery.x, battery.x]
        y_list = [loc_house_y, loc_house_y, battery.y]


    def make_lines_90(self, dictionary_of_house, battery):
        step_count = 0

        # create starting point for creating the grid line
        # and add the starting point to the grid dictionary
        #print('dict', dictionary_of_house['location'])

        x_loc = self.location_house_x
        y_loc = self.location_house_y
        dictionary_of_house['cables'].append(f'{int(x_loc)},{int(y_loc)}')

        # compute distance to use as a constraint for choosing which way
        # to move on the grid line

        #print(self.location_house_x, battery.x)
        #print(self.location_house_x)
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
            dictionary_of_house['cables'].append(f'{int(x_loc)},{int(y_loc)}')

        # take steps until the correct y coordinate is reached
        # and keep track of the grid line
        while y_loc != battery.y:
            if distance_y > 0:
                y_loc -= 1
            else:
                y_loc += 1
            step_count += 1

            # save the individual steps in the grid list in the dictionary of the house
            dictionary_of_house['cables'].append(f'{int(x_loc)},{int(y_loc)}')

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

        return steps_count
