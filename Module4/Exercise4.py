# Dictionaries
person_dict = {
    'f_name': 'Abram',
    'l_name': 'Danielson',
    'age': 30,
    'hometown': 'Fairfax',
    'current_city': 'Anderson',
    'username': 'filetforceones'
}
# Print the entire dictionary
print('Person Dictionary:')
print(person_dict)
print()
# Print each individual key
print("First Name: " + person_dict['f_name'])
print("Last Name: " + person_dict['l_name'])
print("Age: " + str(person_dict['age']))
print("Hometown: " + person_dict['hometown'])
print("Current City: " + person_dict['current_city'])
print("Username: " + person_dict['username'])

# Part 2
print(f"This person's first name is {person_dict['f_name']}, last name is {person_dict['l_name']}, "
      f"and their username is {person_dict['username']}.")
print(f"For security reasons, we might ask them for their hometown, which is {person_dict['hometown']}.")

# Part 3 and 4
definitions = {
    'python': 'popular computer programming language',
    'variable': 'stores values',
    'list': 'mutable sequence of elements',
    'method': 'functions that can manipulate objects',
    'if statement': 'used to check a condition and execute if the condition is true',
    'dictionary': 'stores items in key-value pairs',
    'function': 'block of code that runs when it is called'
}
for key, value in definitions.items():
    print(f"{key.capitalize()}:\n{value}\n")

# Part 5
counties_dict = {
    'Abbeville County': 'Abbeville',
    'Beaufort County': 'Beaufort',
    'Anderson County': 'Anderson',
    'Chesterfield County': 'Chesterfield',
    'Edgefield County': 'Edgefield',
    'Lee County:': 'Bishopville'
}
# Part 6
counties = ['Abbeville County', 'Beaufort County', 'Anderson County', 'Chesterfield County', 'Edgefield County',
            'Lee County', 'Oconee County', 'Richland County', 'Marlboro County', 'Saluda County']
for county in counties:
    if county in counties_dict.keys():
        print(f"{county} is in our dictionary, and the capital/seat is {counties_dict[county]}.")
    else:
        print(f"{county} is not in our dictionary. We will add this county shortly. Thanks!")

# Part 7
county1 = {'Richland': {'Columbia': 133451, 'Forest Acres': 10977, 'Irmo': 11767, 'Blythewood': 3862, 'Hopkins': 3090}}
county2 = {'Charleston': {'Charleston': 150277, 'North Charleston':
    115382, 'Mount Pleasant': 92026, 'Summerville': 52484, 'Goose Creek': 42979}}
county3 = {'Greenville': {'Greenville': 70473, 'Simpsonville': 23980,
                          'Mauldin': 25282, 'Easley': 22212, 'Greer': 34389}}
county4 = {'Horry': {'Myrtle Beach': 35321, 'Conway': 25427, 'North Myrtle '
                                                             'Beach': 16390, 'Surfside Beach': 4037, 'Aynor': 862}}
county5 = {'Spartanburg': {'Spartanburg': 37544, 'Greer': 34389, 'Boiling Springs':
    9415, 'Woodruff': 4127, 'Inman': 2554}}

counties_list = [county1, county2, county3, county4, county5]

for county in counties_list:
    for city, population in county.items():
        for city_name, population_number in population.items():
            print(f"In {city_name.title()}, the current population is {population_number}.")

# Part 8

sc_counties = {
    'Greenville': ['Greenville City', 'Simpsonville', 'Mauldin'],
    'Richland': ['Columbia', 'Forest Acres', 'Irmo'],
    'Charleston': ['Charleston', 'North Charleston', 'Mount Pleasant'],
    'Horry': ['Myrtle Beach', 'Conway', 'North Myrtle Beach'],
    'Lexington': ['Lexington', 'Irmo', 'Cayce']
}

for county, cities in sc_counties.items():
    print(f"In {county} County, the largest cities are {', '.join(cities)}.")

# User Input
user_input = input("What is your name?")
print(f"Welcome to Anderson University, {user_input}!")

# Part 2
money_input = input("How much money do you have? (Enter in digits)")
cash = int(money_input)
if cash >= 550:
    print("You can afford an i9 processor.")
elif cash >= 450:
    print("You can afford an i7 processor.")
elif cash >= 350:
    print("You can afford an i5 processor.")
elif cash >= 250:
    print("You can afford an i3 processor.")
else:
    print("You cannot afford any processors.")

# Part 3
user_input = input("Enter an integer. (Type 'end' to close the program.")

if user_input.lower() == 'exit':
    print("Closing the program. Goodbye.")
else:
    print("This is an incorrect input, please try again.")
number = int(user_input)
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Part 4
def program():
    active = True

    while active:
        user4_input = input("Enter a string value (type 'quit' to exit the program): ")
        if user4_input.lower() == 'quit':
            print("Exiting Program.")
            break
        print(f"Your input is {user4_input}. What does this mean to you?")
program()
# Part 5 
flavors = ["Ubuntu", "Kubuntu", "Ubuntu Cinnamon", "Lubuntu", "Ubuntu Budgie", "Edubuntu"]

user_poll = {}

while True:
    username = input("Enter your username (type 'exit' to end): ")

    if username.lower() == 'exit':
        break

    flavor = input("Enter your favorite Ubuntu flavor: ")

    if flavor in flavors:
        user_poll[username] = flavor
    else:
        print(
            f"{username}, you have entered an invalid Ubuntu flavor. Please choose from the following valid options: {', '.join(flavors)}")

print("\nPoll Results:")
for username, flavor in user_poll.items():
    print(f"{username}: {flavor}")
