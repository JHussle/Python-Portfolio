# Constructor

class Car:
    
    amount_cars = 0
    
    def __init__(self, manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp

# Class Variables
        Car.amount_cars += 1
# Destructors

    def __del__(self):
        print("Object gets deleted!")
        Car.amount_cars -= 1        
        
    def print_cars_amount(self):
        print("Amount: {}".format(Car.amount_cars))
            
    def print_info(self):
        print("Manufacturer: {}, Model: {}, HP: {}".format(self.manufacturer, self.model, self.hp))

        
# Creating Objects

myCar1 = Car("Telsa", "Model X", 525)
# Add'l Objects
myCar2 = Car("BMW", "X3", 200)
myCar3 = Car("VW", "Golf", 100)
myCar4 = Car("Porsche", "911", 520)


# Removing an object
del myCar3


#myCar1.print_info()
myCar1.print_cars_amount()        

# Direct access the attributes of an object

#print(myCar1.manufacturer)
#print(myCar1.model)
#print(myCar1.hp)
      