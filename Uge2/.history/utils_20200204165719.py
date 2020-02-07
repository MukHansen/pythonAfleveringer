from sys import argv
import csv
import platform
import argparse
import os.path
from os import path

def files_in_folder(foldername, lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open(foldername, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        for element in lst :
            output_writer.writerow([element])