# ML.NET for Beginner
https://learn.microsoft.com/en-us/shows/mlnet/?wt.mc_id=educationalmlnet-c9-niner

https://www.youtube.com/watch?v=X0DQjfW09kA&list=PLdo4fOcmZ0oUDTvk5XMNues09FnuB_D0u

https://github.com/dotnet/machinelearning-samples



## ML.NET - Machine Learning Introduction
Machine learning is all about programming un-programmable

## ML.NET Introduction

## Getting started with ML.NET

3 Ways to use ML.NET
- ML.NET API
- ML.NET Model Builder (VS UI)
- ML.NET CLI (Cross platform)

ML workflow
- Prepare data: Load data, Extract Features
- Build & Train model & Evaluate model
- Run/ Consume model
  
### Use ML.NET Model Builder (VS UI)
![ML.NET Tutorial - Get started in 10 minutes](https://dotnet.microsoft.com/en-us/learn/ml-dotnet/get-started-tutorial/intro)

Launch Model Builder:
    Right click on project > Add > Machine Learning Model > Select Machine Learning Model(ML.NET)

Use Model Builder:
- Pick a Scenario: Data classification
  
- Environment: Local(CPU)

- Data: upload csv file, chose column to be predict

- Train
After training is completed, three files are automatically added as code-behind to the SentimentModel.mbconfig:
  - SentimentModel.zip: This file is the trained ML.NET model, which is a serialized zip file.
  - SentimentModel.consumption.cs: This file contains the model input and output classes and a Predict method that can be used for model consumption.
  - SentimentModel.training.cs: This file contains the training pipeline (data transforms, algorithm, and algorithm parameters) used to train the final model.

- Evaluate

- Consume ML.NET model projects, add the model project to application project.
  

### Use ML.NET CLI
https://www.c-sharpcorner.com/article/build-machine-learning-model-with-ml-net-cli/
```
    dotnet tool install --global mlnet-win-x64
    
    dotnet new console -o consumeModelApp

    # old version
    mlnet auto-train --task binary-classification --dataset "wikiDetoxAnnotated40kRows.tsv" --label-column-name"Sentiment" --max-exploration-time 180

    # new versioin
    mlnet classification --dataset "wikipedia-detox-250-line-data.tsv" --label-col "Sentiment" --train-time 10
```

add reference
```
    dotnet add reference ./SampleClassification
    dotnet add package Microsoft.ML
```

Run
```
    dotnet run
```

### Use ML.NET API
Install Microsoft.ML package



## Build a ML model for Sentiment Analysis
Binary classification 

