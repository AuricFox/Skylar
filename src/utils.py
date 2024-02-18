import logging, os, re

PATH = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(
    filename=os.path.join(PATH, './output/app.log'),
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
# Functions for processing text
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