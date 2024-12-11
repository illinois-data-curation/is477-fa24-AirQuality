import pandas as pd

df = pd.read_csv("output/results/merged_data.csv")

cleaned_df = df.dropna(subset=['Deaths', 'Population', 'Primary Exceedance Count', 'Parameter Name'])

# New column for death rate
cleaned_df['Death Rate'] = (cleaned_df['Deaths'] / cleaned_df['Population']) * 100000

pollutant_summary = cleaned_df[['Primary Exceedance Count', 'Observation Count', 'Observation Percent']].describe()

correlation = cleaned_df[['Death Rate', 'Primary Exceedance Count']].corr()

unique_pollutants = cleaned_df['Parameter Name'].nunique()

pollutant_frequency = cleaned_df['Parameter Name'].value_counts()

health_by_pollutant = cleaned_df.groupby('Parameter Name')['Death Rate'].mean().sort_values(ascending=False)

with open('output/results/eda_summary.txt', 'w') as f:
    f.write("\n\nSummary Statistics for Pollutants:\n")
    f.write(pollutant_summary.to_string())
    f.write("\n\nCorrelation between Death Rate and Pollutant Exceedance Count:\n")
    f.write(correlation.to_string())
    f.write("\n\nNumber of Unique Pollutants:\n")
    f.write(str(unique_pollutants))
    f.write("\n\nFrequency of Each Pollutant:\n")
    f.write(pollutant_frequency.to_string())
    f.write("\n\nAverage Death Rate by Pollutant:\n")
    f.write(health_by_pollutant.to_string())