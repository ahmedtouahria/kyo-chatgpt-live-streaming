
def chatGPT_connect(token, query):
    import requests
    url = "https://api.deepai.org/api/chatbot"
    headers = {
        'api-key': token
    }
    response = requests.post(url, headers=headers, data={
        'text': query
    })
    return response.json()['output']

def chatGPT_interact(token, query):
    # make a request to the chatGPT api
    response = chatGPT_connect(token, query)
    # call the function again with the user's response
    output = chatGPT_interact(token, response)
    return output