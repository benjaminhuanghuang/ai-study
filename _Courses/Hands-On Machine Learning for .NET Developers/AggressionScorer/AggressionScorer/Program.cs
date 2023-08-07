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



//Fit the model
Console.WriteLine("Start training model");

var startTime = DateTime.Now;
ITransformer model = trainingPipeline.Fit(trainingDataView);

Console.WriteLine($"Model training finished in {(DateTime.Now - startTime).TotalSeconds} seconds");

//Test the model


//Save the model
Console.WriteLine($"Saving the model");

if (!Directory.Exists("Model"))
{
    Directory.CreateDirectory("Model");
}

var modelFile = @"Model\\AggressionScoreModel.zip";
mlContext.Model.Save(model, trainingDataView.Schema, modelFile);

Console.WriteLine("The model is saved to {0}", modelFile);

