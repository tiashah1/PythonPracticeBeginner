def main():
    total = 0
    correct = 0
    return total,correct

def randomnum():
    import random
    number = random.randint(2,12)
    answer(number)
    return

def answer(number):
    print("What is",number,"to the power of 2")
    answer = input("Answer: ")
    answer = int(answer)
    calculation =(number ** 2)
    calculation = int(calculation)
    answered(calculation,answer)

def answered(calculation,answer):
    if calculation == answer:
        print("Correct, the answer is",calculation)
        calculate_score(total,correct)
    else:
        print("Incorrect, the answer is",calculation)
        calculate_score(total,correct)
    return 

def calculate_score(total,correct):
    if calculation == answer:
        total = total + 1
        correct = correct + 1
        grade(correct,total)
    else:
        total = total + 1
        grade(correct,total)
    return total,correct

def grade(total,correct):
    repeat = input("Do you want another question (Y/N): ")
    if repeat == "Y":
        randomnum()
    else:
        GradeP =(correct / total) * 100
        print("Percentage:",GradeP,"Grade:",correct,"/",total)

main()
randomnum()
