import random
import matplotlib.pyplot as plt

class Cables():
    def compute_distance(x_battery, y_battery, x_loc, y_loc):
        """ this function calculates the distance between location of the battery
        and current location on grid line """

        distance = abs(x_battery - x_loc) + abs(y_battery - y_loc)

        return distance
        
    def random_try(self, list_with_houses, list_with_batteries):
        '''
        This function is an algorithm that connects the houses to the batteries
        by taking a random step, evaluating if this step is closer to the battery
        and repeating the process
        '''
        self.steps_count = 0
        for battery in list_with_batteries:
            for house_dict in battery.dict['connected houses']:

                # find x and y coordinates for the battery and connected house
                x_loc = house_dict['house location'][0]
                y_loc = house_dict['house location'][1]
<<<<<<< HEAD
                # location_battery_x = battery.x
                # location_battery_y = battery.y
=======
>>>>>>> 95750b815c259e40642996e2ed1585bcfc8aa13b

                # compute distance between the battery and the assigned house
                distance = compute_distance(battery.x, battery.y, x_loc, y_loc)

                # save starting point for the grid line
                house_dict['grid'].append(f'{x_loc}, {y_loc}')

                # create list with x and y coordinates of the grid line
                x_list = [x_loc]
                y_list = [y_loc]

                # keep taking steps until the distance between x and y loc and battery location
                # is 0
                while distance != 0:
                    choice = random.randint(1, 4)

                    # take a step left
                    if choice == 1:
                        x_loc -= 1

                        # compute new distance between the new point and the battery
                        new_distance = compute_distance(battery.x, battery.y, x_loc, y_loc)

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                            x_list.append(x_loc)
                            y_list.append(y_loc)

                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            x_loc += 1

                    # take a step right
                    elif choice == 2:
                        x_loc += 1

                        # compute new distance between the new point and the battery
                        new_distance = compute_distance(battery.x, battery.y, x_loc, y_loc)

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                            x_list.append(x_loc)
                            y_list.append(y_loc)

                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            x_loc -= 1

                    # take a step up
                    elif choice == 3:
                        y_loc += 1

                        # compute new distance between the new point and the battery
                        new_distance = compute_distance(battery.x, battery.y, x_loc, y_loc)

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                            x_list.append(x_loc)
                            y_list.append(y_loc)

                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            y_loc -= 1

                    # take a step down
                    else:
                        y_loc -= 1

                        # compute new distance between the new point and the battery
                        new_distance = compute_distance(battery.x, battery.y, x_loc, y_loc)
                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                            x_list.append(x_loc)
                            y_list.append(y_loc)

                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            y_loc += 1

                plt.plot(x_list, y_list, 'k--')
        return self.steps_count
