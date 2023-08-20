
- A model is a structure that is fitted to training data by a machine learning
algorithm, and then used to make predictions

- When measuring the accuracy of the predictions - the model is usually
never 100% correct
- The ML.NET model builder is a Visual Studio extension used for automatically
try out the best machine learning algorithms for your training data and
machine learning scenario directly within Visual Studio


## Install ML.NET model builder extension for Visual Studio
Visual Studio 2019 > Extensions > Manage Extensions > Online > Search for "ML.NET Model Builder" > Install


## Use Model Builder to create a model

Right click on project > Add > Machine Learning > ML.NET Model Builder

Scenario: Value Prediction

Environment: Local

Data: laptoppricesUS.tsv
Column to predict: Price
Advanced options: unselect column not needed

Train: 10 seconds
click Start training


## Use model
modify the code in btnPredictPrice_Click

```
    using static LaptopPricesGUI.LaptopPricePredictionModel;

    ModelInput input = new ModelInput(){...};

    ModelOutput result = LaptopPricePredictionModel.Predict(input);

    return result.Score;
```


## Using ML.NET CLI Tool
The CLI equivalent for Model Builder, can be used on Linux, Mac

```
dotnet tool install -g mlnet

mlnet --version

cd Data

mlnet regression --dataset laptoppricesUS.tsv --label-col Price --train-time 10
```
