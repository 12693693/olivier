import os
import json
import matplotlib.pyplot as plt

def visualise(algo_connections, algo_cables):

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
    plt.title(f'Connections made with {algo_connections} algorithm, cables made with {algo_cables} algorithm')
    plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
    plt.show()
    plt.clf()
