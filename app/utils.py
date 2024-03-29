import logging, os, re, mimetypes

PATH = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(
    filename=os.path.join(PATH, '../logs/app.log'),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s'
)

LOGGER = logging.getLogger(__name__)

# ========================================================================================================================================
# Error Handling
# ========================================================================================================================================
class InvalidFile(Exception): pass
class FileNotFound(Exception): pass
class InvalidInput(Exception): pass

# ========================================================================================================================================
def sanitize(text:str):
    '''
    Removes special characters from the string.

    Parameter(s):
        text (str): the string being sanitized

    Output(s):
        str: a sanitized string
    '''
    return re.sub(r'[\\/*?:"<>|]', '_', text)

# ========================================================================================================================================
def verify_file(file:str):
    '''
    Verifies input file

    Parameter(s):
        file (str): name of the provided file

    Output(s):
        True if the file is valid, else False
    '''

    try:
        # Replace special characters with underscores
        sanitized_name = re.sub(r'[\\/*?:"<>| ]', '_', file)
        # Remove leading and trailing whitespace
        sanitized_name = sanitized_name.strip()
        # Getting the name of the file without the extension
        sanitized_name = sanitized_name.split('.')[0]

        allowed_mime_types = ['application/json']
        allowed_extensions = ['.json']

        # Get the file's MIME type and extension
        file_mime_type, _ = mimetypes.guess_type(file)
        file_extension = os.path.splitext(file)[1].lower()

        # Check if the file's MIME type or extension is allowed
        if file_mime_type is not None and file_mime_type not in allowed_mime_types:
            LOGGER.error(f'{file} MIME type is not supported! MIME type: {file_mime_type}')
            return False

        if file_extension not in allowed_extensions:
            LOGGER.error(f'{file} extension is not supported! Extension: {file_extension}')
            return False
        
        return True

    except Exception as e:
        LOGGER.error(f"An error occured when validating {file}: {e}")
        return False
    
# ========================================================================================================================================
class Cache:
    '''
    Creates a cache of data to prevent repetitive calls
    '''
    def __init__(self):
        '''
        Initializes the cache with an empty dictionary
        '''
        self.cache = {}

    # ------------------------------------------------------------
    def update(self, dict1:dict):
        '''
        Updates the current cache with new data

        Parameter(s):
            dict1 (dict): dictionary with new data

        Output(s): None
        '''
        self.cache.update(dict1)

    # ------------------------------------------------------------
    def drop(self, key:str):
        '''
        Drops a key element from the cahce
        
        Parameter(s):
            key (str): the key element in the dict being dropped

        Output(s):
            Raises a keyError if an error occurs, else None
        '''
        if key in self.cache:
            self.cache.pop(key)
        else:
            raise KeyError(f"Key '{key}' not found in cache")

    # ------------------------------------------------------------
    def clear(self):
        '''
        Resets the cache to an empty dictionary
        '''
        self.cache = {}