import json
import pandas as pd
import numpy as np

with open("resultaten/output.json") as jsonfile:
       df = pd.read_json(jsonfile)

       # Collect all cables.
       cables = []
       for i in range(1, len(df)):
           for house in df.loc[i]["houses"]:
               cables.extend(house["cables"])

       # Determine if cables may be shared and remove duplicates if so.
       if np.isin(["costs-shared"], list(df)):
           cables = list(set(cables))
           cost_label = "costs-shared"
       else:
           cost_label = "costs-own"

       print(cables)

       cable_costs = 9 * len(cables)
       battery_costs = 5000 * len(df[1:])
       total_costs = cable_costs + battery_costs


       print(total_costs)
