import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import mean
df_cables = pd.DataFrame()

df_connections = pd.DataFrame()

df = pd.read_csv('cost greedy, 90 degrees')
mean_greedy_90 = mean(df['0'])
# series = pd.Series(df)
df_cables['greedy, 90 degrees']= df['0']
df_connections['greedy, 90 degrees'] = df['0']

df = pd.read_csv('cost greedy, random try')
mean_greedy_random_try = mean(df['0'])

# series = pd.Series(df)
df_cables['greedy, random try']= df['0']

df = pd.read_csv('cost greedy, search cables')
mean_greedy_search = mean(df['0'])
# series = pd.Series(df)
df_cables['greedy, search cables']= df['0']

df = pd.read_csv('cost greedy, further cables')
mean_greedy_further = mean(df['0'])
# series = pd.Series(df)
df_cables['greedy, further cables']= df['0']

df = pd.read_csv('cost greedy, breadth first')
mean_greedy_closest_to_others = mean(df['0'])
# series = pd.Series(df)
df_cables['greedy, closest to others']= df['0']

sns.histplot(data=df_cables, bins=30)
plt.title('Distribution of costs per algorithm combination')
plt.xlabel('Costs')
plt.show()


df = pd.read_csv('cost random, 90 degrees')
mean_random_90 = mean(df['0'])
df_connections['random, 90 degrees'] = df['0']

df = pd.read_csv('cost hillclimber, 90 degrees')
mean_hillclimber_90 = mean(df['0'])
df_connections['hillclimber, 90 degrees'] = df['0']

df = pd.read_csv('cost simulated annealing, 90 degrees')
mean_simulated_90 = mean(df['0'])
df_connections['simulated annealing, 90 degrees'] = df['0']

sns.histplot(data=df_connections, bins=30)
plt.title('Distribution of costs per algorithm combination')
plt.xlabel('Costs')
plt.show()


# df_mean = pd.DataFrame()
# df_mean['Greedy, 90 degrees'] = mean_greedy_90
# df_mean['Greedy, Random Try'] = mean_greedy_random_try
# df_mean['Greedy, Search Cables'] = mean_greedy_search
# df_mean['Greedy, Further Cables'] = mean_greedy_further
# df_mean['Greedy, Closest To Others'] = mean_greedy_closest_to_others
#
# print(df_mean)
# sns.barplot(data=df_mean)
# plt.show()

print(f'greedy 90{mean_greedy_90}')
print(f'random 90 {mean_random_90}')
print(f'greedy search{mean_greedy_search}')
print(f'greedy further {mean_greedy_further}')
print(f'greedy random try{mean_greedy_random_try}')
print(f'greedy closest {mean_greedy_closest_to_others}')
print(f'random 90{mean_random_90}')
print(f'simulated 90{mean_simulated_90}')
print(f'hillclimber90{mean_hillclimber_90}')
