// See https://aka.ms/new-console-template for more information
using Azure.AI.OpenAI;
using Azure;
using Microsoft.Extensions.Configuration;

var builder = new ConfigurationBuilder().AddJsonFile($"appsettings.json", true, true);
var config = builder.Build();
var apiKey = config["AzureOpenAIApiKey"];

OpenAIClient client = new OpenAIClient(
        new Uri("https://azureopenaistudy.openai.azure.com/"),
        new AzureKeyCredential(apiKey));

string deploymentName = "gpt-35-turbo-20230808";
string prompt = "Tell us something about .NET development.";
Console.Write($"Input: {prompt}");

Response<Completions> completionsResponse = client.GetCompletions(deploymentName, prompt);
string completion = completionsResponse.Value.Choices[0].Text;

Console.WriteLine(completion);

Console.ReadLine();
