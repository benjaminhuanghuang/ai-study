## Install / Update ML.NET CLI
```
    dotnet tool install -g mlnet
    
    dotnet tool update -g mlnet
```

## Create a new ML.NET project
```
    mlnet new -n <project_name> -o <output_folder>
```



## Regression
```
    mlnet regression --dataset data.csv --label-col price --train-time 10
```
```
