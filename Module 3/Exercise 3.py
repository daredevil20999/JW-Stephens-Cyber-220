# 4-1. Pizzas
pizzas = ['pepperoni', 'cheese', 'stuffed crust']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza.')

print("I eat pizza all the time!")
print("It is so so delicious.")
print("I eat it on the weekends, and sometimes I eat the leftovers in the morning.\nI really love pizza!")

# 4-2. Animals
animals = ['shark', 'whale', 'pufferfish']
for animal in animals:
    print("A " + animal + " would make a great pet.")
print('What do these animals have in common?\nThey all live in the ocean!')

# 4-3. Counting to Twenty
for number in range(1, 21):
    print(number)

# 4-4. One Million
for number in range(1, 1000001):
    print(number)

# 4-5. Summing a Million
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6. Odd Numbers
for num in range(1, 21, 2):
    print(num)

# 4-7. Threes
for num in range(3, 31, 3):
    print(num)

# 4-8. Cubes
for num in range(1, 11):
    print(num ** 3)

# 4-9. Cube Comprehension
cubes = [i ** 3 for i in range(1, 11)]
print(cubes)

# 4-10. Slices
sliceanimals = ['shark', 'whale', 'pufferfish', 'orca', 'eel', 'jellyfish', 'octopus', 'shrimp', 'starfish']
front = sliceanimals[:3]
first_three = ', '.join(map(str, front))
print('The first three items in this list are: ' + first_three + '.')
middle = sliceanimals[3:6]
second_three = ', '.join(map(str, middle))
print('Three items from the middle of the list are: ' + second_three + '.')
back = sliceanimals[6:]
last_three = ', '.join(map(str, back))
print('The last three items in this list are: ' + last_three + '.')

# 4-11. My Pizzas, Your Pizzas
friend_pizzas = ['pepperoni', 'cheese', 'stuffed crust', 'hawaiian']
for pizza in pizzas:
    print('My favorite pizzas are: ' + pizza + '.')
for pizza in friend_pizzas:
    print("My friend's favorite pizzas are: " + pizza + ".")

# 4-12. More Loops

# 4-13. Buffet
foods = ('chicken', 'macaroni', 'icecream', 'potatoes', 'salad')
for food in foods:
    print(food)
extra_food = ('french fries', 'pasta')
new_food = foods + extra_food
format = ', '.join(map(str, new_food))
print(format)

# 5-1. Conditional Texts
food = 'apple'
print("Is food == 'apple'? I predict True.")
print(food == 'apple')
print("\nIs food == 'banana'? I predict False.")
print(food == 'banana')

car = 'toyota'
print("Is car == 'toyota'? I predict True.")
print(car == 'toyota')
print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

first_period = 'math'
print("Is first_period == 'math'? I predict True")
print(first_period == 'math')
print("\nIs first_period == 'english'? I predict False ")
print(first_period == 'english')

sport = 'baseball'
print("Is sport == 'baseball'? I predict True.")
print(sport == 'baseball')
print("\nIs sport == 'football? I predict False.")
print(sport == 'football')

girl = 'blonde'
print("Is girl == 'blonde'? I predict True.")
print(girl == "blonde")
print("\nIs girl == 'brunette'? I predict False.")

# 5-2 More Conditional Tests
friend = 'abram'
print("Is friend == 'abram'? I predict True.")
print(friend == 'abram')
print("\nIs friend == 'Jim'? I predict False.")
print(friend == 'Jim')

user_input = input("Enter a word: ")
lowercase_input = user_input.lower()
if lowercase_input == "test":
    print("The input is 'test'.")
else:
    print("The input is not 'test'.")

number_one = 5
number_two = 7
if number_one > number_two:
    print(f"{number_one} is greater than {number_two}.")
elif number_one == number_two:
    print(f"{number_one} is equal to {number_two}.")
else:
    print(f"{number_one} is less than {number_two}.")

car = 'camry'
color = 'red'
if car == 'camry' and color == 'red':
    print("This is a red car")

grade = 'A'
teacher = 'Dr. Grech'
if grade == 'A' or teacher == 'Dr. Grech':
    print("Yay")

list = (1, 2, 3, 4, 5)
item = 3
if item in list:
    print(f"{item} is in the list.")
else:
    print(f"{item} is not in the list.")

menu = ('taco', 'burrito', 'enchilada')
item = 'empañada'
if item not in list:
    print(f"{item} is not in the list.")
else:
    print(f"{item} is in the list.")


# 5-3. Alien Colors #1
alien_color = 'green', 'yellow', 'red'
if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You did not earn any points.")

alien_color_fail = 'green', 'yellow', 'red'
if alien_color_fail == 'purple':
    print("You just earned 5 points!")

# 5-4. Alien Colors #2
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")

# 5-5. Alien Colors #3
if alien_color == 'green':
    print("You have earned 5 points.")
elif alien_color == 'yellow':
    print("You have earned 10 points.")
else:
    print("You have earned 15 points.")

# 5-6. Stages of Life
age = 16
if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

# 5-7. Favorite Fruit
favorite_fruits = ['banana', 'orange', 'grapefruit']
if 'orange' in favorite_fruits:
    print("You really like oranges!")
elif 'banana' in favorite_fruits:
    print("You really like bananas.")
elif 'grapefruit' in favorite_fruits:
    print("You really like grapefruits!")
elif 'apple' in favorite_fruits:
    print("You really like apples!")
elif 'blueberry' in favorite_fruits:
    print("You really like blueberries!")

# 5-8. Hello Admin
usernames = ['admin', 'bob', 'hatman', 'kingpin', 'sicario']
for name in usernames[-4:]:
    print("Hello " + name + ", thank you for logging in again.")
for name in usernames[:1]:
    print("Hello admin, would you like to see a status report.")
# 5-9. No Users
if not usernames:
    print("We need to find some users!")

#5-10. Checking Usernames
current_users = ['josh', 'mia', 'brian', 'abram', 'emily']
new_users = ['sonya', 'mia', 'serra', 'ally', 'emily']
for name1 in current_users:
    for name2 in new_users:
        if name1 == name2:
            print(f"Hello {name1}, you need to enter a new username.")
        else:
            print("This username is available.")

# 5-11. Ordinal Numbers
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(numbers[0] + 'st')
print(numbers[1] + 'nd')
print(numbers[2] + 'rd')
print(numbers[3] + 'th')
print(numbers[4] + 'th')
print(numbers[5] + 'th')
print(numbers[6] + 'th')
print(numbers[7] + 'th')
print(numbers[8] + 'th')
