def test1():
    status = True
    while status != False:
        new_mark = int(input("Enter mark : "))
        if new_mark >= 0 and new_mark <= 34:
            print("Mark =",new_mark,"| Grade = F")
        elif new_mark > 34 and new_mark <= 39:
            print("Mark =",new_mark,"| Grade = E")
        elif new_mark > 39 and new_mark <= 49:
            print("Mark =",new_mark,"| Grade = D")
        elif new_mark > 49 and new_mark <= 64:
            print("Mark =",new_mark,"| Grade = C")
        elif new_mark > 64 and new_mark <= 79:
            print("Mark =",new_mark,"| Grade = B")
        elif new_mark > 79 and new_mark <= 94:
            print("Mark =",new_mark,"| Grade = A")
        elif new_mark > 94 and new_mark <= 100:
            print("Mark =",new_mark,"| Grade = A*")
        else:
            print("Invalid")
    return 


test1()

