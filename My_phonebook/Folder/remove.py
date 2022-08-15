import view

import os
path = os.path.join('Folder', 'Phonebook.txt')

def read_data() -> list:
    with open (path, 'r') as f:        
        lines = f.readlines()
    return lines

def find_data_to_remove(search: str) -> str:       
    with open (path, 'r') as f:
        to_remove = ''        
        for line in f:
            if search in line:            
                view.view_data(line.replace(';', ' ').strip('\n').title())
                to_remove = line
    return to_remove

def remove_data(lines: str, to_remove: str):         
    with open (path, 'w') as f:        
        for line in lines:
            if line != to_remove:
                res = f.write(line)                 
    return res                   
        
                                                   
    