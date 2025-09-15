from PIL import Image

# Define our ASCII character palette from dark to light
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def pixels_to_ascii(image):
    """Converts a grayscale image's pixels to an ASCII string."""
    pixels = image.getdata()
    characters = ""
    for pixel in pixels:
        # The formula maps the 0-255 pixel value to an index in our ASCII_CHARS list
        characters += ASCII_CHARS[pixel * (len(ASCII_CHARS) - 1) // 255]
    return characters

def main():
    # Make sure to change this to the actual name of your image file
    path = "test_image.jpg"
    new_width = 100

    try:
        image = Image.open(path)
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return

    # 1. Resize the image
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    resized_image = image.resize((new_width, new_height))

    # 2. Convert the image to grayscale
    grayscale_image = resized_image.convert("L")

    # 3. Convert grayscale pixels to ASCII characters
    ascii_characters = pixels_to_ascii(grayscale_image)
    
    # 4. Format and print the ASCII art
    pixel_count = len(ascii_characters)
    ascii_image = "\n".join(ascii_characters[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    print(ascii_image)

if __name__ == "__main__":
    main()