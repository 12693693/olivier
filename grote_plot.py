import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df_to_plot = pd.DataFrame()

df = pd.read_csv('cost greedy, 90 degrees')
# series = pd.Series(df)
df_to_plot['greedy, 90 degrees']= df['0']

df = pd.read_csv('cost greedy, random try')
# series = pd.Series(df)
df_to_plot['greedy, random try']= df['0']

df = pd.read_csv('cost greedy, search cables')
# series = pd.Series(df)
df_to_plot['greedy, search cables']= df['0']

df = pd.read_csv('cost greedy, further cables')
# series = pd.Series(df)
df_to_plot['greedy, further cables']= df['0']

df = pd.read_csv('cost greedy, breadth first')
# series = pd.Series(df)
df_to_plot['greedy, breadth first']= df['0']


sns.histplot(data=df_to_plot, bins=30)
plt.title('Distribution of costs per algorithm combination')
plt.xlabel('Costs')
plt.show()
