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
    
def print_lines_containing_email(foldername):
    with open(foldername) as f_obj:
        content = f_obj.readlines()
        for line in content:
            if '@' in line:
                print(line)

# fifth takes a list of md files and writes all headlines 
# (lines starting with #) to a file Make sure your module 
# can be called both from cli and imported to another module 
# Create a new module that imports utils.py and test each function.

def print_lines_with_markdown(*files):
    for file in files:
        for ele in file:
            with open(ele) as f_obj:
                content = f_obj.readlines()
            for line in content:
                if '#' in line:
                    lst.append(line.strip(','))
    write_list_to_file('writeMarkdownToMe.md', lst)


# print_lines_with_markdown(argv[1:])
# print_lines_containing_email(argv[1])
# print_first_line_in_file(argv[1])
# all_files_in_folder_recursiv(argv[1])
# files_in_folder(argv[1], argv[2])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Homemade handler of files")
    parser.add_argument("--write_filenames_to_file", nargs='', help="Write filenames to file")
    parser.add_argument("--write_filenames_to_file_recursively", nargs='', help="Write filenames and folders to file")
    parser.add_argument("--read_first_line_from_files", nargs='', help="Reads first line from file")
    parser.add_argument("--print_lines_with_email", nargs='', help="Prints lines which contain an email / @")
    parser.add_argument("--print_lines_with_markdown", nargs='*', help="Prints lines which contain a # / is a MD")
    args = parser.parse_args()

    if args.all_files_in_folder_recursiv:
        path = argv[2]
        all_files_in_folder_recursiv(path)

    if args.files_in_folder:
        filename = argv[2]
        path = argv[3]
        files_in_folder(filename,path)

    if args.print_first_line_in_file:
        files = argv[2:]
        print_first_line_in_file(files)

    if args.print_lines_containing_email:
        files = argv[2:]
        print_lines_containing_email(files)

    if args.print_lines_with_markdown:
        files = argv[2:]
        print_lines_with_markdown(files)