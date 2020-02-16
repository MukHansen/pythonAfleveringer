class Couse():
    def __init__(self, name, classroom, teacher, ETCS):
        self.name = name 
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS   
        
    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)
    
    def __str__(self):
        return '{name} gender {gender} courses {dSheet} picture {img}(
            name=self.name, gender=self.gender, dSheet=self.data_sheet, img=self.image_url)