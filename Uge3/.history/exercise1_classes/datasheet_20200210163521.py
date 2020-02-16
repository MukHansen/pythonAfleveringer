import course

class DataSheet():
    def __init__(self, *courses):
        self.courses = course(*courses)
        
    def __repr__(self):
        return 'Course(%r )' % (self.courses)
    
    def __str__(self):
        return 'Courses {courses}'.format(
            courses=self.courses)