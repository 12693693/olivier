import math
import random
import copy

def sort_houses(list_with_houses):
    """
    This function sorts the houses based on the maximum output
    """
    new_list_with_houses = sorted(list_with_houses, key=lambda x:x.maxoutput, reverse=True)
    return new_list_with_houses




class Greedy():
    def get_closest_battery(self, house, list_with_batteries):
        """
        This function gets the closest battery to a house and assigns that
        battery to that house.
        """

        # set distance to infinity
        closest_distance = math.inf

        # assign a random battery as closest
        assigned_battery = random.choice(list_with_batteries)

        for battery in list_with_batteries:

            # calculate distance to each battery
            distance = abs(battery.x - house.x) + abs(battery.y - house.y)

            # assign the house closest battery that still has enough capacity
            if distance < closest_distance and house.maxoutput < battery.capacity:
                closest_distance = distance
                assigned_battery = battery

        # adjust the capacity of the battery
        assigned_battery.capacity -= house.maxoutput

        # save the dictionary of the house in the list of houses for that battery
        assigned_battery.dict['houses'].append(house.dict)

        return assigned_battery

    def assign_closest_battery(self, list_with_houses, list_with_batteries):
        """
        This function assigns a house to the closest battery that still has capacity
        or uses the random greedy function if there is no battery with enough
        capacity left.
        """

        # sort the houses based on the maximum capacity
        list_with_houses_sorted = sort_houses(list_with_houses)

        # make a copy of the list with batteries to save the capacities (for
        # the random function)
        batteries_not_changed = copy.deepcopy(list_with_batteries)

        for house in list_with_houses_sorted:

            # get the closest battery
            assigned_battery = self.get_closest_battery(house, list_with_batteries)

            # if the assigned battery does not have enough capacity, use the random
            # greedy function
            if assigned_battery.capacity < 0:
                self.random_greedy(list_with_houses, batteries_not_changed)

    def random_greedy(self, list_with_houses, list_with_batteries):
        """
        This function shuffles the list with houses and assigns a house to the
        closest battery that still has capacity.
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

            # sort the houses random
            random.shuffle(list_with_houses)

            for house in list_with_houses:

                # get the closest battery
                assigned_battery = self.get_closest_battery(house, list_with_batteries)

                # if the assigned battery does not have enough capacity, set
                # valid option to False so it will run the loop again
                if assigned_battery.capacity < 0:
                    valid_option = False
