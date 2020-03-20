from mypackage.exercise1_classes.student import Student
# from mypackage.exercise1_classes.student import Student
# from mypackage.exercise1_classes.datasheet import DataSheet
from mypackage.exercise1_classes.course import Course
import sys


print('__file__:{}\n__name__:{}\n__package__:{}\n'.format(__file__,__name__,str(__package__)))



def testing():
    print('yoyo')

if __name__ == '__main__':
    testing()
    print('arguments given to program from cli:',sys.argv[1:])
