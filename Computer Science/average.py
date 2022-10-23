totalnum = int(input("How many numbers do you want to be averaged: "))
total = 0
average = 0
for counter in range (totalnum):
    number = int(input("Enter a number: "))
    total = total + number

    
average = total / totalnum
print("Average:",average)
