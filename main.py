import argparse
import pandas as pd
import random
import copy
from code.Classes.smartgrid import Smartgrid
from code.Algorithms.randomize import Randomize
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

    # ----------------- random -----------------------
    random_algo = Randomize()
    random_algo.assign_house_random(houses, batteries)


    # for battery in batteries:
    #     print(battery.dict)
