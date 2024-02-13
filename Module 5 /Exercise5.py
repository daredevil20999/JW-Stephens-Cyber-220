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

# 8-7. Album

def make_album(name, title, songs='None'):
    album = {'artist': name, 'title': title}
    if songs:
        album['songs'] = songs
    return album

album1 = make_album('Rod Wave', 'Soulfly')
album2 = make_album('Travis Scott', 'Utopia', songs = 14)

print(album1)
print(album2)

# 8-8 User Albums

def make_album(artist, album, number_of_songs=None):
    album = {'artist': artist, 'title': album}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

while True:
    artist = input("Enter the artist's name (or 'q' to quit): ")
    if artist.lower() == 'q':
        break

    album = input("Enter the album's title (or 'q' to quit): ")
    if album.lower() == 'q':
        break

    album_info = make_album(artist, album)
    print(album_info)
    
# 8-9. Messages
def show_messages(messages):
    for message in messages:
        print(message)

messages = ['wyd?', 'When are we eating?', "I don't like football."]

show_messages(messages)
