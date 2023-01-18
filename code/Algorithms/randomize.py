#from .Classes.smartgrid import Smartgrid
import random
import copy

class Randomize():
    def assign_house_random(self, list_with_houses, list_with_batteries):
        """
        This function assigns the houses to a randomly selected battery.
        """
        valid_option = False

        batteries_copy = copy.deepcopy(list_with_batteries)
        #
        while valid_option == False:


            for i in range(len(list_with_batteries)):
                list_with_batteries[i].capacity = batteries_copy[i].capacity
                #print(batteries_copy[i].capacity, list_with_batteries[i].capacity)

            valid_option = True
            print('run')
            # randomly assign a battery to each house
            for house in list_with_houses:
                print('house')


                assigned_battery = random.choice(list_with_batteries)

                # create copy of the battery list for later
                remaining_batteries = copy.copy(list_with_batteries)
                print(len(list_with_batteries))

                # if the house doesn't fit the battery anymore, choose another battery
                while house.maxoutput > assigned_battery.capacity:

                    # make copy of battery_list and remove the full battery
                    # remaining_batteries = copy.copy(remaining_batteries)
                    remaining_batteries.remove(assigned_battery)
                    print(len(remaining_batteries))

                    if len(remaining_batteries) > 0:
                        # choose another battery
                        assigned_battery = random.choice(remaining_batteries)
                        #print('batteries left')
                    else:
                        valid_option = False
                        print('no battery left')

                        break

                # adjust the capacity of the battery
                assigned_battery.capacity -= house.maxoutput

                # save the dictionary of the house in the list of houses for that battery
                assigned_battery.dict['connected houses'].append(house.dict)

            # if validation == 'valid':
            #     valid_option = True
            #     print('valid_option = True')
