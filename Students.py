class Student:
    grade = 0
    passing_grade = 75
    award_credit = False

    def __init__(self, first,last,status):
        self.first_name = first #these are instance variables
        self.last = last
        self.status = status
        self.student_email = first + last + '@mail.weber.edu'

        #Behavior
        def printStudentInfo(self):
            print('fullname:' self.first, self.last, '\nEmail:' self.email, '\nAward_credit:' self.status)

        def setGrade(self, grade):
            self.student_grade = grade
            self.passingClass()

    def extraCredit(self, points):
        self.grade = self.grade + points
        self.passingClass()

    def passingClass(self):
        if self.grade < self.passing_grade:
            self.award_credit = False
         else:
            self.award_credit = True


