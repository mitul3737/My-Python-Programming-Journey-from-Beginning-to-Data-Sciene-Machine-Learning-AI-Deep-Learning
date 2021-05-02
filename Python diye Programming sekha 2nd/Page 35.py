class Car: #creating a class
    #variables assigned value
    name=""
    color=""

    #method defined
    def start(self):
        print("Starting the engine")


my_car=Car()# creating an object
my_car.name="Allion" #variable getting a value
print(my_car.name)
my_car.start() #calling method