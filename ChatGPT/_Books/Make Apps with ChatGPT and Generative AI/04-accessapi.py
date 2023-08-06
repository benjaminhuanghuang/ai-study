secret_key = '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'

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
