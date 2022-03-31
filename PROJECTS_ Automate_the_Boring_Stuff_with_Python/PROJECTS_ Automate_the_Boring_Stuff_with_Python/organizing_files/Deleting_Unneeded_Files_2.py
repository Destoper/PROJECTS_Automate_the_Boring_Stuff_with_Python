# scans your computer for large files and folders and then gives you the option to delete them or not.
import os, shutil
import pyinputplus as pyip
from pathlib import Path


class FindLargeFiles:
    '''walks through a folder and searches for exceptionally large files or folders to delete
    Args:
        directory (str): path of folder to walk
        requested_size (int): file size in mega bytes to possibly delete
    Returns:
        None
    '''

    def __init__(self, directory, requested_size=0):
        self.directory = directory
        self.requested_size = requested_size
        self.directories_to_delete = []
        self.files_to_delet = []

    def main(self):
        '''Calls the others fuctions and check conditionals'''        
        for element in os.listdir(self.directory):
            complet_path = os.path.join(self.directory, element)
            
            if os.path.isdir(complet_path):                      # Checking if it's directory
                tot_size = self.directory_size(complet_path)
                is_directory = True
            elif os.path.isfile(complet_path):                   # Checking if it's file
                tot_size = self.file_size(complet_path)
                is_directory = False

            greater = self.check_if_its_greater(tot_size)
            if greater:
                self.greater_printer(complet_path, is_directory)
                self.delet_list_appender(complet_path, is_directory)                                
        
        if self.files_to_delet or self.directories_to_delete:
            self.delet_choice()
        else:
            print(f'No files were found larger than {self.requested_size}MB!')
    
    def file_size(self, path):
        '''Checks indidual file size.'''
        total = os.path.getsize(path)
        return total

    def directory_size(self, path):
        '''Checks directory size.'''
        total = 0
        for folder_name, sub_folders, file_names in os.walk(path):  # Looping through the main directory      
            for file in file_names:                                 # Looping through all files in each directory inside the main one.   
                file_path = os.path.join(path, folder_name, file)
                try:
                    indidual_size = os.path.getsize(file_path)
                except FileNotFoundError:
                    indidual_size = 0
                total += indidual_size
        
        return total

    def check_if_its_greater(self, size):
        '''Checks if the file/folder size in greater than the size that the user requested'''
        self.mb_size = size / (1e+6)                                # turning bytes to Mega Bytes
        if self.mb_size >= self.requested_size:
            return True
        return False
    
    def greater_printer(self, complet_path, is_directory):
        '''Prints the infos about the files/directorys that are greater than the size that the user requested'''
        if is_directory:
            print(f'[DIRECTORY] - {complet_path} - SIZE: {self.mb_size:.2f}MB')
        else:
            print(f'[FILE] - {complet_path} - SIZE: {self.mb_size:.2f}MB')

    def delet_list_appender(self, complet_path, is_directory):      
        '''Appends greaters files to its respectives lists.'''
        if is_directory:
            self.directories_to_delete.append(complet_path)
        else:
            self.files_to_delet.append(complet_path)        

    def delet_choice(self):
        '''Gives user options for actions'''
        options_list = ['All', 'Files', 'Directories', 'Cancel']
        inp = pyip.inputMenu(options_list, prompt='\nEnter what you wanna DELET:\n')        
        if inp == 'All' and  self.directories_to_delete and self.files_to_delet:
            self.file_deleter()
            self.directory_deleter()
            self.message_end_delet()
        elif inp == 'Files' and self.files_to_delet:
            self.file_deleter()
            self.message_end_delet()
        elif inp == 'Directories' and self.directories_to_delete:
            self.directory_deleter()
            self.message_end_delet()
        elif inp == 'Cancel':
            print('\nYou chose not to delete any files or directories.')
        else:
            print('\nINVALID CHOICE!\n')
            self.delet_choice()
        print('\n')

    def file_deleter(self):
        '''Delet greaters files'''
        print('')
        for file in self.files_to_delet:
            print(f'DELETING FILE: {file}...')
            os.remove(file)

    def directory_deleter(self):
        '''Delet greaters directories'''
        print('')
        for directory in self.directories_to_delete:
            print(f'DELETING DIRECTORY: {directory}...')
            shutil.rmtree(directory)

    def message_end_delet(self):
        '''Prints a message after after all files has been deleted'''
        print('\nALL SELECTED FILES HAS BEEN DELETED!')

if __name__ == '__main__':           
    def directory_validator(dir):
        if os.path.isdir(dir):
            return dir
        else:
            raise Exception('Invalid Directory!')
   
    directory = pyip.inputCustom(directory_validator, prompt='Absolute Directory: ')
    size_mb = pyip.inputNum(limit = 3, prompt='Minimum size you want to search for [MB]: ') 
    run = FindLargeFiles(directory, size_mb)
    run.main()