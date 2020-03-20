file = "./teams.csv"
from sys import argv
import csv
import platform

output_file = argv[2]
thistuple = ("apple", "banana", "cherry", "orange")
def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()

        for line in content[:20]:
            print(line.strip().split(','))
        #that can print content of a csv file to the console


def write_list_to_file(output_file):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open(output_file, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        for fruit in thistuple:
            output_writer.writerow([fruit])

        # output_writer.writerow(['2015', '1', '0', '5100', '614,5'])
        # output_writer.writerow(['2015', '1', '0', '5104', '2,3'])
        # output_writer.writerow(['2015', '1', '0', '5106', '1'])
        # output_writer.writerow(['2015', '1', '0', '5110', '1'])
        # that can take a list of tuple and write each element to a new line in file
        # rewrite the function so that it gets an arbitrary number of strings instead of a list


def read_csv(input_file):
    pass
    # that take a csv file and read each row into a list
    # Add a functionality so that the file can be called from cli with 2 arguments
    #     path to csv file
    #     an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
    # Add a --help cli argument to describe how the module is used

print_file_content(argv[1])
write_list_to_file(argv[2])