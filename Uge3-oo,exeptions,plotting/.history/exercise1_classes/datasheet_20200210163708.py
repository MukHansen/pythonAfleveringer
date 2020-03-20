import Course

class DataSheet():
    def __init__(self, *Courses):
        self.courses = Course(*Courses)
        
    def __repr__(self):
        return 'Course(%r )' % (self.courses)
    
    def __str__(self):
        return 'Courses {courses}'.format(
            courses=self.courses)