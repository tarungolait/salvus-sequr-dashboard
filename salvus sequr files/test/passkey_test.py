import requests

# Define the Flask API endpoint
API_ENDPOINT = 'http://localhost:5000/userdetail'

# Sample JSON request data
sample_data = {
    "Name": "John",
    "Lastname": "Doe",
    "Email": "john.doe@example.com",
    "phone": "1234567890",
    "device_id": "123456789",
    "barcodeno": "987654321",
    "Product": "ExampleProduct"
}

# Send POST request to the API endpoint with the sample data
response = requests.post(API_ENDPOINT, json=sample_data)

# Check if the request was successful
if response.status_code == 200:
    # Extract passkey from the response JSON
    passkey = response.json().get('passkey')
    if passkey:
        print("Generated Passkey:", passkey)
    else:
        print("Passkey not found in response JSON.")
else:
    print("Failed to send request. Status Code:", response.status_code)
