import pandas as pd

# 1. Load and Merge EPA Datasets
epa_files = [
    "data/epa/annual_conc_by_monitor_2000.csv",
    "data/epa/annual_conc_by_monitor_2001.csv",
    "data/epa/annual_conc_by_monitor_2002.csv",
    "data/epa/annual_conc_by_monitor_2003.csv"
]

epa_dataframes = []

# Loop through files to load and append the 'Year' column based on the filename
for file in epa_files:
    print(f"Processing file: {file}")  
    split_file = file.split("_")  
    print(f"Split file parts: {split_file}") 
    year_part = split_file[-1]  
    year = year_part.split(".")[0]  
    print(f"Extracted year: {year}")  
    df = pd.read_csv(file)
    df['Year'] = int(year)  
    epa_dataframes.append(df)

# Combine all the DataFrames into one
epa_data = pd.concat(epa_dataframes, ignore_index=True)

print("EPA Dataset:")
print(epa_data.head())

# 2. Load CDC Dataset
cdc_file = "data/cdc/Mortality_Rates_2000-2003.json"

cdc_data = pd.read_csv(cdc_file, delimiter="\t", quotechar='"')

print("CDC Dataset:")
print(cdc_data.head())

# Save both datasets to files for further cleaning in the next step
epa_data.to_csv("output/uncleanedInputs/combined_epa_data.csv", index=False)
cdc_data.to_csv("output/uncleanedInputs/cdc_data.csv", index=False)
