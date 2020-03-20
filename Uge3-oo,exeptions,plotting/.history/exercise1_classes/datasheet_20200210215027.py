from course import Course

class DataSheet():
    def __init__(self, courses=[]):
        self.courses = courses
        
    def __repr__(self):
        return 'Course(%r )' % (self.courses)
    
    def __str__(self):
        return 'Courses {courses}'.format(
            courses=self.courses)
    
    def get_grades_as_list(self):
        pass

    def get_avg_grade(self):
        pass
