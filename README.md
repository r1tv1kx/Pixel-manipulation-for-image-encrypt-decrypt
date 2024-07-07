Pixel Image Encryption
This repository contains a simple image encryption and decryption tool using pixel manipulation techniques implemented in Python. The tool utilizes the Pillow and NumPy libraries to perform basic encryption by modifying pixel values. Users can encrypt an image by adding a constant value to each pixel and decrypt it by reversing the process.

Features:
Encrypt images by modifying pixel values.
Decrypt images to restore the original content.
Simple implementation using Python and the Pillow library.

Requirements:
Python 3.x
Pillow library
NumPy library

You can install the required libraries using pip:
pip install pillow numpy

Usage:

Encrypting an Image:
Place your input image in the repository directory.
Update the input_image_path, encrypted_image_path, and encryption_key variables in the script.
Run the encryption script.

Decrypting an Image:
Ensure you have the encrypted image.
Update the input_image_path, decrypted_image_path, and encryption_key variables in the script.
Run the decryption script.
