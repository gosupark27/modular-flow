import requests

url = "http://localhost:8000/mirror-log/"
payload = {
    "user_id": "seth_001",
    "name": "Seth",
    "selected_option": "B",
    "prompt_text": "What’s something you understand deeply but find hard to explain to most people?",
    "flame_role_inference": "Silent Observer"
}

response = requests.post(url, json=payload)
print("Status:", response.status_code)
print("Response:", response.json())
