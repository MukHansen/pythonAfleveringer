
class Couse():
    def __init__(self, *courses):
        self.courses = courses
        
    def __repr__(self):
        return 'Course(%r )' % (self.courses)
    
    def __str__(self):
        return 'Courses {courses}'(
            courses=self.courses)