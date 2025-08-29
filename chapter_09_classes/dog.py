class Dog :
    """A simple attempt to model a dog"""

    def __init__(self , age , name):
        self.age = age
        self.name = name

    def sit(self) :
        """Simulate a dog sitting down in response to a command"""
        print(f"{self.name} is now sitting")
    def roll_over(self):
        """Simulate s dog rolling over in response to a command"""
        print(f"{self.name} is now rolling over")


my_dog = Dog(3.5 , "jimmy")
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old")

my_dog.sit()

