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
