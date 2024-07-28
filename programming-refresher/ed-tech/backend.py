from user import User
from course import Course
from enrollment import Enrollment
from learner import Learner

class Backend:
    def __init__(self):
        self.users = {}
        self.courses = {}
        self.enrollments = {}
        
    def add_user(self, user: User):
        self.users[user.user_id] = user
        
    def add_course(self, course: Course):
        self.courses[course.course_id] = course
        
    def add_enrollment(self, enrollment: Enrollment):
        self.enrollments[enrollment.enrollment_id] = enrollment
        
    def get_learners_of_course(self, course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            course.__class__ = Course
            return list(map(lambda x : x.name, course.learners))
        else:
            return []
        
    def get_courses_of_learner(self, learner_id):
        courses = []
        for course_id in self.courses:
            course = self.courses[course_id]
            course.__class__ = Course
            for learner in course.learners:
                learner.__class__ = Learner
                if learner.user_id == learner_id:
                    courses.append(course)
        return list(map(lambda x : x.course_name, courses))
            