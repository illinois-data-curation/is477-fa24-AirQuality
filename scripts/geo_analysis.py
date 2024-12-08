import pandas as pd
import plotly.express as px

# Assuming 'merged_data' has columns: 'State', 'County', 'County Code', 'Crude Rate'
# Load the merged dataset
merged_data = pd.read_csv('../output/results/merged_data.csv')

# Create a choropleth map of crude death rate by county
fig = px.choropleth(
    merged_data,
    geojson='https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json',  # US counties geojson
    locations='County Code',
    color='Crude Rate',
    hover_name='County',
    color_continuous_scale='Reds',
    title='Crude Death Rate by County'
)

fig.update_geos(fitbounds="locations", visible=False)
fig.write_image('../output/results/geo_analysis.png', scale=2)
