import matplotlib.pyplot as plt
class Cables_90():

    def get_location(self, dictionary_of_house):
        self.location_house_x = dictionary_of_house['house location'][0]
        self.location_house_y = dictionary_of_house['house location'][1]

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
        dictionary_of_house['grid'].append(f'{x_loc}, {y_loc}')

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
            dictionary_of_house['grid'].append(f'{x_loc}, {y_loc}')

        # take steps until the correct y coordinate is reached
        # and keep track of the grid line
        while y_loc != battery.y:
            if distance_y > 0:
                y_loc -= 1
            else:
                y_loc += 1
            step_count += 1

            # save the individual steps in the grid list in the dictionary of the house
            dictionary_of_house['grid'].append(f'{x_loc}, {y_loc}')

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
            for house_dict in battery.dict['connected houses']:
                steps_count += self.make_90_degrees_cable(house_dict, battery)




                # # find x and y coordinates for the battery and connected house
                # self.get_location(house_dict)
                # self.plot_cable(self.location_house_x, self.location_house_y, battery)

                # # extra
                # location_house_x = house_dict['house location'][0]
                # location_house_y = house_dict['house location'][1]
                # location_battery_x = battery.dict['battery location'][0]
                # location_battery_y = battery.dict['battery location'][1]


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
