import matplotlib.pyplot as plt
class Cables_90():

    def get_location(self, dictionary_of_house):
        """
        This function finds the x and y location of the house.
        """

        self.location_house_x = float(dictionary_of_house['location'].split(',')[0])
        self.location_house_y = float(dictionary_of_house['location'].split(',')[1])

    # def plot_cable_90(self, loc_house_x, loc_house_y, battery):
    #
    #     x_list = [loc_house_x, battery.x, battery.x]
    #     y_list = [loc_house_y, loc_house_y, battery.y]


    def make_lines_90(self, dictionary_of_house, battery):
        """
        This function fills the dictionary of the house with 90 degrees cables
        """
        # step_count = 0

        # Create starting point for creating the cables and add to the cables
        # dictionary
        x_loc = self.location_house_x
        y_loc = self.location_house_y
        dictionary_of_house['cables'].append(f'{int(x_loc)},{int(y_loc)}')

        # Compute distance to use as a constraint for choosing which way
        # to move
        distance_x = self.location_house_x - battery.x
        distance_y = self.location_house_y - battery.y

        # Take steps until the correct x coordinate is reached
        while x_loc != battery.x:
            if distance_x > 0:
                x_loc -= 1
            else:
                x_loc += 1
            # step_count += 1

            # Save the individual steps in the cable list in the dictionary of
            # the house
            dictionary_of_house['cables'].append(f'{int(x_loc)},{int(y_loc)}')

        # Take steps until the correct y coordinate is reached
        while y_loc != battery.y:
            if distance_y > 0:
                y_loc -= 1
            else:
                y_loc += 1
            # step_count += 1

            # Save the individual steps in the grid list in the dictionary of
            # the house
            dictionary_of_house['cables'].append(f'{int(x_loc)},{int(y_loc)}')

        # return step_count

    def make_90_degrees_cable(self, dictionary_of_house, battery):
        """
        This function gets the location of the house and lays the cables to the
        matched battery.
        """
        self.get_location(dictionary_of_house)
        #self.plot_cable_90(self.location_house_x, self.location_house_y, battery)
        self.make_lines_90(dictionary_of_house, battery)

        # return step_count


    def make_90_degrees_cables(self, list_with_houses, list_with_batteries):
        """
        This function computes the cables and saves it to the dictionary of
        each house.
        """
        # steps_count = 0


        # Loop over batteries and the houses that are connected to that battery
        # and fill the dictionary with the cables
        for battery in list_with_batteries:
            for house_dict in battery.dict['houses']:
                steps_count += self.make_90_degrees_cable(house_dict, battery)

        # return steps_count
