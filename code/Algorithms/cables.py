
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
            for house_dict in battery.dict['connected houses']:

                # find x and y coordinates for the battery and connected house
                location_house_x = house_dict['house location'][0]
                location_house_y = house_dict['house location'][1]
                location_battery_x = battery.dict['battery location'][0]
                location_battery_y = battery.dict['battery location'][1]

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
                    house_dict['grid'].append(f'{x_loc}, {y_loc}')

                # take steps until the correct y coordinate is reached
                # and keep track of the grid line
                while y_loc != location_battery_y:
                    if distance_y > 0:
                        y_loc -= 1
                    else:
                        y_loc += 1
                    self.steps_count += 1

                    # save the individual steps in the grid list in the dictionary of the house
                    house_dict['grid'].append(f'{x_loc}, {y_loc}')
