import getpass
from learner import Learner
from instructor import Instructor
from backend import Backend
from course import Course
from enrollment import Enrollment
import uuid

def handleOption1() -> bool:
    option1_input = input("Are you a learner or an instructor?\n" +
                        "\t 1 - learner \n" +
                        "\t 2 - instructor \n")
    try:
        int_option1_input = int(option1_input)
        if int_option1_input not in range(1, 3):
            print("Please enter a valid number")
        else:
            name_input = input("Please enter your name:")
            id_input = input("Please enter your id:")
            email_input = input("Please enter your email:")
            password_input = getpass.getpass("Please enter your password:")
            if int_option1_input == 1:
                user = Learner(id_input, name_input, email_input, password_input)
            else:
                user = Instructor(id_input, name_input, email_input, password_input)
            backend.add_user(user)
            return True
    except ValueError:
        print("Please enter a number")
    return False

def handleOption2():
    course_id_input = input("What is the course id?")
    course_name_input = input("What is the name of the course?")
    added_course = Course(course_id_input, course_name_input)
    backend.add_course(added_course)
    
def handleOption3() -> bool:
    enroll_learner_id = input("What is the id of the learner?")
    if enroll_learner_id in backend.users:
        user = backend.users[enroll_learner_id]
        if isinstance(user, Learner):
            enroll_course_id = input("What is the id of the course?")
            if enroll_course_id in backend.courses:
                course = backend.courses[enroll_course_id]
                enrollment = Enrollment(uuid.uuid4(), user, course)
                enrollment.enroll_course()
                backend.add_enrollment(enrollment)
                return True
            else:
                print("No such course id found. Please enter a valid course id:")
        else:
            print("This user is not a learner. Please enter a valid user id:")
    else:
        print("No such learner id. Please enter a valid user id:")
    return False

def handleOption4() -> bool:
    course_id = input("Please enter the course id:")
    if course_id in backend.courses:
        learners = backend.get_learners_of_course(course_id)
        course_name = backend.courses[course_id].course_name
        print(f"The following learners are enrolled in the course {course_name}: \n {learners}")
        return True
    else:
        print("Course not found. Please enter a valid course id:")
    return False
    
def handleOption5() -> bool:
    learner_id = input("Please enter a learner id:")
    if learner_id in backend.users:
        learner = backend.users[learner_id]
        if isinstance(learner, Learner):
            courses = backend.get_courses_of_learner(learner_id)
            learner_name = backend.users[learner_id].name
            print(f"The learner {learner_name} is enrolled in the following courses: \n {courses}")
            return True
        else:
            print("This user is not a learner. Please enter a valid learner id:")
    else:
        print("No such learner id found. Please enter a valid learner id:")
    return False


'''
Start of the program
'''
backend = Backend()

while True:
    print()
    user_input = input("Please select a number from the following: \n" +
                       "\t 1 - Add use \n" + 
                       "\t 2 - Add course \n" +
                       "\t 3 - Enroll learner in course \n" +
                       "\t 4 - View enrolled learners in a course \n" +
                       "\t 5 - View courses in which a learner is enrolled \n" +
                       "\t 6 - Exit \n")
    
    try:
        int_input = int(user_input)
        if int_input not in range(1, 7):
            print("Please input a number from 1 to 6")
        else:
            if int_input == 1:
                while not handleOption1():
                    continue
            if int_input == 2:
                handleOption2()
            if int_input == 3:
                while not handleOption3():
                    continue
            if int_input == 4:
                while not handleOption4():
                    continue
            if int_input == 5:
                while not handleOption5():
                    continue
            if int_input == 6:
                break
    except ValueError as e:
        print(e)
        print("Please enter a number")
    