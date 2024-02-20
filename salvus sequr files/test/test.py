import requests
import base64

# URL of your Flask application endpoints
post_url = 'http://localhost:5000/post'
update_url = 'http://localhost:5000/update_qr_data'

# Example encrypted QR data
encrypted_data = 'b3LkhZQcQkwVleSEUM1VNkgWv3ORtvD68Dpppbyl3mVZNavLY+EuczQzooDt0gMoftGNCz9YJqUw9vIaWmMwTw=='

# Decode the base64 encoded encrypted data
decoded_data = base64.b64decode(encrypted_data)

# JSON payload for POST request to /post endpoint
post_payload = {'QRcode': base64.b64encode(decoded_data).decode('utf-8')}  # Encode the decoded binary data back to base64

# Send POST request to /post endpoint
post_response = requests.post(post_url, json=post_payload)

# Check the response status code for /post endpoint
if post_response.status_code == 200:
    # Print the JSON response for /post endpoint
    print("Response from /post endpoint:")
    print(post_response.json())
else:
    print('Error:', post_response.status_code)

# Example user data for updating QR code data
user_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone_number": "1234567890",
    "device_id": "device123",
    "device_type": "TypeXYZ",
    "service_provider_data": "Service Provider XYZ",
    "location_data": "Location XYZ",
    "qr_code": "your_qr_code_here"  
}

# Send POST request to /update_qr_data endpoint
update_response = requests.post(update_url, json=user_data)

# Check the response status code for /update_qr_data endpoint
if update_response.status_code == 200:
    # Print the JSON response for /update_qr_data endpoint
    print("\nResponse from /update_qr_data endpoint:")
    print(update_response.json())
else:
    print('Error:', update_response.status_code)
