import random
import matplotlib.pyplot as plt

class Search_Cables():
    def search_cables(self, list_with_houses, list_with_batteries):
        '''
        This function uses the previously defined cables function to connect
        to the houses. It adds in a new condition which ensures that if there is
        a choice between cables with the same distance to the house that it choses
        the path along the cable which is already there. This would optimize the
        distance as well as the cost for the cables.
        '''
        self.existing_cable_dict = {}
        self.steps_count = 0
        count = 0

        for battery in list_with_batteries:
            print(len(battery.dict['connected houses']))
            for house_dict in battery.dict['connected houses']:
                count+=1


                self.cable_list = []
                # set starting point to the location of the house
                location_house_x = house_dict['house location'][0]
                location_house_y = house_dict['house location'][1]

                # compute distance between the battery and the assigned house
                distance = abs(battery.x - location_house_x) + abs(battery.y - location_house_y)
                #
                # set starting point to the location of the house
                x_loc = location_house_x
                y_loc = location_house_y

                house_dict['grid'].append(f'{x_loc}, {y_loc}')

                #save the individuap cable step in a list to later add it to a dictionary
                # self.cable_list.append(x_loc)
                # self.cable_list.append(y_loc)

                x_list = [x_loc]
                y_list = [y_loc]

                # self.step_score_list = []
                # self.step_list = []
                # self.distance_list = []

                #while x_loc != location_battery_x and y_loc != location_battery_y:
                while distance != 0:
                    self.step_score_list = []
                    self.step_list = []
                    self.distance_list = []
                    # print('old location', x_loc, y_loc)
                    #print(distance, 'oud')
                    #choice = random.randint(1, 4)
                    # print('hello')
                    for choice in range(1,5):
                        #print('in forloop')
                        if choice == 1:
                            #print('1')
                            step_score_1 = 0
                            step_1 = [x_loc, y_loc, (x_loc - 1), y_loc]
                            step_1_hash = tuple(step_1)

                            #compute the potential new distance with this stap
                            new_distance_1 = abs(battery.x - (x_loc - 1)) + abs(battery.y - y_loc)
                            #print(new_distance_1)

                            if new_distance_1 < distance and step_1_hash in self.existing_cable_dict:
                                step_score_1 = 2
                            if new_distance_1 < distance and step_1_hash not in self.existing_cable_dict:
                                step_score_1 = 1
                            # else:
                            #     step_score_1 = 0

                            #print(step_score_1)
                            self.step_score_list.append(step_score_1)
                            self.step_list.append(step_1)
                            self.distance_list.append(new_distance_1)

                        if choice == 2:
                            #print('2')
                            step_score_2 = 0
                            step_2 = [x_loc, y_loc, (x_loc + 1), y_loc]
                            step_2_hash = tuple(step_2)

                            #compute the potential new distance with this stap
                            new_distance_2 = abs(battery.x - (x_loc + 1)) + abs(battery.y - y_loc)

                            if new_distance_2 < distance and step_2_hash in self.existing_cable_dict:
                                step_score_2 = 2
                            if new_distance_2 < distance and step_2_hash not in self.existing_cable_dict:
                                step_score_2 = 1
                            # else:
                            #     step_score_2 = 0

                            self.step_score_list.append(step_score_2)
                            self.step_list.append(step_2)
                            self.distance_list.append(new_distance_2)

                        if choice == 3:
                            #print('3')
                            step_score_3 = 0
                            step_3 = [x_loc, y_loc, x_loc, (y_loc + 1)]
                            step_3_hash = tuple(step_3)

                            #compute the potential new distance with this stap
                            new_distance_3 = abs(battery.x - x_loc) + abs(battery.y - (y_loc + 1))

                            if new_distance_3 < distance and step_3_hash in self.existing_cable_dict:
                                step_score_3 = 2
                            if new_distance_3 < distance and step_3_hash not in self.existing_cable_dict:
                                step_score_3 = 1
                            # else:
                            #     step_score_3 = 0

                            self.step_score_list.append(step_score_3)
                            self.step_list.append(step_3)
                            self.distance_list.append(new_distance_3)

                        if choice == 4:
                            #print('4')
                            step_score_4 = 0
                            step_4 = [x_loc, y_loc, x_loc, (y_loc - 1)]
                            step_4_hash = tuple(step_4)

                            #compute the potential new distance with this stap
                            new_distance_4 = abs(battery.x - x_loc) + abs(battery.y - (y_loc - 1))

                            # Add score to each step based on it's characteristics
                            if new_distance_4 < distance and step_4_hash in self.existing_cable_dict:
                                step_score_4 = 2
                            if new_distance_4 < distance and step_4_hash not in self.existing_cable_dict:
                                step_score_4 = 1
                            # else:
                            #     step_score_4 = 0

                            self.step_score_list.append(step_score_4)
                            self.step_list.append(step_4)
                            self.distance_list.append(new_distance_4)



                        # find step with highest score
                    if self.step_score_list.count(2) > 1:
                        list_index_2 =  []

                        for score in self.step_score_list:
                            # indexen vna de 1
                            if score == 2:
                                list_index_2.append(self.step_score_list.index(score))

                        highest_index = random.choice(list_index_2)
                    elif self.step_score_list.count(1) > 1:
                        list_index_1 =  []

                        for score in self.step_score_list:
                            # indexen vna de 1
                            if score == 1:
                                list_index_1.append(self.step_score_list.index(score))
                        highest_index = random.choice(list_index_1)
                    else:
                        highest_index = self.step_score_list.index(max(self.step_score_list))

                    # find the step which belongs with the highest score
                    for index, highest in enumerate(self.step_score_list):
                        cable_key = tuple(self.step_list[highest_index])
                        # print(cable_key, 'step')


                        #find the new distance which belongs with the highest score
                    for index, distance in enumerate(self.step_score_list):
                        new_distance = self.distance_list[highest_index]
                        # print(new_distance, 'distance')
                    #
                    # print(self.step_score_list)
                    # print(self.step_list)
                    # print(self.distance_list)

                    distance = new_distance
                    # print(distance, 'new')

                    x_loc = cable_key[2]
                    y_loc = cable_key[3]

                    # print('new location', x_loc, y_loc)

                    x_list.append(x_loc)
                    y_list.append(y_loc)
                    # house_dict['grid'].append(f'{x_loc}, {y_loc}')
                    # print(house_dict['grid'])

                    # Add this list to the dictionary
                    if cable_key not in self.existing_cable_dict:
                        self.existing_cable_dict[cable_key] = 1
                    #     self.steps_count += 1
                    #
                    # self.costs = (self.steps_count * 9) + 2500

                house_dict['grid'].append(f'{x_loc}, {y_loc}')

                plt.plot(x_list, y_list, 'k--')
            print(count)

        return self.steps_count, self.cable_list, self.existing_cable_dict

    


# #-------------------- step left ------------------
#                     # take a step left
#                         if choice == 1:
#                             step_score_1 = 0
#                             #define the step that would be taken in this case
#                             step = (x_loc, y_loc, (x_loc - 1), y_loc)
#
#                             #compute the potential new distance with this stap
#                             new_distance = abs(battery.x - (x_loc - 1)) + abs(battery.y - y_loc)
#
#                             #Add the condition in which you look for this step in the
#                             # existing cables if this distance is smaller than the old one
#                             if step in self.existing_cable_dict and new_distance < distance:
#                                 x_loc -= 1
#                                 step_score = 2
#                                 # Add this grid to the grid dictionary.
#                                 house_dict['grid'].append(f'{x_loc}, {y_loc}')
#
#                             else:
#                                 self.cable_list = []
#                                 self.cable_list.append(x_loc)
#                                 self.cable_list.append(y_loc)
#
#                                 x_loc -= 1
#
#                                 # compute new distance between the new point and the battery
#                                 new_distance = abs(battery.x - x_loc) + abs(battery.y - y_loc)
#
#                                 # if the new point is closer to the battery location, take the step
#                                 if new_distance < distance:
#                                     distance = new_distance
#                                     self.steps_count += 1
#
#                                     # save the individual steps in the grid list in the dictionary of the house
#                                     house_dict['grid'].append(f'{x_loc}, {y_loc}')
#
#                                     x_list.append(x_loc)
#                                     y_list.append(y_loc)
#                                     self.cable_list.append(x_loc)
#                                     self.cable_list.append(y_loc)
#
#                                     # Add the final step to a cable list
#                                     cable_key = f'{self.cable_list}'
#
#                                     # Add this list to the dictionary
#                                     self.existing_cable_dict[cable_key] = 1
#
#                                 else:
#                                     x_loc += 1
#
# #------------------- step right ------------------
#                         # take a step right
#                         elif choice == 2:
#                             #define the step that would be taken in this case
#                             step = (x_loc, y_loc, (x_loc + 1), y_loc)
#
#                             #compute the potential new distance with this stap
#                             new_distance = abs(battery.x - (x_loc + 1)) + abs(battery.y - y_loc)
#
#                             #Add the condition in which you look for this step in the
#                             # existing cables if this distance is smaller than the old one
#                             if step in self.existing_cable_dict and new_distance < distance:
#                                 x_loc += 1
#
#                                 # Add this grid to the grid dictionary.
#                                 house_dict['grid'].append(f'{x_loc}, {y_loc}')
#
#
#                             # If this step is not in the dictionary or if it's not
#                             # smaller than the current distance use the previous method to
#                             # find the new step.
#                             else:
#                                 self.cable_list = []
#                                 self.cable_list.append(x_loc)
#                                 self.cable_list.append(y_loc)
#
#                                 x_loc += 1
#
#                                 # compute new distance between the new point and the battery
#                                 new_distance = abs(battery.x - x_loc) + abs(battery.y - y_loc)
#
#                                 # if the new point is closer to the battery location, take the step
#                                 if new_distance < distance:
#                                     distance = new_distance
#                                     self.steps_count += 1
#
#                                     # save the individual steps in the grid list in the dictionary of the house
#                                     house_dict['grid'].append(f'{x_loc}, {y_loc}')
#
#                                     x_list.append(x_loc)
#                                     y_list.append(y_loc)
#                                     self.cable_list.append(x_loc)
#                                     self.cable_list.append(y_loc)
#
#                                     # Add the final step to a cable list
#                                     cable_key = f'{self.cable_list}'
#
#                                     # Add this list to the dictionary
#                                     self.existing_cable_dict[cable_key] = 1
#
#                                 # if the new point is not closer to the battery location,
#                                 # reset the step
#                                 else:
#                                     x_loc -= 1
#
#     #------------------- step up -----------------
#                         # take a step up
#                         elif choice == 3:
#                             step = (x_loc, y_loc, x_loc, (y_loc + 1))
#                             new_distance = abs(battery.x - x_loc) + abs(battery.y - (y_loc + 1))
#                             if step in self.existing_cable_dict and new_distance < distance:
#                                 y_loc += 1
#                                 house_dict['grid'].append(f'{x_loc}, {y_loc}')
#
#                             else:
#                                 self.cable_list = []
#                                 self.cable_list.append(x_loc)
#                                 self.cable_list.append(y_loc)
#
#                                 y_loc += 1
#
#                                 # compute new distance between the new point and the battery
#                                 new_distance = abs(battery.x - x_loc) + abs(battery.y - y_loc)
#
#                                 # if the new point is closer to the battery location, take the step
#                                 if new_distance < distance:
#                                     distance = new_distance
#                                     self.steps_count += 1
#
#                                     # save the individual steps in the grid list in the dictionary of the house
#                                     house_dict['grid'].append(f'{x_loc}, {y_loc}')
#
#                                     x_list.append(x_loc)
#                                     y_list.append(y_loc)
#                                     self.cable_list.append(x_loc)
#                                     self.cable_list.append(y_loc)
#
#                                     # Add the final step to a cable list
#                                     cable_key = f'{self.cable_list}'
#
#                                     # Add this list to the dictionary
#                                     self.existing_cable_dict[cable_key] = 1
#                                 # if the new point is not closer to the battery location,
#                                 # reset the step
#                                 else:
#                                     y_loc -= 1
#
#
#     #-------------------- step down ----------------
#                         # take a step down
#                         else:
#                             step = (x_loc, y_loc, x_loc, (y_loc + 1))
#                             new_distance = abs(battery.x - x_loc) + abs(battery.y - y_loc - 1)
#                             if step in self.existing_cable_dict and new_distance < distance:
#                                 y_loc -= 1
#                                 house_dict['grid'].append(f'{x_loc}, {y_loc}')
#
#                             else:
#                                 self.cable_list = []
#                                 self.cable_list.append(x_loc)
#                                 self.cable_list.append(y_loc)
#
#                                 y_loc -= 1
#
#                                 # compute new distance between the new point and the battery
#                                 new_distance = abs(battery.x - x_loc) + abs(battery.y - y_loc)
#
#                                 # if the new point is closer to the battery location, take the step
#                                 if new_distance < distance:
#                                     distance = new_distance
#                                     self.steps_count += 1
#
#                                     # save the individual steps in the grid list in the dictionary of the house
#                                     house_dict['grid'].append(f'{x_loc}, {y_loc}')
#
#                                     x_list.append(x_loc)
#                                     y_list.append(y_loc)
#                                     self.cable_list.append(x_loc)
#                                     self.cable_list.append(y_loc)
#
#                                     # Add the final step to a cable list
#                                     cable_key = f'{self.cable_list}'
#
#                                     # Add this list to the dictionary
#                                     self.existing_cable_dict[cable_key] = 1
#                                 # if the new point is not closer to the battery location,
#                                 # reset the step
#                                 else:
#                                     y_loc += 1
#
#                     # # Add the final step to a cable list
#                     # cable_key = f'{self.cable_list}'
#                     #
#                     # # Add this list to the dictisonary
#                     # self.existing_cable_dict[cable_key] = 1
#
#                 plt.plot(x_list, y_list, 'k--')
#
#         return self.steps_count, self.cable_list, self.existing_cable_dict
