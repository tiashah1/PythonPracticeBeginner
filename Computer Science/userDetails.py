def gettitle():
    title = input("Enter your title (Mr, Mrs, Miss, Ms, Dr): ")
    while not(title == "Mr" or title == "Mrs" or title == "Miss" or title == "Ms" or title == "Dr"):
        title = input("Enter your title (Mr, Mrs, Miss, Ms, Dr): ")
    print("Title:",title)
    return title

def getgender():
    gender = input("Enter your gender (male / female): ")
    while not(gender == "male" or gender == "female"):
        gender = input("Enter your gender: ")
    print("Gender:",gender)
    return gender

def getfirstname(): 
    firstname = input("Enter firstname: ")
    while not(len(firstname) > 4):
        firstname = input("Enter firstname: ")
    print("Firstname:",firstname)
    return firstname

def getsurname():
    surname = input("Enter surname: ")
    while not(len(surname) > 4):
        surname = input("Enter surname: ")
    print("Surname:",surname)
    return surname

def getusername():
    username = input("Enter a username: ")
    while not(len(username) > 4):
        username = input("Enter a username: ")
    print("Username:",username)
    return username

def getpassword():
    password = input("Enter a password(at least 8 characters, 1 uppercase, 1 lowercase & 1 special character): ")
    while not(len(password) > 8):
        password = input("Enter a password: ")
    confirm = input("Confirm your password: ")
    while confirm != password:
        confirm = input("Confirm your password: ")
    print("Password:",password)
    return password

def getemail():
    email = input("Enter your email(at least 9 characters, contains @ and .): ")
    while not(len(email) > 9):
        email = input("Enter your email(at least 9 characters, contains @ and .): ")
    print("Email:",email)
    return email

def getsecurity1():
    question1 = input("Enter 1st security question: ")
    print("Question 1:",question1)
    return question1

def securityanswer1():
    answer1 = input("Enter answer: ")
    print("Answer 1:",answer1)
    return answer1
    
def getsecurity2():
    question2 = input("Enter 2nd security question: ")
    print("Question 2:",question2)
    return question2

def securityanswer2():
    answer2 = input("Enter answer: ")
    print("Answer 2:",answer2)
    return answer2
    
def save_user(title,gender,firstname,surname,username,password,email,question1,answer1,question2,answer2):
    file = open("userDetails.txt","a")
    c = ","
    print(title + c + gender + c + firstname + c + surname + c + password + c)
    data = title + c + gender + c + firstname + c + surname + c + password + c
    data = data + email + c + question1 + c + answer1 + c + question2 + c + answer2 +"\n"
    file.write(data)
    file.close()
    return

def register():
    print("\n------Registration------")
    title = gettitle() 
    gender = getgender()
    firstname = getfirstname()
    surname = getsurname()
    username = getusername()
    password = getpassword()
    email = getemail()
    question1 = getsecurity1()
    answer1 = securityanswer1()
    question2 = getsecurity2()
    answer2 = securityanswer2()
    save_user(title,gender,firstname,surname,username,password,email,question1,answer1,question2,answer2)
    print("\n" * 50)
    print("-------------------------------")
    print("Title:",title)
    print("Gender:",gender)
    print("Firstname:",firstname)
    print("Surname:",surname)
    print("Username:",username)
    print("Password:",password)
    print("Email:",email)
    return


def menu():
    print("1 - login")
    print("2 - register")
    print("3 - display")
    print("4 - several")
    print("Q - quit")
    status = True
    choice = input("Enter a choice: ")
    while not(choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "Q"):
        choice = input("Enter a choice: ")
    if choice == "Q":
        status = False
    elif choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        display()
    else:
        several()

menu()
