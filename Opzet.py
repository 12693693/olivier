import argparse
import pandas as pd
import matplotlib.pyplot as plt

class Experiment():
    def __init__(self, batteries_df, houses_df):
        self.houses_and_batteries = []
        self.add_batteries(batteries_df)
        self.add_houses(houses_df)
        self.draw_plot()


    def add_batteries(self, batteries_df):
        for index, row in batteries_df.iterrows():
            battery = Batteries(row[0], row[1], row[2])
            self.houses_and_batteries.append(battery)

    def add_houses(self, houses_df):
        for index, row in houses_df.iterrows():
            house = Houses(row[0], row[1], row[2])
            self.houses_and_batteries.append(house)


    def draw_plot(self):
        pos_x_list = []
        pos_y_list = []
        color_list = []

        for thing in self.houses_and_batteries:
            pos_x_list.append(thing.x)
            pos_y_list.append(thing.y)
            color_list.append(thing.color)

        plt.scatter(pos_x_list, pos_y_list, color=color_list)
        plt.show()


class Batteries():
    def __init__(self, capacity, x, y):
        self.capacity = capacity
        self.x = x
        self.y = y
        self.output = 0
        self.color = 'blue'
    #
    # def plot_batteries(self):
    #     print(self.x, self.y)
    #     plt.plot(self.x, self.y, 'bo')


#
#     def add_house(self, x, y, maxoutput):
#         # check of de output niet teveel wordt voor de batterij bij het toevoegen van een huis
#         self.output += maxoutput
#         if self.output < self.capacity:
#           # lijntje trekken
#
#
class Houses():
    def __init__(self, x, y, maxoutput):
        self.x = x
        self.y = y
        self.maxoutput = maxoutput
        self.color = 'red'

    # def plot_houses(self):
    #     plt.plot(self.x, self.y, 'ro')

#     def compute_distance(self, position_battery):
#
#
#     def closest_battery(self, batteries):
#
#         for battery in batteries:
#           distance = compute_distance(self.position, battery)
#           # extra
#           if distance < smallest_distance:
#             smallest_distance = distance


def load_df(houses_csv, batteries_csv):
    df_houses1 = pd.read_csv(houses_csv)
    df_batteries1 = pd.read_csv(batteries_csv)

    # create and fill lists of seperate coordinates for the batteries
    x_list = []
    y_list = []

    for index, row in df_batteries1.iterrows():
        x = row[0].split(',')[0]
        y = row[0].split(',')[1]

        x_list.append(int(x))
        y_list.append(int(y))

    # modify the dataframe to add the lists and remove unnecessary columns
    df_batteries1['x'] = x_list
    df_batteries1['y'] = y_list
    df_batteries1 = df_batteries1.drop('positie', axis=1)


    return df_houses1, df_batteries1




if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "adding houses to batteries")

    # Adding arguments
    #parser.add_argument("output", help = "output file (csv)")
    parser.add_argument("input_houses", help="houses file")
    parser.add_argument("input_batteries", help="batteries_file")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    df_houses1, df_batteries1 = load_df(args.input_houses, args.input_batteries)

    my_experiment = Experiment(df_batteries1, df_houses1)

# houses_list1 = []
# for index, row in df_houses1.iterrows():
#     house = Houses(row[0], row[1], row[2])
#     houses_list1.append(house)
#     house.plot_houses()
#
#
# batteries_list1 = []
# for index, row in df_batteries1.iterrows():
#     battery = Batteries(row[0], row[1], row[2])
#     batteries_list1.append(battery)
#     battery.plot_batteries()

# plt.xlim(0, 55)
# plt.ylim(0, 55)
# plt.show()
#
# print('aantal huizen', len(houses_list1))
# print('aantal batterijen', len(batteries_list1))


cables_list = []
house_dict = {} # location, output and cables of each house
houses_list_per_batterie = [] # the houses that are connected to that battery
battery_dict = {} #location, capacity and houses that are connected
district_cost_dict = {} # what district and cost
main_list = [] #battery_dict and district_cost_dict
