# Insert a cat logo on images bigger than 300x300
import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
ACCEPTED_FORMATS = ('.png', '.jpeg', '.gif', '.bmp')


logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not filename.lower().endswith(ACCEPTED_FORMATS) or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print(f'Resizing {filename}...')
        im = im.resize((width, height))

    # Add the logo if the image size is large enough for it to look good.
    new_width, new_height = im.size
    if logoWidth * 2 > new_width or logoHeight > new_height:
        print(f'the logo was not added to {filename} because its dimensions were too small!')
    else:        
        print(f'Adding logo to {filename}...')
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))