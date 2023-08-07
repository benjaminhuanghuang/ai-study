// See https://aka.ms/new-console-template for more information


using Microsoft.ML;
using SentimentAanalysis;
using static SentimentAanalysis.SentimentAnalysisModel;


var input = new ModelInput();
input.SentimentText = "That is rudes";

var result = SentimentAnalysisModel.Predict(input);



Console.WriteLine(result.PredictedLabel);