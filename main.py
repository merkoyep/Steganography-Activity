"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://tech-at-du.github.io/ACS-3230-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# : Run `pip3 install Pillow` before running the code.
from PIL import Image, ImageDraw, ImageFont


def decode_image(path_to_png):
    """
    Add docstring and complete implementation.
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    # Using the variables declared above, replace `print(red_channel)` with a complete implementation:

    for x in range(x_size):
        for y in range(y_size):
            red_pixel = red_channel.getpixel((x, y))
            bit = red_pixel & 1
            if bit == 0:
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = (255, 255, 255)
 # Start coding here!

    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")


def encode_image(path_to_png, binary_image_path):
    """
    TODO: Add docstring and complete implementation.
    """
    original_image = Image.open(path_to_png)
    binary_image = Image.open(binary_image_path).convert("1")
    binary_image = binary_image.resize(original_image.size)

    pixels = original_image.load()
    binary_pixels = binary_image.load()

    x_size, y_size = original_image.size

    for x in range(x_size):
        for y in range(y_size):
            red, green, blue = pixels[x, y]

            # Binary image pixel (0: black, 1: white)
            bit_to_embed = 1 if binary_pixels[x, y] == 255 else 0

            # Modify the LSB of the red channel
            red = (red & ~1) | bit_to_embed
            pixels[x, y] = (red, green, blue)

    original_image.save("encoded_image.png")
    print("Secret text has been encoded into encoded_image.png")


def write_text(text_to_write, binary_image_path):
    """
    TODO: Add docstring and complete implementation.
    """
    font_size = 20
    width = 300
    height = 100
    background_color = (0, 0, 0)  
    text_color = (255, 255, 255)  

    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()  

    text_bbox = draw.textbbox((0, 0), text_to_write, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Draw the white text onto the black background
    draw.text((text_x, text_y), text_to_write, fill=text_color, font=font)

    image.save(binary_image_path)
    print(f"Text image saved as '{binary_image_path}'")
    return binary_image_path



decode_image("encoded_image.png")


