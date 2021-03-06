file = "./teams.csv"
from sys import argv
import csv
import platform

strings = argv[4:]
filename
def print_file_content(filename):
    with open(filename) as f_obj:
        content = f_obj.readlines()

        for line in content[:20]:
            print(line.strip().split(','))
    print("Done <----------->")

def write_list_to_file(filename, *lst):
    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open(filename, 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        for element in strings:
            output_writer.writerow([element])
        # that can take a list of tuple and write each element to a new line in file
        # rewrite the function so that it gets an arbitrary number of strings instead of a list


def read_csv(filename):
    lst = []
    with open(filename) as f_obj:
        content = f_obj.readlines()

        for line in content[:20]:
            lst.append(line.strip("\n"))
    # that take a csv file and read each row into a list
    # Add a functionality so that the file can be called from cli with 2 arguments
    #     path to csv file
    #     an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
    # Add a --help cli argument to describe how the module is used
    print(lst)

if __name__ == '__main__':
    globals()[argv[1]](argv[2], argv[3:])

print_file_content(argv[1])
write_list_to_file(argv[3], strings)
read_csv(argv[2])