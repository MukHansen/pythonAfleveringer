from sys import argv
import csv
import platform
import argparse
import os.path
from os import path
from exercise1 import write_list_to_file


def files_in_folder(foldername, filename):
    write_list_to_file(filename, os.listdir(foldername))

def second_function(foldername, filename):
    lst = os.listdir() 




files_in_folder(argv[1], argv[2])
