import os
import json
import matplotlib.pyplot as plt

# def draw_plot():
    # """
    # # This function draws a plot of the houses and batteries in the village.
    # # """
    # # create lists in which to store the information for the plot
    # pos_x_list = []
    # pos_y_list = []
    # color_list = []
    # shape_list = []
    #
    # # find x and y coordinates and the color of the thing to be plotted
    # for thing in self.houses_and_batteries:
    #     pos_x_list.append(thing.x)
    #     pos_y_list.append(thing.y)
    #     color_list.append(thing.color)
    #
    # # plot all houses and batteries
    # plt.scatter(pos_x_list, pos_y_list, color=color_list, marker='s', s=40)
    # plt.show()
    # plt.clf()

def visualise():
    cur_path = os.path.dirname(__file__)

    with open(cur_path + '/../../resultaten/output.json', 'r') as file:
        data_list = json.load(file)
        print(data_list)

    position_x_list = []
    position_y_list = []
    color_list = []
    grid_color_list = ['m', 'c', 'g', 'tab:orange', 'tab:brown']

    i = 0

    for battery in data_list[1:]:
        position_x_list.append(int(battery['location'].split(',')[0]))
        position_y_list.append(int(battery['location'].split(',')[1]))
        color_list.append('blue')

        color = grid_color_list[i]
        i += 1

        for house in battery['houses']:
            position_x_list.append(int(house['location'].split(',')[0]))
            position_y_list.append(int(house['location'].split(',')[1]))
            color_list.append('red')

            cables_x_list = []
            cables_y_list = []
            for cable in house['grid']:
                cables_x_list.append(int(cable.split(',')[0]))
                cables_y_list.append(int(cable.split(',')[1]))
            plt.plot(cables_x_list, cables_y_list, marker='--', color=color)

    plt.clf()
    plt.scatter(position_x_list, position_y_list, color=color_list, marker='s', s=40)
    plt.show()
    plt.clf()
