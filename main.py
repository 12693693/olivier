import argparse
import pandas as pd
import random
import copy
import seaborn as sns
import matplotlib.pyplot as plt
from code.Classes.smartgrid import Smartgrid
from code.Algorithms.randomize import Randomize
from code.Algorithms.cable_90_degree import Cables_90
from code.Algorithms.random_try import Cables
from code.Algorithms.greedy import Greedy
from code.Algorithms.search_cables import Search_Cables
from code.Algorithms.hill_climber import Hill_Climber
from code.Algorithms.simulated_annealing import Simulated_Annealing
from code.Algorithms.breadth_first import Breadth_first
from code.Algorithms.further_cables import Further_Cables
#from code.Algorithms.breadth_first import Breadth_first

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
    # create class objects to work with
    random_algo = Randomize()
    greedy_algo = Greedy()
    cable_90_degree = Cables_90()
    cable_random = Cables()

    #cable_breadth = Breadth_first()

    search_cables = Search_Cables()
    cable_breadth = Breadth_first()
    further_cables = Further_Cables()


    # prompt the user to give the district number
    my_smartgrid.district_name()

    # batteries_filled = copy.deepcopy(batteries)
    # houses_filled = copy.deepcopy(houses)

# ----------------------loop with greedy and breadth
    # list_with_costs_greedy_breadth = []
    #
    # for i in range(100):


    # -------------------- loop with random and 90 degrees ----------
    # create list in which to store the costs of this algorithm combination
    # list_with_costs_random_90 = []
    #
    # for i in range(100):
    #

    #     # create battery and houses list of the smartgrid, by making deepcopies
    #     my_smartgrid.battery_list = copy.deepcopy(batteries)
    #     my_smartgrid.houses_list = copy.deepcopy(houses)
    #

    #     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     cable_breadth.breadth(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     my_smartgrid.costs_shared()
    #     my_smartgrid.create_district_dict()
    #     list = my_smartgrid.make_output()
    #     list_with_costs_greedy_breadth.append(list[0]['costs shared'])
    # my_smartgrid.draw_plot()
    #
    # series_with_costs_greedy_breadth = pd.Series(list_with_costs_random_90)
    # print(series_with_costs_greedy_breadth)
    #
    # # plot the distribution of costs for this algorithm
    # plt.clf()
    # plt.title('houses greedy assigned with breadth first cables')
    # sns.histplot(data=series_with_costs_greedy_breadth)
    # plt.show()

    #     # assign the houses with the random algorithm
    #     random_algo.assign_house_random(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # lay the cables with the 90 degrees algorithm
    #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # calculate the costs of the grid
    #     my_smartgrid.costs_shared()
    #
    #     # make sure the output is made
    #     my_smartgrid.create_district_dict()
    #     list = my_smartgrid.make_output()
    #
    #     # append the cost to the list of costs for this combination of algorithms
    #     list_with_costs_random_90.append(list[0]['costs shared'])
    #     print('costs', list[0]['costs shared'])
    #     print(f'{i}/1000')
    #
    # # draw a smartgrid of this combination of algorithms to demonstrate
    # my_smartgrid.draw_plot()
    #
    #
    # # create series of the costs of the algorithm to plot
    # series_with_costs_random_90 = pd.Series(list_with_costs_random_90)
    # print(series_with_costs_random_90)
    #
    # # plot the distribution of costs for this algorithm
    # plt.clf()
    # plt.title('houses random assigned with 90 degree cables')
    # sns.histplot(data=series_with_costs_random_90)
    # plt.show()


#----------------------------loop with greedy and 90 degrees -------------------
# kan voor beide dus!
    # create list in which to keep track of the costs for this combination of algorithms
    # list_with_costs_greedy_90 = []
    #
    # for i in range(100):
    #
    #     # create battery and houses list of the smartgrid, by making deepcopies
    #     my_smartgrid.battery_list = copy.deepcopy(batteries)
    #     my_smartgrid.houses_list = copy.deepcopy(houses)
    #
    #     # assign the houses with the greedy algorithm
    #     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # lay the cables with the 90 degrees algorithm
    #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
    #
    #     # calculate the costs
    #     my_smartgrid.costs_shared()
    #
    #     # create output
    #     my_smartgrid.create_district_dict()
    #     list = my_smartgrid.make_output()
    #
    #     # append costs to the list of costs for this combination of algorithms
    #     list_with_costs_greedy_90.append(list[0]['costs shared'])
    #
    #     print('costs', list[0]['costs shared'])
    #     print(f'{i}/1000')
    #
    # # create plot of smartgrid for demonstration
    # my_smartgrid.draw_plot()
    #
    # # make series to plot later
    # series_with_costs_greedy_90 = pd.Series(list_with_costs_greedy_90)
    # print(series_with_costs_greedy_90)
    #
    # # plot the distribution of costs
#     plt.clf()
#     plt.title('houses assigned with greedy and 90 degree cables')
#     sns.histplot(data=series_with_costs_greedy_90)
#     plt.show()
#
# #------------------------- loop with hillclimber and 90 degrees ----------------

    # # create list in which to store the costs of this combination of algorithms
    # list_with_costs_hillclimber_90 = []
    # for i in range(100):
    #
    #     # create deepcopy to ensure that filling the grid lists is correct
    #     my_smartgrid_filled = copy.deepcopy(my_smartgrid)
    #
    #     # create battery and houses list by making deepcopies
    #     my_smartgrid_filled.battery_list = copy.deepcopy(batteries)
    #     my_smartgrid_filled.house_list = copy.deepcopy(houses)
    #
    #     # connect the houses using the random algorithm
    #     random_algo.assign_house_random(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
    #
    #     # lay the cables using the 90 degree algorithm
    #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
    #
    #     # calculate the costs
    #     my_smartgrid_filled.costs_shared()
    #
    #     # initiate hill climber
    #     random_hill_climber = Hill_Climber(my_smartgrid_filled)
    #     random_hill_climber.run(500)
    #
    #     # create output
    #     my_smartgrid_filled.create_district_dict()
    #     list = my_smartgrid_filled.make_output()
    #
    #     # append cost to the list with costs for this algorithm combination
    #     list_with_costs_hillclimber_90.append(list[0]['costs shared'])
    #
    #     print('costs', list[0]['costs shared'])
    #     print(f'{i}/1000')
    #
    # # plot the smartgrid for demonstration
    # my_smartgrid.draw_plot()
    #
    # # create series to plot later
    # series_with_costs_hillclimber_90 = pd.Series(list_with_costs_hillclimber_90)
    # print(series_with_costs_hillclimber_90)
    #
    # # plot the distribution of costs for this algorithm combination
    # plt.clf()
    # plt.title('houses assigned with hillclimber and cables 90 degrees')
    # sns.histplot(data=series_with_costs_hillclimber_90)
    # plt.show()


# -----------------------------------------------------------------------------
# list_with_costs_greedy_breadth = []
#
# for i in range(100):
#     # create battery and houses list of the smartgrid, by making deepcopies
#     my_smartgrid.battery_list = copy.deepcopy(batteries)
#     my_smartgrid.houses_list = copy.deepcopy(houses)
#
#     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     cable_breadth.breadth(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     my_smartgrid.costs_shared()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     list_with_costs_greedy_breadth.append(list[0]['costs shared'])
# my_smartgrid.draw_plot()
#
# series_with_costs_greedy_breadth = pd.Series(list_with_costs_random_90)
# print(series_with_costs_greedy_breadth)
#
# # plot the distribution of costs for this algorithm
# plt.clf()
# plt.title('houses greedy assigned with breadth first cables')
# sns.histplot(data=series_with_costs_greedy_breadth)
# plt.show()
#
# list_with_costs_greedy_breadth = []
#
#
# for i in range(100):
#     # create battery and houses list of the smartgrid, by making deepcopies
#     my_smartgrid.battery_list = copy.deepcopy(batteries)
#     my_smartgrid.houses_list = copy.deepcopy(houses)
#
#     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     cable_breadth.breadth(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     my_smartgrid.costs_shared()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     list_with_costs_greedy_breadth.append(list[0]['costs shared'])
# my_smartgrid.draw_plot()
#
# series_with_costs_greedy_breadth = pd.Series(list_with_costs_random_90)
# print(series_with_costs_greedy_breadth)
#
# # plot the distribution of costs for this algorithm
# plt.clf()
# plt.title('houses greedy assigned with breadth first cables')
# sns.histplot(data=series_with_costs_greedy_breadth)
# plt.show()
# >>>>>>> 194b396a835e32ec32e5925805c01e3b3a8b6e5d
#     # -------------------- loop with random and 90 degrees ----------
# #     # create list in which to store the costs of this algorithm combination
#     list_with_costs_random_90 = []
#
#     for i in range(100):
#
#         # create battery and houses list of the smartgrid, by making deepcopies
#         my_smartgrid.battery_list = copy.deepcopy(batteries)
#         my_smartgrid.houses_list = copy.deepcopy(houses)
#
#         # assign the houses with the random algorithm
#         random_algo.assign_house_random(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # lay the cables with the 90 degrees algorithm
#         step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # calculate the costs of the grid
#         my_smartgrid.costs_shared()
#
#         # make sure the output is made
#         my_smartgrid.create_district_dict()
#         list = my_smartgrid.make_output()
#
#         # append the cost to the list of costs for this combination of algorithms
#         list_with_costs_random_90.append(list[0]['costs shared'])
#         print('costs', list[0]['costs shared'])
#         print(f'{i}/1000')
#
#     # draw a smartgrid of this combination of algorithms to demonstrate
#     my_smartgrid.draw_plot()
#
#
#     # create series of the costs of the algorithm to plot
#     series_with_costs_random_90 = pd.Series(list_with_costs_random_90)
#     print(series_with_costs_random_90)
#
#     # plot the distribution of costs for this algorithm
#     plt.clf()
#     plt.title('houses random assigned with 90 degree cables')
#     sns.histplot(data=series_with_costs_random_90)
#     plt.show()
#
#
# #----------------------------loop with greedy and 90 degrees -------------------
# # kan voor beide dus!
#     # create list in which to keep track of the costs for this combination of algorithms
#     list_with_costs_greedy_90 = []
#
#     for i in range(100):
#
#         # create battery and houses list of the smartgrid, by making deepcopies
#         my_smartgrid.battery_list = copy.deepcopy(batteries)
#         my_smartgrid.houses_list = copy.deepcopy(houses)
#
#         # assign the houses with the greedy algorithm
#         greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # lay the cables with the 90 degrees algorithm
#         step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # calculate the costs
#         my_smartgrid.costs_shared()
#
#         # create output
#         my_smartgrid.create_district_dict()
#         list = my_smartgrid.make_output()
#
#         # append costs to the list of costs for this combination of algorithms
#         list_with_costs_greedy_90.append(list[0]['costs shared'])
#
#         print('costs', list[0]['costs shared'])
#         print(f'{i}/1000')
#
#     # create plot of smartgrid for demonstration
#     my_smartgrid.draw_plot()
#
#     # make series to plot later
#     series_with_costs_greedy_90 = pd.Series(list_with_costs_greedy_90)
#     print(series_with_costs_greedy_90)
#
#     # plot the distribution of costs
#     plt.clf()
#     plt.title('houses assigned with greedy and 90 degree cables')
#     sns.histplot(data=series_with_costs_greedy_90)
#     plt.show()
#
# #------------------------- loop with hillclimber and 90 degrees ----------------
#
#     # # create list in which to store the costs of this combination of algorithms
#     # list_with_costs_hillclimber_90 = []
#     # for i in range(100):
#     #
#     #     # create deepcopy to ensure that filling the grid lists is correct
#     #     my_smartgrid_filled = copy.deepcopy(my_smartgrid)
#     #
#     #     # create battery and houses list by making deepcopies
#     #     my_smartgrid_filled.battery_list = copy.deepcopy(batteries)
#     #     my_smartgrid_filled.house_list = copy.deepcopy(houses)
#     #
#     #     # connect the houses using the random algorithm
#     #     random_algo.assign_house_random(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
#     #
#     #     # lay the cables using the 90 degree algorithm
#     #     step_count = cable_90_degree.make_90_degrees_cables(my_smartgrid_filled.house_list, my_smartgrid_filled.battery_list)
#     #
#     #     # calculate the costs
#     #     my_smartgrid_filled.costs_shared()
#     #
#     #     # initiate hill climber
#     #     random_hill_climber = Hill_Climber(my_smartgrid_filled)
#     #     random_hill_climber.run(500)
#     #
#     #     # create output
#     #     my_smartgrid_filled.create_district_dict()
#     #     list = my_smartgrid_filled.make_output()
#     #
#     #     # append cost to the list with costs for this algorithm combination
#     #     list_with_costs_hillclimber_90.append(list[0]['costs shared'])
#     #
#     #     print('costs', list[0]['costs shared'])
#     #     print(f'{i}/1000')
#     #
#     # # plot the smartgrid for demonstration
#     # my_smartgrid.draw_plot()
#     #
#     # # create series to plot later
#     # series_with_costs_hillclimber_90 = pd.Series(list_with_costs_hillclimber_90)
#     # print(series_with_costs_hillclimber_90)
#     #
#     # # plot the distribution of costs for this algorithm combination
#     # plt.clf()
#     # plt.title('houses assigned with hillclimber and cables 90 degrees')
#     # sns.histplot(data=series_with_costs_hillclimber_90)
#     # plt.show()
#
# # -----------------------------------------------------------------------------

    # random_algo = Randomize()
    # random_algo.assign_house_random(houses, batteries)
    #
    # cable_90_degree = Cables_90()
    # step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
    #
    # #my_smartgrid.draw_plot()
    # my_smartgrid.costs_shared()
    # #my_smartgrid.district_name()
    # my_smartgrid.make_f_string()
    # my_smartgrid.create_district_dict()
    # list = my_smartgrid.make_output()
    # #print(list)
    # #print('costs', list[0]['costs shared'])

# # ------------------------greedy & random-try ---------------------------------
#     # create list in which to store the costs for this combination of algorithms
#     list_with_costs_greedy_random_try = []
#
#     for i in range(100):
#
#         # create battery and houses list by making a deepcopy
#         my_smartgrid.battery_list = copy.deepcopy(batteries)
#         my_smartgrid.houses_list = copy.deepcopy(houses)
#
#         # connect houses to batteries using the greedy algorithm
#         greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # lay cables using the random try algorithm
#         count = cable_random.random_try(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#         # calculate costs
#         my_smartgrid.costs_shared()
#
#         # create output
#         my_smartgrid.create_district_dict()
#         list = my_smartgrid.make_output()
#
#         # append cost to list with costs for this algorithm combination
#         list_with_costs_greedy_random_try.append(list[0]['costs shared'])
#
#         print('costs', list[0]['costs shared'])
#         print(f'{i}/500')
#
#     # draw smartgrid for demonstration
#     my_smartgrid.draw_plot()
#
#     # create series to plot later
#     series_with_costs_greedy_random_try = pd.Series(list_with_costs_greedy_random_try)
#     print(series_with_costs_greedy_random_try)
#
#     # plot the distribution of costs for this algorithm combination
#     plt.clf()
#     plt.title('houses assigned with greedy, cables with random-try')
#     sns.histplot(data=series_with_costs_greedy_random_try)
#     plt.show()
#
# #------------------------print lists of costs ------------------------
# print(series_with_costs_greedy_90.describe())
# print(series_with_costs_random_90.describe())
# # print(series_with_costs_hillclimber_90.describe())
# print(series_with_costs_greedy_random_try.describe())
#
# mean_greedy_90 = series_with_costs_greedy_90.mean()
# mean_random_90 = series_with_costs_random_90.mean()
# mean_greedy_random_try = series_with_costs_greedy_random_try.mean()
#
# dict_means = {'algorithm':['greedy, 90 degrees', 'random, 90 degrees', 'greedy, random try'], 'means':[mean_greedy_90, mean_random_90, mean_greedy_random_try]}
# df_means = pd.DataFrame(dict_means)
# plt.clf()
# df_means.plot.bar(x='algorithm', y='means')
# plt.show()
#------------------------- search cables --------------------------
#
# list_with_costs_greedy_random_try = []
#
# for i in range(100):
#
#     # create battery and houses list by making a deepcopy
#     my_smartgrid.battery_list = copy.deepcopy(batteries)
#     my_smartgrid.houses_list = copy.deepcopy(houses)
#
#     # connect houses to batteries using the greedy algorithm
#     greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     # lay cables using the random try algorithm
#     count = cable_random.search_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)
#
#     # calculate costs
#     my_smartgrid.costs_shared()
#
#     # create output
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#
#     # append cost to list with costs for this algorithm combination
#     list_with_costs_greedy_random_try.append(list[0]['costs shared'])
#
#     print('costs', list[0]['costs shared'])
#     print(f'{i}/500')
#
# # draw smartgrid for demonstration
# my_smartgrid.draw_plot()
#
# # create series to plot later
# series_with_costs_greedy_random_try = pd.Series(list_with_costs_greedy_random_try)
# print(series_with_costs_greedy_random_try)

# plot the distribution of costs for this algorithm combination
# plt.clf()
# plt.title('houses assigned with greedy, cables with random-try')
# sns.histplot(data=series_with_costs_greedy_random_try)
# plt.show()

# #------------------------print lists of costs ------------------------
# print(series_with_costs_greedy_90.describe())
# print(series_with_costs_random_90.describe())
# # print(series_with_costs_hillclimber_90.describe())
# print(series_with_costs_greedy_random_try.describe())
#
# mean_greedy_90 = series_with_costs_greedy_90.mean()
# mean_random_90 = series_with_costs_random_90.mean()
# mean_greedy_random_try = series_with_costs_greedy_random_try.mean()
#
# dict_means = {'algorithm':['greedy, 90 degrees', 'random, 90 degrees', 'greedy, random try'], 'means':[mean_greedy_90, mean_random_90, mean_greedy_random_try]}
# df_means = pd.DataFrame(dict_means)
# plt.clf()
# df_means.plot.bar(x='algorithm', y='means')
# plt.show()

    #---------------- Search cables ---------------------------------------------

#
#     random_algo = Randomize()
#     random_algo.assign_house_random(my_smartgrid.house_list, my_smartgrid.battery_list)
#
#     cable_search = Search_Cables()
#     step_count, cable_list, existing_cable_dict = cable_search.search_cables(my_smartgrid.house_list, my_smartgrid.battery_list)
#
#     my_smartgrid.draw_plot()
#     my_smartgrid.costs(step_count)
#     # my_smartgrid.district_name()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     #print(list)
# # print('costs', list[0]['costs shared'])
#     print(cable_list)
#
# #     self.assign_house_random() # CHECK
# self.make_cables()

    #---------------- further cables ---------------------------------------------

        # random_algo = Randomize()
        # random_algo.assign_house_random(my_smartgrid.house_list, my_smartgrid.battery_list)
        #
        # further_cable_search = Further_Cables()
        # step_count, cable_list, existing_cable_dict = further_cable_search.further_cables(my_smartgrid.house_list, my_smartgrid.battery_list)
        #
        # my_smartgrid.draw_plot()
        # my_smartgrid.costs_shared()
        # # my_smartgrid.district_name()
        # my_smartgrid.create_district_dict()
        # list = my_smartgrid.make_output()
        # #print(list)
        # print('costs', list[0]['costs shared'])
        # print(cable_list)
#____________________________________________________________________

# kan voor beide dus!
    # create list in which to keep track of the costs for this combination of algorithms
    list_with_costs_further = []

    for i in range(200):

        # create battery and houses list of the smartgrid, by making deepcopies
        my_smartgrid.battery_list = copy.deepcopy(batteries)
        my_smartgrid.houses_list = copy.deepcopy(houses)

        # assign the houses with the greedy algorithm
        greedy_algo.assign_closest_battery(my_smartgrid.houses_list, my_smartgrid.battery_list)

        # lay the cables with the 90 degrees algorithm
        step_count = further_cables.further_cables(my_smartgrid.houses_list, my_smartgrid.battery_list)

        # calculate the costs
        my_smartgrid.costs_shared()

        # create output
        my_smartgrid.create_district_dict()
        list = my_smartgrid.make_output()

        # append costs to the list of costs for this combination of algorithms
        list_with_costs_further.append(list[0]['costs shared'])

        print('costs', list[0]['costs shared'])
        print(f'{i}/1000')

    # create plot of smartgrid for demonstration
    my_smartgrid.draw_plot()

    # make series to plot later
    series_with_costs_further = pd.Series(list_with_costs_further)
    print(series_with_costs_further)

    # plot the distribution of costs
    plt.clf()
    plt.title('houses assigned with greedy and further search algorithm')
    sns.histplot(data=series_with_costs_further)
    plt.show()


    # print(series_with_costs_greedy_90.describe())
    # print(series_with_costs_random_90.describe())
    # print(series_with_costs_hillclimber_90.describe())
    print(series_with_costs_further.describe())

    # mean_greedy_90 = series_with_costs_greedy_90.mean()
    # mean_random_90 = series_with_costs_random_90.mean()
    #mean_greedy_random_try = series_with_costs_greedy_random_try.mean()
    mean_greedy_further = series_with_costs_further.mean()

    dict_means = {'algorithm':['greedy, further cables'], 'means':[mean_greedy_further]}
    df_means = pd.DataFrame(dict_means)
    plt.clf()
    df_means.plot.bar(x='algorithm', y='means')
    plt.show()
    #---------------- hill climber ---------------------------------------------
#     random_algo = Randomize()
#     random_algo.assign_house_random(houses, batteries)
#
#     cable_90_degree = Cables_90()
#     step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
#
#     my_smartgrid.draw_plot()
#     my_smartgrid.costs_shared()
#     #my_smartgrid.district_name()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     #print(list)
# # print('costs', list[0]['costs shared'])
#     #print(existing_cable_dict)
#     #print(cable_list)
#
#
#
#     random_hill_climber = Hill_Climber(my_smartgrid)
#     random_hill_climber.run(2000)

    #---------------- simulated annealing ---------------------------------------------
#     random_algo = Randomize()
#     random_algo.assign_house_random(houses, batteries)
#
#     cable_90_degree = Cables_90()
#     step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
#
#     my_smartgrid.draw_plot()
#     my_smartgrid.costs_shared()
#     #my_smartgrid.district_name()
#     my_smartgrid.create_district_dict()
#     list = my_smartgrid.make_output()
#     #print(list)
# # print('costs', list[0]['costs shared'])
#     #print(existing_cable_dict)
#     #print(cable_list)
#
#
#
#     random_sa = Simulated_Annealing(my_smartgrid, temperature=200)
#     random_sa.run(2000)
