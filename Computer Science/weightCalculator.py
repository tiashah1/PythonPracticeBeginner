class WeightCalculator:

    def __init__(self):

        self.menu()

    def getNumber(self,message):
        value = input("Enter a number: ")
        value = float(value)
        return value
    
    def kg_to_g(self,value):
        g = value * 1000
        return g
    
    def kg_to_mg(self,value):
        mg = value * 1000000
        return mg

    def kg_to_tonnes(self,value):
        tonnes = value * 0.001
        return tonnes
    
    def kg_to_pounds(self,value):
        pounds = value * 2.2
        return pounds

    def kg_to_stones(self,value):
        stones = value * 0.157473
        return stones

    def pounds_to_kg(self,value):
        kg = value / 2.2
        return kg

    def pounds_to_ounces(self,value):
        ounces = value * 16
        return ounces

    def pounds_to_stones(self,value):
        value1 = self.pounds_to_kg(value)
        stones = self.kg_to_stones(value1)
        return stones

    def pounds_to_g(self,value):
        value1 = self.pounds_to_kg(value)
        g = self.kg_to_g(value1)
        return g

    def pounds_to_tonnes(self,value):
        value1 = self.pounds_to_kg(value)
        tonnes = self.kg_to_tonnes(value1)
        return tonnes

    def stones_to_kg(self,value):
        kg = value / 0.157473
        return kg

    def stones_to_pounds(self,value):
        value1 = self.stones_to_kg(value)
        pounds = self.kg_to_pounds(value1)
        return pounds

    def pounds_to_mg(self,value):
        value1 = self.pounds_to_kg(value)
        mg = self.kg_to_mg(value1)
        return mg

    def kg_to_ounces(self,value):
        ounces = value * 35.274
        return ounces
    
    def menu(self):
        Status = True
        while Status == True:
            print("1. kg --> g")
            print("2. kg --> mg")
            print("3. kg --> tonnes")
            print("4. kg --> pounds")
            print("5. kg --> stones")
            print("6. pounds --> kg")
            print("7. pounds --> ounces")
            print("8. pounds --> stones")
            print("9. pounds --> g")
            print("10. pounds --> tonnes")
            print("11. stones --> kg")
            print("12. stones --> pounds")
            print("13. pounds --> mg")
            print("14. kg --> ounces")
            print("Q = quit")
            option = input("Select a conversion: ")
            if option == "Q":
                Status = False
            if option == "1":
                value = self.getNumber("Enter a number:")
                g = self.kg_to_g(value)
                print(value,"in kilograms is",g,"in grams")
            if option == "2":
                value = self.getNumber("Enter a number:")
                mg = self.kg_to_mg(value)
                print(value,"in kilograms is",mg,"in miligrams")
            if option == "3":
                value = self.getNumber("Enter a number:")
                tonnes = self.kg_to_tonnes
                print(value,"in kilograms is",tonnes,"in tonnes")
            if option == "4":
                value = self.getNumber("Enter a number:")
                pounds = self.kg_to_tonnes(value)
                print(value,"in kilograms is",pounds,"in pounds")
            if option == "5":
                value = self.getNumber("Enter a number:")
                stones = self.kg_to_stones(value)
                print(value,"in kilograms is",stones,"in stones")
            if option == "6":
                value = self.getNumber("Enter a number:")
                kg = self.pounds_to_kg(value)
                print(value,"in pounds is",kg,"in kilograms")
            if option == "7":
                value = self.getNumber("Enter a number:")
                ounces = self.pounds_to_ounces(value)
                print(value,"in pounds is",ounces,"in ounces")
            if option == "8":
                value = self.getNumber("Enter a number:")
                stones = self.pounds_to_stones(value)
                print(value,"in pounds is",stones,"in stones")
            if option == "9":
                value = self.getNumber("Enter a number:")
                g = self.pounds_to_g(value)
                print(value,"in pounds is",g,"in grams")
            if option == "10":
                value = self.getNumber("Enter a number")
                tonnes = self.pounds_to_tonnes(value)
                print(value,"in pounds is",tonnes,"in tonnes")
            if option == "11":
                value = self.getNumber("Enter a number")
                kg = self.stones_to_kg(value)
                print(value,"in stones is",kg,"in kilograms")
            if option == "12":
                value = self.getNumber("Enter a number")
                pounds = self.stones_to_pounds(value)
                print(value,"in stones is",pounds,"in pounds")
            if option == "13":
                value = self.getNumber("Enter a number")
                mg = self.pounds_to_mg(value)
                print(value,"in pounds is",mg,"in miligrams")
            if option == "14":
                value = self.getNumber("Enter a number")
                ounces = self.kg_to_ounces(value)
                print(value,"in kilograms is",ounces,"in ounces")

wc = WeightCalculator()
