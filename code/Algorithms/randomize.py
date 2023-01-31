#from .Classes.smartgrid import Smartgrid
import random
import copy

class Randomize():
    def assign_house_random(self, list_with_houses, list_with_batteries):
        """
        This function assigns the houses to a randomly selected battery.
        """

        # set valid_option to False so it will enter the while loop
        valid_option = False

        # make a copy of the list with batteries to save the capacities
        batteries_copy = copy.deepcopy(list_with_batteries)

        # assign all of the houses to a battery
        # do this untill every house is assigned to a battery that has enough capacity
        while valid_option == False:

            # reset the capacities and empty the houses
            for i in range(len(list_with_batteries)):
                list_with_batteries[i].capacity = batteries_copy[i].capacity
                list_with_batteries[i].dict['houses'] = []

            # set valid_option to true so if all houses are assigned to a battery
            # that has enough capacity it will leave the while loop
            valid_option = True

            # randomly assign a battery to each house
            for house in list_with_houses:

                # Choose a battery of the list_with_batteries
                assigned_battery = random.choice(list_with_batteries)

                # Create copy of the battery list for later
                remaining_batteries = copy.copy(list_with_batteries)

                # If the house doesn't fit the battery anymore, choose another battery
                while house.maxoutput > assigned_battery.capacity:

                    # Remove the full battery of the remaining_batteries
                    remaining_batteries.remove(assigned_battery)

                    if len(remaining_batteries) > 0:
                        # Choose another battery if there are any still availeble
                        assigned_battery = random.choice(remaining_batteries)
                    else:
                        # go further with the previous assigned battery that is
                        # already full, but set the valid option to false so it
                        # will run through the while loop again
                        valid_option = False
                        break

                # adjust the capacity of the battery
                assigned_battery.capacity -= house.maxoutput

                # save the dictionary of the house in the list of houses for that battery
                assigned_battery.dict['houses'].append(house.dict)
