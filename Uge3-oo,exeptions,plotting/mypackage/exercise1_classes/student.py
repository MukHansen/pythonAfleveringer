class Student():
    """A simple book model consisting of chapters, which in 
    turn consist of paragraphs."""

    def __init__(self, name, gender, data_sheet, image_url):
        """Initialize title, the author, and the chapters."""
        self.name = name 
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url   
        
    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)
    
    def __str__(self):
        return '{name} gender {gender} courses {dSheet} picture {img}'.format(
            name=self.name, gender=self.gender, dSheet=self.data_sheet, img=self.image_url)
    
    def get_avg_grade(self):
        return sum(self.data_sheet.get_grades_as_list)/len(self.data_sheet.get_grades_as_list)


    # def read(self, chapter=1):
    #     """Simulate reading a chapter, by calling the reading 
    #     method of a chapter.""" 
    #     self.chapters[chapter - 1].read()
        
    # def open_book(self, chapter=1) -> Chapter:
    #     """Simulate opening a book, which returns a chapter 
    #     object.""" 
    #     return self.chapters[chapter - 1]