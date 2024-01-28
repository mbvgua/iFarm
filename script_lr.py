import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Generate some example data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Feature
y = 4 + 3 * X + np.random.randn(100, 1)  # Target with noise

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# Plot scatter plot with fitted regression line
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Fitted line')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Linear Regression: Features vs. Target')
plt.legend()
plt.grid(True)
plt.show()
