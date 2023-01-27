# def draw_plot():
#     """
#     This function draws a plot of the houses and batteries in the village.
#     """
#     # create lists in which to store the information for the plot
#     pos_x_list = []
#     pos_y_list = []
#     color_list = []
#     shape_list = []
#
#     # find x and y coordinates and the color of the thing to be plotted
#     for thing in self.houses_and_batteries:
#         pos_x_list.append(thing.x)
#         pos_y_list.append(thing.y)
#         color_list.append(thing.color)
#
#     # plot all houses and batteries
#     plt.scatter(pos_x_list, pos_y_list, color=color_list, marker='s', s=40)
#     plt.show()
#     plt.clf()

def visualise():
    cur_path = os.path.dirname(__file__)

    with open(cur_path + '/../../resultaten/output.json', 'r') as file:
        data = json.load(file)
