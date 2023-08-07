secret_key = 'YOUR_SECRET_KEY'

import openai
openai.api_key = secret_key

#print(openai.Model.list())

output = openai.Completion.create(
    model='gpt-3.5-turbo',
    prompt='Tell me a slogan',
    max_tokens=200,
    temperature=0,
)


print(output['choices'][0]['text'])
