# Find directories that have photos in it. (size must be more than 500x500)
import os
from pathlib import Path
from PIL import Image

ACCEPTED_FORMATS = ('.png', '.jpeg')
HOME = str(Path.home())
MINIMUM_PICTURES_SIZE = 500 

for folder_name, sub_folder, filenames in os.walk('/home/marcio/Downloads'):    
    num_photo_files = 0
    num_non_photo_files = 0

    for filename in filenames:
        full_path = os.path.join(folder_name, filename)
        # Check if file extension it's not in ACCEPTED_FORMATS
        if not filename.endswith(ACCEPTED_FORMATS):
            num_non_photo_files += 1
            continue    # Skip to next file
        
        # Try to open image
        try:
            img = Image.open(full_path)            
        except FileNotFoundError:
            print(f'Error to open {filename}')
            continue    # Skip to next file
        else:
            img_width, img_height = img.size

        # Check if width and height are larger than MINIMUM_PICTURES_SIZE
        if img_width > MINIMUM_PICTURES_SIZE and img_height > MINIMUM_PICTURES_SIZE:
            num_photo_files += 1
        else:
            num_non_photo_files += 1

    # Print photo directories
    if num_photo_files >= num_non_photo_files:
        print(f'PHOTO DIRECTORY: {os.path.join(folder_name)}')
    