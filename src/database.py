import sqlite3, sys, os, utils, setup
from tabulate import tabulate

LOGGER = utils.LOGGER
PATH = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(PATH, 'Skylar.db')

# ==============================================================================================================
# ADMIN TABLE FUNCTIONS
# ==============================================================================================================
def create_tables():
    '''
    Initializes the empty tables.

    Parameter(s): None

    Output(s): 
        Bool: returns true if the tables are created, else returns false
    '''
    
    try:
        with sqlite3.connect(DATABASE) as conn:      

            c = conn.cursor()
            # Force forgein key support
            c.execute("PRAGMA foreign_keys = ON;")

            # Customer Elements
            LOGGER.info("Creating Customer Table...")
            c.execute("""CREATE TABLE Customer(
                    cid INTEGER PRIMARY KEY AUTOINCREMENT,
                    cname TEXT,
                    address TEXT,
                    city TEXT,
                    state TEXT
            )""")
        
            # Customer contact information
            LOGGER.info("Creating ContactInfo Table...")
            c.execute("""CREATE TABLE ContactInfo(
                    cid INTEGER,
                    type TEXT, 
                    value TEXT,
                    PRIMARY KEY (cid, type, value),
                    FOREIGN KEY (cid) REFERENCES Customer(cid)
            )""")

            # Owner information
            LOGGER.info("Creating Owner Table...")
            c.execute("""CREATE TABLE Owner(
                    Oid INTEGER PRIMARY KEY AUTOINCREMENT,
                    oname TEXT
            )""")

            # Restaurant information
            LOGGER.info("Creating Restaurant Table...")
            c.execute("""CREATE TABLE Restaurant(
                    rid INTEGER PRIMARY KEY AUTOINCREMENT,
                    rname TEXT,
                    city TEXT,
                    state TEXT,
                    rating TEXT,
                    ownerID INTEGER,
                    FOREIGN KEY (ownerID) REFERENCES Owner(Oid)
            )""")

            # Reservation information
            LOGGER.info("Creating Reservation Table...")
            c.execute("""CREATE TABLE Reservation(
                    cid INTEGER,
                    rid INTEGER,
                    date TEXT,
                    num_adults INTEGER,
                    num_child INTEGER,
                    PRIMARY KEY (cid, rid),
                    FOREIGN KEY (cid) REFERENCES Customer(cid),
                    FOREIGN KEY (rid) REFERENCES Restaurant(rid)
            )""")

            conn.commit()
        
        return True
        
    except Exception as e:
        LOGGER.error(f"An error occured when creating tables: {e}")

# ==============================================================================================================
def clear_tables():
    '''
    Clears all the data from the tables.

    Parameter(s): None

    Output(s): 
        Bool: returns true if the tables are wiped, else returns false
    '''

    try:
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()

            # Get all table names
            tables = [table for table in get_tables().keys()]

            for table in tables:
                LOGGER.info(f"Deleting Data From {table} Table...")
                c.execute(f"DELETE FROM {table}")

            conn.commit()

        return True
    
    except sqlite3.Error as e:
        LOGGER.error(f"An error occurred when deleting all records from the tables: {e}")
        return False

# ==============================================================================================================
def print_tables():
    '''
    Prints the contents of Skylar

    Parameter(s): None

    Output(s):
        Prints tables to command terminal
    '''

    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()

        # Get all table names
        table_info = get_tables()

        for table, values in table_info.items():
            print(f"{table} Table Data:")
            c.execute(f"SELECT * FROM {table}")
            data = c.fetchall()
            print(tabulate(data, headers=values, tablefmt="grid"))

        conn.commit()

# ==============================================================================================================
def drop_table(table_name:str):
    '''
    Drops the selected table from the database

    Parameter(s):
        table_name (str): name of the table being dropped

    Output(s):
        True if the table was successfully dropped, else False
    '''
    try:
        with sqlite3.connect(DATABASE) as conn:
            LOGGER.info(f"Dropping {table_name} from the database ...")

            c = conn.cursor()
            c.execute(f"DROP TABLE IF EXISTS {table_name}")
            conn.commit()

        return True

    except Exception as e:
        LOGGER.error(f"An error occured when dropping {table_name} from the database: {e}")
        return False
    
# ==============================================================================================================
def drop_all_tables():
    '''
    Drops all the tables from the database

    Parameter(s): None

    Output(s):
        True if the table was successfully dropped, else False
    '''
    try:
        # Get all table names
        tables = [table for table in get_tables().keys()]
        # Drop all tables
        deleted = [drop_table(table) for table in tables]

        if False in deleted:
            raise Exception("Failed to delete table!")

        return True

    except Exception as e:
        LOGGER.error(f"An error occured when dropping tables from the database: {e}")
        return False

# ==============================================================================================================
# DATABASE INSERTION FUNCTIONS
# ==============================================================================================================
def insert_customer(cname:str, address:str, city:str, state:str):
    '''
    Inserts the customer data in the database
    
    Parameter(s):
        cname (str): customer name
        address (str): the street address of the customer's home
        city (str): the city in which the customer resides
        state (str): the state in which the customer lives
    
    Output(s)
        A primary key (int) that represents the customer in the Customer table if added, else None
    '''

    try:
        with sqlite3.connect(DATABASE) as conn:      

            c = conn.cursor()
            c.execute("INSERT INTO Customer (cname, address, city, state) VALUES (?,?,?,?)", (cname, address, city, state))
            conn.commit()

            key = c.lastrowid
        
            return key
        
    except Exception as e:
        LOGGER.error(f"An error occured when inserting into Customer table: {e}")
        return None

# ==============================================================================================================
def insert_contact(key:int, type:str, value:str):
    '''
    Inserts the contact information of a customer
    
    Parameter(s):
        key (int): the primary key referencing the customer
        type (str): the contact type such as an email or phone number
        value (str): an email address or phone number
    
    Output(s):
        True if the contact is successfully added, else false
    '''

    try:
        with sqlite3.connect(DATABASE) as conn:      

            c = conn.cursor()
            c.execute("INSERT INTO ContactInfo (cid, type, value) VALUES (?,?,?)", (key, type, value))
            conn.commit()
        
        return True
        
    except Exception as e:
        LOGGER.error(f"An error occured when inserting into ContactInfo table: {e}")
        return False
    
# ==============================================================================================================
def insert_owner(oname:str):
    '''
    Inserts the owner data into the database
    
    Parameter(s):
        oname (str): name of the owner
    
    Output(s):
        A primary key (int) that represents the owner in the Owner table if added, else None
    '''
    try:
        with sqlite3.connect(DATABASE) as conn:

            c = conn.cursor()
            c.execute("INSERT INTO Owner (oname) VALUES (?)", (oname,))
            conn.commit()

            key = c.lastrowid
        
            return key
        
    except Exception as e:
        LOGGER.error(f"An error occured when inserting into Owner table: {e}")
        return None

# ==============================================================================================================
def insert_restaurant(rname:str, city:str, state:str, rating:int, ownerID:int):
    '''
    Inserts the reservation data into the database
    
    Parameter(s):
        rname (str): name of the restaurant
        city (str): city in which the restaurant is located
        state (str): state in which the restaurant is located
        rating (int): the customer rating of the restaurant
        ownerID (int): the primary key of the owner of the restaurant
        
    Output(s):
        True if the restaurant is successfully added, else false
    '''

    try:
        with sqlite3.connect(DATABASE) as conn:

            c = conn.cursor()
            c.execute("INSERT INTO Restaurant (rname, city, state, rating, ownerID) VALUES (?,?,?,?,?)", (rname, city, state, rating, ownerID))
            conn.commit()
        
        return True
        
    except Exception as e:
        LOGGER.error(f"An error occured when inserting into Reservation table: {e}")
        return False

# ==============================================================================================================
def insert_reservation(cid:int, rid:int, date:str, num_adults:int, num_child:int):
    '''
    Inserts the reservation data into the database
    
    Parameter(s):
        cid (int): customer primary key
        rid (int): restaurant primary key
        data (str): day and time the reservantion is placed
        num_adults (int): the number of adults attending
        num_child (int): the number of children attending
        
    Output(s):
        True if the reservation is successfully added, else false
    '''

    try:
        with sqlite3.connect(DATABASE) as conn:      

            c = conn.cursor()
            c.execute("INSERT INTO Reservation (cid, rid, date, num_adults, num_child) VALUES (?,?,?,?,?)", (cid, rid, date, num_adults, num_child))
            conn.commit()
        
        return True
        
    except Exception as e:
        LOGGER.error(f"An error occured when inserting into Reservation table: {e}")
        return False

# ==============================================================================================================
# ABSTRACT DATABASE FUNCTIONS
# ==============================================================================================================
def verify_query(table_name:str, query_id:tuple=None):
    '''
    Verifies the user defined inputs to mitigate sql injection

    Parameter(s):
        table_name (str): table where data is being added
        query_id (tuple, default=None): column names where the data is being queried
        
    Output(s):
        Returns True if the inputs are valid, esle False
    '''
    # Whitelist of allowed column names for each table
    table_info = get_tables()

    # Current table is not valid
    if table_name not in table_info.keys():
        LOGGER.error(f"{table_name} is not a valid table!")
        return False

    invalid_columns = []
    # Check for invalid column names
    if query_id:
        invalid_columns = [col for col in query_id if col not in table_info.get(table_name, [])]

    # Current column names are invalid
    if invalid_columns:
        LOGGER.error((f"Invalid column name(s): {', '.join(invalid_columns)}"))
        return False
    
    return True

# ==============================================================================================================
def insert_query(table_name:str, query_id:tuple, query_set:tuple):
    '''
    Inserts the relavent data into the database
    
    Parameter(s):
        table_name (str): table where data is being added
        query_id (tuple): column names where the data is being inserted
        query_set (tuple): data being added to the table
        
    Output(s):
        True if the data is successfully added, else false
    '''

    try:
        # Check if the lengths match
        if len(query_id) != len(query_set):
            raise ValueError("Length of query_id and query_set mismatch")
        
        # Check validity of the input data
        if not verify_query(table_name=table_name, query_id=query_id):
            raise ValueError("Invalid table or column name entered!")
        
        # Build Input query string
        placeholders = ', '.join(['?' for _ in query_id])
        columns = ', '.join(query_id)
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        with sqlite3.connect(DATABASE) as conn:      

            c = conn.cursor()
            c.execute(query, query_set)
            conn.commit()
        
        return True
        
    except Exception as e:
        LOGGER.error(f"An error occured when inserting into data into {table_name}: {e}")
        return False

# ==============================================================================================================
def select_query(table_name:str, query_id:tuple=None):
    '''
    Retrieves the relavent data from the database
    
    Parameter(s):
        table_name (str): table where data is being accessed
        query_id (tuple, default=None): column names where the data is being selected from if provided, else
            select all the table attributes
        
    Output(s):
        response (list): a list of the queried data formatted into a dictionary
            response = [{col1: value1, col2: value1, ...}, {col1: value2, col2: value2, ...}, ...]
    '''
    response = []

    try:
        # Check if the inputs are valid
        if not verify_query(table_name=table_name, query_id=query_id):
            raise ValueError("Invalid table or column name used!")
        
        # Format quiered columns
        if query_id: columns = ', '.join(query_id)
        else: columns = '*'
        
        # Build Input query string
        query = f"SELECT {columns} FROM {table_name}"

        with sqlite3.connect(DATABASE) as conn:      
            c = conn.cursor()

            # Get the column names of all fields
            if not query_id:
                c.execute(f"PRAGMA table_info({table_name})")
                columns_info = c.fetchall()
                query_id = [info[1] for info in columns_info]

            # Get the queried data
            c.execute(query)
            data = c.fetchall()

            # Convert the queried data from tuples to dictionaries
            for d in data:
                keys = query_id
                response.append({key: value for key, value in zip(keys, d)})
        
    except Exception as e:
        LOGGER.error(f"An error occured when selecting data from {table_name}: {e}")
    
    return response
    
# ==============================================================================================================
def db_query(query:str):
    '''
    Executes a user defined CRUD operation in the database

    Parameter(s):
        query (str): user defined 

    Output(s):
        repsonse (list, default={}): a dictionary containing the relanvent data to the query, an 
        error message if the query fails, or an empty dict if the query isn't a SELECT type 
        (create, update, or delete)

        response = {
            'column_id': [column_name1, column_name2, ... ],
            'data': [(value_1, value_2, ...), (value_1, value_2, ...), ... ],
            'error': 'Error Message'
        }
    '''
    response = {}

    try:
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()

            LOGGER.info(f"Executing Query:\n{query}")
            c.execute(query)

            # Get selected data if there is any
            if query.strip().upper().startswith('SELECT'):
                response['column_id'] = [column[0] for column in c.description]     # Column names
                response['data'] = c.fetchall()                                     # Queried data

            conn.commit()

        return response
    
    except sqlite3.Error as e:
        LOGGER.error(f"An error occurred when executing the query {query}: {e}")
        response['error'] = f"An error occurred when executing the query {query}: {e}"

        return response

# ==============================================================================================================
def get_tables():
    '''
    Retrieves all the tables and their column names in the Skylar database
    
    Parameter(s): None
    
    Output(s):
        response (dict): a dictionary containing the table names as keys and a list of the column names as values
    ''' 
    response = {}
    try:
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()

            # Get all the table names in the database
            LOGGER.info(f"Retrieving table info from the database ...")
            c.execute('SELECT * FROM sqlite_master WHERE type="table" AND name NOT LIKE "sqlite_%"')
            tables = [table[1] for table in c.fetchall()]

            # Get the column names of the tables
            for table in tables:
                c.execute(f"PRAGMA table_info({table})")
                columns_info = c.fetchall()
                response[table] = [info[1] for info in columns_info]

        return response
    
    except sqlite3.Error as e:
        LOGGER.error(f"An error occurred when retrieving tables info from the database: {e}")
        return response
    
# ==============================================================================================================
def init_database(new_db:bool=False, file:str=None):
    '''
    Initializes the database with new or refreshed tables
    
    Parameter(s):
        new_db (bool, default=False): initialized the database with new data if true, else inits it with the data from a JSON file
        file (str, default=None): name of the JSON file used to migrate the data to the database

    Ouput(s):
        True if the database is successfully initialized, else False
    '''
    try:
        # Init database with new data
        if new_db: setup.Init_db()
        # Init database with data from input json
        elif not new_db and file: setup.from_json(file=file)
        # Init database with old json file
        else: setup.from_json()

        return True
    
    except Exception as e:
        LOGGER.error(f"An error occurred when initializing the database: {e}")
        return False

# ==============================================================================================================
if __name__ == "__main__":
    '''
    Handles command line entries to manually set the database tables

    Parameter(s): 
        Two system arguments that include a input flag: 
        python ./init_db.py [flag]

    flag(s):
        Create tables, "-c", initializes the Flashcard and Figure tables
        Clear tables, "-d", deletes all the rows in both tables
        Print tables, "-p", prints all the rows in both tables

    Output(s): None
    '''

    # python .\phylogeny.py input_file
    if(len(sys.argv) != 2):
        print(f"Only two inputs allowed, {len(sys.argv)} were entered!")
    # Create Tables
    elif(sys.argv[1] == "-c"): create_tables()
    # Delete Tables
    elif(sys.argv[1] == "-d"): clear_tables()
    # Print Tables
    elif(sys.argv[1] == "-p"): print_tables()
    # Print table info
    elif(sys.argv[1] == "-i"): print(get_tables())

    else:
        print(f"Invalid Arguments!\n"
              f"Create Tables: -c\n"
              f"Delete Tables: -d\n"
              f"Print Tables: -p\n"
              f"Print Table Info: -i\n")