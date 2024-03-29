from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

# Ciphertext to decrypt
ciphertext = "wb89ne2VEkuDGDKJuORnFgz4PuRh1wRiXDlqECQgSiYEQIgSv8SxK0JWHNLb6ihPbDdYMfqfbPMDQibHleU2pQ=="

# Key and IV used for encryption (must match the ones used for encryption)
key = 'helloworldhelloo'.encode('utf-8')
iv = 'helloworldhelloo'.encode('utf-8')

# Decode ciphertext from base64
decoded_ciphertext = base64.b64decode(ciphertext)

# Create AES cipher object in decryption mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt ciphertext and remove padding
plaintext = unpad(cipher.decrypt(decoded_ciphertext), AES.block_size)

# Convert plaintext bytes to string
decrypted_data = plaintext.decode('utf-8')

print("Decrypted data:", decrypted_data)
