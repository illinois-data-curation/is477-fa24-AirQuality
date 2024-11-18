---
title: 'Relationship between Air Quality and Health Outcomes'
output: pdf_document
author: 
  - Kashan Ali
  - Izhaan Hussain
date: "2024-10-30"
---

## Project Objective

The goal of this project is to study the trends over time for different places in the association of health outcomes with air quality. The specific hypothesis that this study will try to address is:

**"How do changes in air quality impact health outcomes in different areas?"**


## How project Is Set Up

To start off the project is laid out like this :

- project
- - data
- - - cdc
- - - - Mortality_Rates_2000-2003.json
- - - epa
- - - - annual_conc_by_monitor_2000.csv
- - - - annual_conc_by_monitor_2001.csv
- - - - annual_conc_by_monitor_2002.csv
- - - - annual_conc_by_monitor_2003.csv
- - output
- - - cleanedInputs
- - - - Data
- - - results
- - - - Results
- - - uncleanedInputs
- - - - Data
- - scripts
- - - all scripts
- - ProjectPlan.md
- - README.md

To run the scripts the project must be set up in this format. **"Note: only the folders for the output need to be created the scripts will populate the folders"**

This is the following order for running the code :
1. load_data.py
2. clean_data.py
