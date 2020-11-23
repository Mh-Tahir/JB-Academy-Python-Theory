# Right triangle area calculation
class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2


    def get_area(self):
        print(self.a * self.b / 2)


c, a, b = input().split()
t = RightTriangle(int(c), int(a), int(b))
if t.c ** 2 == t.a ** 2 + t.b ** 2:
    t.get_area()
else:
    print('Not right')

# Create student id
class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = self.name[0] + self.last_name + self.birth_year


n, l, y = input(), input(), input()
Dan = Student(n, l, y)
print(Dan.id)

#Sphere volume
class Sphere:
    PI = 3.1415
    def __init__(self, radius):
        self.radius = radius
        self.volume = (self.radius ** 3) * self.PI * 4 / 3

# Ship
class Ship:
    def __init__(self, name, capacity, destination):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.destination = destination

    # the old sail method that you need to rewrite
    def sail(self):
        print("The {} has sailed for {}!".format(self.name, self.destination))


black_pearl = Ship("Black Pearl", 800, input())
black_pearl.sail()

# Stack class
class Stack():

    def __init__(self):
        self.s = []

    def push(self, el):
        self.s.append(el)

    def pop(self):
        return self.s.pop()

    def peek(self):
        return self.s[-1]

    def is_empty(self):
        return self.s == []

# Friend class
class User:
    def __init__(self, username):
        self.username = username
        self.friends = 0

    def add_friends(self, n):
        self.friends += n
        print("{} now has {} friends.".format(self.username, self.friends))

# Bank deposit class
class Bank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        if self.cents + deposit_cents < 100:
            self.cents += deposit_cents
        else:
            self.cents += deposit_cents
            self.dollars += self.cents // 100
            self.cents = self.cents % 100
