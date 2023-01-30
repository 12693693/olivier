# from .Classes.smartgrid import Smartgrid
# my_smartgrid = Smartgrid()
# class Visualize():
#     def plot_grid(self, list_with_batteries):
#         # create lists in which to store the information for the plot
#         pos_x_list = []
#         pos_y_list = []
#         color_list = []
#         shape_list = []
#
#         # find x and y coordinates and the color of the thing to be plotted
#         for thing in my_smartgrid.houses_and_batteries:
#             pos_x_list.append(thing.x)
#             pos_y_list.append(thing.y)
#             color_list.append(thing.color)
#
#         # plot all houses and batteries
#         plt.scatter(pos_x_list, pos_y_list, color=color_list, marker='s', s=40)
#         plt.show()
#
#         for battery in list_with_batteries:
#             for house_dict in battery.dict['connected houses']:
#                 for cable in house_dict['grid']:
#                     for step in cable:
#                         x_loc = float(step.split(', ')[0])
#                         y_loc = float(step.split(', ')[1])
#
#                         x_list.append(x_loc)
#                         y_list.append(y_loc)
#
#                         # plt.gcf()
#                         plt.pause(0.001)
#                         plt.plot(x_list, y_list, 'k--')
#                         plt.draw()
import os
import json
import matplotlib.pyplot as plt

def visualise():
    cur_path = os.path.dirname(__file__)

    with open(cur_path + '/../../resultaten/output.json', 'r') as file:
        data_list = json.load(file)
        #print(data_list)

    position_x_list = []
    position_y_list = []
    color_list = []
    grid_color_list = ['m', 'c', 'g', 'tab:orange', 'tab:brown']

    i = 0
    plt.clf()

    for battery in data_list[1:]:
        position_x_list.append(int(float(battery['location'].split(',')[0])))
        position_y_list.append(int(float(battery['location'].split(',')[1])))
        color_list.append('blue')

        color = grid_color_list[i]
        i += 1

        for house in battery['houses']:
            position_x_list.append(int(float(house['location'].split(',')[0])))
            position_y_list.append(int(float(house['location'].split(',')[1])))
            color_list.append('red')

            cables_x_list = []
            cables_y_list = []
            for cable in house['cables']:
                cables_x_list.append(int(cable.split(',')[0]))
                cables_y_list.append(int(cable.split(',')[1]))
            plt.plot(cables_x_list, cables_y_list, linestyle='dashed', color=color)


    plt.scatter(position_x_list, position_y_list, color=color_list, marker='s', s=60)
    plt.show()
    plt.clf()
