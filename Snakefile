rule load_data:
    output:
        "output/uncleanedInputs/cdc_data.csv",
        "output/uncleanedInputs/combined_epa_data.csv"
    shell:
        "python scripts/load_data.py"

rule clean_data:
    input:
        "output/uncleanedInputs/cdc_data.csv",
        "output/uncleanedInputs/combined_epa_data.csv"
    output:
        "output/cleanedInputs/cleaned_epa_data.csv",
        "output/cleanedInputs/cleaned_cdc_data.csv"
    shell:
        "python scripts/clean_data.py"

rule merge_data:
    input:
        "output/cleanedInputs/cleaned_epa_data.csv",
        "output/cleanedInputs/cleaned_cdc_data.csv"
    output:
        "output/results/merged_data.csv"
    shell:
        "python scripts/merge_data.py"

rule eda_generation:
    input:
        "output/results/merged_data.csv" 
    output:
        "output/results/eda_summary.txt"
    shell:
        "python scripts/eda.py"

rule exceedance_vs_deaths:
    input:
        "output/results/merged_data.csv" 
    output:
        "output/results/primary_exceedance_vs_crude_rate.png"
    shell:
        "python scripts/exceedance_vs_deaths.py"

rule geo_analysis:
    input:
        "output/results/merged_data.csv" 
    output:
        "output/results/geo_analysis.png"
    shell:
        "python scripts/geo_analysis.py"

rule parameter_analysis:
    input:
        "output/results/merged_data.csv" 
    output:
        "output/results/parameter_analysis.png"
    shell:
        "python scripts/parameter_analysis.py"

rule time_analysis:
    input:
        "output/results/merged_data.csv"  
    output:
        "output/results/death_pollutants_over_time.png"
    shell:
        "python scripts/time_analysis.py"

rule regression:
    input:
        "output/results/merged_data.csv"  
    output:
        "output/results/regressions"
    shell:
        "python scripts/regression.py"
