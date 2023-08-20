```
    pip install azureml-sdk   # V1

    pip install azure-ai-ml   # V2
```


```
    from azureml.core import Workspace

    ws = Workspace.from_config()
    for computer_name in ws.computer_targets:
        computer = ws.computer_targets[computer_name]
        print(computer.name, ":", computer.type)
```


