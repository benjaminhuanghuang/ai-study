![](./data.png)

```
    mkdir data/raw
    
    mkdir dataset/img
    mkdir dataset/json

```
Copy all data into data/raw
Covert all data into dataset/img and dataset/json

```
    mkdir node
```
Create folder for nodejs project

generate samples.json
```
    [
        {"id":1,"label":"car","student_name":"Radu","student_id":1663053145814},
        ...
    ]
```

Install canvas in nodejs environment
```
    npm i


    const { createCanvas } = require("canvas")
```

Create folder used for communication between nodejs app with web app
```
    mkdir common/js_objects
```


Process data
```
    node i 
    or
    node process_data.js
```
