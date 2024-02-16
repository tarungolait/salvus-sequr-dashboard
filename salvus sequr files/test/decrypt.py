from Crypto.Cipher import AES
import base64

def decrypt_aes(ciphertext, key, iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = aes.decrypt(ciphertext)
    return decrypted_bytes.rstrip(b'\x10')  # Remove padding

def main():
    encrypted_string = input("Enter the encrypted string: ").strip()

    # Convert the base64 encoded string to bytes
    ciphertext = base64.b64decode(encrypted_string)

    # Define key and IV
    key = 'helloworldhelloo'.encode('utf-8')  # encryption key
    iv = 'helloworldhelloo'.encode('utf-8')   # initialization vector (IV)

    # Decrypt the ciphertext
    decrypted_bytes = decrypt_aes(ciphertext, key, iv)

    # Convert the decrypted bytes to a string
    decrypted_string = decrypted_bytes.decode('utf-8')

    print("Decrypted string:", decrypted_string)

if __name__ == "__main__":
    main()
