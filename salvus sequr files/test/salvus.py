import requests
import json

# Define the URL of your Flask application
url = 'http://127.0.0.1:5000/decrypt'

# Example encrypted data (replace with your actual encrypted data)
encrypted_data = "b3LkhZQcQkwVleSEUM1VNg+kEGT0d/+5X3h0f04Gem8HY4k0DJfwqRYx+QJ6DSqfS1wWTuMCPwSl3kujYUdFgA=="

# Create a dictionary with the encrypted data
data = {'encrypted_data': encrypted_data}

# Send a POST request to the /decrypt endpoint
response = requests.post(url, json=data)

# Print the response from the server
print(response.json())
