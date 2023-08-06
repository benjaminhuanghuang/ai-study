

Setup
```
pip install openai
```


## Azure Function
In VS code + Azure Functions extension
Select Function App

Create function
```
Select Workspace > Select Create Function(the flash icon)
```

Add dependencies in requirements.txt
```
openai
```

Add code in __init__.py
```
req_body = req.get_json()

model=req_body.get('model')
prompt=req_body.get('prompt')

```

Deploy
```
Select Workspace > Select Create Function(the flash icon) > Deploy to Function App
```

Test
```
https://openaistudyfunciton.azurewebsites.net/api/basicOpenAI?name=teeeeeee
```
