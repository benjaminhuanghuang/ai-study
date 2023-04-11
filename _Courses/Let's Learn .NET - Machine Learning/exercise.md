

## Create a class library named "PredictiveMaintenance"



## Add machine learning to project
1. In Visual Studio Solution Explorer, right-click your project.

2. Select Add > Machine Learning Model.

3. From the list of new items in the Add New Item dialog, select Machine Learning Model (ML.NET).

4. In the Name text box, use the name "PredictiveMaintenanceModel.mbconfig" for your model and select Add.


## Choose your scenario
In the Scenario step of the Model Builder screen, select the "Data classification" scenario

## Env
In the Environment step of the Model Builder screen, `Local (CPU)` is selected by default.
Select Next step.

## Data
Load and prepare your data
Download data ai4i2020.csv 
Remove the special characters from the column names.
In the Data step of the Model Builder screen, select File (csv, tsv, txt) for Data source type.

Choose your label column
Choose Machine failure from the Column to predict (Label) dropdown list.
Select `Advanced data options`.
Use the advanced data options to ignore those redundant columns.


## Train
In the Train step of the Model Builder screen, set Time to train (seconds) to 30.
Select Train.