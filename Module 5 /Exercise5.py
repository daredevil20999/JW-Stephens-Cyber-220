# 8-3. T-Shirt
def make_shirt():
    size_input = input("What size do you want your shirt?")
    message_input = input("What message do you want on your shirt?")
    print(f"Your shirt is{size_input}, and your message is {message_input}.")

make_shirt()


def shirt(size=None, message=None):
    if size is None:
        size_input = input("What size do you want your shirt? ")
    else:
        size_input = size

    if message is None:
        message_input = input("What message do you want on your shirt? ")
    else:
        message_input = message

    print(f"Your shirt is {size_input}, and your message is '{message_input}'.")

shirt(size="medium", message="Hello, World!")

# 8-4. Large Shirts
def make_shirts(size='large', message='CTF is Fun!'):
    print(f"Your shirt is a size {size}, and your message is '{message}'.")

make_shirts()


make_shirts(size='medium')
make_shirts(size= 'extra-large', message='I love AU!')

# 8-5. Cities
def describe_city(city='London', country='England'):
    print(f"{city} is in {country}.")
describe_city()

describe_city(city='Liverpool')

describe_city(city='New York', country='The United States')

# 8-6. City Names
def city_country(city, country):
    return f"{city.title()}, {country.title()}"
print(city_country('La Paz', 'Bolivia'))
print(city_country('Jerusalem', 'Israel'))
print(city_country('Tegucigalpa', 'Honduras'))
