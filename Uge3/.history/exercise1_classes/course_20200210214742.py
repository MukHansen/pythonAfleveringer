class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade=0):
        self.name = name 
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade        
        
    def __repr__(self):
        return 'Course(%r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.ETCS)
    
    def __str__(self):
        return '{name} classroom {classroom} teacher {teacher} ETCS {ETCS}'.format(
            name=self.name, classroom=self.classroom, teacher=self.teacher, ETCS=self.ETCS)