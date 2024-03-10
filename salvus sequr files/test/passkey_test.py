import requests

# Define the base URL of the Flask app
BASE_URL = 'http://127.0.0.1:5000'

# Test the /decrypt endpoint
def test_decrypt_endpoint():
    url = BASE_URL + '/decrypt'
    encrypted_data = "b3LkhZQcQkwVleSEUM1VNg+kEGT0d/+5X3h0f04Gem8HY4k0DJfwqRYx+QJ6DSqfS1wWTuMCPwSl3kujYUdFgA=="  # Replace with actual encrypted data
    response = requests.post(url, json={'encrypted_data': encrypted_data})
    print("Decrypt Endpoint Response:")
    print(response.json())

# Test the /insert_data endpoint
def test_insert_data_endpoint():
    url = BASE_URL + '/insert_data'
    data = {
        'device_id': '123',
        'barcodeno': '6265101617',
        'qrcode': '8827',
        'name': 'Johny',
        'last_name': 'Doee',
        'phone': '12345678940',
        'email': 'johen.doe@example.com'
    }
    response = requests.post(url, json=data)
    print("Insert Data Endpoint Response:")
    print(response.json())

if __name__ == '__main__':
    test_decrypt_endpoint()
    test_insert_data_endpoint()
