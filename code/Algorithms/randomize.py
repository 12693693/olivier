#from .Classes.smartgrid import Smartgrid
import random
import copy

class Randomize():

    def assign_house_random(self, list_with_houses, list_with_batteries):
        """
        This function assigns the houses to a randomly selected battery.
        """
        valid_option = False

        #
        while valid_option == False:
            valid_option = True
            print('run')
            # randomly assign a battery to each house
            for house in list_with_houses:

                assigned_battery = random.choice(list_with_batteries)

                # create copy of the battery list for later
                new_battery_list = copy.copy(list_with_batteries)

                # if the house doesn't fit the battery anymore, choose another battery
                while house.maxoutput > assigned_battery.capacity:

                    # make copy of battery_list and remove the full battery
                    new_battery_list = copy.copy(new_battery_list)
                    new_battery_list.remove(assigned_battery)

                    if len(new_battery_list) > 0:
                        # choose another battery
                        assigned_battery = random.choice(new_battery_list)
                    else:
                        valid_option = False
                        #print('no battery left')
                        
                        break

                # adjust the capacity of the battery
                assigned_battery.capacity -= house.maxoutput

                # save the dictionary of the house in the list of houses for that battery
                assigned_battery.dict['connected houses'].append(house.dict)

            # if validation == 'valid':
            #     valid_option = True
            #     print('valid_option = True')
