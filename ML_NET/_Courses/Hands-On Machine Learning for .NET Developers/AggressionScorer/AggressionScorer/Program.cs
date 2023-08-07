// See https://aka.ms/new-console-template for more information
using AggressionScorerModel;
using AggressionScorer;
using Microsoft.ML;

Console.WriteLine("Aggression scroer model builder started!");

var mlContext = new MLContext(0);

//Build pipeline
var inputDataPerpare = mlContext
    .Transforms
    .Text
    .FeaturizeText("Features", "Comment")
    .AppendCacheCheckpoint(mlContext);

// Create a training algorithm
var trainer = mlContext
    .BinaryClassification
    .Trainers
    .LbfgsLogisticRegression();


var trainingPipeline = inputDataPerpare.Append(trainer);


//Load data 
var createdInputFile = @"Data\preparedInput.tsv";
DataPreparer.CreatePreparedDataFile(createdInputFile, onlySaveSmallSubset: true);

IDataView trainingDataView = mlContext.Data.LoadFromTextFile<ModelInput>(
    path: createdInputFile,
    hasHeader: true,
    separatorChar: '\t',
    allowQuoting: true
);

//-- split data for testing
var inputDataSplit = mlContext.Data.TrainTestSplit(trainingDataView, testFraction: .2, seed: 0);

//Build pipeline
var inputDataPreparer = mlContext
                        .Transforms
                        .Text
                        .FeaturizeText("Features", "Comment")
                        .Append(mlContext.Transforms.NormalizeMeanVariance("Features"))
                        .AppendCacheCheckpoint(mlContext)
                        .Fit(inputDataSplit.TrainSet);

//Fit the model
Console.WriteLine("Start training model");

var startTime = DateTime.Now;
var transformedData = inputDataPreparer.Transform(inputDataSplit.TrainSet);
ITransformer model = trainer.Fit(transformedData);

Console.WriteLine($"Model training finished in {(DateTime.Now - startTime).TotalSeconds} seconds");

//Test the model
EvaluateModel(mlContext, model, inputDataPreparer.Transform(inputDataSplit.TestSet));


//Save the model
Console.WriteLine($"Saving the model");

if (!Directory.Exists("Model"))
{
    Directory.CreateDirectory("Model");
}

var modelFile = @"Model\\AggressionScoreModel.zip";
mlContext.Model.Save(model, trainingDataView.Schema, modelFile);

Console.WriteLine("The model is saved to {0}", modelFile);




static void EvaluateModel(MLContext mlContext, ITransformer trainedModel, IDataView testData)
{
    Console.WriteLine();
    Console.WriteLine("-- Evaluating binary classification model performance --");
    Console.WriteLine();

    var predictedData = trainedModel.Transform(testData);

    var metrics = mlContext.BinaryClassification.Evaluate(predictedData);

    Console.WriteLine($"Accuracy: {metrics.Accuracy:0.###}");

    Console.WriteLine();

    Console.WriteLine("Confusion Matrix");
    Console.WriteLine();
    Console.WriteLine(metrics.ConfusionMatrix.GetFormattedConfusionTable());
    Console.WriteLine();
}