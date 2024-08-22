import os
from subprocess import run
from pathlib import Path
"""
remember: the list names are jokes..
"""
listuspathus = []
listusfilus = []
listusnuhuh = []


reader_file = open('ausgabe_rekursion.txt', 'w', encoding="utf-8")
def reader(path):
    """

    Mainfunction
    """
    try:
        for i in os.listdir(path):
            if i in ('.', '..'):
                continue


            pathmaximus = os.path.join(path, i)

            if os.path.isdir(pathmaximus):
                listusfilus.append(i)
                reader(pathmaximus)
            if os.path.isfile(pathmaximus):
                listuspathus.append(i)


    except PermissionError:
        listusnuhuh.append(path)
        return

def get_file_size(path):
    # Dateigröße in Bytes abrufen

    size_bytes = os.path.getsize(path)

    # Größe in Kilobytes umwandeln
    size_kb = size_bytes / 1024

    # Größe auf 3 Dezimalstellen begrenzen
    size_kb_rounded = round(size_kb, 3)

    return size_kb_rounded
def scanner_printer(listobj, name=str):
    """

    Function for indv. printing
    """

    reader_file.write(f'{name} \n')
    for i in listobj:
        reader_file.write('{0:50} {1:50} {2:30}'.format(i, os.getcwd(), get_file_size(os.getcwd())) +'\n')

def scanner(path):
    """

    Funktion for main
    """
    reader(path)
    scanner_printer(listuspathus, 'Files:\n')
    scanner_printer(listusfilus,'\nFolders: \n')
    scanner_printer(listusnuhuh,  '\nPermissionErrors:\n')

def scanner_filter(path, typus:str):
    """

    Function for filtering spec. filetypes
    """
    reader(path)
    filter_list = []
    for i in listuspathus:
        if(str.__contains__(i,('.' + typus))):
            filter_list.append(i)
    scanner_printer(filter_list, 'Filtered Files:\n')

def scanner_programm(path, option):
    """

    MainFunction for main
    """
    if option == 1:
        scanner(path)
    if option == 2:
        filetype = input('What type of Files?')
        scanner_filter(path, filetype)
