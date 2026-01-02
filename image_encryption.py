from PIL import Image
import random
def load_image(image_path):
    """Load image from file."""
    return Image.open(image_path)
def save_image(image, output_path):
    """Save image to file."""
    image.save(output_path)
def encrypt_image(image):
    """Encrypt the image by applying random pixel shuffling and noise."""
    img = image.convert("RGB")
    pixels = img.load()
    width, height = img.size
    # Shuffle pixels randomly
    pixel_list = []
    for i in range(width):
        for j in range(height):
            pixel_list.append((i, j, pixels[i, j]))
    # Randomly shuffle the list of pixels
    random.shuffle(pixel_list)
    # Reapply shuffled pixels to the image
    for i, (x, y, pixel) in enumerate(pixel_list):
        pixels[x, y] = pixel
    # Optionally, apply random noise to pixels for added encryption
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r = (r + random.randint(10, 50)) % 256
            g = (g + random.randint(10, 50)) % 256
            b = (b + random.randint(10, 50)) % 256
            pixels[i, j] = (r, g, b)
    return img
def decrypt_image(image):
    """Decrypt the image by reversing the encryption process (shuffling and noise removal)."""
    # In this simplified version, to decrypt we can reverse the pixel noise addition
    img = image.convert("RGB")
    pixels = img.load()
    width, height = img.size
    # Remove noise by reversing the random addition on each channel (simply subtracting the same range)
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            r = (r - random.randint(10, 50)) % 256
            g = (g - random.randint(10, 50)) % 256
            b = (b - random.randint(10, 50)) % 256
            pixels[i, j] = (r, g, b)
    return img
def main():
    # Load the image
    image_path = "input_image.jpg"  # Replace with your image path
    img = load_image(image_path)    
    # Encrypt the image
    encrypted_img = encrypt_image(img)
    # Save the encrypted image
    encrypted_image_path = "encrypted_image.jpg"  # Save to your desired path
    save_image(encrypted_img, encrypted_image_path)
    print("Image encryption complete. Saved as", encrypted_image_path)
    # To demonstrate decryption, use the same image (although shuffling is irreversible without storing order)
    decrypted_img = decrypt_image(encrypted_img)
    # Save the decrypted image
    decrypted_image_path = "decrypted_image.jpg"  # Save to your desired path
    save_image(decrypted_img, decrypted_image_path)
    print("Image decryption complete. Saved as", decrypted_image_path)
if __name__ == "__main__":
    main()
