import logging
import openai
import azure.functions as func
# sample request
# {"model": "text-davinci-003", "prompt": "give me a slogan for a cookie company", "max_tokens": 200, "temperature": 0}

secret_key = '***************'

def main(reg: func.HttpRequest) -> func.HttpResponse:
    logging. info('Python HTTP trigger function processed a request.')
    
    openai.api_key = secret_key

    req_body = reg.get_json()
    
    output = openai.Completion.create(
        model=req_body['model'],
        prompt=req_body['prompt'],
        max_tokens=req_body['max_tokens'],
        temperature=req_body['temperature']
    )


    out_text = output['choices'][0]['text']

    return func.HttpResponse(out_text, status_code=200)
