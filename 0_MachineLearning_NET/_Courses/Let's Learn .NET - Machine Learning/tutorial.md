# Train a machine learning model for predictive maintenance by using ML.NET Model Builder
https://learn.microsoft.com/en-us/training/modules/predictive-maintenance-model-builder/



## The model training process
1. Choose a scenario
2. Choose an environment
3. Load and prepare the data
4. Train
5. Evaluate the model
   

## Model Builder configuration file   
The Machine Learning Model (ML.NET) item adds a .mbconfig file to the project. 
.mbconfig file allow you to:
- Provide a name for your model.
- Collaborate with others on your team via source control.
- Persist state. If at any point in the training process you need to close Model Builder, your state is saved

## scenario
- Categorizing data: Organize news articles by topic.
- Predicting a numerical value: Estimate the price of a home.
- Grouping items with similar characteristics: Segment customers.
- Classifying images: Tag an image based on its contents.
- Recommending items: Recommend movies.
- Detecting objects in an image: Detect pedestrians and bicycles at an intersection.

The scenarios map to machine learning tasks


Machine learning tasks tend to fall into two categories:
- Supervised (label is known)
  - Classification
    - Binary (two categories)
    - Multiclass (two or more categories)
    - Image
  - Regression
- Unsupervised (label is unknown)
  - Clustering
  - Anomaly detection

## Supported environments in Model Builder


## Load and prepare your data
1. Choose your data source type.
2. Provide the location of your data.
3. Choose column purpose.


## Training and consumption code
After your model is done training, Model Builder generates the following files and adds them to your project：
- <MODEL-NAME>.zip: The artifact for the machine learning model. This file contains a serialized version of your model.

- <MODEL-NAME>.training.cs: This file contains the `model training pipeline`. Your model training pipeline consists of the data transformations and algorithm that are used to train your machine learning model. For more information, see Data transforms and How to choose an ML.NET algorithm.

- <MODEL-NAME>.consumption.cs: This file contains the classes that define the schema of your model input and output. It also contains the Predict method, which uses your model to create a PredictionEngine API and make predictions. PredictionEngine is a convenience API that allows you to perform a prediction on a single instance of data.

## Evaluate your model
Overfitting: when your model learns the patterns in your training dataset too well. When you try to use the model with new data, it doesn't provide accurate results.


## Consume machine learning models

