import requests

API_URL = "https://cloud.flowiseai.com/api/v1/prediction/820b3033-28c5-453f-8e47-ee14b2287015"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()
    
output = query({
    "question": "Hey, how are you?",
})

print(output)