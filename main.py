import argparse
import pandas as pd
import random
import copy
import seaborn as sns
import matplotlib.pyplot as plt
from code.Classes.smartgrid import Smartgrid
from code.Algorithms.randomize import Randomize
from code.Algorithms.cable_90_degree import Cables_90
#from code.Algorithms.search_cables import Search_Cables
from code.Algorithms.random_try import Cables
from code.Algorithms.greedy import Greedy
#from code.Algorithms.search_cables import Search_Cables
from code.Algorithms.hill_climber import Hill_Climber
#
# dit moet eigenlijk in classmethod
def load_df(houses_csv, batteries_csv):
    """
    This function loads the villages and saves them as dataframes
    """
    df_houses = pd.read_csv(houses_csv)
    df_batteries = pd.read_csv(batteries_csv)

    # create and fill lists of seperate coordinates for the batteries
    x_list = []
    y_list = []

    for index, row in df_batteries.iterrows():
        x = row[0].split(',')[0]
        y = row[0].split(',')[1]

        x_list.append(int(x))
        y_list.append(int(y))

    # modify the dataframe to add the lists and remove unnecessary columns
    df_batteries['x'] = x_list
    df_batteries['y'] = y_list
    df_batteries = df_batteries.drop('positie', axis=1)


    return df_houses, df_batteries

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
    df_houses, df_batteries = load_df(args.input_houses, args.input_batteries)
    my_smartgrid = Smartgrid(df_houses, df_batteries)

    #my_smartgrid = Smartgrid.from_file(args.input_houses, args.input_batteries)

    houses, batteries = my_smartgrid.add_houses_and_batteries(df_houses, df_batteries)
    #print(houses, batteries)

    # # ----------------- random houses and 90 degrees cables-----------------------
    random_algo = Randomize()
    greedy_algo = Greedy()
    cable_90_degree = Cables_90()
    cable_random = Cables()


    list_with_costs_random_90= []
    my_smartgrid.district_name()

    # batteries_filled = copy.deepcopy(batteries)
    # houses_filled = copy.deepcopy(houses)

    # -------------------- loop with random and 90 degrees ----------
    list_with_costs_random_90 = []

    for i in range(1000):

        batteries_filled = copy.deepcopy(batteries)
        houses_filled = copy.deepcopy(houses)

        random_algo.assign_house_random(houses_filled, batteries_filled)

        step_count = cable_90_degree.make_90_degrees_cables(houses_filled, batteries_filled)

        # my_smartgrid.draw_plot()
        my_smartgrid.costs(step_count)
        my_smartgrid.create_district_dict()
        list = my_smartgrid.make_output()
        list_with_costs.append(list[0]['costs shared'])
        print('costs', list[0]['costs shared'])
        print(f'{i}/1000')


    series_with_costs_random_90 = pd.Series(list_with_costs_random_90)
    print(series_with_costs_random_90)
    plt.clf()
    plt.title('houses random assigned with 90 degree cables')
    sns.histplot(data=series_with_costs_random_90)
    plt.show()


#----------------------------loop with greedy and 90 degrees -------------------
    list_with_costs_greedy_90 = []

    for i in range(500):

        batteries_filled = copy.deepcopy(batteries)
        houses_filled = copy.deepcopy(houses)

        greedy_algo.assign_closest_battery(houses_filled, batteries_filled)

        step_count = cable_90_degree.make_90_degrees_cables(houses_filled, batteries_filled)

        # my_smartgrid.draw_plot()
        my_smartgrid.costs(step_count)
        my_smartgrid.create_district_dict()
        list = my_smartgrid.make_output()
        list_with_costs_greedy_90.append(list[0]['costs shared'])
    # print(list)
        print('costs', list[0]['costs shared'])
        print(f'{i}/1000')


    series_with_costs_greedy_90 = pd.Series(list_with_costs_greedy_90)
    print(series_with_costs_greedy_90)
    plt.clf()
    plt.title('houses assigned with greedy and 90 degree cables')
    sns.barplot(data=series_with_costs_greedy_90)
    plt.show()

#------------------------- loop with hillclimber and 90 degrees ----------------

    list_with_costs_hillclimber_90 = []
    for i in range(500):

        my_smartgrid_filled = copy.deepcopy(my_smartgrid)

        my_smartgrid_filled.battery_list = copy.deepcopy(batteries)
        my_smartgrid_filled.house_list = copy.deepcopy(houses)

        random_algo.assign_house_random(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)

        step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)

        my_smartgrid_filled.costs(step_count)

        random_hill_climber = Hill_Climber(my_smartgrid_filled)
        random_hill_climber.run(500)
        # print('step_count', step_count)
        # my_smartgrid.draw_plot()

        my_smartgrid_filled.create_district_dict()
        list = my_smartgrid_filled.make_output()
        list_with_costs_hillclimber_90.append(list[0]['costs shared'])

    # print(list)
        print('costs', list[0]['costs shared'])
        print(f'{i}/1000')

    series_with_costs_hillclimber_90 = pd.Series(list_with_costs_hillclimber_90)
    print(series_with_costs_hillclimber_90)
    plt.clf()
    sns.histplot(data=series_with_costs_hillclimber_90)
    plt.show()


# -----------------------------------------------------------------------------

    # random_algo = Randomize()
    # random_algo.assign_house_random(houses, batteries)
    #
    # cable_90_degree = Cables()
    # step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
    #
    # my_smartgrid.draw_plot()
    # my_smartgrid.costs(step_count)
    # my_smartgrid.district_name()
    # my_smartgrid.create_district_dict()
    # list = my_smartgrid.make_output()
    # print(list)
    # print('costs', list[0]['costs shared'])

# ------------------------greedy & random-try ---------------------------------
    list_with_costs_greedy_random_try = []

    for i in range(500):
        batteries_filled = copy.deepcopy(batteries)
        houses_filled = copy.deepcopy(houses)

        greedy_algo.assign_closest_battery(houses_filled, batteries_filled)
        step_count = cable_random.random_try(houses_filled, batteries_filled)

    # my_smartgrid.draw_plot()
        my_smartgrid.costs(step_count)
        my_smartgrid.create_district_dict()
        list = my_smartgrid.make_output()
        list_with_costs_greedy_random_try.append(list[0]['costs shared'])

        print('costs', list[0]['costs shared'])
        print(f'{i}/500')

    series_with_costs_greedy_random_try = pd.Series(list_with_costs_greedy_random_try)
    print(series_with_costs_greedy_random_try)
    plt.clf()
    sns.histplot(data=series_with_costs_greedy_random_try)
    plt.show()

    # ------------------- greedy houses and cables 90 ------------
    #
    # greedy_algo.assign_closest_battery(houses, batteries)
    #
    # for i in range(500):
    #
    #     batteries_filled = copy.deepcopy(batteries)
    #     houses_filled = copy.deepcopy(houses)
    #
    #     step_count = cable_90_degree.make_90_degrees_cables(houses_filled, batteries_filled)
    #
    #     # my_smartgrid.draw_plot()
    #     my_smartgrid.costs(step_count)
    #     # my_smartgrid.district_name()
    #     my_smartgrid.create_district_dict()
    #     list = my_smartgrid.make_output()
    #     list_with_costs.append(list[0]['costs shared'])
    #
    #     print('costs', list[0]['costs shared'])
    #     print(f'{i}/1000')
    #
    #
    # series_with_costs = pd.Series(list_with_costs)
    # print(series_with_costs.describe())
    # plt.clf()
    # sns.histplot(data=series_with_costs)
    # plt.show()
        #print(list)
        # print('costs', list[0]['costs shared'])
        # self.assign_house_random() # CHECK
        # self.make_cables()


#------------------------- search cables --------------------------

#     random_algo = Randomize()
#     random_algo.assign_house_random(houses, batteries)
#
#     cable_search = Search_Cables()
#     step_count, cable_list, existing_cable_dict= cable_search.search_cables(houses, batteries)
#
#     my_smartgrid.draw_plot()
#     my_smartgrid.costs(step_count)
#     my_smartgrid.district_name()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     #print(list)
# # print('costs', list[0]['costs shared'])
#     print(existing_cable_dict)



    #self.assign_house_random() # CHECK
    #self.make_cables()


    #---------------- hill climber ---------------------------------------------
#     random_algo = Randomize()
#     random_algo.assign_house_random(houses, batteries)
#
#     cable_90_degree = Cables()
#     step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
#
#     my_smartgrid.draw_plot()
#     my_smartgrid.costs(step_count)
#     my_smartgrid.district_name()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     #print(list)
# # print('costs', list[0]['costs shared'])
#     #print(existing_cable_dict)
#     #print(cable_list)
#
#
#     #self.assign_house_random() # CHECK
#     #self.make_cables()
#
#
#     random_hill_climber = Hill_Climber(my_smartgrid)
#     random_hill_climber.run(2000)
