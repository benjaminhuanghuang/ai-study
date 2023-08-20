
## Setup Azure OpenAI service
1. Create Azure OpenAI Workspace
Azure OpenAI -> Create

2. Deploy a model
Select the created workspace 
Resource Management  ->  Model Deployments

Or go to Azure OpenAI Studio -> Models select a model and deploy it



3. Get the endpoint and key
Resource Management  ->  Keys and Endpoint


## Create a .NET application
```
    mkdir HelloWorld
    cd HelloWorld
    dotnet new console --framework net7.0

    dotnet add package Azure.AI.OpenAI --version 1.0.0-beta.6
    dotnet run
```

   
