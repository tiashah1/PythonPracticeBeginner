def new_mark():
    new_mark = input("Enter the mark: ")
    new_mark = int(new_mark)
    return new_mark

def calculate_grade(new_mark):
    if new_mark >= 0 and new_mark <= 34:
        grade = "F"
    elif new_mark > 34 and new_mark <= 39:
        grade = "E"
    elif new_mark > 39 and new_mark <= 49:
        grade = "D"
    elif new_mark > 49 and new_mark <= 64:
        grade = "C"
    elif new_mark > 64 and new_mark <= 79:
        grade = "B"
    elif new_mark > 79 and new_mark <= 94:
        grade = "A"
    elif new_mark > 94 and new_mark <= 100:
        grade = "A*"
    else:
        grade = "Invalid"
    return grade

def display(grade):
    print("Grade =",grade)


def TestGrade():
    status = True
    while status:
        mark = new_mark()
        if mark == 0:
            status = False
        else:
            grade = calculate_grade(mark)
            display(grade)


TestGrade()
