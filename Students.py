class Student:
    def __init__(self, first,last,status):
        self.first_name = first #these are instance variables
        self.last = last
        self.status = status
        self.student_email = first + last + '@mail.weber.edu'

W01234 = Student('Kyle', 'Anderson','Pass')
W01235 = Student('Willy','Wanka', 'Pass')

print(W01234.first, W01234.last, W01234.email, W01234.status)
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

