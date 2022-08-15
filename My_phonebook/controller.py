import view
from Folder import add, remove, search

import os
path = os.path.join('Folder', 'Phonebook.txt')

def button_click():
    view.view_data('Phone book')    
    while True:
        action = view.input_data('Press "a" to add contact, "s" to search contact, "r" to remove contact: ' )
        if action == 'a' or 's' or 'r':
            match action:                     
                case 'a':            
                    my_data = ''
                    surname = view.input_data('Enter a surname: ').lower()
                    name = view.input_data('Enter a name: ').lower()
                    numb = view.input_data('Enter a phone number: ')
                    descr = view.input_data('Enter a description: ')
                    my_data = surname + ";" + name + ";" + numb + ";" + descr
                    my_res = add.add_data(my_data)
                    view.view_data('This contact is added')
                    break

                case 's':
                    while True:
                        to_find = view.input_data('Enter surname to search: ').lower()
                        my_res = search.search_data(to_find)
                        if my_res != '':
                            view.view_data(my_res)
                            break                        
                        else:
                            view.view_data('Not found! Try again')
                            continue                                                       
                    break

                case 'r':
                    my_lines = remove.read_data()
                    while True:
                        my_search = view.input_data('Enter surname to remove: ').lower()
                        my_to_remove = remove.find_data_to_remove(my_search)
                        if my_to_remove != '':
                            break                        
                        else:
                            view.view_data('Not found! Try again')
                            continue   
                    while True:
                        confirm = view.input_data('Press "c" to confirm the removal: ')
                        if confirm != 'c':
                            view.view_data('Error! Try again')
                            continue
                        else:           
                            my_res = remove.remove_data(my_lines, my_to_remove)
                            view.view_data('This contact is removed')
                            break
                    break
        else:
            view.view_data('Error! Try again')
            continue
       
   
        
