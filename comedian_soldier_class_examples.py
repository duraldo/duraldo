### First example brings back syntax error, anyone know why? Haven't looked into yet. But will...

class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!

### Gives me error:
### ERROR!
### File "<string>", line 11
###    return f"{self.first_name} {self.last_name} is {self.age}. Surprise!   #don't know why, don't matter, it helped me figure out how to do city_elevation question.
           ^
SyntaxError: unterminated string literal (detected at line 11)

### I found this example online, very simple example on how Class and attributes work. as well as the 'f-string' function. Looking at this made sense of the city_elevation problem
### https://realpython.com/python-f-strings/ (source I believe).

### Another example (with a Soldat, anyone play that old game?, this code works.

class Soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier()
print(soldier_one.get_speed())
# prints "6"

#Hopefully these 2 examples help. I feel week 5 (it's optional) Object Oriented Programming isn't very detailed, if you're like me reading online is difficult.
