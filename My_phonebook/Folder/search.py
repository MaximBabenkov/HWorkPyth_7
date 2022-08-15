import os
path = os.path.join('Folder', 'Phonebook.txt')

def search_data(search: str) -> str:    
    with open (path, 'r') as f: 
        res = ''
        for line in f:
            if search in line:
                res = line.replace(';', ' ').strip('\n').title()              
    return res
        