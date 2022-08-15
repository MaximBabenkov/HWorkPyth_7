import os
path = os.path.join('Folder', 'Phonebook.txt')

def add_data(data: str):
    with open (path, 'a') as f:      
        res = f.writelines(f'{data}\n')
    return res
