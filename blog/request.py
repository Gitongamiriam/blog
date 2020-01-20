from .models import Quote
import requests

url ="http://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
    '''
    a function to return the quotes class instance
    '''
    response = requests.get(url).json()
    random_quote = Quote(response.get("author"), response.get("quote"))
    return response