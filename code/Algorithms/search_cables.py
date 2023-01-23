import random
import matplotlib.pyplot as plt

class Search_Cables():
    def search_cables(self, list_with_houses, list_with_batteries):
        '''
        This function uses the previously defined cables function to connect the
        to the houses. It adds in a new condition which ensures that if there is
        a choice between cables with the same distance to the house that it choses
        the path along the cable which is already there. This would optimize the
        distance as well as the cost for the cables.
        '''
        self.existing_cable_dict = {}
        self.steps_count = 0
        for battery in list_with_batteries:
            for house_dict in battery.dict['connected houses']:

                self.cable_list = []
                # find x and y coordinates for the battery and connected house
                location_house_x = house_dict['house location'][0]
                location_house_y = house_dict['house location'][1]

                # compute distance between the battery and the assigned house
                distance = abs(battery.x - location_house_x) + abs(battery.y - location_house_y)

                # set starting point to the location of the house
                x_loc = location_house_x
                y_loc = location_house_y

                house_dict['grid'].append(f'{x_loc}, {y_loc}')

                #save the individuap cable step in a list to later add it to a dictionary
                self.cable_list.append(x_loc)
                self.cable_list.append(y_loc)

                x_list = [x_loc]
                y_list = [y_loc]


                #while x_loc != location_battery_x and y_loc != location_battery_y:
                while distance != 0:
                    choice = random.randint(1, 4)

#-------------------- step left ------------------
                    # take a step left
                    if choice == 1:
                        #define the step that would be taken in this case
                        step = (x_loc, y_loc, (x_loc - 1), y_loc)

                        #compute the potential new distance with this stap
                        new_distance = abs(battery.x - (x_loc - 1)) + abs(battery.y - y_loc)

                        #Add the condition in which you look for this step in the
                        # existing cables if this distance is smaller than the old one
                        if step in self.existing_cable_dict and new_distance < distance:
                            x_loc -= 1

                            # Add this grid to the grid dictionary.
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                        else:
                            self.cable_list = []
                            self.cable_list.append(x_loc)
                            self.cable_list.append(y_loc)

                            x_loc -= 1

                            # compute new distance between the new point and the battery
                            new_distance = abs(battery.x - x_loc) + abs(battery.y - y_loc)

                            # if the new point is closer to the battery location, take the step
                            if new_distance < distance:
                                distance = new_distance
                                self.steps_count += 1

                                # save the individual steps in the grid list in the dictionary of the house
                                house_dict['grid'].append(f'{x_loc}, {y_loc}')

                                x_list.append(x_loc)
                                y_list.append(y_loc)
                                self.cable_list.append(x_loc)
                                self.cable_list.append(y_loc)

                                # Add the final step to a cable list
                                cable_key = f'{self.cable_list}'

                                # Add this list to the dictionary
                                self.existing_cable_dict[cable_key] = 1

                            else:
                                x_loc += 1

#------------------- step right ------------------
                    # take a step right
                    elif choice == 2:
                        #define the step that would be taken in this case
                        step = (x_loc, y_loc, (x_loc + 1), y_loc)

                        #compute the potential new distance with this stap
                        new_distance = abs(battery.x - (x_loc + 1)) + abs(battery.y - y_loc)

                        #Add the condition in which you look for this step in the
                        # existing cables if this distance is smaller than the old one
                        if step in self.existing_cable_dict and new_distance < distance:
                            x_loc += 1

                            # Add this grid to the grid dictionary.
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')


                        # If this step is not in the dictionary or if it's not
                        # smaller than the current distance use the previous method to
                        # find the new step.
                        else:
                            self.cable_list = []
                            self.cable_list.append(x_loc)
                            self.cable_list.append(y_loc)

                            x_loc += 1

                            # compute new distance between the new point and the battery
                            new_distance = abs(battery.x - x_loc) + abs(battery.y - y_loc)

                            # if the new point is closer to the battery location, take the step
                            if new_distance < distance:
                                distance = new_distance
                                self.steps_count += 1

                                # save the individual steps in the grid list in the dictionary of the house
                                house_dict['grid'].append(f'{x_loc}, {y_loc}')

                                x_list.append(x_loc)
                                y_list.append(y_loc)
                                self.cable_list.append(x_loc)
                                self.cable_list.append(y_loc)

                                # Add the final step to a cable list
                                cable_key = f'{self.cable_list}'

                                # Add this list to the dictionary
                                self.existing_cable_dict[cable_key] = 1

                            # if the new point is not closer to the battery location,
                            # reset the step
                            else:
                                x_loc -= 1

#------------------- step up -----------------
                    # take a step up
                    elif choice == 3:
                        step = (x_loc, y_loc, x_loc, (y_loc + 1))
                        new_distance = abs(battery.x - x_loc) + abs(battery.y - (y_loc + 1))
                        if step in self.existing_cable_dict and new_distance < distance:
                            y_loc += 1
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                        else:
                            self.cable_list = []
                            self.cable_list.append(x_loc)
                            self.cable_list.append(y_loc)

                            y_loc += 1

                            # compute new distance between the new point and the battery
                            new_distance = abs(battery.x - x_loc) + abs(battery.y - y_loc)

                            # if the new point is closer to the battery location, take the step
                            if new_distance < distance:
                                distance = new_distance
                                self.steps_count += 1

                                # save the individual steps in the grid list in the dictionary of the house
                                house_dict['grid'].append(f'{x_loc}, {y_loc}')

                                x_list.append(x_loc)
                                y_list.append(y_loc)
                                self.cable_list.append(x_loc)
                                self.cable_list.append(y_loc)

                                # Add the final step to a cable list
                                cable_key = f'{self.cable_list}'

                                # Add this list to the dictionary
                                self.existing_cable_dict[cable_key] = 1
                            # if the new point is not closer to the battery location,
                            # reset the step
                            else:
                                y_loc -= 1


#-------------------- step down ----------------
                    # take a step down
                    else:
                        step = (x_loc, y_loc, x_loc, (y_loc + 1))
                        new_distance = abs(battery.x - x_loc) + abs(battery.y - y_loc - 1)
                        if step in self.existing_cable_dict and new_distance < distance:
                            y_loc -= 1
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                        else:
                            self.cable_list = []
                            self.cable_list.append(x_loc)
                            self.cable_list.append(y_loc)

                            y_loc -= 1

                            # compute new distance between the new point and the battery
                            new_distance = abs(battery.x - x_loc) + abs(battery.y - y_loc)

                            # if the new point is closer to the battery location, take the step
                            if new_distance < distance:
                                distance = new_distance
                                self.steps_count += 1

                                # save the individual steps in the grid list in the dictionary of the house
                                house_dict['grid'].append(f'{x_loc}, {y_loc}')

                                x_list.append(x_loc)
                                y_list.append(y_loc)
                                self.cable_list.append(x_loc)
                                self.cable_list.append(y_loc)

                                # Add the final step to a cable list
                                cable_key = f'{self.cable_list}'

                                # Add this list to the dictionary
                                self.existing_cable_dict[cable_key] = 1
                            # if the new point is not closer to the battery location,
                            # reset the step
                            else:
                                y_loc += 1

                    # # Add the final step to a cable list
                    # cable_key = f'{self.cable_list}'
                    #
                    # # Add this list to the dictionary
                    # self.existing_cable_dict[cable_key] = 1

                plt.plot(x_list, y_list, 'k--')

        return self.steps_count, self.cable_list, self.existing_cable_dict
