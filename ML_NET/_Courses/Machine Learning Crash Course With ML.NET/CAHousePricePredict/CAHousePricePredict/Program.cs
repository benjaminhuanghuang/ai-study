// See https://aka.ms/new-console-template for more information
using CAHousePricePredict;
using Microsoft.ML;

var mlContext = new MLContext();



var data = mlContext.Data.LoadFromTextFile<HousingData>("houding.csv", hasHeader: true, separatorChar: ',');


var split = mlContext.Data.TrainTestSplit(data, testFraction: 0.2);


var features  = split.TrainSet.Schema
    .Select(col => col.Name)
    .Where(colName => colName != "Label" && colName!= "OceanProximity")
    .ToArray();


var pipeline = mlContext.Transforms.Text.FeaturizeText("Text", "OceanProximity")
    .Append(mlContext.Transforms.Concatenate("Features", features))
    .Append(mlContext.Transforms.Concatenate("Feature", "Feature", "Text"))
    .Append(mlContext.Regression.Trainers.LbfgsPoissonRegression());


var model = pipeline.Fit(split.TrainSet);

var predictions = model.Transform(split.TestSet);

var metrics = mlContext.Regression.Evaluate(predictions);


Console.WriteLine($"R^2 - {metrics.RSquared}");


