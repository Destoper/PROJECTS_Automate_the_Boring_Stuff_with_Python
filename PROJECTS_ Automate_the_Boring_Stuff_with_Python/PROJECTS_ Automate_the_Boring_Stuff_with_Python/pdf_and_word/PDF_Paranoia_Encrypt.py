# Find all PDF files on a directory and try to encripty it
import PyPDF2, os, sys
from PyPDF2.utils import PdfReadError
from pathlib import Path

def create_save_dir():
    home = str(Path.home())
    os.makedirs(os.path.join(home, 'Encrypted_PDF'), exist_ok=True) 

def encrypt_and_delete(pdf_file, num, base_name):    
    
    dir = str(Path.home())
    full_path = os.path.join(dir, 'Encrypted_PDF', f'[ENCRYPTED]{base_name}')
    
    # Create PdfFileWriter object
    filewriter = PyPDF2.PdfFileWriter()

    # Copy pdf pages to filewriter object    
    for index in range(num):        
        page = file.getPage(index)   
        filewriter.addPage(page)

    # Encrypting filewriter object
    print(f'\nENCRYPTING: {base_name}...')
    filewriter.encrypt(pw)
        
    # Write encrypted filewriter object as pdf file
    with open(full_path, "wb") as f:  
        filewriter.write(f)    
    print(f'Encrypted File save: {full_path}')

    # Deleting Original File
    print(f'Deleting Original File: {base_name}')
    os.remove(original_pdf) 

if len(sys.argv) < 2:
    print('Usage: PDF_Paranoia_Encrypt.py PASSWORD')
    sys.exit()
pw = sys.argv[1]

encrypted = 0
create_save_dir()
# Find PDF files
pdf_files = []
for directory, subfolder, files in os.walk('.'):
    for file in files:
        if file.endswith(".pdf"):
            pdf_files.append(os.path.join(directory, file))
            print(f'PDF FOUND: {file}...')

# Encrypting files
for original_pdf in pdf_files:
    base_name = os.path.basename(original_pdf)    
    try:
        file = PyPDF2.PdfFileReader(original_pdf)
        num = file.numPages
    except PdfReadError:
        print(f'\nCould NOT read the file:  {base_name}...')
    else:
        encrypt_and_delete(file, num, base_name)
        encrypted += 1

print(f'\nENCRYPTED FILES: {encrypted}')