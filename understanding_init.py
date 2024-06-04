class Animal:
    def __init__(self, species):
        self.species = species

    def assign_name(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__('Dog')  # Calls the __init__ method of Animal
        self.name = name
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

my_dog = Dog('Buddy', 'Golden Retriever')
print(my_dog.species)  # Outputs: Dog
print(my_dog.name)     # Outputs: Buddy
print(my_dog.breed) 
my_dog.assign_name('Buddy New')
print(my_dog.name)     # Outputs: Buddy New

print("----------\n")
my_cat = Cat('Kitty', 'Siamese')
# print(my_cat.species)  # AttributeError: 'Cat' object has no attribute 'species'
print(my_cat.name)     # Outputs: Kitty
print(my_cat.breed)
my_cat.assign_name('Kitty New')
print(my_cat.name)     # Outputs: Kitty New


# super().init() is used to call the __init__ method of the parent class (Animal) explicitly. 
# This is necessary because the __init__ method of the parent class is overridden in the child class (Dog).
# In the case of the Cat class, the __init__ method of the parent class is not overridden, so there is no need to call it explicitly. 
# why it is bad to not call the parent class __init__ method in the Dog class?
# Because the parent class may have some initialization code that needs to be executed,
# and by not calling the parent class __init__ method, you are skipping that initialization code.
# In this case, the parent class Animal has an __init__ method that initializes the species attribute,
# and by not calling it in the Dog class, the species attribute is not initialized, which can lead to unexpected behavior.