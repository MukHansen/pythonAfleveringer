    # Create a python file with 3 functions:
import teams.csv as file    
def print_file_content(file):
    with open(file) as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)
        #that can print content of a csv file to the console
def write_list_to_file(output_file, lst):
    pass
        # that can take a list of tuple and write each element to a new line in file
        # rewrite the function so that it gets an arbitrary number of strings instead of a list
def read_csv(input_file):
    pass
    # that take a csv file and read each row into a list
    # Add a functionality so that the file can be called from cli with 2 arguments
    #     path to csv file
    #     an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
    # Add a --help cli argument to describe how the module is used