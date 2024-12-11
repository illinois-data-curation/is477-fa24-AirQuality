import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data_path = 'output/results/merged_data.csv'  
data = pd.read_csv(data_path)

# Create a subfolder for regression graphs
results_folder = 'output/results' 
regressions_folder = os.path.join(results_folder, 'regressions')
os.makedirs(regressions_folder, exist_ok=True)

# List of column pairs for regression analysis
regression_pairs = [
    ('Primary Exceedance Count', 'Crude Rate'),
    ('Population', 'Crude Rate'),
    ('Population', 'Deaths')
]

# Generate and save regression plots
for x_col, y_col in regression_pairs:
    plt.figure(figsize=(10, 6))
    sns.regplot(
        x=x_col, 
        y=y_col, 
        data=data, 
        scatter_kws={'alpha': 0.3, 'color': 'gray'},  # Scatter points in gray
        line_kws={'color': 'blue', 'linewidth': 2}   # Regression line in blue
    )
    plt.title(f"Regression: {x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    # Save the plot
    filename = f"{x_col.replace(' ', '_')}_vs_{y_col.replace(' ', '_')}.png"
    save_path = os.path.join(regressions_folder, filename)
    plt.savefig(save_path)
    plt.close()  # Close the plot to avoid overlap in the loop

print(f"All regression plots saved in: {regressions_folder}")
