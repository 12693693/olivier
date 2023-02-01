import os
import json
import matplotlib.pyplot as plt

def visualise(algo_connections, algo_cables):
    """
    This function makes the plot of the smartgrid with all the cables.
    """

    cur_path = os.path.dirname(__file__)

    with open(cur_path + '/../../resultaten/output.json', 'r') as file:
        data_list = json.load(file)

    # Make the plot clear
    plt.clf()

    # Make empty list for position and color for the houses and batteries
    position_x_list = []
    position_y_list = []
    color_list = []

    # Make a list with colors for each battery
    grid_color_list = ['m', 'c', 'g', 'tab:orange', 'tab:brown']

    # Make an index to decide which color to use
    color_i = 0

    # Add the location and color of the batteries to the list of positions
    for battery in data_list[1:]:
        position_x_list.append(int(float(battery['location'].split(',')[0])))
        position_y_list.append(int(float(battery['location'].split(',')[1])))
        color_list.append('blue')

        # Define the color for cables of the houses that are assigned to that battery
        color = grid_color_list[color_i]

        # Add the location and color of the houses to the list of positions
        for house in battery['houses']:
            position_x_list.append(int(float(house['location'].split(',')[0])))
            position_y_list.append(int(float(house['location'].split(',')[1])))
            color_list.append('red')

            # Make empty list for coordinates of the cables
            cables_x_list = []
            cables_y_list = []

            # Add the location and color of the cables to the cables lists
            for cable in house['cables']:
                cables_x_list.append(int(cable.split(',')[0]))
                cables_y_list.append(int(cable.split(',')[1]))

            #Plot the cables
            plt.plot(cables_x_list, cables_y_list, linestyle='dashed', color=color)

        # Choose the next color for the next battery
        color_i += 1

    # Plot the houses and batteries, give the plot a title and remove axes
    # (axes numbers are not relevant for the visualisation)
    plt.scatter(position_x_list, position_y_list, color=color_list, marker='s', s=60)
    plt.title(f'Connections made with {algo_connections} algorithm, cables made with {algo_cables} algorithm')
    plt.tick_params(left = False, right = False , labelleft = False ,
                labelbottom = False, bottom = False)
    plt.show()
