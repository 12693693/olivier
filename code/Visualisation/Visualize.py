from .Classes.smartgrid import Smartgrid
my_smartgrid = Smartgrid()
class Visualize():
    def plot_grid(self, list_with_batteries):
        # create lists in which to store the information for the plot
        pos_x_list = []
        pos_y_list = []
        color_list = []
        shape_list = []

        # find x and y coordinates and the color of the thing to be plotted
        for thing in my_smartgrid.houses_and_batteries:
            pos_x_list.append(thing.x)
            pos_y_list.append(thing.y)
            color_list.append(thing.color)

        # plot all houses and batteries
        plt.scatter(pos_x_list, pos_y_list, color=color_list, marker='s', s=40)
        plt.show()

        for battery in list_with_batteries:
            for house_dict in battery.dict['connected houses']:
                for cable in house_dict['grid']:
                    for step in cable:
                        x_loc = float(step.split(', ')[0])
                        y_loc = float(step.split(', ')[1])

                        x_list.append(x_loc)
                        y_list.append(y_loc)

                        # plt.gcf()
                        plt.pause(0.001)
                        plt.plot(x_list, y_list, 'k--')
                        plt.draw()
