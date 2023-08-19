# Train and Evaluate Regression Models
Regression is where models predict a number

In machine learning, the goal of regression is to create a model that can predict a numeric quantifiable value. 

Regression works by establishing a relationship between observation(features) and the prediction(label).

Find a straight line with `minimal overall variance` from the plotted points.




Supervised machine learning techniques involve training a model to operate on `a set of features` and predict a label using a dataset that includes some already-known label values. 
The training process fits the features to the known labels to define a general function that can be applied to new features for which the labels are unknown, and predict them. 

The goal of training the model is to find a function that performs some kind of calculation to the x values that produces the result y. 
We do this by applying a machine learning algorithm that tries to fit the x values to a calculation that produces y reasonably accurately for all of the cases in the training dataset.

There are many machine learning algorithms for supervised learning, and we can broadly divide them into two types:
- Regression algorithms: Algorithms that predict a y value that is a numeric value, such as the price of a house or the number of sales transactions.
- Classification algorithms: Algorithms that predict to which category, or class, an observation belongs. The y value in a classification model is a `vector of probability values between 0 and 1, one for each class`, indicating the probability of the observation belonging to each class.

## Prepare the data
- detect and fix issues in the data (such as dealing with missing values, errors, or outlier values), 
- deriving new feature columns by transforming or combining existing features (a process known as feature engineering), 
- normalizing numeric features (values you can measure or count) so they're on a similar scale, 
- encoding categorical features (values that represent discrete categories) as numeric indicators.



## residuals
When comparing a predicted value (y-hat) with an observed value (y), we refer to the difference between them as the residuals.

You can quantify the residuals by calculating a number of commonly used evaluation metrics.
- Mean Square Error (MSE): The mean of the squared differences between predicted and actual values. This yields a relative metric in which the smaller the value, the better the model's fit.
- Root Mean Square Error (RMSE): The square root of the MSE. This yields an absolute metric in the same unit as the label (in this case, numbers of rentals). The smaller the value, the better the model (in a simplistic sense, it represents the average number of rentals by which the predictions are wrong).
- Coefficient of Determination (usually known as R-squared or R2): A relative metric in which the higher the value, the better the model's fit. In essence, this metric represents how much of the variance between predicted and actual label values the model is able to explain.

## Improve models with hyperparameters
Simple models with small datasets can often be fit in a single step, while larger datasets and more complex models must be fit by repeatedly using the model with training data and comparing the output with the expected label. If the prediction is accurate enough, we consider the model trained. If not, we adjust the model slightly and loop again.

Hyperparameters are values that change the way that the model is fit during these loops. Learning rate, for example, is a hyperparameter that sets how much a model is adjusted during each training cycle. A high learning rate means a model can be trained faster, but if it’s too high the adjustments can be so large that the model is never ‘finely tuned’ and not optimal.
