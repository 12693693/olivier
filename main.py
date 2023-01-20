import argparse
import pandas as pd
import random
import copy
from code.Classes.smartgrid import Smartgrid
from code.Algorithms.randomize import Randomize
from code.Algorithms.cable_90_degree import Cables
<<<<<<< HEAD
=======
from code.Algorithms.search_cables import Search_Cables
# hoi
>>>>>>> 2680677643db6a18b88a9761aa13b5c6461f84d3
#from code.Algorithms.random_try import Cables
from code.Algorithms.greedy import Greedy
from code.Algorithms.search_cables import Search_Cables
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

    # ----------------- random houses and 90 degrees cables-----------------------
<<<<<<< HEAD
=======
    random_algo = Randomize()
    random_algo.assign_house_random(houses, batteries)

    cable_90_degree = Cables()
    step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)

    my_smartgrid.draw_plot()
    my_smartgrid.costs(step_count)
    my_smartgrid.district_name()
    my_smartgrid.create_district_dict()
    list = my_smartgrid.make_output()
    print(list)
    print('costs', list[0]['costs shared'])

>>>>>>> 2680677643db6a18b88a9761aa13b5c6461f84d3
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
    # #print(list)
    # print('costs', list[0]['costs shared'])
<<<<<<< HEAD
=======


    # ------------------ random houses and cables -------------
>>>>>>> 2680677643db6a18b88a9761aa13b5c6461f84d3

    # random_algo = Randomize()
    # random_algo.assign_house_random(houses, batteries)
    #
    # cable_random = Cables()
    # step_count = cable_random.random_try(houses, batteries)
    #
    # my_smartgrid.draw_plot()
    # my_smartgrid.costs(step_count)
    # my_smartgrid.district_name()
    # my_smartgrid.create_district_dict()
    # list = my_smartgrid.make_output()
    # print(list)

    # ------------------- greedy houses and cables 90 ------------

    # greedy_algo = Greedy()
    # greedy_algo.assign_closest_battery(houses, batteries)
    #
    # cable_90_degree = Cables()
<<<<<<< HEAD
    # step_count, house_dict = cable_90_degree.make_90_degrees_cables(houses, batteries)
=======
    # step_count = cable_90_degree.make_90_degrees_cables(houses, batteries)
>>>>>>> 2680677643db6a18b88a9761aa13b5c6461f84d3
    #
    # my_smartgrid.draw_plot()
    # my_smartgrid.costs(step_count)
    # my_smartgrid.district_name()
    # my_smartgrid.create_district_dict()
    # list = my_smartgrid.make_output()
    # #print(list)
<<<<<<< HEAD
    # #print('costs', list[0]['costs shared'])
    #self.assign_house_random() # CHECK
    #self.make_cables()

#------------------------- search cables --------------------------

    random_algo = Randomize()
    random_algo.assign_house_random(houses, batteries)

    cable_search = Search_Cables()
    step_count, house_dict = cable_search.search_cables(houses, batteries)

    my_smartgrid.draw_plot()
    my_smartgrid.costs(step_count)
    my_smartgrid.district_name()
    my_smartgrid.create_district_dict()
    list = my_smartgrid.make_output()
    #print(list)
    print('costs', list[0]['costs shared'])
    print(house_dict['grid'])
=======
    # print('costs', list[0]['costs shared'])

    # my_smartgrid.draw_plot()
    # my_smartgrid.costs(step_count)
    # my_smartgrid.district_name()
    # my_smartgrid.create_district_dict()
    # list = my_smartgrid.make_output()
    # #print(list)
    # print('costs', list[0]['costs shared'])
    # print(existing_cable_dict)
    #self.assign_house_random() # CHECK
    #self.make_cables()



>>>>>>> 2680677643db6a18b88a9761aa13b5c6461f84d3



    #self.assign_house_random() # CHECK
    #self.make_cables()
