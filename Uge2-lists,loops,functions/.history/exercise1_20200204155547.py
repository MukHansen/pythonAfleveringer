from sys import argv
import csv
import platform
import argparse

def print_file_content(filename):
    with open(filename) as f_obj:
        content = f_obj.readlines()

        for line in content[:20]:
            print(line.strip().split(','))
    print("Done <----------->")

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
    print("whatever")
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
    if args.read_csv:
        read_csv(argv[2])

    if args.rwite_to_file:
        write_list_to_file(argv[2], argv[3:])

    if args.print_file:
        print_file_content(argv[2])

    if args.exercise1:
        print_file_content(filename)
    if args.exercise2:
        inputlist = argv[3:]
        write_list_to_file(filename,inputlist)
    if args.exercise3:
        read_csv(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--read_csv")
    parser.add_argument("--write_to_file")
    parser.add_argument("--print_file")
    args = parser.parse_args()
    run()