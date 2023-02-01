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
from code.Algorithms.further_cables import Further_Cables
from code.Visualisation import Visualize as vis
from code.Algorithms.closest_to_others import Closest_to_others
from statistics import mean

def load_df(houses_csv, batteries_csv):
    """
    This function loads the districts and saves them as dataframes
    """

    # Load in the csv files
    df_houses = pd.read_csv(houses_csv)
    df_batteries = pd.read_csv(batteries_csv)

    # create and fill lists of seperate coordinates for the batteries
    x_list = []
    y_list = []

    # Loop over the batteries and find the x and y of this battery
    for index, row in df_batteries.iterrows():
        x = row[0].split(',')[0]
        y = row[0].split(',')[1]

        x_list.append(int(x))
        y_list.append(int(y))

    # Modify the dataframe to add the lists and remove unnecessary columns
    df_batteries['x'] = x_list
    df_batteries['y'] = y_list
    df_batteries = df_batteries.drop('positie', axis=1)

    return df_houses, df_batteries

if __name__ == "__main__":
    # Set-up parsing command line arguments
    parser = argparse.ArgumentParser(description = "adding houses to batteries")
    parser.add_argument("district", help = "district")

    # Read arguments from command line
    args = parser.parse_args()

    # Run main with provide arguments
    df_houses, df_batteries = load_df(f'data/district_{args.district}/district-{args.district}_houses.csv', f'data/district_{args.district}/district-{args.district}_batteries.csv')
    my_smartgrid = Smartgrid(df_houses, df_batteries)

    houses, batteries = my_smartgrid.add_houses_and_batteries(df_houses, df_batteries)

    # create class objects to work with
    random_algo = Randomize()
    greedy_algo = Greedy()
    cable_90_degree = Cables_90()
    cable_random = Cables()
    search_cables = Search_Cables()
    further_cables = Further_Cables()
    cable_closest = Closest_to_others()

    # -------------------------------- User Inputs ------------------------------------
    print('Algorithms for making connections: random, greedy, hillclimber, simulated annealing')
    connections_input = input('What algorithm do you want to use for the connections?: ')
    print('Algorithms for making cables: 90 degrees, search cables, further cables, closest to others, random try')
    cables_input = input('What algorithm do you want to use for the cables?: ')
    shared_input = input('Do you want to share the cables? (yes / no): ')
    loop_input = input('How many times do you want to loop? (1 / 1000): ')

    connections_dict = {'random': 'random_algo.assign_house_random(houses_list, batteries_list)', 'greedy' : 'greedy_algo.assign_closest_battery(houses_list, batteries_list)', 'hillclimber' : 'random_hill_climber', 'simulated annealing': 'random_sa'}
    cables_dict = {'90 degrees': 'cable_90_degree.make_90_degrees_cables(houses_list, batteries_list)', 'search cables' : 'search_cables.run_search(houses_list, batteries_list)', 'further cables': 'further_cables.run_further(houses_list, batteries_list)', 'closest to others': 'cable_closest.run(houses_list, batteries_list)', 'random try': 'cable_random.run(houses_list, batteries_list)'}


    # ------------------------------- Experiment -----------------------------------------

    # Run experiment for Hill Climber or simulated annealing for 1 run.
    if (connections_input == 'hillclimber' or connections_input == 'simulated annealing') and loop_input == '1':

        # Define the houses and batteries and assign them to the random algorithm.
        houses_list = houses
        batteries_list = batteries
        random_algo.assign_house_random(houses, batteries)

        # Turns 'cables_dict' from string into a function and initiates this function.
        eval(cables_dict[cables_input])

        # Initiates the output function for the cables.
        my_smartgrid.make_output(args.district, shared_input)
        print(my_smartgrid.total_cost)

        # Initiate the hill climber and simulated annealing.
        random_hill_climber = Hill_Climber(my_smartgrid, shared_input)
        random_sa = Simulated_Annealing(my_smartgrid, shared_input, temperature=200)

        eval(connections_dict[connections_input]).run(3000, cables_dict[cables_input])

        # Turns 'connections_dict' from string into a function.
        eval(connections_dict[connections_input]).run(2000, cables_dict[cables_input])

        #Initializes the output for the connections.
        my_smartgrid.make_output(args.district, shared_input)

        # Initialize the visualisation for the connections and cables.
        vis.visualise(connections_input, cables_input)

    # Run experiment for Hill Climber or simulated annealing for more than 1 run.
    elif connections_input == 'hillclimber' or connections_input == 'simulated annealing' and loop_input != '1':
        list_costs_total = []
        df = pd.DataFrame()

        # Loop for as many times as user_input.
        for i in range(int(loop_input)):
            print(f'{i}/{loop_input}')

            cable_algo = cables_dict[cables_input].split('(')[0] + '(my_smartgrid_filled.houses_list, my_smartgrid_filled.battery_list)'

            # create deepcopy to ensure that filling the grid lists is correct
            my_smartgrid_filled = copy.deepcopy(my_smartgrid)
            # create battery and houses list of the smartgrid, by making deepcopies
            my_smartgrid_filled.battery_list = copy.deepcopy(batteries)
            my_smartgrid_filled.houses_list = copy.deepcopy(houses)

            # Assign the houses based on the random algorithm
            random_algo.assign_house_random(my_smartgrid_filled.houses_list, my_smartgrid_filled.battery_list)

            # Turn the cable_algo into a functiona and runs this
            eval(cable_algo)

            #Initializes the output for the connections.
            my_smartgrid_filled.make_output(args.district, shared_input)

            # Initiate the hill climber and simulated annealing.
            random_hill_climber = Hill_Climber(my_smartgrid_filled, shared_input)
            random_sa = Simulated_Annealing(my_smartgrid_filled, shared_input, temperature=35)

            my_smartgrid_filled, list_costs = eval(connections_dict[connections_input]).run(3000, cables_dict[cables_input])
            #Initializes the output for the connections.
            my_smartgrid_filled.make_output(args.district, shared_input)

            # Append cost to the list with costs for this algorithm combination
            list_costs_total.append(my_smartgrid_filled.total_cost)

            df[f'run {i}'] = pd.Series(list_costs)

        mean_cost = mean(list_costs_total)

        # Plot the histogram.
        sns.lineplot(data=df.mean(axis=1))
        plt.show()

        df_cost = pd.DataFrame(list_costs_total)
        df_cost.to_csv(f'cost {connections_input}, {cables_input}')


        plt.clf()
        sns.histplot(data=list_costs, bins=20)
        plt.title(f'connections made with {connections_input}, cables made with {cables_input}')
        plt.xlabel('costs')
        plt.show()

    # Run experiment for not Hill Climber or simulated annealing for 1 run.
    elif loop_input == '1' and connections_input != 'hillclimber' and connections_input != 'simulated annealing':
            houses_list = houses
            batteries_list = batteries
            # Assign the houses
            eval(connections_dict[connections_input])

            # Make the cables
            eval(cables_dict[cables_input])

            # Make output
            my_smartgrid.make_output(args.district, shared_input)
            print(my_smartgrid.total_cost)

            # Initialize the visualize
            vis.visualise(connections_input, cables_input)


    # Run experiment for not Hill Climber or simulated annealing for more than 1 run.
    elif loop_input != '1' and connections_input != 'hillclimber' and connections_input != 'simulated annealing':
        list_costs = []

        for i in range(int(loop_input)):
            # Create battery and houses list of the smartgrid, by making deepcopies
            my_smartgrid.battery_list = copy.deepcopy(batteries)
            my_smartgrid.houses_list = copy.deepcopy(houses)
            houses_list = my_smartgrid.houses_list
            batteries_list = my_smartgrid.battery_list

            # Assign the houses to battery
            eval(connections_dict[connections_input])

            # Make the cables
            eval(cables_dict[cables_input])

            my_smartgrid.make_output(args.district, shared_input)
            print(my_smartgrid.total_cost)

            # Append the costs to the grid lis.
            list_costs.append(my_smartgrid.total_cost)

        # Plot graph
        mean_cost = mean(list_costs)
        df_cost = pd.DataFrame(list_costs)
        df_cost.to_csv(f'cost {connections_input}, {cables_input}')

        plt.clf()
        sns.histplot(data=list_costs, bins=20)
        plt.title(f'connections made with {connections_input}, cables made with {cables_input}')
        plt.xlabel('costs')
        plt.show()
