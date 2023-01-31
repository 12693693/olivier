import json
import pandas as pd
import numpy as np

# with open("resultaten/output.json") as jsonfile:
#        df = pd.read_json(jsonfile)
#
#        # Collect all cables.
#        cables = []
#        for i in range(1, len(df)):
#            for house in df.loc[i]["houses"]:
#                cables.extend(house["cables"])
#
#        # Determine if cables may be shared and remove duplicates if so.
#        if np.isin(["costs-shared"], list(df)):
#            cables = list(set(cables))
#            cost_label = "costs-shared"
#        else:
#            cost_label = "costs-own"
#
#        print(len(cables))
#
#        cable_costs = 9 * len(cables)
#        battery_costs = 5000 * len(df[1:])
#        total_costs = cable_costs + battery_costs
#
#
#        print(total_costs)


with open("resultaten/output.json") as jsonfile:
    df = pd.read_json(jsonfile)

    # Collect all cable segments.
    cable_segments = []
    for i in range(1, len(df)):
        battery_id = df.loc[i]["location"]

        for house in df.loc[i]["houses"]:
            for cable_a, cable_b in zip(house["cables"][:-1], house["cables"][1:]):
                cable_segments.append((cable_a, cable_b, battery_id))

    # Determine if cables may be shared and remove duplicates if they are connected to the same battery
    if np.isin(["costs-shared"], list(df)):
        cable_segments = list(set(cable_segments))
        cost_label = "costs-shared"
    else:
        cost_label = "costs-own"

    cable_costs = 9 * len(cable_segments)
    battery_costs = 5000 * len(df[1:])
    total_costs = cable_costs + battery_costs
    print(total_costs)
