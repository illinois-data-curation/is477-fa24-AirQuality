
# Project Status Report

## 1. Overview of the Project and Objectives
The primary goal of this project is to find the correspondence between air quality and its health ouctomes in different areas. This project aims to accomplish the following:
- **Objective 1**: Whether there are specific regions where the relationship is stronger
- **Objective 2**: The impact of specific pollutants
- **Objective 3**: Lagged affects of air quality on health

These objectives guide the development and implementation phases to ensure the the final deliverable is able to answer the general impact air quality has on health outcomes.

---

## 2. Task-by-Task Status Update
Below is an update on each task as outlined in the initial project plan, including progress, current status, and relevant artifacts.

### Task 1: Data Collection
- **Status**: Completed
- **Artifacts**: CDC Wonder API: https://wonder.cdc.gov/cmf-icd10.html, EPA API: https://aqs.epa.gov/aqsweb/documents/data_api.html
- **Description**: Initially, one of the datasets we were planning on using was not extremely valuable toward our final vision. Therefore, one of the first things we did was find one from the CDC that worked better with our project plan. The first dataset we accessed was from the CDC Wonder API. According to the data use restrictions, we are using the data for analysis only and are making no attempts to learn the identities of people included in the data. We wanted to focus our research on the years 2000-2003, and extracted that specific data from the API into datasets within our "data" folder. Similarly with above, to get information on the air quality, we accessed the Air Quality System API given by the EPA. According to their license, the data is considered public domain, therefore we can use the data without need for explicit permission. We also took the data from this and included it in our "data folder" for the corresponding years.

### Task 2: Data Cleaning
- **Status**: Completed
- **Description**: Looking at out two types of datasets, we were planning on merging the two. However, they were formatted differently and in order to combine the two we would need to perform some cleaning. This included cleaning the "County" variable in the CDC dataset and we would need to split it into just the County name since the variable included the state code in it as well.

### Task 3: Data Integration
- **Status**: Completed
- **Description**: In order to integrate the data, we combined the EPA data by year since they are all different files. We then marged the two datasets together by state.

---

## 3. Updated Timeline

The following timeline provides an updated view of the project’s progress, indicating which tasks have been completed, delayed, or are on track.

 **Week**       | **Tasks**                                                                                                           | **Team Member(s)**       |
|----------------|---------------------------------------------------------------------------------------------------------------------|--------------------------|
| **Week 1**     | **Data Collection**: Acquire datasets from EPA API and CDC WONDER API. Implement integrity checks. COMPLETED                 | [Kashan]                 |
| **Week 2**     | **Data Cleaning**: Programmatic integration of datasets (merge air quality and health outcome data). COMPLETED             | [Izhaan, Kashan ]        |
| **Week 3**     | **Data Integration**: Profile and clean datasets, handle missing values, and ensure consistency. COMPLETED                       | [Kashan]                 |
| **Week 4**     | **Exploratory Data Analysis**: Initial analysis to identify trends, correlations, and patterns.                     | [Izhaan]                 |
| **Week 5**     | **Data Analysis**: Perform correlation and regression analysis to explore air quality-health outcome relationships. | [Izhaan]                 |
| **Week 6**     | **Visualization**: Generate visualizations for trends and correlations between air quality and health outcomes.     | [Izhaan]                 |
| **Week 7**     | **Documentation and Final Report**: Document data acquisition, cleaning, and analysis steps. Compile findings and prepare deliverable   | [Kashan, Izhaan]         |


From the initial timeline, we switched week 2 and 3 in order to complete the data cleaning before we merged the data. We also combined weeks 7 and 8 in order to finish the deliverable on time.

---

## 4. Changes to the Project Plan

Based on the progress and challenges faced thus far, the following adjustment have been made to the original project plan:

Due to the way we are planning on merging the data and the data we have available to us, we are no longer going to be analyzing the seasonality changes of health outcomes as it relates to air quality. Instead, we are going to be exploring a different sub-topic that relates more to the location and region.

---

## 5. Next Steps

As of now, we completed the data cleaning and integration and are all set to start the data analysis. As part of our exploratory data analysis, we are also going to be looking into the best types of visualizations for our data. We are currently exploring creating a heat map that shows health outcomes.

---