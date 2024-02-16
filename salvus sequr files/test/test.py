import requests
import base64

# URL of your Flask application endpoint
url = 'http://localhost:5000/post'

# Example encrypted QR data
encrypted_data = 'b3LkhZQcQkwVleSEUM1VNkgWv3ORtvD68Dpppbyl3mVZNavLY+EuczQzooDt0gMoftGNCz9YJqUw9vIaWmMwTw=='

# Decode the base64 encoded encrypted data
decoded_data = base64.b64decode(encrypted_data)

# JSON payload to send in the POST request
payload = {'QRcode': base64.b64encode(decoded_data).decode('utf-8')}  # Encode the decoded binary data back to base64

# Send POST request to the Flask application endpoint
response = requests.post(url, json=payload)

# Check the response status code
if response.status_code == 200:
    # Print the JSON response
    print(response.json())
else:
    print('Error:', response.status_code)
