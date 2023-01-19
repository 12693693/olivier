def get_location():
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
            y_loc = location_house_y

            x_list = [x_loc]
            y_list = [y_loc]
