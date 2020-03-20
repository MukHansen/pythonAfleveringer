from mypackage.exercise1_classes.course import Course

class DataSheet():
        def init(self, courses):
            self.courses = []
            for course in courses:
                new_course = Course(course.name, course.classroom, course.teacher, course.ETCS, course.grade)
                self.courses.append(new_course)
        
    def __repr__(self):
        return 'Course(%r )' % (self.courses)
    
    def __str__(self):
        return 'Courses {courses}'.format(
            courses=self.courses)
    
    def get_grades_as_list(self):
        grades_list = []
        for course in self.courses:
            grades_list.append(course.grade())
        return grades_list