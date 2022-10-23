def main_power():
    x = input("Enter a number: ")
    y = input("Enter a number: ")
    x = int(x)
    y = int(y)
    answer = powerof(x,y)
    print("x^y =",answer)

def powerof(x,y):
    answer = x ** y
    return answer

#main_power()

def age25(age):
    answer = age + 25
    return answer

def main_age():
    name = input("Enter name: ")
    age = input("Enter age: ")
    name = str(name)
    age = int(age)
    answer = age25(age)
    print(name, "in 25 years you will be", answer)

#main_age()

def age_yr(age,year):
    answer = age + (year - 2020)
    return answer

def main_agex():
    name = input("Enter name: ")
    age = input("Enter age: ")
    name = str(name)
    age = int(age)
    year = input("Enter a year: ")
    year = int(year)
    answer = age_yr(age,year)
    print(name,"in",year,"you will be",answer)

#main_agex()

def compare(num1,num2):
    if num1 > num2:
        print("The first number is greater than the second number")
    elif num1 < num2:
        print("The first number is less than The second number")
    else:
        print("The first number is equal to The second number")
    return

def mainCompare():
    num1 = input("Enter a number: ")
    num2 = input("Enter a number: ")
    num1 = int(num1)
    num2 = int(num2)
    compare(num1,num2)

#mainCompare()

def SecretWord(word):
    secret = "apple"
    count = 0
    while word != secret:
        word = input("Enter a word: ")
        if word == secret:
            print("Correct")
            return 
        else:
            count = count + 1
            if count >= 3:
                print("Too many tries")
                return 

def mainSecret():
    word = input("Enter word: ")
    SecretWord(word)

#mainSecret()

def mainCheckName():
    attempt = 0
    status = False
    while status == False and attempt <= 4:
        word = input("Enter a word: ")
        wordStatus = CheckMessage(word)
        if wordStatus == True:
            status = True
            print("correct")
        else:
            print("incorrect")
            attempt = attempt + 1

def CheckMessage(word):
    status = False
    secret = "apple"
    if secret == word:
        status = True
        return status

mainCheckName()


    

