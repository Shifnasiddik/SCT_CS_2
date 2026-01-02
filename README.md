# Image Encryption Tool Using Pixel Manipulation

## Project Overview:
This project is a simple tool for encrypting and decrypting images through pixel manipulation techniques. The tool applies operations like swapping pixel values and performing basic mathematical transformations on RGB values. The process encrypts the image by scrambling pixel data and allows decryption by reversing the applied operations.  
By utilizing these pixel manipulation techniques, this tool demonstrates the basics of image encryption, focusing on beginner-friendly concepts and Python programming.

## Features:
1. **Encrypt images using pixel manipulation**:
    - **Pixel swapping**: Swap pixels in pairs to obscure image data.
    - **Mathematical operations**: Apply operations like addition or XOR to the RGB values of each pixel.
    - **Randomization**: Use random shifts in pixel values to add unpredictability to the encryption.
2. **Decryption**: Restore the original image by reversing the encryption steps.
3. **Simple implementation**: The code is beginner-friendly, using Python’s **Pillow (PIL)** library for image processing.
4. **Customizable**: Modify pixel manipulation techniques for more advanced encryption methods.

## How to Use

### Encrypt an Image:
1. Download or create an image file.
2. Replace the image path in the Python script:
   image_path = "input_image.jpg"  # Replace with your image path
3.Run the Python script to encrypt the image:
   python image_encryption.py
4.The encrypted image will be saved as encrypted_image.jpg.

### Decrypt an Image:
To decrypt the image, reverse the encryption operations by swapping the pixels back and undoing the mathematical operation. Refer to the decryption code in the repository for more details.
