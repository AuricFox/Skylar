import sqlite3, sys, utils as utils

LOGGER = utils.LOGGER

# ==============================================================================================================
def create_tables():
    '''
    Initializes the empty tables.

    Parameter(s): None

    Output(s): 
        Bool: returns true if the tables are created, else returns false
    '''
    
    try:
        with sqlite3.connect('Skylar.db') as conn:      

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
                    state TEXT,
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
        with sqlite3.connect('Skylar.db') as conn:
            c = conn.cursor()

            # Customer Elements
            LOGGER.info("Deleting Data From Customer Table...")
            c.execute("DELETE FROM Customer")
        
            # Customer contact information
            LOGGER.info("Deleting Data From ContactInfo Table...")
            c.execute("DELETE FROM ContactInfo")

            # Owner information
            LOGGER.info("Deleting Data From Owner Table...")
            c.execute("DELETE FROM Owner")

            # Restaurant information
            LOGGER.info("Deleting Data From Restaurant Table...")
            c.execute("DELETE FROM Restaurant")

            # Reservation information
            LOGGER.info("Deleting Data From Reservation Table...")
            c.execute("DELETE FROM Reservation")

            conn.commit()

        return True
    
    except sqlite3.Error as e:
        LOGGER.error(f"An error occurred when deleting all records from the tables: {e}")
        return False   

# ==============================================================================================================
def db_query(query:str):
    '''
    Executes a user defined CRUD operation in the database

    Parameter(s):
        query (str): user defined 

    Output(s):
        repsonse (list, default=[]): a list of tuples containing the relanvent data to the query, else an 
        empty list if the query fails or the query isn't a SELECT type (create, update, or delete)
    '''
    response = []

    try:
        with sqlite3.connect('Skylar.db') as conn:
            c = conn.cursor()

            LOGGER.info(f"Executing Query:\n{query}")
            c.execute(query)

            # Get selected data if there is any
            if query.strip().upper().startswith('SELECT'):
                response = c.fetchall()

            conn.commit()

        return response
    
    except sqlite3.Error as e:
        LOGGER.error(f"An error occurred when executing the query {query}: {e}")
        return response

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
    if(sys.argv[1] == "-c"): create_tables()
    # Delete Tables
    elif(sys.argv[1] == "-d"): clear_tables()
    else:
        print("Invalid Arguments!\nCreate Tables: -c\nDelete Tables: -d\n")