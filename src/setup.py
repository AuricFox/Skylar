'''
Used to populate an empty database with randomized data or migrate data to/from a JSON file
'''
import sys, random, json, utils, database
from datetime import datetime

LOGGER = utils.LOGGER

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
    ('Jackson', 'Norton'), ('Stella', 'Hale'), ('Greyson', 'Griffin'), ('Lauren', 'Adams'), ('Mason', 'Black'), ('Jack', 'Brown'),
    ('Peter', 'Williams'), ('Isaac', 'Newton'), ('Bill', 'Hayes'), ('Howard', 'Clark')
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
# GENERATING DATA FOR THE TABLES
# ==============================================================================================================
def gen_number():
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
def gen_email():
    '''
    Generates a random email
    
    Parameter(s): None
    
    Output(s):
        An email string email that was randomly generated
    '''
    domains = ['gmail.com', 'yahoo.com', 'aol.com', 'outlook.com', 'hotmail.com', 'icloud.com']
    username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=random.randint(5, 10)))
    domain = random.choice(domains)
    email = f"{username}@{domain}"

    return email

# ==============================================================================================================
def gen_contacts(minc:int=0, maxc:int=3):
    '''
    Generates the contacts for an individual customer

    Parameter(s):
        minc (int, default=0): minimum number of contacts
        maxc (int, default=3): maximum number of contacts

    Output(s):
        A dictionary of email or phone numbers used as contacts
    '''
    contacts = []

    if minc < 0 or maxc < 0:
        LOGGER.warning(f"The number of contacts cannot be negative: min: {minc}, max: {maxc}")
        return contacts
    
    if maxc < minc:
        LOGGER.warning(f"The maximum number of contacts must be greater than the minimum number of contacts: min: {minc}, max: {maxc}")
        return contacts

    contact_types = ['email', 'home', 'cell']
    # The range of contacts a customer can have
    num_contacts = random.randint(minc, maxc)

    # Iterate thru the number of contacts
    for _ in range(num_contacts):
        contact_type = random.choice(contact_types)

        # Append to the email list
        if contact_type == 'email':
            contacts.append({
                'type': 'email',
                'value': gen_email()
            })
        
        # Append to the phone number list
        else:
            p_type, num = gen_number()
            contacts.append({
                'type': p_type, 
                'value': num
            })

    return contacts

# ==============================================================================================================
def gen_customers(num:int=100, minc:int=0, maxc:int=3):
    '''
    Generates the customers and their info

    Parameter(s):
        num (int, default=100): number of customers
        minc (int, default=0): minimum number of contacts
        maxc (int, default=3): maximum number of contacts

    Output(s):
        a dictionary list of customer information
    '''
    customers = []

    if num < 0:
        LOGGER.warning(f"Number of customers must be positive: {num}")
        return customers
    
    if minc < 0 or maxc < 0:
        LOGGER.warning(f"The number of contacts cannot be negative: min: {minc}, max: {maxc}")
        return customers
    
    if maxc < minc:
        LOGGER.warning(f"The maximum number of contacts must be greater than the minimum number of contacts: min: {minc}, max: {maxc}")
        return customers

    for i in range(num):
        # Get a name from the list
        name = NAMES[i % len(NAMES)]

        full_name = f"{name[0]} {name[1]}"
        address = random.choice(STREET_ADDRESSES)
        city, state = random.choice(CITY_STATE)

        contacts = gen_contacts(minc=minc, maxc=maxc)

        customers.append({
            'cname': full_name, 
            'address': address, 
            'city': city, 
            'state': state,
            'contacts': contacts
        })

    return customers

# ==============================================================================================================
def gen_owners(num:int=25, min_res:int=0, max_res:int=5):
    '''
    Generates a list of owners and the restaurants they own
    
    Parameter(s):
        num (int, default=25): number of owners
        min_res (int, default=0): minimum number of owned restaurants
        max_res (int, default=5): maximum number of owned restaurants
    
    Output(s):
        A dictionary list of restaurant owner infomation
    '''
    owners = []

    if num < 0:
        LOGGER.error(f"The number of owners must be positive: {num}")

    if min_res < 0 or max_res < 0:
        LOGGER.error(f"Number of restaurants must be positive: min: {min_res}, max: {max_res}")
        return owners

    if max_res < min_res:
        LOGGER.error(f"The maximum number of restaurants must be greater then the minimum number of restaurants: min: {min_res}, max: {max_res}")
        return owners

    for _ in range(num):
        full_name = ' '.join(random.choice(NAMES))
        restaurants = []

        # Build a list of the owner's restaurants
        for _ in range(random.randint(min_res, max_res)):
            restaurant = random.choice(RESTAURANTS)
            city, state = random.choice(CITY_STATE)
            rating = random.randint(0,5)

            restaurants.append({
                'rname': restaurant,
                'city': city,
                'state': state,
                'rating': rating
            })

        owners.append({
            'oname': full_name,
            'restaurants': restaurants
        })
    
    return owners

# ==============================================================================================================
def gen_date(start:int=2000, end:int=2030):
    '''
    Generates a random data (YYYY-MM-DD HH:MM)
    
    Parameter(s):
        start (int, default=2000): starting year
        end (int, default=2030): ending year

    Output(s):
        A randomly generated date as a string
    '''

    year = random.randint(start, end)
    month = random.randint(1, 12)

    # Month of February
    if month == 2: 
        day = random.randint(1, 28)
    # Months with 30 days
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    # Months with 31 days
    else:
        day = random.randint(1, 31)

    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    
    date_time = datetime(year, month, day, hour, minute)
    return date_time.strftime('%Y-%m-%d %H:%M')

# ==============================================================================================================
def gen_reservations(num:int=30):
    '''
    Generates a list of reservation data

    NOTE: Must be run after the customer and restaurant data has been added to the tables,
    Otherwise no reservations will be created.

    Parameter(s):
        num (int, default=30): number of reservations

    Output(s):
        A dictionary list of reservation information
    '''
    reservations = []

    if num < 0:
        LOGGER.error(f"Number of reservations must be positive: {num}")
        return reservations

    try:
        # Get all customer id's
        customers = database.select_query(table_name='Customer', query_id=('cid',))
        # Get all restaurant id's
        restaurants = database.select_query(table_name='Restaurant', query_id=('rid',))
        
        # No reservations can be placed
        if customers == [] or restaurants == []: 
            return restaurants
        # Generate random reservations
        for _ in range(num):
            reservations.append({
                'cid': random.choice(customers)['cid'],     # Save customer cid
                'rid': random.choice(restaurants)['rid'],   # Save restaurant rid
                'date': gen_date(),
                'num_adults': random.randint(1,20),
                'num_child': random.randint(0,20)
            })
    
    except Exception as e:
        LOGGER.error(f"An error occured when generating reservations: {e}")
    
    return reservations

# ==============================================================================================================
# MIGRATING THE DATA
# ==============================================================================================================
def to_json(file:str='data.json'):
    '''
    Migrates the data in the database to a JSON file

    Parameter(s):
        file (str, default='data.json'): a file where the migrated data is saved

    Output(s):
        True if the data was successfully migrated to a JSON files and saves in the same directory

    JSON Format:
    {
        table_name: {
            'data': [
                {column_name: value, column_name: value, ... }, 
                {column_name: value, column_name: value, ... }, ... ], 
            'create': SQL_Create_Query
        },
        table_name: {
            'data': [
                {column_name: value, column_name: value, ... }, 
                {column_name: value, column_name: value, ... }, ... ], 
            'create': SQL_Create_Query
        },
        ....
    }
    '''
    try:
        LOGGER.info("Migrating data to JSON file ....")

        if not utils.verify_file(file=file):
            raise Exception("Invalid filename or type!")
        
        table_info = database.get_tables()
        data = {}

        # Package all the table info
        for table_name, value in table_info.items():
            data[table_name] = {
                'data': database.select_query(table_name=table_name),
                'create': value['create']
            }

        # Write data to the JSON file
        with open(file, 'w') as f:
            json.dump(data, f)

        return True

    except Exception as e:
        LOGGER.error(f"An error occured when migrating data to a json file: {e}")
        return False

# ==============================================================================================================
def from_json(file:str='data.json'):
    '''
    Migrates data from a JSON file to the database
    
    Parameter(s):
        file (str, default='data.json'): a json file where the data is being migrated from

    JSON Format:
    {
        table_name: {
            'data': [
                {column_name: value, column_name: value, ... }, 
                {column_name: value, column_name: value, ... }, ... ], 
            'create': SQL_Create_Query
        },
        table_name: {
            'data': [
                {column_name: value, column_name: value, ... }, 
                {column_name: value, column_name: value, ... }, ... ], 
            'create': SQL_Create_Query
        },
        ....
    }
    
    Output(s):
        True if the data is successfully migrated to the database, else False
    '''
    try:
        LOGGER.info("Migrating data from JSON file ....")

        if not utils.verify_file(file=file):
            raise Exception("Invalid filename or type!")
        
        # Drop all tables currently in the database
        if not database.drop_all_tables():
            raise Exception("Failed to drop all tables!")
        
        # Read data from the JSON file
        with open(file, "r") as f:
            data = json.load(f)

        # Get all create queries in data
        create_queries = [query['create'] for query in data.values()]
        if not database.create_query(queries=create_queries):
            raise Exception("Failed to create tables!")

        # Iterating over the json data
        for table_name,values in data.items():
            # Iterating over the table elements
            for row in values.get('data', []):
                query_id = tuple(row.keys())
                query_set = tuple(row.values())

                success = database.insert_query(table_name=table_name, query_id=query_id, query_set=query_set)
                
                if not success:
                    LOGGER.warning(f"Failed to insert data into table {table_name}: {query_set}")
        
        LOGGER.info("Successfully migrated data from JSON file!")
        return True
    
    except FileNotFoundError:
        LOGGER.error(f"File '{file}' not found!")
        return False
    
    except json.JSONDecodeError as e:
        LOGGER.error(f"Error decoding JSON file '{file}': {e}")
        return False
    
    except Exception as e:
        LOGGER.error(f"An error occurred when migrating data from JSON file '{file}': {e}")
        return False
# ==============================================================================================================
# POPULATING THE DATABASE
# ==============================================================================================================
class Init_db:
    def __init__(
            self,
            num_customers:int = 100,
            min_contacts:int = 0,
            max_contacts:int = 3,
            num_owers:int = 25,
            min_restaurants:int = 0,
            max_restaurants:int = 5,
            num_reservations:int = 30
    ):
        '''
        Populates the database by getting the randomly generated customer, contact, owner, and restaurant data. 
        The data is then added to the database afterwhich the reservation data is created and then added to the database
        
        Parameter(s):
            num_customers (int, default=100): number of customers
            min_contacts (int, default=0): minimum number of customer contacts
            max_contacts (int, default=3): maximum number of customer contacts
            num_owers (int, default=25): number of owners
            min_restaurants (int, default=0): minimum number of restaurants that can be owned
            max_restaurants (int, default=5): maximum number of restaurants that can be owned
            num_reservations (int, default=30): number of reservations
        
        Output(s): None
        '''
        # Clear the database
        database.drop_all_tables()
        # Reinitialize default tables
        database.create_tables()

        self.customers = gen_customers(num=num_customers, minc=min_contacts, maxc=max_contacts)
        self.owners = gen_owners(num=num_owers, min_res=min_restaurants, max_res=max_restaurants)

        self.add_customers()
        self.add_owners()
        self.add_reservations(num=num_reservations)
    
    # ----------------------------------------------------------------------------------------------------------
    def add_customers(self):
        '''
        Populates the Customer and ContactInfo tables in the database

        Parameter(s):
            self.customers must be populated with data

        Output(s):
            True if the customers and contacts are successfully added to the database, else False
        '''
        try:
            LOGGER.info("Adding customers and contact info to database...")

            # Add all the customers to the database
            for customer in self.customers:
                # Add the customer and get their primary key
                key = database.insert_customer(
                    cname=customer['cname'],
                    address=customer['address'],
                    city=customer['city'],
                    state=customer['state']
                )

                # Add all the customers contact info
                for contact in customer['contacts']:
                    database.insert_contact(
                        key=key,
                        type=contact['type'],
                        value=contact['value']
                    )

            LOGGER.info("Successfully added customers and contact info to the database!")
            return True
        
        except Exception as e:
            LOGGER.error(f'An error occured when adding customers and contact info to the database: {e}')
            return False
    
    # ----------------------------------------------------------------------------------------------------------
    def add_owners(self):
        '''
        Populates the Owner and Restaurant tables in the database

        Parameter(s):
            self.owners must be populated with data

        Output(s):
            True if the owners and restaurants are successfully added to the database, else False
        '''

        try:
            LOGGER.info("Adding Owners and Restaurants to database...")

            # Add all the owners to the database
            for owner in self.owners:
                # Add the owner and get their primary key
                key = database.insert_owner(
                    oname=owner['oname']
                )

                # Insert all the restaurants the owner has
                for restaurant in owner['restaurants']:
                    database.insert_restaurant(
                        rname=restaurant['rname'],
                        city=restaurant['city'],
                        state=restaurant['state'],
                        rating=restaurant['rating'],
                        ownerID=key
                    )

            LOGGER.info("Successfully added Owners and Restaurants to the database!")
            return True
        
        except Exception as e:
            LOGGER.error(f'An error occured when adding owners and restaurants to the database: {e}')
            return False
    
    # ----------------------------------------------------------------------------------------------------------
    def add_reservations(self, num:int=30):
        '''
        Populates the Reservation table in the database
        NOTE:The Customer and Restaurant tables must be populated

        Parameter(s):
            num (int, default=30): number of reservations

        Output(s):
            True if the reservations are successfully added to the database, else False
        '''
        try:
            LOGGER.info("Adding reservations to database...")
            reservations = gen_reservations(num=num)

            for reservation in reservations:
                database.insert_reservation(
                    cid=reservation['cid'],
                    rid=reservation['rid'],
                    date=reservation['date'],
                    num_adults=reservation['num_adults'],
                    num_child=reservation['num_child']
                )

            LOGGER.info("Successfully added Reservations to the database!")
            return True
        
        except Exception as e:
           LOGGER.error(f'An error occured when adding reservations to the database: {e}')
           return False
    
# ==============================================================================================================
if __name__ == '__main__':
    '''
    Handles command-line inputs
    
    Parameter(s):
        ./setup.py [flag] [filename]

    Flag(s):
        -g: generate tables
        -t: migrate data from tables to a JSON file
        -f: migrate data from a JSON file to the database tables
        -c: clear data from tables
        -p: print tabulated data from tables
    
    Output(s):
        -g: None, populates the database tables
        -t: a JSON file containing the migrated data
        -f: None, migrates the data to the database tables
        -c: None, clears all tables
        -p: None, prints the data to the command terminal
    '''

    if(len(sys.argv) == 2 and sys.argv[1] == "-g"): db = Init_db()                  # Populate the tables with data
    elif(len(sys.argv) == 2 and sys.argv[1] == "-t"): to_json(file='data.json')     # Migrate data to json file
    elif(len(sys.argv) == 3 and sys.argv[1] == "-t"): to_json(file=sys.argv[2])     # Migrate data to a user defined json file
    elif(len(sys.argv) == 2 and sys.argv[1] == "-f"): from_json(file='data.json')   # Migrate data from json file
    elif(len(sys.argv) == 3 and sys.argv[1] == "-f"): from_json(file=sys.argv[2])   # Migrate data from a user defined json file
    elif(len(sys.argv) == 2 and sys.argv[1] == "-c"): database.clear_tables()       # Clear database tables
    elif(len(sys.argv) == 2 and sys.argv[1] == "-p"): database.print_tables()       # Print table data to screen
    else: print("Invalid Arguments!")