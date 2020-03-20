from sys import argv
import csv
import platform
import argparse
import os.path
from os import path
utils = import './utils.py'

def print_file_content(filename):
    with open(filename) as f_obj:
        content = f_obj.readlines()

        for line in content[:20]:
            print(line.strip().split(','))
    print("Done <----------->")

# def write_list_to_file(filename, *lst):
def write_list_to_file(filename, lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open(filename, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        for element in lst :
            output_writer.writerow([element])
        # that can take a list of tuple and write each element to a new line in file
        # rewrite the function so that it gets an arbitrary number of strings instead of a list


def read_csv(filename):
    with open(filename) as f_obj:
        content = f_obj.readlines()

        for line in content[:20]:
            print(line.rstrip())
    # that take a csv file and read each row into a list
    # Add a functionality so that the file can be called from cli with 2 arguments
    #     path to csv file
    #     an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
    # Add a --help cli argument to describe how the module is used
def run():
    if argv[1] == "read_csv" :
        read_csv(argv[2])

    if argv[1] == "write_list_to_file" :
        write_list_to_file(argv[2], argv[3:])

    if argv[1] == "print_file_content" :
        print_file_content(argv[2])

def run2():
    if args.read_csv:
        read_csv(argv[2])

    if args.write_to_file:
        write_list_to_file(argv[2], argv[3:])

    if args.print_file:
        print_file_content(argv[2])

    if args.file:
        if path.exists(argv[2]):
            write_list_to_file(argv[2], argv[3:])
        else:
            print("File not found", argv[2])
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Module to read/write files")
    parser.add_argument("--read_csv", help="prints chosen .csv file")
    parser.add_argument("--write_to_file", nargs="*", help="write list to file")
    parser.add_argument("--print_file", help="reads file and prints a list in console")
    parser.add_argument("--file", nargs="*", help="will write input in console, if file cannot be found")
    args = parser.parse_args()
    # run()
    run2()