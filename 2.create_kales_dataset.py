# gdd for kales
import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for 2000 days
num_days = 500

# Generate temperatures for Nyeri, Kenya (ranges are approximate)
max_temps = np.random.normal(25, 3, num_days)
min_temps = np.random.normal(10, 2, num_days)

# Ensure temperatures are within realistic bounds
max_temps = np.clip(max_temps, 18, 30)
min_temps = np.clip(min_temps, 5, 15)

# Calculate GDD based on a base temperature of 18 degrees Celsius for kales
base_temperature_kales = 0
gdd = np.maximum((max_temps + min_temps) / 2 - base_temperature_kales, 0)

# Generate synthetic data for additional features
humidity_levels = np.random.uniform(40, 80, num_days)
soil_types = np.random.choice(['Loam', 'Clay', 'Sandy'], num_days)
daily_precipitation = np.random.uniform(0, 10, num_days)
sunlight_duration = np.random.uniform(6, 12, num_days)

# Create a DataFrame
data = pd.DataFrame({
    'Max_Temperature_C': max_temps,
    'Min_Temperature_C': min_temps,
    'GDD': gdd,
    'Humidity_Level': humidity_levels,
    'Soil_Type': soil_types,
    'Daily_Precipitation_mm': daily_precipitation,
    'Sunlight_Duration_hrs': sunlight_duration
})

# Display the first few rows of the dataset
print(data.head())

# Save the dataset to a CSV file
data.to_csv('nyeri_kales_dataset2.csv', index=False)
