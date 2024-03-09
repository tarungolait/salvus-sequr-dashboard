import requests
import json

url = "http://localhost:5000/post"  # Adjust URL if needed
data = {
    "QRcode": "b3LkhZQcQkwVleSEUM1VNg+kEGT0d/+5X3h0f04Gem8HY4k0DJfwqRYx+QJ6DSqfS1wWTuMCPwSl3kujYUdFgA=="
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print("API Response:")
    print(response.json())
else:
    print("Error:", response.status_code)
