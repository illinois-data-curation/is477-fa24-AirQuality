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

The underlying concept here is that worse air quality has negative health impacts, potentially increasing hospitalizations and other respiratory issues. In theory, this knowledge of the relationship could provide special attention by policymakers, physicians, and environmental groups to areas with higher concerns due to air pollution.

In this regard, the research would take into consideration data regarding air quality in different years and places with various levels of health outcomes to identify the trend that will help develop public health policy and resource allocation. Such a study will eventually go a long way in contributing knowledge for better decision-making for the mitigation of adverse health consequences of poor air quality and improvement in public health.

## 2. Research Questions

The primary aim of this research is to establish the regional variation in air quality and how such differences in quality impact health consequences. In this respect, the temporal variation in air quality and health outcomes will be examined by studying regional and seasonal differences. In particular, the following key questions are used as guidelines in undertaking this research:

### 2.1 Primary Research Question

    - **How does air quality affect health outcomes across different regions over time?**

        -It will then analyze if the areas with poor air quality indicate more adverse health outcomes, such as respiratory problems or hospital admissions. Thus, this question aims to see whether there is general correspondence between air pollution and health indicators.

### 2.2 Sub-Questions

Several sub-questions are considered in order to satisfy the main topic. These sub-questions allow a closer view through the division of the main topic into particular facets of location, seasonality, and pollutant kinds:

1. **Seasonal Impact on Health Outcomes**:

   - **Do health outcomes associated with air quality vary seasonally within the same area?**

        -This sub-question examines the hypothesis that poorer health outcomes may be associated with specific seasons. For instance, in those locations experiencing large changes in air quality, heating emissions in winter or higher levels of ozone in summer can produce spikes in adverse health effects.

2. **Geographic Differences in Air Quality and Health Outcome Relationship**:

   - **Are there specific regions where the relationship between air quality and health outcomes is stronger?**

        -The following query looks into geographic variability to assess whether there are areas that would be most susceptible to the adverse health effects of changes in air quality. This will review differences across urban, suburban, and rural areas to look at whether there is greater association between air quality and health outcomes in some places compared to others.

3. **Type of Pollutant and Its Differential Impact on Health Outcomes**:

   - **Do specific pollutants (e.g., PM2.5, NO2, O3) have a different effect on health outcomes?**

        -Air quality statistics also involve different categories of pollutants. This sub-question will, therefore, investigate whether some categories of pollutants have a greater effect on health outcomes in determining which ones are most harmful to public health.

4. **Threshold Levels and Health Outcome Sensitivity**:

   - **Is there a threshold level of pollutant concentration that significantly impacts health outcomes?**

        -The following question asks whether there is a threshold for levels of pollutants beyond which measurable health outcomes noticeably deteriorate. For instance, do health problems become appreciably more common when PM2.5 levels rise over a particular threshold?

5. **Lagged Effects of Air Quality on Health Outcomes**:

   - **Do changes in air quality in one period (e.g., previous month or season) predict changes in health outcomes in subsequent periods?**
   
        -It will further investigate whether the variation in air quality in one period has a lagged health consequence in another month or season. This project will contribute to the identification of time lags in the adverse health effects caused by poor air quality.

### 2.3 Hypotheses

Based on the questions above, the study will test the following hypotheses:

**Hypothesis 1**: The incidence of poor health outcomes is related to poorer air quality in the same location and over the same time period.

**Hypothesis 2**: The relationships between air quality and health outcomes vary between regions because vulnerability differs.

**Hypothesis 3**: The health effect from different pollutants varies, and PM2.5 probably contributes a worse impact compared with other contaminants.

**Hypothesis 4**: There exists a threshold level of air pollution beyond which the risk of adverse health consequences abruptly increases at any location.
In other words, the level of air pollution from one period affects health outcomes in later periods.

**Hypothesis 5**: Health outcome changes due to air quality changes will only unfold over a certain period of time.

## 3. Team

- **[Kashan]**: Responsible for data collection, data cleaning, and integration of datasets. Also assisting with initial data analysis and ensuring reproducibility.

- **[Izhaan]**: Responsible for conducting advanced data analysis, creating visualizations, and compiling the report. Will also manage documentation and project archiving.

## 4. Datasets

### 4.1 Dataset Sources

#### EPA Air Quality Data: https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual

This dataset, sourced from the U.S. Environmental Protection Agency’s (EPA) Air Quality System (AQS), offers comprehensive annual air quality data spanning multiple years and geographic locations within the United States. The dataset includes measurements of various pollutants, such as particulate matter (PM2.5, PM10), ozone (O3), sulfur dioxide (SO2), nitrogen dioxide (NO2), and carbon monoxide (CO). These pollutants are monitored across numerous state and local air quality stations, providing a detailed overview of air quality trends over time and across regions.

In alignment with the project’s objective—to examine the association of health outcomes with air quality over time in various locations—this dataset can serve as a critical input for analyzing how fluctuations in pollutant levels impact respiratory health and other health outcomes. With data spanning from 2000-2010, researchers can use this dataset to study pollution trends, seasonal variations, and specific events affecting air quality, ultimately supporting policy development and resource allocation to mitigate adverse health effects.

#### CDC Health Outcomes Data: https://www.cdc.gov/brfss/annual_data/annual_data.htm

This dataset, provided by the CDC’s Behavioral Risk Factor Surveillance System (BRFSS), includes annual health survey data across U.S. states and territories. The BRFSS dataset contains self-reported health information on a variety of topics, including chronic respiratory conditions like asthma and chronic obstructive pulmonary disease (COPD), as well as general health, healthcare access, and risk factors such as smoking status.

In the context of this project, which aims to analyze the impact of air quality on health outcomes over time in different regions, the BRFSS dataset can serve as a key source of health-related information. The dataset spans from 2000 to 2010, allowing researchers to assess long-term health trends alongside air quality changes. With its state-level breakdown, the BRFSS data can be used to correlate air pollution exposure with reported respiratory health issues and hospitalization rates, supporting analyses on the geographic and temporal impacts of air quality on public health.


## 5. Timeline

| **Week**       | **Tasks**                                                                                                           | **Team Member(s)**       |
|----------------|---------------------------------------------------------------------------------------------------------------------|--------------------------|
| **Week 1**     | **Data Collection**: Acquire datasets from EPA API and CDC WONDER API. Implement integrity checks.                  | [Kashan]                 |
| **Week 2**     | **Data Integration**: Programmatic integration of datasets (merge air quality and health outcome data).             | [Izhaan, Kashan ]        |
| **Week 3**     | **Data Cleaning**: Profile and clean datasets, handle missing values, and ensure consistency.                       | [Kashan]                 |
| **Week 4**     | **Exploratory Data Analysis**: Initial analysis to identify trends, correlations, and patterns.                     | [Izhaan]                 |
| **Week 5**     | **Data Analysis**: Perform correlation and regression analysis to explore air quality-health outcome relationships. | [Izhaan]                 |
| **Week 6**     | **Visualization**: Generate visualizations for trends and correlations between air quality and health outcomes.     | [Izhaan]                 |
| **Week 7**     | **Documentation**: Document data acquisition, cleaning, and analysis steps.                                         | [Kashan, Izhaan]         |
| **Week 8**     | **Final Report and Submission**: Compile findings, prepare project deliverables, and archive with metadata.         | [Kashan, Izhaan]         |
