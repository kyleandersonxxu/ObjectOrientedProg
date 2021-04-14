from Students import Student


def main ():

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





if __name__ == "__main__":
    main