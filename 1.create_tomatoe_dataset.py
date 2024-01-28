import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for 2000 days
num_days = 2000

# Generate temperatures for Nyeri, Kenya (ranges are approximate)
max_temps = np.random.normal(25, 3, num_days)   # Normal distribution for max temperatures around 25 degrees Celsius
min_temps = np.random.normal(10, 2, num_days)   # Normal distribution for min temperatures around 10 degrees Celsius

# Ensure temperatures are within realistic bounds
max_temps = np.clip(max_temps, 18, 30)
min_temps = np.clip(min_temps, 5, 15)

# Calculate GDD based on a base temperature of 11 degrees Celsius
base_temperature = 11
gdd = np.maximum((max_temps + min_temps) / 2 - base_temperature, 0)  # GDD calculation

# Create a DataFrame
data = pd.DataFrame({'Max_Temperature_C': max_temps,
                     'Min_Temperature_C': min_temps,
                     'GDD': gdd})

# Display the first few rows of the dataset
print(data.head())

# Save the dataset to a CSV file
data.to_csv('nyeri_temperature_dataset2.csv', index=False)


# additional attributes
import pandas as pd
import numpy as np

# Set a random seed for reproducibility
np.random.seed(42)

# Generate synthetic data for 2000 days
num_days = 2000

# Generate temperatures for Nyeri, Kenya (ranges are approximate)
max_temps = np.random.normal(25, 3, num_days)
min_temps = np.random.normal(10, 2, num_days)

# Ensure temperatures are within realistic bounds
max_temps = np.clip(max_temps, 18, 30)
min_temps = np.clip(min_temps, 5, 15)

# Calculate GDD based on a base temperature of 11 degrees Celsius
base_temperature = 11
gdd = np.maximum((max_temps + min_temps) / 2 - base_temperature, 0)

# Generate synthetic data for additional features
humidity_levels = np.random.uniform(40, 80, num_days)  # Random humidity levels between 40% and 80%
soil_types = np.random.choice(['Loam', 'Clay', 'Sandy'], num_days)  # Random selection of soil types
daily_precipitation = np.random.uniform(0, 10, num_days)  # Random daily precipitation between 0 and 10 mm
sunlight_duration = np.random.uniform(6, 12, num_days)  # Random sunlight duration between 6 and 12 hours

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
data.to_csv('nyeri_crop_dataset.csv', index=False)


