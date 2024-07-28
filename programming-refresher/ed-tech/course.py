from learner import Learner

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.learners = []
        
    def add_learner(self, learner: Learner):
        self.learners.append(learner)
        
    def drop_learner(self, learner: Learner):
        if learner in self.learners:
            self.learners.remove(learner)
            
    def display_learners(self):
        return list(map(lambda x : x.name, self.learners))