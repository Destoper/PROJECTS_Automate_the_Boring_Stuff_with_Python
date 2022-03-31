# searches for file with .pdf extension
#   then copy them to a destination folder

import os, shutil
from pathlib import Path

p = Path.home()
folder = f'{p}/Downloads'
destination_folder = f'{p}/Documentos'

for foldername, subfolders, filenames in os.walk(folder):    
    for filename in filenames:            
            if filename.endswith('.pdf'):
                print(f'COPING: {filename} TO {destination_folder}...')                
                absWorkingDir = os.path.abspath(f'{foldername}')
                final_path = f'{absWorkingDir}/{filename}'
                shutil.copy(final_path, destination_folder)


