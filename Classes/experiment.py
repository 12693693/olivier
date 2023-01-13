import argparse
import pandas as pd
import matplotlib.pyplot as plt
import random

class Experiment():
    def __init__(self, batteries_df, houses_df):
        self.houses_and_batteries = []
        self.add_batteries(batteries_df)
        self.add_houses(houses_df)
        #self.draw_plot()
        self.houses_list_per_batterie = []
        self.battery_dict = {}
        self.assign_house()


    def add_batteries(self, batteries_df):
        self.battery_list = []
        self.battery_dict = {}

        for index, row in batteries_df.iterrows():
            battery = Batteries(row[0], row[1], row[2])
            self.houses_and_batteries.append(battery)
            self.battery_list.append(battery)



        # maak key van battery in die dict

    def add_houses(self, houses_df):
        self.house_list = []

        for index, row in houses_df.iterrows():
            house = Houses(row[0], row[1], row[2])
            self.houses_and_batteries.append(house)
            self.house_list.append(house)

            # maak dictionary per house aan


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

    def assign_house(self):

        # randomly assign a battery for each house
        for house in self.house_list:
            assigned_battery = random.choice(self.battery_list)
            #print(assigned_battery.x, assigned_battery.y)
            assigned_battery.capacity -= house.maxoutput

            if house.maxoutput > assigned_battery.capacity:

                # make copy of battery_list and remove the full battery
                new_battery_list = battery_list.remove(assigned_battery)


                # choose another battery
                assigned_battery = random.choice(new_battery_list)
