# Build a Full-Stack Apps Using React, Node.js, Express and ChatGPT API
Natural Language to SQL Query Converter

https://morioh.com/p/e8979a61f921?f=60c59d87cb33627fbcc0a0f3

https://www.youtube.com/watch?v=kjUSOa_KOts&t=153

https://github.com/alejandro-ao/openai-sql-generator  

React + Node.js + Express + ChatGPT API


## Create client project
```     
npm create vite@latest
? Project name: client
? Select a framework: React
? Select a variant: JavaScript

cd client
npm i
npm run dev
```
delete App.css and index.css


https://beta.openai.com/docs/developer-quickstart/overview
Quickstart > Build your application
Copy index.module.css

Copy icon from flaticon.com

Create UI

##  OpenAI API access
https://platform.openai.com/
Personal > View API keys

Create a key and put it in .env file


## Create backend project
```
cd server
npm init -y

npm i openai dotenv express cors
```
setup OpenAI client in api.js


create own apis in the index.js
```
cd server
npm i express cors
```

## generate SQL query
