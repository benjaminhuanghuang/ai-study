﻿
// This file was auto-generated by ML.NET Model Builder. 

using SentimentAnalysisModel_ConsoleApp;

// Create single instance of sample data from first line of dataset for model input
SentimentAnalysisModel.ModelInput sampleData = new SentimentAnalysisModel.ModelInput()
{
    SentimentText = @"== OK! ==  IM GOING TO VANDALIZE WILD ONES WIKI THEN!!!",
    LoggedIn = true,
};



Console.WriteLine("Using model to make single prediction -- Comparing actual Sentiment with predicted Sentiment from sample data...\n\n");


Console.WriteLine($"Sentiment: {1F}");
Console.WriteLine($"SentimentText: {@"== OK! ==  IM GOING TO VANDALIZE WILD ONES WIKI THEN!!!"}");
Console.WriteLine($"LoggedIn: {true}");


var sortedScoresWithLabel = SentimentAnalysisModel.PredictAllLabels(sampleData);
Console.WriteLine($"{"Class",-40}{"Score",-20}");
Console.WriteLine($"{"-----",-40}{"-----",-20}");

foreach (var score in sortedScoresWithLabel)
{
    Console.WriteLine($"{score.Key,-40}{score.Value,-20}");
}

Console.WriteLine("=============== End of process, hit any key to finish ===============");
Console.ReadKey();
