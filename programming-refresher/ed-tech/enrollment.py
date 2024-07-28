from course import Course
from learner import Learner

class Enrollment:
    def __init__(self, enrollment_id, learner: Learner, course: Course):
        self.enrollment_id = enrollment_id
        self.learner = learner
        self.course = course
        
    def enroll_course(self):
        self.course.add_learner(self.learner)
        self.learner.enroll_course(self.course)
        
    def drop_course(self):
        self.course.drop_learner(self.learner)
        self.learner.drop_course(self.course)