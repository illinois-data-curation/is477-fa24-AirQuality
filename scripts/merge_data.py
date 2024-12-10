import pandas as pd

# Load the datasets
cdc_data = pd.read_csv('../output/cleanedInputs/cleaned_cdc_data.csv')
epa_data = pd.read_csv('../output/cleanedInputs/cleaned_epa_data.csv')

# Convert State Code and County Code to integers in both datasets
cdc_data['State Code'] = cdc_data['State Code'].astype(int)
cdc_data['County Code'] = cdc_data['County Code'].astype(int)
epa_data['State Code'] = epa_data['State Code'].astype(int)
epa_data['County Code'] = epa_data['County Code'].astype(int)

# Create a combined County Code in the EPA data by concatenating State Code and County Code
epa_data['County Code'] = epa_data['State Code'] * 1000 + epa_data['County Code']

# Merge the datasets on State Code, County Code, and Year
merged_data = pd.merge(
    cdc_data,
    epa_data,
    how='inner',
    on=['State Code', 'County Code', 'Year']
)

merged_data = merged_data.drop(columns=['County Name', 'State Name'], errors='ignore')  

merged_data.to_csv("../output/results/merged_data.csv", index=False)
