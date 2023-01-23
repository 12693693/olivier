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
                location_battery_x = battery.dict['battery location'][0]
                location_battery_y = battery.dict['battery location'][1]



                # compute distance between the battery and the assigned house
                distance = abs(battery.x - location_house_x) + (battery.y - location_house_y))

                # set starting point to the location of the house
                x_loc = location_house_x
                y_loc = location_house_y

                #save the individuap cable step in a list to later add it to a dictionary
                self.cable_list.append(x_loc)
                self.cable_list.append(y_loc)


                x_list = [x_loc]
                y_list = [y_loc]


                #while x_loc != location_battery_x and y_loc != location_battery_y:
                while distance != 0:
                    choice = random.randint(1, 4)

                    # take a step left
                    if choice == 1:
                        x_loc -= 1

                        # compute new distance between the new point and the battery
                        new_distance = abs((battery.x - x_loc) + (battery.y - y_loc))

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                            x_list.append(x_loc)
                            y_list.append(y_loc)

                            #save the final point of the cable in list
                            # self.cable_list.append(x_loc)
                            # self.cable_list.append(y_loc)
                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            x_loc += 1
                            # self.cable_list.append(x_loc)
                            # self.cable_list.append(y_loc)

                    # take a step right
                    elif choice == 2:
                        x_loc += 1

                        # compute new distance between the new point and the battery
                        new_distance = abs((battery.x - x_loc) + (battery.y - y_loc))

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                            x_list.append(x_loc)
                            y_list.append(y_loc)

                            # self.cable_list.append(x_loc)
                            # self.cable_list.append(y_loc)
                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            x_loc -= 1
                            # self.cable_list.append(x_loc)
                            # self.cable_list.append(y_loc)

                    # take a step up
                    elif choice == 3:
                        y_loc += 1

                        # compute new distance between the new point and the battery
                        new_distance = abs((battery.x - x_loc) + (battery.y - y_loc))

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                            x_list.append(x_loc)
                            y_list.append(y_loc)

                            # self.cable_list.append(x_loc)
                            # self.cable_list.append(y_loc)

                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            y_loc -= 1
                            # self.cable_list.append(x_loc)
                            # self.cable_list.append(y_loc)

                    # take a step down
                    else:
                        y_loc -= 1

                        # compute new distance between the new point and the battery
                        new_distance = abs((battery.x - x_loc) + (battery.y - y_loc))

                        # if the new point is closer to the battery location, take the step
                        if new_distance < distance:
                            distance = new_distance
                            self.steps_count += 1

                            # save the individual steps in the grid list in the dictionary of the house
                            house_dict['grid'].append(f'{x_loc}, {y_loc}')

                            x_list.append(x_loc)
                            y_list.append(y_loc)
                            # self.cable_list.append(x_loc)
                            # self.cable_list.append(y_loc)

                        # if the new point is not closer to the battery location,
                        # reset the step
                        else:
                            y_loc += 1

                            self.cable_list.append('--')
                            self.cable_list.append(x_loc)
                            print(x_loc)
                            self.cable_list.append(y_loc)
                            print(y_loc)

                            cable_key = f'{self.cable_list}'

                            self.existing_cable_dict[cable_key] = 1

                plt.plot(x_list, y_list, 'k--')

        return self.steps_count, self.cable_list, self.existing_cable_dict



















































#____________________________________________________________________________________________





        # existing_cable_dict = {}
        # self.steps_count = 0
        #
        # # loop over batteries and the houses that are connected to that battery
        # for battery in list_with_batteries:
        #
        #     for house_dict in battery.dict['connected houses']:
        #
        #         # find x and y coordinates for the battery and connected house
        #         location_house_x = house_dict['house location'][0]
        #         location_house_y = house_dict['house location'][1]
        #         location_battery_x = battery.dict['battery location'][0]
        #         location_battery_y = battery.dict['battery location'][1]
        #
        #         x_list = [location_house_x, location_battery_x, location_battery_x]
        #         y_list = [location_house_y, location_house_y, location_battery_y]
        #         plt.plot(x_list, y_list, 'k--')
        #
        #         # create starting point for creating the grid line
        #         x_loc = location_house_x
        #         y_loc = location_house_y
        #
        #         # compute distance to use as a constraint for choosing which way
        #         # to move on the grid line
        #         distance_x = location_house_x - location_battery_x
        #         distance_y = location_house_y - location_battery_y
        #
        #         temporary_distance_x = battery_point[0] - existing_cable_dict[walking_point][0]
        #         temporary_distance_y = battery_point[0] - existing_cable_dict[walking_point][1]
        # #
        #         battery_point = [location_battery_x, location_battery_y]
        #         walking_point = [x_loc,y_loc]
        #         while walking_point != battery_point:
        #             if walking_point in existing_cable_dict[key][0]:
        #                 if temporary_distance_x =< battery_point[0] - walking_point[0]
        #                 or temporary_distance_y =< battery_point[1] - walking_point[1]:
        #                     walking_point = existing_cable_dict[key][1]
        # #             else:
        #                 while x_loc != battery_point[0]:
        #                     if distance_x > 0:
        #                         x_loc -= 1
        #                     else:
        #                         x_loc += 1
        #
        #                 while y_loc != battery_point[1]:
        #                     if distance_y > 0:
        #                         y_loc -= 1
        #                     else:
        #                         y_loc += 1
        #                     walking_point = [x_loc, y_loc]
        #
        #                     self.steps_count += 1
        #
        # #         # take steps until the correct x coordinate is reached
        # #         # and keep track of the steps count
        # #         while x_loc != location_battery_x:
        # #             #for point in existing_cables_list:
        # #             if distance_x > 0:
        # #                 x_loc -= 1
        # #             else:
        # #                 x_loc += 1
        # #             self.steps_count += 1
        # #
        # #             # save the individual steps in the grid list in the dictionary of the house
        # #             house_dict['grid'].append(f'{x_loc}, {y_loc}')
        # #
        # #         # take steps until the correct y coordinate is reached
        # #         # and keep track of the grid line
        # #         while y_loc != location_battery_y:
        # #             if distance_y > 0:
        # #                 y_loc -= 1
        # #             else:
        # #                 y_loc += 1
        # #             self.steps_count += 1
        # #
        # #             # save the individual steps in the grid list in the dictionary of the house
        # #             house_dict['grid'].append(f'{x_loc}, {y_loc}')
        # #
        # #     for start_point in house_dict['grid']:
        # #         existing_cable_dict[start_point] = house_dict['grid'][start_point + 1]
        # #
        # # return self.steps_count, house_dict
