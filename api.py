from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


class OpenData:

    def get_last_100(self):

        url = 'https://data.jerseycitynj.gov/api/v2/catalog/datasets?'
        parameters = {'limit':'10',
                      'order_by':'modified desc',
                      'offset':'0',
                      'timezone':'UTC'
        }
        # headers = {
        #   'Accepts': 'application/json',
        #   'X-CMC_PRO_API_KEY': 'enter-your-api-key-here',
        # }
        headers = {
          'Accepts': 'application/json'
        }

        session = Session()
        session.headers.update(headers)

        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data['datasets']
      

    def get_attachments(self, url):
      
        headers = {
          'Accepts': 'application/json'
        }

        session = Session()
        session.headers.update(headers)
        response = session.get(url)
        data = json.loads(response.text)
        return data['attachments']
    
      
# https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python

from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()


