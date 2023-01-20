import math
def sort_houses(list_with_houses):
    """
    This function sorts the houses based on the maximum output
    """
    new_list_with_houses = sorted(list_with_houses, key=lambda x:x.maxoutput, reverse=True)
    return new_list_with_houses

class Greedy():
    def assign_closest_battery(self, list_with_houses, list_with_batteries):
        """
        This function assign a house to the closest battery that still has capacity
        """"

        # sort the houses based on the maximum capacity
        list_with_houses_sorted = sort_houses(list_with_houses)

        for house in list_with_houses_sorted:
            print('new house')
            print('output', house.maxoutput)

            # set distance to infinity
            closest_distance = math.inf

            for battery in list_with_batteries:
                print(battery.capacity)

                # calculate distance to each battery
                distance = abs((battery.x - house.x) + (battery.y - house.y))

                # assign the house closest battery that still has enough capacity
                if distance < closest_distance and house.maxoutput < battery.capacity:
                    closest_distance = distance
                    assigned_battery = battery

            # adjust the capacity of the battery
            assigned_battery.capacity -= house.maxoutput
            print(assigned_battery.x, assigned_battery.capacity)

            # save the dictionary of the house in the list of houses for that battery
            assigned_battery.dict['connected houses'].append(house.dict)
