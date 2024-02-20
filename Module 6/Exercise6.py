# 9-1. Restaurant 
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")
restaurant = Restaurant("Chipotle", "Mexican")
print("Restaurant Name:", restaurant.restaurant_name)
print("Cuisine Type:", restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is now open!")
restaurant1 = Restaurant("Chipotle", "Mexican")
restaurant2 = Restaurant("Taco Bell", "Mexican")
restaurant3 = Restaurant("Five Guys", "Burgers")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3. Users
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location

    def describe_user(self):
        print("User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

user1 = User("JW", "Stephens", "Daredevil", "kingpin@gmail.com", "New York")
user2 = User("Bruce", "Wayne", "Batman", "justice@gotham.com", "Gotham")
user3 = User("Wanda", "Maximoff", "ScarWitch", "vision@reality.com", "Sokovia")


user1.describe_user()
user1.greet_user()


user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

# 9-5. Login Attempts
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0  # Adding the login_attempts attribute with initial value 0

    def describe_user(self):
        print("User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Clark", "Kent", "Superman", "man0fsteel@dailyplanet.com", "Metropolis")


user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()


print("Login Attempts:", user1.login_attempts)


user1.reset_login_attempts()

print("After reset, Login Attempts:", user1.login_attempts)

# 9-7. Admin
class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.privileges = []

    def describe_user(self):
        print("User Information:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")
    
    def show_privileges(self):
        print("This adminstrator can add posts, delete posts, and lock user accounts.")

user1 = User("JW", "Stephens", "Daredevil", "kingpin@gmail.com", "New York")
user2 = User("Bruce", "Wayne", "Batman", "justice@gotham.com", "Gotham")
user3 = User("Wanda", "Maximoff", "ScarWitch", "vision@reality.com", "Sokovia")
admin = User("Tony", "Stark", "Ironman", "peace@hotnet.mail", "Malibu")

user1.describe_user()
user1.greet_user()


user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

admin.describe_user()
admin.show_privileges()

admin.greet_user()

# 9-8 Privileges
class Privileges:
    def __init__(self):
        self.privileges = []
        
    def show_privileges(self):
        print("This administrator can add posts, delete posts, and lock user accounts.")
        
class Admin:
    def __init__(self, first_name, last_name, username, email, location):
        self.privileges = Privileges()
        
admin_user = Admin("Bruce", "Banner", "HULK", "smash@email.com", "Avengers Tower")

admin_user.privileges.privileges = ["can add post", "can delete post", "can ban user"]

admin_user.privileges.show_privileges()

# 9-11 Imported Admin 
class Privileges:
    def __init__(self):
        self.privileges = []
    def show_privileges(self):
        print("This administrator can add posts, delete posts, and lock user accounts.")


class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.privileges = Privileges()


class Admin(User):
    def __init__(self, first_name, last_name, username, email, location):
      self.privileges = Privileges()

# Separate Module

from module_one import Admin

admin_user = Admin("Frank", "Castle", "Punisher", "kandahar@gmail.com", "Hell's Kitchen")

admin_user.privileges.privileges = ["can shoot to kill", "cannot die", "can act outisde of the law"]

admin_user.privileges.show_privileges()

# 9-12. Multiple Modules
class Privileges:
    def __init__(self):
        self.privileges = []
    def show_privileges(self):
        print("This administrator can add posts, delete posts, and lock user accounts.")
class Admin:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.privileges = Privileges()



# Separate Module

class User:
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location



# Separate Module

from privileges_admin_module import Admin

admin_user = Admin("Frank", "Castle", "Punisher", "kandahar@gmail.com", "Hell's Kitchen")

admin_user.privileges.privileges = ["can shoot to kill", "cannot die", "can act outisde of the law"]

admin_user.privileges.show_privileges()


# 9-13. Dice
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"Rolling a {self.sides}-sided die:")
        for _ in range(10):
            print(random.randint(1, self.sides))

six_sided_die = Die()
print("Let's roll a 6-sided die 10 times:")
six_sided_die.roll_die()
print()

ten_sided_die = Die(sides=10)
print("Let's roll a 10-sided die 10 times:")
ten_sided_die.roll_die()
print()

twenty_sided_die = Die(sides=20)
print("Let's roll a 20-sided die 10 times:")
twenty_sided_die.roll_die()

# 9-14 Lottery 
import random
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_chars = [random.choice(lottery) for _ in range(4)]

print(f"Any ticket that matches these four characters: {winning_chars}, is a winning ticket!")


# 10-1 Learning Python
learning_python.txt
In Python you can use if, elif, and else statements to control your program based on different scenarios
In Python you can store that you don't want to be changed in a tuple, which is an immutable list. 

filename = 'learning_python.txt'

print("Reading the entire file at once:")
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

print("\nReading the file by looping over each line:")
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
