import pandas as pd

# Load previously saved datasets
epa_data = pd.read_csv("output/uncleanedInputs/combined_epa_data.csv")
cdc_data = pd.read_csv("output/uncleanedInputs/cdc_data.csv")

# 1. Cleaning EPA Data
epa_data = epa_data.drop(columns=[ 'Site Num', 'Parameter Code', 'Latitude', 'Longitude', 'Datum', 'Sample Duration', 
                            'Pollutant Standard', 'Metric Used', 'Method Name','Event Type',
                            'Completeness Indicator', 'Valid Day Count', 'Required Day Count',
                            'Null Data Count', 'Secondary Exceedance Count', 
                            'Secondary Exceedance Count', 'Certification Indicator',
                            'Certification Indicator', 'Num Obs Below MDL',
                            'Arithmetic Mean', 'Arithmetic Standard Dev', '1st Max Value','1st Max DateTime',
                            '2nd Max Value', '2nd Max DateTime', '3rd Max Value', '3rd Max DateTime',
                            '4th Max Value', '4th Max DateTime', '1st Max Non Overlapping Value', 
                            '1st NO Max DateTime', '2nd Max Non Overlapping Value',
                            '2nd NO Max DateTime', '99th Percentile', '98th Percentile', '95th Percentile',
                            '90th Percentile','75th Percentile', '50th Percentile', '10th Percentile',
                            'Address', 'Date of Last Change'   ], errors='ignore')

epa_data = epa_data.dropna()

print("Cleaned EPA Data:")
print(epa_data.head())

# 2. Cleaning CDC Data
cdc_data = cdc_data.drop(columns=['Notes','Year Code', 'Crude Rate Lower 95% Confidence Interval',
                                  'Crude Rate Upper 95% Confidence Interval','Crude Rate Standard Error'], errors='ignore')  

cdc_data = cdc_data.dropna()

print("Cleaned CDC Data:")
print(cdc_data.head())

# Save the cleaned datasets for further analysis
epa_data.to_csv("output/cleanedInputs/cleaned_epa_data.csv", index=False)
cdc_data.to_csv("output/cleanedInputs/cleaned_cdc_data.csv", index=False)
