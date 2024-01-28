# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns  # Additional library for data visualization
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the dataset from a CSV file
dataset_path = '2.nyeri_temperature_dataset(indexed)your/dataset.csv'
data = pd.read_csv(dataset_path)

# Display the first few rows of the dataset
print("Initial dataset:")
print(data.head())

# Data Cleaning
# Example: Remove rows with missing values
data = data.dropna()

# Example: Remove outliers (using a simple z-score approach)
z_scores = np.abs((data - data.mean()) / data.std())
data_cleaned = data[(z_scores < 3).all(axis=1)]

# Display the first few rows of the cleaned dataset
print("Cleaned dataset:")
print(data_cleaned.head())

# Exploratory Data Analysis (EDA)
# Visualize the distribution of the target variable
plt.figure(figsize=(10, 6))
sns.histplot(data_cleaned['Target_Variable_Column'], bins=30, kde=True)
plt.title('Distribution of Target Variable')
plt.xlabel('Target Variable')
plt.ylabel('Frequency')
plt.show()

# Visualize the correlation matrix
correlation_matrix = data_cleaned.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# Pairplot to visualize relationships between variables
sns.pairplot(data_cleaned, vars=['Feature1', 'Feature2', 'Target_Variable_Column'])
plt.show()

# Split the dataset using the 80-20 rule
X = data_cleaned.drop('Target_Variable_Column', axis=1)  # Replace 'Target_Variable_Column' with your actual target variable
y = data_cleaned['Target_Variable_Column']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model on Linear Regression
linear_reg_model = LinearRegression()
linear_reg_model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = linear_reg_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error on the test set:", mse)

# Hyperparameter Tuning for Linear Regression (GridSearchCV)
param_grid = {'normalize': [True, False]} #Invalid parameter 'normalize' for estimator LinearRegression(). Valid parameters are: ['copy_X', 'fit_intercept', 'n_jobs', 'positive'].
grid_search = GridSearchCV(LinearRegression(), param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)

best_linear_reg_model = grid_search.best_estimator_
best_params = grid_search.best_params_

print("Best Hyperparameters for Linear Regression:", best_params)

# Normalize the data and retrain the model using the best hyperparameters
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

best_linear_reg_model.fit(X_train_scaled, y_train)

# Evaluate the model on the scaled test set
y_pred_scaled = best_linear_reg_model.predict(X_test_scaled)
mse_scaled = mean_squared_error(y_test, y_pred_scaled)
print("Mean Squared Error on the scaled test set:", mse_scaled)

# Train a neural network using TensorFlow (as an example)
# You may need to install TensorFlow using: pip install tensorflow
model = Sequential([
    Dense(units=64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(units=1)  # Assuming it's a regression task
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, validation_data=(X_test_scaled, y_test))

# Save the trained models if needed
linear_reg_model.save('linear_regression_model.h5')
best_linear_reg_model.save('best_linear_regression_model.h5')
model.save('neural_network_model.h5')
```

This script includes visualizations for the distribution of the target variable, a correlation matrix, and a pairplot for relationships between variables. Adjust these visualizations based on the characteristics of your dataset.
