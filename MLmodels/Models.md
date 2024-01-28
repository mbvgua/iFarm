# Linear Regression

Most basic type of machine learning model that is basic and easy to use. It is a fundamental statistical technique used for modeling the relationship between a dependent variable (target) and one or more independent variables (features). In the context of machine learning, linear regression is a supervised learning algorithm commonly employed for regression tasks. It basically involves:

1. **Linear relationship**: assumes that there is a linear relationship between the independent variables(features) and the dependent variables(target). 
### ![dependent and independent variables image]()
the relationship could either be positive,*where the slope will have a positive gradient*, or negative,*where the slope will have a negative gradient*.
Mathematically this relationship is represente as `y=mX+b`. Where:
	+ y = dependent variable(target) 
	+ x = independent variable(feature)
	+ m = slope of the the line.represents the effect of the feature on the target.
	+ c = is the intercept, indicating the value of `y` when `x` is zero.

2. **Objective**: the objective of a linear regression model is to find the best line of fit, which will minimize the differences between the predicted values and the actual values of the target variable. This could be achieved y minimizing a loss function, such as the Mean Squared Error*MSE*, that measures the average squared diffrence between predicted and actual values.

3. **Model Training**: in this phase the algorithm will adjust the values of the slope `m` and the intercept `b` to minimize the loss function. this will involve finding the optimal parameters that best describe the relationship between features and the target.

4. **Prediction**: once the model has been trained, it can be used to make predictions on new data. This is termed as generalization. Given values of the independent variable, the model should calculate the predicted value of the dependent variable using the equation of the line `y=mX + c` 

5. **Evaluation**: The performance of the linear regression model is usually calculated using various metrics that quantify how well the model fits the data and how accurate its predictions are. These include:
	+ `Coefficient of Determination`(*R<sup>2</sup>*):- represents the proportion of the variance in the dependent variable that is predictable from the independent variables. It ranges from 0 to 1, where 1 indicates a perfect fit. \( R^2 \) can be calculated using the following formula:

   ![R<sup>2</sup> Image]()

   Where:
   - SSR (Sum of Squared Residuals) is the sum of the squared differences between the predicted values and the mean of the dependent variable.
   - SST (Total Sum of Squares) is the total sum of squared differences between each observation and the mean of the dependent variable.

   Higher R<sup>2</sup> values indicate better fit, with 1 being the best possible score.

	+ `Root Mean Squared Error`(RMSE) :- RMSE represents the average deviation of the predicted values from the actual values. It is calculated by taking the square root of the average of the squared differences between predicted and actual values. RMSE is given by:

   ![RMSE Image]()

   Where:
   + n :- is the number of observations.
   + y :- is the actual value of the dependent variable for observation \( i \).
   + <sup>~</sup>y :- is the predicted value of the dependent variable for observation \( i \).

	>Lower RMSE values indicate better performance, with 0 being the best possible score.

	+ `Mean Absolute Error`(MAE) :- represents the average absolute difference between the predicted and actual values. It is calculated as:
		
		![Image for MAE]()

   MAE provides a more interpretable measure of prediction error compared to RMSE, as it is in the same units as the dependent variable.

----------

# Decision Trees

------------

# Gradient Boosting

----------
