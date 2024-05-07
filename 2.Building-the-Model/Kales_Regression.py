#Kales Linear Regression Model

#1.Import the neccessary modules
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import joblib as jl

# load dataset to a variable using the pandas library
dataset = pd.read_csv('nyeri_kales_dataset2.csv')

# print out the number of rows and columns in a tuple form
dataset.shape

# give a list of all th columns in the dataset
dataset.columns

# get a brief statistical analysis of columns on the entire dataset
dataset.describe()

# check whether there are any missing values
dataset.isnull().sum()

# display first 5 rows of dataset
dataset.head()

# display the last 5 rows of dataset
dataset.tail()

# 2.Explaratory Data Analysis(EDA)
# Give us the number of rows and columns and their respective datatypes 
dataset.info()

# using pandas library, i want to get an overview of how the elements are correlated
dataset_numeric = dataset.select_dtypes(include=[np.number])
dataset_numeric.corr()

# visualize the correlation matrix using seaborn and matplotlib library
dataset_numeric = dataset.select_dtypes(include=[np.number])
correlation_matrix = dataset_numeric.corr()
plt.figure(figsize=(12, 8))
sb.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# since you use a linear regression, remain with only dependent and independent variables
drop_columns = ['Humidity_Level', 'Soil_Type', 'Daily_Precipitation_mm', 'Sunlight_Duration_hrs']
df = dataset.drop(drop_columns, axis=1)

# display new dataframe
df

# display correlation without a visual representation
df.corr()

# visualize the correlation matrix
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sb.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()

# visualize the type of correlation
for label in df.columns[:-1]: #all columns except the last GDD one
    plt.scatter(df[label], df['GDD']) #see how each label affects the GDD 
    plt.title(label) #title of diagram should be the variable being used
    plt.ylabel('GDD') #y label is GDD
    plt.xlabel(label) #X label is the variable being used
    plt.show()

# visualize its distribution
plt.figure(figsize=(10, 8))
sb.histplot(df['GDD'], bins=20, kde=True)  #bins is the width of each bar
plt.title('Distribution of Growing Degree Days')
plt.xlabel('GDD')
plt.ylabel('Frequency')
plt.show()

# extract only the dependent variable from X axis to y axis
X = df.drop('GDD', axis=1) 
y = df['GDD']

# display the features(values on x-axis)
X

# display the target(values on y-axis)
y

# Pairplot to visualize relationships between variables
sb.pairplot(df, vars=['Min_Temperature_C', 'Max_Temperature_C', 'GDD'])
plt.suptitle('Pairplot of features and the target') #sup for title to appear at the top centre
plt.show()

# 3,Building the Model
# divide both features and target into training and testing data
X_train, X_test, y_train,y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# initialize a variable as the linearRegression model
lr = LinearRegression()

# fit the model
lr.fit(X_train,y_train)

# to get the intercept, i.e y when x is 0
c = lr.intercept_
c

# to get the slope(coefficient)of the line
m = lr.coef_
m

## here i was getting alot of errors due to the y_pred_train and the y_train being of 
## different datatypes and i converted them both to an array type
## first print out the datatype
# print( 'y_train is a',type(y_train))
# print('y_pred_train is a ', type(y_pred_train))
## next convert them to a numpy array
y_train = np.array(y_train).reshape(-1,1)  # Convert pandas Series to NumPy 2D array
y_pred_train = np.array(y_pred_train).reshape(-1,1)
print( 'type y_train is a ',type(y_train))
print('y_pred_train is a ', type(y_pred_train))

# use inbuilt method to see accuracy
lr.score(X_test, y_test)

# Evaluate the model using R2 
r2 = r2_score(y_train,y_pred_train)
r2

# Evaluate the model on the test set using the MSE
mse = mean_squared_error(y_train, y_pred_train) #parameters are the values for real target and the predicted target
print("Mean Squared Error on the test set:", mse)

# Evaluate the model using RMSE
rmse = np.sqrt(mse)
print("Root Mean Squared Error on the test set:", rmse)

# Evaluate the model using MAE(BEST MEASURE)
mae = mean_absolute_error(y_train, y_pred_train)
print("Mean Absolute Error on the test set:", mae)

# still cant explain. consulte
plt.figure(figsize=(8, 6))
plt.scatter(y_train, y_pred_train, color='blue', label='Actual vs. Predicted')
plt.plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'k--', lw=2, color='red', label='Perfect Prediction')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs. Predicted Values')
plt.legend()
plt.grid(True)
plt.show()	

# Load your trained TensorFlow model
model = lr

# saving the model
jl.dump(model, 'linear_regression_model.pkl')

# To load the model back into memory as a file
saved_model = jl.load('linear_regression_model.pkl')



