print('__file__:{}\n__name__:{}\n__package__:{}\n'.format(__file__,__name__,str(__package__)))

from exercise1_classes.student import Student
from exercise1_classes.datasheet import DataSheet
from exercise1_classes.course import Course
import sys

def testing():
    mod2.print_name('hul igennem')

if __name__ == '__main__':
    testing()
    print('arguments given to program from cli:',sys.argv[1:])
