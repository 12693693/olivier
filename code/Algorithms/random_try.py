import random

class Cables():
    def random_try(self, list_with_houses, list_with_batteries):
        '''
        this function is an algorithm that connects the houses to the batteries
        by taking a random step, evaluating if this step is closer to the battery
        and repeating the process
        '''

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
                y_loc = loctation_house_y

                while x_loc != location_battery_x or y_loc != location_battery_y:
                    choice = random.randint(1, 4)

                    # take a step left
                    if choice == 1:
                        x_loc -= 1

                        # compute new distance between the new point and the battery
                        new_distance = abs((location_battery_x - x_loc))

                    # take a step right
                    elif choice == 2:

                    # take a step up
                    elif choice == 3:

                    # take a step down
                    else:
