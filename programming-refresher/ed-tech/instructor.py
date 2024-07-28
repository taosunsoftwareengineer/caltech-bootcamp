from user import User

class Instructor(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.taught_courses = []
        
    def add_taught_courses(self, course_name):
        self.taught_courses.append(course_name)
        
    def drop_taught_courses(self, course_name):
        if course_name in self.taught_courses:
            self.taught_courses.remove(course_name)