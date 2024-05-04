# class
# abstraction - hide information only give a way that user wants.
# private?


# for doing it in python we use _ (underscore) to make a property private.
# that can't be accessed from outside the class.
# for example:

# class PlayerCharacter:
#     '''
#     # what is __init__?
#     # __init__ is a special method that is called when a new object is created.
#     # it is used to initialize the attributes of the object.
#     # for example:
#     '''
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
    
#     def run(self):
#         print('run')
        
#     def speak(self):
#         print(f'my name is {self.name} and I am {self.age} years old')

# player1 = PlayerCharacter('Cindy', 43)
# print(player1._name)
# print(len((2,3,4,5,6)))

# player1.speak()

