// Initialize MLContext
using Microsoft.ML;
using Microsoft.ML.Data;

// Create ML context
MLContext mlContext = new MLContext();

// load data
var dataPath = Path.GetFullPath(@"..\..\..\..\Data\taxi-fare-train.csv");
IDataView trainingDataView = mlContext.Data.LoadFromTextFile<ModelInput>(
    path: "",
    hasHeader: true,
    separatorChar: '\t',
    allowQuoting: true,
    allowSparse: false);


// Create pipeline to extract features and add algorithm
IEstimator<ITransformer> trainingPipeline = mlContext.Transforms.Text.FeaturizeText(outputColumnName: "Features", inputColumnName: nameof(ModelInput.Sentiment))
    .Append(mlContext.BinaryClassification.Trainers.SdcaLogisticRegression(labelColumnName: "Sentiment", featureColumnName: "Features"));


// Train model
ITransformer model = trainingPipeline.Fit(trainingDataView);


// Evaluate model
var metrics = mlContext.BinaryClassification.CrossValidateNonCalibrated(trainingDataView, trainingPipeline, numberOfFolds: 5, labelColumnName: "Sentiment");

// Try model
PredictionEngine<ModelInput, ModelOutput> predictionFunciton = mlContext.Model.CreatePredictionEngine<ModelInput, ModelOutput>(model);

ModelInput sampleStatement = new ModelInput
{
    SentimentText = "This is rudes"
};

var resultPrediciton = predictionFunciton.Predict(sampleStatement);

Console.WriteLine($"Toxic sentiment = {resultPrediciton.SentimentText}");

public class ModelInput
{
    [LoadColumn(0)]
    [ColumnName(@"Sentiment")]
    public float Sentiment { get; set; }

    [LoadColumn(1)]
    [ColumnName(@"SentimentText")]
    public string SentimentText { get; set; }
}

public class ModelOutput
{
    [ColumnName(@"Sentiment")]
    public uint Sentiment { get; set; }

    [ColumnName(@"SentimentText")]
    public float[] SentimentText { get; set; }

    [ColumnName(@"Features")]
    public float[] Features { get; set; }

    [ColumnName(@"PredictedLabel")]
    public float PredictedLabel { get; set; }

    [ColumnName(@"Score")]
    public float[] Score { get; set; }

}