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
fileslst = []
def all_files_in_folder_recursiv(foldername):
    entries = os.listdir(foldername)
    for entry in entries:
        if os.path.isdir(entry):
            all_files_in_folder_recursiv(entry)
        else:
            lst.append(entry)
    
    write_list_to_file(argv[2], lst)

def print_first_line_in_file(foldername):
    entries = os.listdir(foldername)
    for entry in entries:
        if os.path.isfile(entry):
            with open(entry) as f_obj:
                content = f_obj.readline()
                print(content)
    
def fourth(foldername):
    with open(foldername) as f_obj:
        content = f_obj.readlines()
        for line in content:
            if '@' in line:
                print(line)

# fifth takes a list of md files and writes all headlines 
# (lines starting with #) to a file Make sure your module 
# can be called both from cli and imported to another module 
# Create a new module that imports utils.py and test each function.


def fifth():
fourth(argv[1])
third(argv[1])
all_files_in_folder_recursiv(argv[1])
files_in_folder(argv[1], argv[2])
