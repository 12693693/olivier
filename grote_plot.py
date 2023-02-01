import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df_cables = pd.DataFrame()

df = pd.read_csv('cost greedy, 90 degrees')
# series = pd.Series(df)
df_cables['greedy, 90 degrees']= df['0']

df = pd.read_csv('cost greedy, random try')
# series = pd.Series(df)
df_cables['greedy, random try']= df['0']

df = pd.read_csv('cost greedy, search cables')
# series = pd.Series(df)
df_cables['greedy, search cables']= df['0']

df = pd.read_csv('cost greedy, further cables')
# series = pd.Series(df)
df_cables['greedy, further cables']= df['0']

df = pd.read_csv('cost greedy, breadth first')
# series = pd.Series(df)
df_cables['greedy, closest to others']= df['0']


sns.histplot(data=df_cables, bins=30)
plt.title('Distribution of costs per algorithm combination')
plt.xlabel('Costs')
plt.show()

df_connections = pd.DataFrame()

df = pd.read_csv('cost random, 90 degrees')
df_connections['random, 90 degrees'] = df['0']
