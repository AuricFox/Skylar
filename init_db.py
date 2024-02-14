import sqlite3, sys, os, utils
from tabulate import tabulate

LOGGER = utils.LOGGER

# ==============================================================================================================
def create_tables():
    '''
    Creates the tables used by the flask server.

    Parameter(s): None

    Output(s): 
        Bool: returns true if the tables are created, else returns false
    '''
    
    try:
        with sqlite3.connect('flashcards.db') as conn:      

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
                    cid INTEGER REFERENCES Customer(cid),
                    type TEXT, 
                    value TEXT
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
                    ownerID INTEGER REFERENCES Customer(Oid)
            )""")

            # Reservation information
            LOGGER.info("Creating Reservation Table...")
            c.execute("""CREATE TABLE Reservation(
                    cid INTEGER REFERENCES Customer(cid),
                    rid INTEGER REFERENCES Restaurant(rid),
                    date TEXT,
                    num_adults INTEGER,
                    num_child INTEGER
            )""")

            conn.commit()
        
        return True
        
    except Exception as e:
        LOGGER.error(f"An error occured when creating tables: {e}")

# ==============================================================================================================
def clear_tables():
    '''
    Clears the data from the tables used by the flask server.

    Parameter(s): None

    Output(s): 
        Bool: returns true if the tables are wiped, else returns false
    '''

    try:
        with sqlite3.connect('flashcards.db') as conn:
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