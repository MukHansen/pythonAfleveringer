class Couse():
    def __init__(self, name, classroom, teacher, ETCS):
        self.name = name 
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS   
        
    def __repr__(self):
        return 'Course(%r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.ETCS)
    
    def __str__(self):
        return '{name} classroom {classroom} teacher {teacher} ETCS {ETCS}'(
            name=self.name, classroom=self.classroom, teacher=self.teacher, ETCS=self.ETCS)