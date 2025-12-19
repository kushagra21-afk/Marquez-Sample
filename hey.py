import requests
import json

with open('open.json') as f:
    events = json.load(f)

for event in events:
    response = requests.post('http://localhost:9000/api/v1/lineage', 
                             json=event, 
                             headers={'Content-Type': 'application/json'})
    print(f"Event: {event['job']['name']}, Status: {response.status_code}, Response: {response.text}")



