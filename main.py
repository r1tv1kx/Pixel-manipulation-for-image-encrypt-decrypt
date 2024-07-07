from PIL import Image
import numpy as np

# Function to encrypt an image
def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Apply a simple encryption algorithm (e.g., adding a key value to each pixel)
    encrypted_array = (img_array + key) % 256
    
    # Convert encrypted array back to image
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    # Save the encrypted image
    encrypted_img.save(output_image_path)
    print(f"Image encrypted and saved as {output_image_path}")

# Function to decrypt an image
def decrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Apply the reverse of the encryption algorithm (e.g., subtracting the key value from each pixel)
    decrypted_array = (img_array - key) % 256
    
    # Convert decrypted array back to image
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    # Save the decrypted image
    decrypted_img.save(output_image_path)
    print(f"Image decrypted and saved as {output_image_path}")

# Paths to input and output images
input_image_path = 'images/input_image.png'
encrypted_image_path = 'images/encrypted_image.png'
decrypted_image_path = 'images/decrypted_image.png'

# Key for encryption/decryption
encryption_key = 50

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, encryption_key)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key)
