


## Train classification model using code
Create a class library "AggressionScorerModel"
    Create ModelOutput.cs
    Create ModelInput.cs



Create a new console app "AggressionScorer"
Install Microsoft.ML nuget package
prepare data 
train model
save model to a zip file


## Using model in web API
Install Microsoft.ML nuget package for the web API project

Previously, you used the Prediction Engine class to use your model
But the prediction engine is not thread safe, and therefore not suitable to
use in a multi threaded environment such as a Web API

Instead, you should use the PredictionEnginePool from the Microsoft.Extensions.ML NuGet package and inject it into your controller
```
builder.Services.AddSingleton<AggressionScorer>();


```

Add AggressionScorerServiceExtensions.cs into AggressionScorerModel project

Copy the AggressionScoreModel from folder under AggressionScorer to AggressionScorerModel


## Test
