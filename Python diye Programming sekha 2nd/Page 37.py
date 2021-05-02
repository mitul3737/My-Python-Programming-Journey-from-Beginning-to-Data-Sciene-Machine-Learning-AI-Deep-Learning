class Car: #creating a class
    #variables defined
    name="" #this are of no use
    color="" #this is of no use

    def __init__(self,n,c):#when any object is created , this __init__ method is called
        self.name=n #here "self.name" object is assigned with "n' attribute value
        self.color=c #here "self.color" is assigned with "c" attribute value


    #method defined
    def start(self):
        print("Starting the engine")


my_car=Car("Corolla",'White')#when this object my_car is created , __init__(self,n,c) is called automatically and n gets the value Corolla and c gets White
#Then when self.name=n called, then it means my_car gets "name" attribute and same way "color" attribute gets assigned for my_car
print(my_car.name)
print(my_car.color)
my_car.start() #method start() called