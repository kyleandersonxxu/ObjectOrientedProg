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
            if self.grade < self.passing_grade:
                self.award_credit = False
            else:
                self.award_credit = True
    def extraCredit(self, points):
        newGrade = slef.grade + points
        return newGrade


W01234 = Student('Kyle', 'Anderson') #instance of Student Class
W01235 = Student('Willy','Wanka')

print('Start of the semester')
print('-----------------------')

W01234.extraCredit(30)

print(W01234.passing_grade)
print(W01235.first, W01235.last, W01235.email, W01235.status)


print(W01234)
print(W01235)

W01234.first = "Kyle"
W01234.last = "Anderson"
W01234.Email = "masterblaste@mail.weber.edu"
W01234.status = "Pass"

W01235.first = "Willy"
W01235.last = "Wonka"
W01235.email = "kidsoup@mail.weber.edu"
W01235.status = "Pass"

# print(W01234.email)
# print(W01235.email)

