// See https://aka.ms/new-console-template for more information
using Microsoft.ML;
using Microsoft.ML.AutoML;

var mlContext = new MLContext();

var columnInfo = mlContext.Auto().InferColumns("./machine.csv", labelColumnName: "RelativePerf", separatorChar: ',');

var textLoader = mlContext.Data.CreateTextLoader(columnInfo.TextLoaderOptions);

var data = textLoader.Load("./machine.csv");

var settings = new RegressionExperimentSettings
{
    MaxExperimentTimeInSeconds = 15,
    OptimizingMetric = RegressionMetric.RSquared
};

var result = mlContext.Auto().CreateRegressionExperiment(settings)
    .Execute(data, labelColumnName: "RelativePerf");

Console.WriteLine(result.BestRun.ValidationMetrics.RSquared);