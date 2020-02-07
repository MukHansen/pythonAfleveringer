from sys import argv
import csv
import platform
import argparse
import os.path
from os import path
from exercise1 import write_list_to_file


def files_in_folder(foldername, filename):
    write_list_to_file(filename, os.listdir(foldername))

lst = []
def second_function(foldername):
    entries = os.listdir(folderpath)
    for entry in entries:
        if os.path.isdir(entry)
            second_function(entry)
        else:
            lst.append(entry)
    
    




files_in_folder(argv[1], argv[2])
