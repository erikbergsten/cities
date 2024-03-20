import json
import random

# Function to generate a random city name
def generate_city_name():
    prefixes = ['North', 'South', 'New', 'East', 'West', 'Lake', 'Port']
    names = ['York', 'Derry', 'London', 'Chester', 'Burming', 'Random']
    suffixes = ['town', 'ville', 'city', 'burg', 'stead', 'ton', 'land']
    name = random.choice(prefixes) + ' ' + random.choice(names) + random.choice(suffixes)
    return name

# Function to generate a random city description
def generate_city_description():
    adjectives = ['beautiful', 'bustling', 'peaceful', 'thriving', 'picturesque']
    nouns = ['community', 'city', 'town', 'capital', 'metropolis']
    description = f"A {random.choice(adjectives)} {random.choice(nouns)} known for its hospitality."
    return description

# Function to generate a random longitude and latitude
def generate_random_location():
    # Longitude values can range from -180 to 180 and latitude values range from -90 to 90
    longitude = round(random.uniform(-180, 180), 2)
    latitude = round(random.uniform(-90, 90), 2)
    return [longitude, latitude]

# Function to generate a list of made-up cities
def generate_cities(num_cities):
    cities_list = []
    for _ in range(num_cities):
        city = {
            "name": generate_city_name(),
            "description": generate_city_description(),
            "location": generate_random_location()
        }
        cities_list.append(city)
    return cities_list

# Number of cities to generate
num_cities_to_generate = 1000

# Generate the cities
cities = generate_cities(num_cities_to_generate)

# Print the JSON output
print(json.dumps(cities, indent=2))
