def menu():
    Status = True
    while Status == True:
        print("1. m --> km")
        print("2. cm --> m")
        print("3. mm --> cm")
        print("4. km --> m")
        print("5. m --> cm")
        print("6. cm --> mm")
        print("7. mm --> km")
        print("8. km --> mm")
        print("9. cm --> km")
        print("10. km --> cm")
        print("11. mm -->m")
        print("12. m --> mm")
        print("Q = quit")
        option = input("Select a conversion: ")
        if option == "Q":
            Status = False
        elif option == "1":
            value = input("Enter a number: ")
            value = float(value)
            km = m_to_km(value)
            print(value,"in meters is",km,"in kilometers")
        elif option == "2":
            value = input("Enter a number: ")
            value = float(value)
            m = cm_to_m(value)
            print(value,"in centimeters is",m,"in meters")
        elif option == "3":
            value = input("Enter a number: ")
            value = float(value)
            cm = mm_to_cm(value)
            print(value,"in milimeters is",cm,"in centimeters")
        elif option == "4":
            value = input("Enter a number: ")
            value = float(value)
            m = km_to_m(value)
            print(value,"in kilometers is",m,"in meters")
        elif option == "5":
            value = input("Enter a number: ")
            value = float(value)
            cm = m_to_cm(value)
            print(value,"in meters is",cm,"in centimeters")
        elif option == "6":
            value = input("Enter a number: ")
            value = float(value)
            mm = cm_to_mm(value)
            print(value,"in centimeters is",mm,"in milimeters")
        elif option == "7":
            value = input("Enter a number: ")
            value = float(value)
            km = mm_to_km(value)
            print(value,"in milimeters is",km,"in kilometers")
        elif option == "8":
            value = input("Enter a number: ")
            value = float(value)
            mm = km_to_mm(value)
            print(value,"in kilometers is",mm,"in milimeters")
        elif option == "9":
            value = input("Enter a number: ")
            value = float(value)
            km = cm_to_km(value)
            print(value,"in centimeters is",km,"in kilometers")
        elif option == "10":
            value = input("Enter a number: ")
            value = float(value)
            cm = km_to_cm(value)
            print(value,"in kilometers is",cm,"in centimeters")
        elif option == "11":
            value = input("Enter a number: ")
            value = float(value)
            m = mm_to_m(value)
            print(value,"in milimeters is",m,"in meters")
        elif option == "12":
            value = input("Enter a number: ")
            value = float(value)
            mm = m_to_mm(value)
            print(value,"in meters is",mm,"in milimeters")
        else:
            print("This is an invlid option")

def m_to_km(value):
    km = value / 1000
    return km

def cm_to_m(value):
    m = value / 100
    return m

def mm_to_cm(value):
    cm = value / 10
    return cm

def km_to_m(value):
    m = value * 1000
    return m

def m_to_cm(value):
    cm = value * 100
    return cm

def cm_to_mm(value):
    mm = value * 10
    return mm

def mm_to_km(value):
    value1 = mm_to_cm(value)
    value2 = cm_to_m(value1)
    km = m_to_km(value2)
    return km

def km_to_mm(value):
    value1 = km_to_m(value)
    value2 = m_to_cm(value1)
    mm = cm_to_mm(value2)
    return mm

def cm_to_km(value):
    value1 = cm_to_m(value)
    km = m_to_km(value1)
    return km

def km_to_cm(value):
    value1 = km_to_m(value)
    cm = m_to_cm(value1)
    return cm

def mm_to_m(value):
    value1 = mm_to_cm(value)
    m = cm_to_m(value1)
    return m

def m_to_mm(value):
    value1 = m_to_cm(value)
    mm = cm_to_mm(value1)
    return mm

menu()



    
