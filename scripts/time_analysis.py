import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../output/results/merged_data.csv')

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year', y='Primary Exceedance Count', label='Primary Exceedance Count')
sns.lineplot(data=df, x='Year', y='Crude Rate', label='Crude Death Rate')
plt.title('Trends in Pollution Exceedance and Crude Death Rate Over Time')
plt.legend()

plt.savefig('../output/results/death_pollutants_over_time.png', dpi=300, bbox_inches='tight')