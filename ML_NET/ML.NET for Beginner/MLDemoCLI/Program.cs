// Add input data
var sampleData = new SampleClassification.ConsoleApp.ModelInput()
{
    Col0 = "This restaurant was wonderful."
};

// Load model and predict output of sample data
var result = SampleClassification.ConsoleApp.Predict(sampleData);

// If Prediction is 1, sentiment is "Positive"; otherwise, sentiment is "Negative"
var sentiment = result.PredictedLabel == 1 ? "Positive" : "Negative";
Console.WriteLine($"Text: {sampleData.Col0}\nSentiment: {sentiment}");