import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/results/merged_data.csv")

parameter_summary = df.groupby('Parameter Name').agg({
    'Primary Exceedance Count': ['mean', 'median', 'max'],
    'Crude Rate': ['mean', 'median', 'max']
}).reset_index()

parameter_summary.columns = ['Parameter Name', 
                             'Mean Exceedance Count', 
                             'Median Exceedance Count', 
                             'Max Exceedance Count',
                             'Mean Crude Rate', 
                             'Median Crude Rate', 
                             'Max Crude Rate']


# Creates a bar chart for Mean Exceedance Count and Mean Crude Rate
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(parameter_summary['Parameter Name'], parameter_summary['Mean Crude Rate'], color='tab:blue', label='Mean Crude Rate')
ax1.set_xlabel('Parameter Name')
ax1.set_ylabel('Mean Crude Rate', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')
plt.xticks(rotation=45)
plt.title('Mean Crude Rate by Pollutant')
fig.tight_layout()
plt.grid(True)

plt.savefig('output/results/parameter_analysis.png', dpi=300, bbox_inches='tight')
