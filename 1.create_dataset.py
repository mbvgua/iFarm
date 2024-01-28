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



# gdd for kales
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

# Calculate GDD based on a base temperature of 18 degrees Celsius for kales
base_temperature_kales = 18
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
data.to_csv('nyeri_kales_dataset.csv', index=False)


# dated dataset
Certainly! To add labels indicating the years 2018 to 2022 and expand the dataset with additional rows, we need to modify the script. Here's an updated version of your script:

```python
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

# Calculate GDD based on a base temperature of 18 degrees Celsius for kales
base_temperature_kales = 18
gdd = np.maximum((max_temps + min_temps) / 2 - base_temperature_kales, 0)

# Generate synthetic data for additional features
humidity_levels = np.random.uniform(40, 80, num_days)
soil_types = np.random.choice(['Loam', 'Clay', 'Sandy'], num_days)
daily_precipitation = np.random.uniform(0, 10, num_days)
sunlight_duration = np.random.uniform(6, 12, num_days)

# Generate synthetic date range from 2018 to 2022
date_range = pd.date_range(start='2018-01-01', periods=num_days, freq='D')

# Create a DataFrame
data = pd.DataFrame({
    'Date': date_range,
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
data.to_csv('nyeri_kales_dataset_labeled.csv', index=False)
```

This script adds a 'Date' column to the DataFrame, representing a date range from January 1, 2018, to the subsequent 2000 days. The data is then saved to a CSV file named 'nyeri_kales_dataset_labeled.csv'. Adjust the date range and other parameters as needed for your specific requirements.