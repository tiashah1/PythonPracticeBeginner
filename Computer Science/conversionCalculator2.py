class WeightCalculator:

    def __init__(self):

        self.menu()

    def getNumber(self,message):
        value = input("Enter a number: ")
        value = float(value)
        return value
    
    def m_to_km(self,value):
        km = value / 1000
        return km

    def cm_to_m(self,value):
        m = value / 100
        return m
    
    def mm_to_cm(self,value):
        cm = value / 10
        return cm

    def km_to_m(self,value):
        m = value * 1000
        return m

    def m_to_cm(self,value):
        cm = value * 100
        return cm

    def cm_to_mm(self,value):
        mm = value * 10
        return mm

    def mm_to_km(self,value):
        value1 = self.mm_to_cm(value)
        value2 = self.cm_to_m(value1)
        km = self.m_to_km(value2)
        return km

    def km_to_mm(self,value):
        value1 = self.km_to_m(value)
        value2 = self.m_to_cm(value1)
        mm = self.cm_to_mm(value2)
        return mm

    def cm_to_km(self,value):
        value1 = self.cm_to_m(value)
        km = self.m_to_km(value1)
        return km

    def km_to_cm(self,value):
        value1 = self.km_to_m(value)
        cm = self.m_to_cm(value1)
        return cm

    def mm_to_m(self,value):
        value1 = self.mm_to_cm(value)
        m = self.cm_to_m(value1)
        return m

    def m_to_mm(self,value):
        value1 = self.m_to_cm(value)
        mm = self.cm_to_mm(value1)
        return mm

    def mm_table2(self):
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))
        step = int(input("Enter the step: "))

        
        print('\n'*50)
        print('{0:^8}{1:^8}{2:^8}{3:^8}'.format('MM','CM','M','KM'))
        print('{0:^8}{1:^8}{2:^8}{3:^8}'.format('-------','-------','-------','-------'))
        while start <= end:
            cm = self.mm_to_cm(start)
            m = self.mm_to_m(start)
            km = self.mm_to_km(start)
    
            print('{0:^8}{1:^8}{2:^8}{3:^8}'.format(start, cm, m, km))
            start += step
        input('Press Enter to continue')
        return
    
    def mm_table(self):
        start = int(input("Enter start number: "))
        end = int(input("Enter end number: "))
        step = int(input("Enter the step: "))

        
        print('\n'*50)
        print('{0:^8}{1:^8}{2:^8}{3:^8}'.format('MM','CM','M','KM'))
        print('{0:^8}{1:^8}{2:^8}{3:^8}'.format('-------','-------','-------','-------'))

        for mm in range( start, end+step, step):
            cm = self.mm_to_cm(mm)
            m = self.mm_to_m(mm)
            km = self.mm_to_km(mm)
    
            print('{0:^8}{1:^8}{2:^8}{3:^8}'.format(mm, cm, m, km))
    
        input('Press Enter to continue')
        return
        
    def menu(self):
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
            print("13. mm Table")
            print("Q = quit")
            option = input("Select a conversion: ")
            if option == "Q":
                Status = False
            elif option == "1":
                value = self.getNumber("Enter a number in metres: ")
                km = self.m_to_km(value)
                print(value,"in meters is",km,"in kilometers")
            elif option == "2":
                value = self.getNumber("Enter a number in centimeters: ")
                m = self.cm_to_m(value)
                print(value,"in centimeters is",m,"in meters")
            elif option == "3":
                value = self.getNumber("Enter a number in milimeters: ")
                cm = self.mm_to_cm(value)
                print(value,"in milimeters is",cm,"in centimeters")
            elif option == "4":
                value = self.getNumber("Enter a number in kilometers: ")
                m = self.km_to_m(value)
                print(value,"in kilometers is",m,"in meters")
            elif option == "5":
                value = self.getNumber("Enter a number in meters: ")
                cm = self.m_to_cm(value)
                print(value,"in meters is",cm,"in centimeters")
            elif option == "6":
                value = self.getNumber("Enter a number in centimeters: ")
                mm = self.cm_to_mm(value)
                print(value,"in centimeters is",mm,"in milimeters")
            elif option == "7":
                value = self.getNumber("Enter a number in milimeters: ")
                km = self.mm_to_km(value)
                print(value,"in milimeters is",km,"in kilometers")
            elif option == "8":
                value = self.getNumber("Enter a number in kilometers: ")
                mm = self.km_to_mm(value)
                print(value,"in kilometers is",mm,"in milimeters")
            elif option == "9":
                value = self.getNumber("Enter a number in centimeters: ")
                km = self.cm_to_km(value)
                print(value,"in centimeters is",km,"in kilometers")
            elif option == "10":
                value = self.getNumber("Enter a number in kilometers: ")
                cm = self.km_to_cm(value)
                print(value,"in kilometers is",cm,"in centimeters")
            elif option == "11":
                value = self.getNumber("Enter a number in milimeters: ")
                m = self.mm_to_m(value)
                print(value,"in milimeters is",m,"in meters")
            elif option == "12":
                value = self.getNumber("Enter a number in meters: ")
                mm = self.m_to_mm(value)
                print(value,"in meters is",mm,"in milimeters")
            elif option == "13":
                self.mm_table()
            else:
                print("This is an invlid option")


wc = WeightCalculator()
