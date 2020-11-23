# no more than 10 puppies restriction
class Puppy:
    n_puppies = 0
    
    def __new__(cls):
        if cls.n_puppies < 10:
            cls.n_puppies += 1

# Print info about the class
class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    def __str__(self):
        return "{} by {}. ${}. [{}]".format(self.title, self.author, self.price, self.book_id)

# user representation
class MyClass:
    n_objects = 0

    def __new__(cls):
        if cls.n_objects < 5:
            cls.n_objects += 1
            return object.__new__(cls)

    def __str__(self):
        return "An object of MyClass"

# unambiguous representation for developers and a readable string for users
class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return "{} {}. {}".format(self.name, self.last_name, self.age)

    def __repr__(self):
        return "Object of the class Patient. name: {}, last_name: {}, age: {}".format(self.name, self.last_name, self.age)
