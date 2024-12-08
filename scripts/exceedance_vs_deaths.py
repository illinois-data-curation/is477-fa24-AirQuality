import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../output/results/merged_data.csv')

# Scatter plot of Primary Exceedance Count vs Crude Death Rate
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Primary Exceedance Count', y='Crude Rate', alpha=0.6)

# Add plot title and labels
plt.title('Primary Exceedance Count vs Crude Death Rate')
plt.xlabel('Primary Exceedance Count')
plt.ylabel('Crude Death Rate (per 100,000)')

# Display grid for better readability
plt.grid(True)

# Save the plot to a file (PNG format)
plt.savefig('../output/results/primary_exceedance_vs_crude_rate.png', dpi=300, bbox_inches='tight')

