import random

class Cables():
    def random_try(self, list_with_houses, list_with_batteries):
        '''
        this function is an algorithm that connects the houses to the batteries
        by taking a random step, evaluating if this step is closer to the battery
        and repeating the process
        '''
        self.steps_count = 0
        for battery in list_with_batteries:
            for house_dict in battery.dict['connected houses']:

                # find x and y coordinates for the battery and connected house
                location_house_x = house_dict['house location'][0]
                location_house_y = house_dict['house location'][1]
                location_battery_x = battery.dict['battery location'][0]
                location_battery_y = battery.dict['battery location'][1]

                # compute distance between the battery and the assigned house
                distance = abs((location_battery_x - location_house_x) + (location_battery_y - location_house_y))

                # set starting point to the location of the house
                x_loc = location_house_x
                y_loc = location_house_y

                #while x_loc != location_battery_x and y_loc != location_battery_y:
                while distance != 0:
                    print(x_loc)
                    print(y_loc)
                    choice = random.randint(1, 4)

                    # take a step left
                    if choice == 1:
                        x_loc -= 1

                        # compute new distance between the new point and the battery
                        new_distance = abs((location_battery_x - x_loc) + (location_battery_y - y_loc))
                        print('links')

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            x_loc += 1

                    # take a step right
                    elif choice == 2:
                        x_loc += 1

                        # compute new distance between the new point and the battery
                        new_distance = abs((location_battery_x - x_loc) + (location_battery_y - y_loc))
                        print('rechts')

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            x_loc -= 1

                    # take a step up
                    elif choice == 3:
                        y_loc += 1

                        # compute new distance between the new point and the battery
                        new_distance = abs((location_battery_x - x_loc) + (location_battery_y - y_loc))
                        print('omhoog', y_loc)

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            y_loc -= 1

                    # take a step down
                    else:
                        y_loc -= 1

                        # compute new distance between the new point and the battery
                        new_distance = abs((location_battery_x - x_loc) + (location_battery_y - y_loc))
                        print('omlaag')

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            y_loc += 1
        return self.steps_count
