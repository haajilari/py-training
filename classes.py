class Parent:
    def __init__(self):
        self.parent_member = "I am a parent member"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_member = "I am a child member"


class MyClass:
    a = 5
    print("This is a class variable")

    def hello(self):
        print("Hello from MyClass")

myClass = MyClass()

print("Accessing class variable: ", myClass.a)
print("Accessing method: ", myClass.hello())

print(" ######################### ")
class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass
        # Functionality to calculate the costs from the area of the house

house = House()
print(house.num_rooms)
print(House.num_rooms)