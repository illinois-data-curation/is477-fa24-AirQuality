# Relationship between Air Quality and Health Outcomes

## Archived Record
https://zenodo.org/records/14404672?token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6ImQ4M2MwNTczLTFjMzEtNDk5MC04MjJhLWNlMTNlNDUyNWU1MCIsImRhdGEiOnt9LCJyYW5kb20iOiI5YzcyMTlhNTJhYjIwOTE2MmVmZTQ4NTg3ZDYxM2EyYiJ9.DQgXQFnOj8_hEtJjOpNuX9nDoYQsklcigCSBoQWYfKvhDXnsWxshQKFdTHweEHu-I0D1x0u-8N7hyyAfNvYP4Q

Identifier: 10.5281/zenodo.14404672

## Contributors
- Izhaan Hussain
  - ORCID: 0009-0005-2240-8773
- Kashan Ali
  - ORCID: 0009-0008-5062-9276

## Description of Research

The objective of this project is to analyze trends over time across various regions to understand the relationship between air quality and health outcomes. Specifically, the study aims to address the hypothesis:

"How do changes in air quality impact health outcomes in different areas?"

The main idea that we are tackling is that worse air quality affects health outcomes in a negative way, potentially leading to increased illnesses and respiratory conditions. Poor air quality can also worsen existing chronic conditions such as asthma or cardiovascular diseases, further burdening health effects in society. Understanding this relationship is important for informing public health officials and policymakers. Accurate data on the impact of air quality on health outcomes allows policymakers to identify areas where this is a problem and implement necessary measures to combat this, such as stricter emissions regulations, public health advisories, and increased funding for healthcare infrastructure in affected regions. Healthcare providers can also use this information to predict patient needs, and use that to offer preventive care, as well design community health programs aimed at preventing the deadly effects of air pollution. Additionally, orgnaizations serving to improve the environment can leverage these insights to advocate for cleaner air policies, promote sustainable practices, and raise public awareness about the health risks associated with such air pollution. Furthermore, this study can help direct resources toward populations that are the most at risk, such as children, the elderly, and individuals with pre-existing conditions, who are most affected by poor air quality. Ultimately, addressing air pollution through evidence-based strategies can lead to healthier communities, reduced healthcare costs, and improve the overall quality of life.

To improve reproducibility, all generated plots, code, and datasets have been archived and referenced below. Regression models were designed to provide deeper insights into pollutant-health relationships, specifically highlighting how population size correlates to mortality rates and crude rates.

We will be using the following objectives to guide our research:

- **Objective 1: The overall effect of air quality and pollutants on health outcomes**
  - What is the overall effect certain pollutants have on health effects?
  - We will be looking at whether pollutants have an effect on health outcomes, and what type of effect.
- **Objective 2: Geographic Differences in Air Quality and Health Outcome Relationship**
  - Are there specific regions where the relationship between air quality and health outcomes is stronger?
  - The following query looks into geographic variability to assess whether there are areas that would be most susceptible to the adverse health effects of changes in air quality. This will review differences across urban, suburban, and rural areas to look at whether there is greater association between air quality and health outcomes in some places compared to others.
- **Objective 3: The impact of specific pollutants**
  - Do specific pollutants (e.g., PM2.5, NO2, O3) have a different effect on health outcomes?
  - Air quality statistics also involve different categories of pollutants. This sub-question will, therefore, investigate whether some categories of pollutants have a greater effect on health outcomes in determining which ones are most harmful to public health.
- **Objective 4: Lagged effects of air quality on health**
  - Do changes in air quality in one period (e.g., previous month or season) predict changes in health outcomes in subsequent periods?
  - It will further investigate whether the variation in air quality in one period has a lagged health consequence in another period. This project will contribute to the identification of lagged health effects caused by poor air quality.

This research, guided by the outlined objectives, aims to provide a thorough analysis of the relationship between air quality and health outcomes. By examining the overall effects of pollutants, exploring geographic differences, assessing the impact of specific pollutants, and identifying potential lagged health effects, the study seeks to offer a multi-faceted understanding of how air quality influences public health.

## Data Profile

- Centers for Disease Control and Prevention Wonder API
  - https://wonder.cdc.gov/cmf-icd10.html
- Environmental Protection Agency API
  - https://aqs.epa.gov/aqsweb/documents/data_api.html

The first dataset we selected was obtained through the CDC Wonder API. The dataset includes statistics surrounding deaths occurring within the U.S., with variables categorized by demographic factors such as age, sex, race, and location (state and county level). The data was pulled from death certificates filed in most United States territories and is coded according to the ICD-10 (International Classification of Diseases).

This API allows us to access data on mortalities spanning from the years of 1999 to present day, which make it suitable in our case of long-term trend analysis. Researchers can also filter the data by things such as causes of death, and filter results by parameters such as year, place of death, and population. The dataset also provides mortality rates, counts of deaths, and age-adjusted rates, enabling comprehensive epidemiological research. Since our research focuses on the years from 2000-2003, we filtered the API to those years.

The CDC API actualy supports public health initiatives by offering insights into these patterns and trends in deaths and mortalities, including causes related to chronic and infectious diseases, injuries, and other related health conditions. It is particularly useful for identifying health conditions across different locations and populations in the United States, as well as analyzint the effects over time of public health policies. However, in order to safeguard the individuals' identities who were used in the ata, there are restrictions in place. In order to comply with the data use restrictions, we are using this data solely for analysis and are not attempting to identify any individuals within the dataset. We extracted the relevant data from the API and stored it in our "data" folder.

The second dataset, obtained from the U.S. Environmental Protection Agency's (EPA) Air Quality System (AQS), provides annual air quality data covering severals regions throughout the United States for several years. It contains statistics for a range of pollutants, including particle matter, ozone, sulfur dioxide, nitrogen dioxide, and carbon monoxide. These pollutants were tracked by state and local air quality monitoring stations, offering a detailed view on air quality trends over time and across different areas.

This dataset is a useful tool for understanding how changes in pollutant levels and other related variables impact respiratory health and other health issues, which supports our project's objective of examining the relationship between health outcomes and air quality across time in different regions. This data, which spans the years 2000–2003, aids in studies on seasonal patterns, pollution trends, and events that affect air quality. The analysis's findings can help with resource allocation and policy development to lessen the harmful health impacts of air pollution.

This data was accessed directly by the API, and since the data is classified as public domain under the EPA's license, we are permitted to use it without needing explicit permission. This data was also stored in our "data" folder for the corresponding years.

## Findings
#### Exploratory Analysis
In order to observe basic trends and correlations in our data, we calculate some summary statistics that are in output/results/eda_summary.txt. The most notable statistic in the summaries for pollutants is the average primary exceedance count being 11.3 which is the number of times pollutant levels exceeded regulatory standards. We can also see that there is a slight correlation between death rate and primary exceedance count. Given the context of this, it is still a significant amount. As far as the pollutants themselves go, the number of unique pollutants in our data is 6. The most frequently recorded pollutant was PM2.5 - Local Conditions, appearing in 23,511 observations, followed by Ozone with 13,604 observations. When we grouped the death rate along with the pollutants, we found sulfur dioxide had the highest average death rate (903 per 100,000), reinforcing its significance as a health risk factor.

#### Pollutant Levels and Mortality Rates
In order to find how pollutant levels affected mortality rates, we created a scatterplot of two relevant variables. To assess pollutant levels, we used "Primary Exceedance Count" and to assess mortality rates, we used "Crude Death Rate". This results in the following plot: 

![Primary Exceedance Count vs Crude Death Rate](output/results/primary_exceedance_vs_crude_rate.png)

Although there is a weak positive correlation and a slight upward trend, indicating that higher exceedance counts may be associated with higher death rates, the relationship is not strong enough to draw definitive conclusions. This weak correlation implies that while pollutant exceedances contribute to health outcomes, other factors such as socioeconomic conditions, healthcare access, and underlying health conditions likely play significant roles in influencing crude death rates.

#### Geographic Distribution of Mortality
The second objective we wanted to tackle was the geographic distribution of crude death rates across US counties. This resulted in the following plot:

![Geographic Distribution of Crude Death Rates](output/results/geo_analysis.png)

In some areas of the southern and western United States, higher crude fatality rates were noted. Geographic variability indicates that factors like population density, proximity to pollution sources, and socioeconomic differences cause various locations to experience differing degrees of air quality and health implications.

The significance of region-specific policies and interventions in efficiently addressing air quality challenges is underscored by this spatial study. To lessen negative health effects, areas with greater death rates might need more healthcare resources, more stringent pollution regulations, and focused public health initiatives.

#### Mean Crude Rate by Pollutant
In order to find which pollutants had the biggest effect on crude death rate, we created a bar chart to visualize this:

![Geographic Distribution of Crude Death Rates](output/results/parameter_analysis.png)

Sulfur dioxide and PM2.5 - Local Conditions were associated with the highest mean crude death rates, while Carbon monoxide and Nitrogen dioxide (NO2) were linked to comparatively lower crude rates. These results suggest that certain pollutants, particularly Sulfur dioxide and PM2.5, can pose a greated risk to public health-related effects and contribute more significantly to adverse health outcomes compared to others. This finding underscores the need for targeted interventions to reduce emissions of these harmful pollutants.

#### Trends Over Time
In order to see whether there are lagged effects of pollutants on health outcomes, we created a line chart showing "Primary Exceedance Count" and "Crude Death Rate":

![Geographic Distribution of Crude Death Rates](output/results/death_pollutants_over_time.png)

The chart shows relatively stable patterns. This suggests that although there are fluctuations, there may not be immediate impacts on death rates within short time frames. It also raises the possibility that long-term exposure to even low levels of pollutants can have cumulative health effects.

#### Regression Analysis
To further investigate the relationship between population size, pollutant exceedances, and health outcomes, we generated the following regression plots:

1. **Population vs. Crude Rate**
   ![Population vs Crude Rate](output\results\regressions\Population_vs_Crude_Rate.png)
   - **Analysis**: The regression shows a negative correlation between population size and crude death rates. This result suggests that larger populations tend to have lower crude death rates, possibly due to better healthcare access, infrastructure, and preventive measures in densely populated areas.

2. **Population vs. Deaths**
   ![Population vs Deaths](output\results\regressions\Population_vs_Deaths.png)
   - **Analysis**: The regression reveals a strong positive correlation between population size and the number of deaths, which is an expected finding as larger populations have more individuals at risk. This emphasizes the importance of using normalized metrics like crude death rates for comparisons across regions with differing population sizes.

3. **Primary Exceedance Count vs. Crude Rate**
   ![Primary Exceedance Count vs Crude Rate](output\results\regressions\Primary_Exceedance_Count_vs_Crude_Rate.png)
   - **Analysis**: The regression line indicates a slight positive correlation between pollutant exceedances and crude death rates. While this correlation is weak, it aligns with the hypothesis that areas experiencing more frequent exceedances of pollutant thresholds tend to have slightly worse health outcomes.

These regression findings underscore the need for further investigation into causal factors, as well as the integration of additional variables such as socioeconomic status, healthcare access, and chronic disease prevalence to improve model robustness.

## Future Work
We learned a number of crucial lessons about the connection between air quality and health outcomes during this study, as well as the difficulties in analyzing data in this area. The significance of choosing relevant datasets that support the project's goals was one important learning. After first identifying datasets that did not adequately support our research objectives, we refined our data sources by adding information from the EPA's Air Quality System (AQS) and the CDC WONDER API. 

The difficulty of evaluating associations between air quality and health outcomes was another important lesson learned. The general relationship between pollution exceedance counts and health outcomes was minimal, however some pollutants, such sulfur dioxide and PM2.5, demonstrated a significant link with higher crude death rates. This emphasizes how a variety of factors, such as socioeconomic status, access to healthcare, and pre-existing medical issues, affect health outcomes. It takes a multidisciplinary approach and more in-depth investigation than simple correlation to comprehend these links.

Furthermore, the geographical differences in crude mortality rates demonstrated how crucial it is to take contextual and regional factors into account when evaluating air quality statistics. The degree of pollution and its effects on health vary by location, including urban, suburban, and rural settings. This realization highlights the necessity of region-specific public health initiatives and strategies.

Finally, we learned the value of combining visual analysis (charts and maps) with statistical summaries to provide a more comprehensive understanding of the data. Visualizations helped identify patterns and anomalies that were not immediately obvious from raw data alone.

In order to take this research futher, there are several things we can do to refine our research. We could incorporate additional variables which will help us understand the factors influencing health outcomes more. This can include things such as healthcare access, demographics, and pre-existing conditions. We can also expand our analysis to cover a long period of time which will help us espcially figure out the cumulative effects of pollution. Further exploration of the lagged effects of air quality on health outcomes could provide insights into longer health consequences of pollution exposure. This analysis could help predict future health burdens based on current pollution levels and help inform timely solutions. We can also apply more advanced statistical models to understand how exactly a pollutant will affect outcomes based off estimates of coefficients. These methods could also help identify causal relationships rather than simple correlations. Finally, if we investigate the impact of environmental policies and regulations in improving air quality, we can understand whether implementing these would help improve health outcomes.

## Reproducing
1. Download the archived dataset and scripts from the link above.
2. Ensure all required dependencies are installed (see `requirements.txt`).
3. Run `scripts/load_data.py`, `scripts/clean_data.py` , and `scripts/merge_data.py`  to preprocess and merge datasets.
4. Run the remaining scripts not including the regression.py to create the scatter plots needed
5. Execute `scripts/regression.py` to generate regression visualizations.
6. Review outputs in the `results` folder for analysis and findings.


## Work Split

All Team members contributed equally to this project. All data cleaning, preprocessing, and merging was done by Kashan. While the initial data analyis was done by Izhaan. The final data analysis and all written portions were done by Kashan & Izhaan.


## References
- Centers for Disease Control and Prevention Wonder API: https://wonder.cdc.gov/cmf-icd10.html
- Environmental Protection Agency API: https://aqs.epa.gov/aqsweb/documents/data_api.html

## Output
All output is available with the following link:
https://uofi.box.com/s/qeu64ckn2i50oen30wktcroo2psgnx5u