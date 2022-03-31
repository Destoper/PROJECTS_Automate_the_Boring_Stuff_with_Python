# Reads all the Excel files in the current working directory and outputs them as CSV files

import csv, os, openpyxl

os.makedirs('excel_to_CSV', exist_ok=True)

def excel_to_csv(excel_filename):
    # turn a excel file to csv
    wb = openpyxl.load_workbook(excel_filename)     # open Excel file
    sheets_list = wb.sheetnames         # getting a list of sheets' names from the current file

    for item in sheets_list:
        print(f'Saving {item} sheet from {excel_filename} as CSV!')
        sheet = wb[item]
        
        file_basename = '.'.join(excel_filename.split('.')[:-1])        # removing .xlsx from file name
        file_savename = f'{file_basename}_{item}.csv'       # joining filename with the specific sheet name 

        output_csv = open(os.path.join('excel_to_CSV', file_savename), 'w',
                    newline='')                                             # opening the file to be saved as CSV
        output_writer = csv.writer(output_csv)      # making a writer CSV object
        
        for row in range(1, sheet.max_row+1):       # looping through each Excel sheet's row and write it down on CSV file
            row_content = []
            
            for column in range(1, sheet.max_column+1):
                cell_value = sheet.cell(row=row, column=column).value
                row_content.append(cell_value)          
            output_writer.writerow(row_content)
    
        output_csv.close()          # Closing file




# Loop through every file in the current working directory 
#   and search for Excel files
flag = False
for excel_filename in os.listdir('.'):
    if excel_filename.endswith('.xlsx'):
        print(f'\nEXCEL FOUND: {excel_filename}')
        excel_to_csv(excel_filename)
        flag = True

if flag == False:
    print('No Excel File was found on current working directory!')