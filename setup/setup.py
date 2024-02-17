'''
NOTE: This is a single use program used to generate a json file used for populating the database tables
'''
import random

NAMES = [
    ('John', 'Doe'), ('Jane', 'Smith'), ('Michael', 'Johnson'), ('Emily', 'Brown'), ('William', 'Jones'), ('Emma', 'Davis'), 
    ('Daniel', 'Martinez'), ('Olivia', 'Garcia'), ('James', 'Rodriguez'), ('Sophia', 'Wilson'), ('Liam', 'Miller'), ('Isabella', 'Taylor'),
    ('Benjamin', 'Anderson'), ('Ava', 'Thomas'), ('Jacob', 'Jackson'), ('Mia', 'White'), ('Ethan', 'Harris'), ('Charlotte', 'Martin'),
    ('Alexander', 'Thompson'), ('Amelia', 'Robinson'), ('Michael', 'Lewis'), ('Harper', 'Walker'), ('Matthew', 'Allen'), ('Ella', 'Young'),
    ('Daniel', 'Hill'), ('Abigail', 'Scott'), ('William', 'Nelson'), ('Emily', 'King'), ('David', 'Carter'), ('Sofia', 'Mitchell'),
    ('Joseph', 'Perez'), ('Victoria', 'Roberts'), ('Christopher', 'Turner'), ('Grace', 'Phillips'), ('Andrew', 'Campbell'), ('Chloe', 'Parker'),
    ('Samuel', 'Evans'), ('Zoe', 'Edwards'), ('John', 'Collins'), ('Lillian', 'Stewart'), ('Ryan', 'Morris'), ('Addison', 'Murphy'),
    ('Nathan', 'Rogers'), ('Audrey', 'Cook'), ('Anthony', 'Morgan'), ('Scarlett', 'Cooper'), ('Logan', 'Peterson'), ('Evelyn', 'Reed'),
    ('Christian', 'Bailey'), ('Hannah', 'Kelly'), ('Dylan', 'Howard'), ('Brooklyn', 'Hughes'), ('Aaron', 'Long'), ('Avery', 'Foster'),
    ('Isaac', 'Sanders'), ('Madison', 'Bennett'), ('Caleb', 'Price'), ('Layla', 'Barnes'), ('Elijah', 'Wood'), ('Hailey', 'Ross'),
    ('Gabriel', 'Watson'), ('Aria', 'Bryant'), ('Logan', 'Gomez'), ('Sophie', 'Diaz'), ('James', 'Reyes'), ('Aubrey', 'Russell'),
    ('Luke', 'Hayes'), ('Leah', 'Henderson'), ('Christopher', 'Coleman'), ('Samantha', 'Simmons'), ('Isaiah', 'Patterson'), ('Allison', 'Jordan'),
    ('Elizabeth', 'Harrison'), ('Joshua', 'Gordon'), ('Aaliyah', 'Lynch'), ('David', 'Fisher'), ('Anna', 'Fowler'), ('Colton', 'Myers'),
    ('Mila', 'Sullivan'), ('Jonathan', 'Wallace'), ('Natalie', 'Lambert'), ('Nicholas', 'Lawrence'), ('Alyssa', 'Weaver'), ('Jordan', 'Bishop'),
    ('Lincoln', 'Barker'), ('Brianna', 'Pearson'), ('Hunter', 'Hansen'), ('Alexis', 'Keller'), ('Julian', 'Burns'), ('Claire', 'Bates'),
    ('Jackson', 'Norton'), ('Stella', 'Hale'), ('Greyson', 'Griffin'), ('Lauren', 'Adams'), ('Mason', 'Black')
]

CITY_STATE = [
    ('New York City', 'NY'), ('Los Angeles', 'CA'), ('Chicago', 'IL'), ('Houston', 'TX'), ('Phoenix', 'AZ'),
    ('Philadelphia', 'PA'), ('San Antonio', 'TX'), ('San Diego', 'CA'), ('Dallas', 'TX'), ('San Jose', 'CA'),
    ('Austin', 'TX'), ('Jacksonville', 'FL'), ('Fort Worth', 'TX'), ('Columbus', 'OH'), ('Charlotte', 'NC'),
    ('San Francisco', 'CA'), ('Indianapolis', 'IN'), ('Seattle', 'WA'), ('Denver', 'CO'), ('Washington', 'DC'),
    ('Boston', 'MA'), ('El Paso', 'TX'), ('Nashville', 'TN'), ('Detroit', 'MI'), ('Oklahoma City', 'OK'),
    ('Portland', 'OR'), ('Las Vegas', 'NV'), ('Memphis', 'TN'), ('Louisville', 'KY'), ('Baltimore', 'MD'),
    ('Milwaukee', 'WI'), ('Albuquerque', 'NM'), ('Tucson', 'AZ'), ('Fresno', 'CA'), ('Sacramento', 'CA'),
    ('Mesa', 'AZ'), ('Kansas City', 'MO'), ('Atlanta', 'GA'), ('Long Beach', 'CA'), ('Colorado Springs', 'CO'),
    ('Raleigh', 'NC'), ('Miami', 'FL'), ('Virginia Beach', 'VA'), ('Omaha', 'NE'), ('Oakland', 'CA'),
    ('Minneapolis', 'MN'), ('Tulsa', 'OK'), ('Arlington', 'TX'), ('New Orleans', 'LA'), ('Wichita', 'KS'),
    ('Cleveland', 'OH'), ('Tampa', 'FL'), ('Bakersfield', 'CA'), ('Aurora', 'CO'), ('Anaheim', 'CA'),
    ('Honolulu', 'HI'), ('Santa Ana', 'CA'), ('Riverside', 'CA'), ('Corpus Christi', 'TX'), ('Lexington', 'KY'),
    ('Stockton', 'CA'), ('St. Louis', 'MO'), ('Saint Paul', 'MN'), ('Henderson', 'NV'), ('Pittsburgh', 'PA'),
    ('Cincinnati', 'OH'), ('Anchorage', 'AK'), ('Greensboro', 'NC'), ('Plano', 'TX'), ('Newark', 'NJ'),
    ('Lincoln', 'NE'), ('Orlando', 'FL'), ('Irvine', 'CA'), ('Toledo', 'OH'), ('Jersey City', 'NJ'),
    ('Chula Vista', 'CA'), ('Durham', 'NC'), ('Fort Wayne', 'IN'), ('St. Petersburg', 'FL'), ('Laredo', 'TX'),
    ('Buffalo', 'NY'), ('Madison', 'WI'), ('Lubbock', 'TX'), ('Chandler', 'AZ'), ('Scottsdale', 'AZ'),
    ('Reno', 'NV'), ('Glendale', 'AZ'), ('Norfolk', 'VA'), ('Winston-Salem', 'NC'), ('North Las Vegas', 'NV'),
    ('Irving', 'TX'), ('Chesapeake', 'VA'), ('Gilbert', 'AZ'), ('Hialeah', 'FL')
]

STREET_ADDRESSES = [
    '1234 Pine St', '5678 Main St', '987 Cedar Ln', '456 Elm St', '789 Maple Ave',
    '321 Washington St', '654 Park Ave', '101 Lake St', '2468 First St', '1357 Oak St',
    '246 Pine St', '789 Main St', '123 Maple Ave', '456 Washington St', '789 Cedar Ln',
    '1234 Park Ave', '567 Lake St', '901 First St', '234 Oak St', '567 Main St',
    '890 Cedar Ln', '123 Washington St', '456 Park Ave', '789 Lake St', '234 First St',
    '567 Pine St', '890 Main St', '123 Cedar Ln', '456 Washington St', '789 Oak St',
    '234 Park Ave', '567 Lake St', '890 First St', '123 Main St', '456 Cedar Ln',
    '789 Washington St', '123 Oak St', '456 Park Ave', '789 Cedar Ln', '1234 Pine St',
    '567 Main St', '890 Park Ave', '123 Lake St', '456 First St', '789 Oak St',
    '1234 Washington St', '567 Park Ave', '890 Cedar Ln', '123 Main St', '456 Maple Ave',
    '789 Washington St', '123 Pine St', '456 Park Ave', '789 Lake St', '1234 First St',
    '567 Main St', '890 Cedar Ln', '123 Oak St', '456 Washington St', '789 Park Ave',
    '123 Lake St', '456 Main St', '789 Cedar Ln', '1234 Washington St', '567 Park Ave',
    '890 Cedar Ln', '123 Main St', '456 Maple Ave', '789 Washington St', '123 Pine St',
    '456 Park Ave', '789 Lake St', '1234 First St', '567 Main St', '890 Cedar Ln',
    '123 Oak St', '456 Washington St', '789 Park Ave', '123 Lake St', '456 Main St',
    '789 Cedar Ln', '1234 Washington St', '567 Park Ave', '890 Cedar Ln', '123 Main St',
    '456 Maple Ave', '789 Washington St', '123 Pine St', '456 Park Ave', '789 Lake St',
    '1234 First St', '567 Main St', '890 Cedar Ln', '123 Oak St', '456 Washington St',
    '789 Park Ave', '123 Lake St', '456 Main St', '789 Cedar Ln', '1234 Washington St',
    '567 Park Ave', '890 Cedar Ln', '123 Main St', '456 Maple Ave', '789 Washington St',
    '123 Pine St', '456 Park Ave', '789 Lake St', '1234 First St'
]

RESTAURANTS = [
    "The Hungry Fox", "Golden Spoon", "Mama Mia's Pizzeria", "Sizzling Grill", "The Cozy Cafe",
    "Flavors of India", "Taste of Thailand", "Bella Italia", "Smokehouse BBQ", "The Green Leaf",
    "Casa del Sol", "Sushi Samurai", "El Rancho Mexican Grill", "Peking Garden", "Taste of Greece",
    "The Rusty Spoon", "Fire & Ice", "Cafe Paris", "Sunrise Diner", "Harborview Seafood",
    "La Piazza", "The Great Wall", "Fusion Bistro", "The Flying Pig", "Cinnamon Spice",
    "Blue Bayou", "Rustic Tavern", "Lucky Dragon", "Pho King", "The Olive Branch",
    "Sabor Latino", "Taste of Jamaica", "Misty Mountain Cafe", "Sushi Heaven", "Fiesta Mexicana",
    "Sweet Basil", "The Spice Route", "Burger Barn", "Cafe Luna", "Sunflower Cafe",
    "Mango Tango", "Savory Bites", "Ocean Grill", "Aloha Grill", "The Red Onion",
    "Taste of China", "Salsa Verde", "The Blue Plate", "The Roasted Bean", "Cafe Mosaic",
    "Bella Luna", "Sizzling Wok", "The Greek Garden", "Spice Island", "The Lazy Dog",
    "Thai Orchid", "Casa de Amigos", "Bollywood Bites", "The Hungry Pelican", "Taste of Morocco",
    "Smokey Joe's BBQ", "Taste of Vietnam", "The Brick Oven", "Cafe de Paris", "Sushi Bay",
    "The Mango Tree", "Taste of Argentina", "Rustic Roots", "The Green Turtle", "Flamingo Grill",
    "Taco Town", "The Rustic Cabin", "Spice Lounge", "The Bean Counter", "Bistro 101",
    "Cafe Soleil", "The Whistle Stop", "Bella Napoli", "Taste of Portugal", "Sushi House",
    "The Spice Market", "Chopsticks", "The Crispy Chicken", "The Tomato Vine", "Taste of the Islands",
    "Lighthouse Cafe", "The Wandering Chef", "Cafe Aurora", "The Copper Kettle", "Savor",
    "The Smiling Goat", "Pasta Perfection", "The Noodle House", "Sunny Side Up", "The Grill House",
    "Taste of Ethiopia", "The Lemon Tree", "Flourish", "The Laughing Cow", "Cafe Mirage"
]

# ==============================================================================================================
def generate_number():
    '''
    Generates a random phone number

    Parameter(s): None

    Output(s):
        A tuple containing the phone type and phone number, both are strings
    '''
    phone_types = ["home", "cell"]

    number = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    phone_type = random.choice(phone_types)

    return (phone_type, number)

# ==============================================================================================================
def generate_email():
    '''
    Generates a random email
    
    Parameter(s): None
    
    Output(s):
        A tuple containing the string email and the randomly generated email
    '''
    domains = ['gmail.com', 'yahoo.com', 'aol.com', 'outlook.com', 'hotmail.com', 'icloud.com']
    username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(5, 10)))
    domain = random.choice(domains)
    email = f"{username}@{domain}"

    return ('email', email)

# ==============================================================================================================
def generate_customers():
    '''
    Generates a list of customers and their info

    Parameter(s): None

    Output(s):
        a list of customer information
    '''
    customers = []

    # Iterate through all customer names
    for name in NAMES:

        full_name = f"{name[0]} {name[1]}"
        address = random.choice(STREET_ADDRESSES)
        city, state = random.choice(CITY_STATE)

        customers.append([full_name, address, city, state])

    return customers

# ==============================================================================================================