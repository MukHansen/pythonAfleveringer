from sys import argv
import csv
import platform
import argparse
import os.path
from os import path
from exercise1 import write_list_to_file

def files_in_folder(foldername):
    lst = []
    with open(foldername) as f_obj:
        content = f_obj.readlines()

        for line in content[:20]:
            lst.append(line)
