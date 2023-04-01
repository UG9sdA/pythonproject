class Course:
    def __init__(self, course_name):
        self.__course_students = {}
	self.__course_name = course_name
    def get_course_name(self):
        return self.__course_name
    def get_course(self):
        return f'Name: {self.__course_info[0]}'

    def set_attendance(self,int: lecture, student_id, present):   #Attendance of student in each course
        self.__course_students[student_id][lecture-1] = present
    def get_attendance(self, student_id):
        return sum(self.__course_students[student_id][0:10])

    def set_midTerm(self, student_id, mark):  #Midterm of student in each course
        self.__course_students[student_id][10] = mark
    def get_midTerm(self, student_id):
        return self.__course_students[student_id][10]

    def set_final(self, student_final, id):  #Midterm of student in each course
        self.__course_info[1][student_id][11] = mark
    def get_final(self, student_id):
        return self.__course_students[student_id][11]

    def add_student(self,student_id):
	if student_id in self.__course_students:
	    overwrite = input("Student ID already exist in this course, do you want to overwrite?")
	    if overwrite != 1:
		return 0
	self.__course_students[student_id] = [0]*12
    def show_student():
	for student in self.__course_students:
	    print(f"Student ID: {student} - Attendance: {get_attendance(student)} - Mid: {get_midtearm(student)} Final: {get_final(student)} ")

