import argparse
import pandas as pd

class Batteries():
    def __init__(self, capacity, x, y):
        self.capacity = capacity
        self.x = x
        self.y = y
        self.output = 0
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
    df_houses1 = pd.read_csv('Huizen&Batterijen/district_1/district-1_houses.csv')
    df_batteries1 = pd.read_csv('Huizen&Batterijen/district_1/district-1_batteries.csv')

    # create and fill lists of seperate coordinates for the batteries
    x_list = []
    y_list = []

    for index, row in df_batteries1.iterrows():
        x = row[0].split(',')[0]
        y = row[0].split(',')[1]

        x_list.append(x)
        y_list.append(y)

    # modify the dataframe to add the lists and remove unnecessary columns
    df_batteries1['x'] = x_list
    df_batteries1['y'] = y_list
    df_batteries1 = df_batteries1.drop('positie', axis=1)

    print(df_batteries1)

# houses_list1 = []
# for index, row in df_houses1.iterrows():
#     house = Houses(row[0], row[1], row[2])
#     houses_list1.append(house)
#
# batteries_list1 = []
# for index, row in df_batteries1.iterrows():
#     battery = Batteries(row[0], row[1], row[2])
#     batteries_list1.append(battery)
#
# print('aantal huizen', len(houses_list1))
# print('aantal batterijen', len(batteries_list1))





        # blablabla
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
    load_df(args.input_houses, args.input_batteries)

cables_list = []
house_dict = {} # location, output and cables of each house
houses_list_per_batterie = [] # the houses that are connected to that battery
battery_dict = {} #location, capacity and houses that are connected
district_cost_dict = {} # what district and cost
main_list = [] #battery_dict and district_cost_dict
