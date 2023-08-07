## Evaluate Model
A trained model is evaluated by comparing model predictions with the actual correct values(Labelled data)


Add code to Program.cs in AggressionScorer project

```
var predictedData = trainedModel.Transform(testData);

var metrics = mlContext.BinaryClassification.Evaluate(predictedData);

Console.WriteLine($"Accuracy: {metrics.Accuracy:0.###}");

Console.WriteLine(metrics.ConfusionMatrix.GetFormattedConfusionTable());

```

## Cross validation
