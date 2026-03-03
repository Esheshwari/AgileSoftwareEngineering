# Course Enrollment Management System

courses = {}   # Dictionary to store course_name: list_of_students


def add_course():
    course_name = input("Enter course name: ")
    if course_name in courses:
        print("Course already exists.")
    else:
        courses[course_name] = []
        print("Course added successfully.")


def enroll_student():
    course_name = input("Enter course name: ")
    if course_name not in courses:
        print("Course does not exist.")
        return
    
    student_name = input("Enter student name: ")
    
    if student_name in courses[course_name]:
        print("Student already enrolled.")
    else:
        courses[course_name].append(student_name)
        print("Student enrolled successfully.")


def drop_course():
    course_name = input("Enter course name: ")
    if course_name not in courses:
        print("Course does not exist.")
        return
    
    student_name = input("Enter student name: ")
    
    if student_name in courses[course_name]:
        courses[course_name].remove(student_name)
        print("Student dropped from course.")
    else:
        print("Student not enrolled in this course.")


def view_courses():
    if not courses:
        print("No courses available.")
        return
    
    for course, students in courses.items():
        print(f"\nCourse: {course}")
        if students:
            for student in students:
                print(" -", student)
        else:
            print(" No students enrolled.")


def menu():
    while True:
        print("\n===== Course Enrollment System =====")
        print("1. Add Course")
        print("2. Enroll Student")
        print("3. Drop Course")
        print("4. View Courses")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_course()
        elif choice == "2":
            enroll_student()
        elif choice == "3":
            drop_course()
        elif choice == "4":
            view_courses()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


menu()
