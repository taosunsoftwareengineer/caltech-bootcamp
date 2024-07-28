from user import User

class Learner(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.enrolled_courses = []
        
    def enroll_course(self, course_name):
        self.enrolled_courses.append(course_name)
        
    def drop_course(self, course_name):
        if course_name in self.enrolled_courses:
            self.enrolled_courses.remove(course_name)