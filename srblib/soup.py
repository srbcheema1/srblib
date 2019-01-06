import grequests
from bs4 import BeautifulSoup

from .colour import Colour

class Soup:

    def __init__(self,inp):
        if type(inp) is str:
            self.soup = Soup.get_soup(inp)
        elif type(inp) is BeautifulSoup:
            self.soup = inp
        elif type(inp) is Soup._trusted:
            self.soup = inp._data
        else:
            raise Exception('requires string as argument')

        self._sync()

        # ignore_var_list = ['__class__','__weakref__','__dir__']
        # ignore_var_list.extend(Soup._defined_vars)
        # list_vars = dir(self.soup)
        # _soup = self.soup
        # for var in list_vars:
            # if not var in ignore_var_list:
                # setattr(self,var,getattr(_soup,var))


    _defined_vars = ['__getitem__','find_all']

    def __getitem__(self,index):
        if(type(index) is tuple):
            return self.find_all(*index)
        return self.find_all(index)

    def find_all(self,*args,**kwargs):
        ret = self.soup.find_all(*args,**kwargs)
        return Soup._SO(ret)

    def __getattr__(self, name): # this one is better way
        try:
            return getattr(self,name)
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            return getattr(self.soup,name)

    def __str__(self):
        return self.soup.prettify()

    def _sync(self):
        if self.soup.parent is None:
            self.parent = None
        else:
            self.parent = Soup(Soup._trusted(self.soup.parent))

    @staticmethod
    def get_soup(url):
        '''
        takes url and return soup.
        returns None if there is bad connection or bad response code.
        '''
        unsent_requests = (grequests.get(url) for url in [url])
        result = grequests.map(unsent_requests)[0]
        if(result is None or result.status_code is not 200):
            if(result == None):
                temp_unsent_requests = (grequests.get(url) for url in ['https://google.com'])
                temp_result = grequests.map(temp_unsent_requests)[0]
                if(temp_result == None):
                    colour.print('please check your internet connection', colour.red)
                else:
                    colour.print('please check your url', colour.red)
            else:
                Colour.print('soup result on '+url+' :'+Colour.END+str(result), Colour.RED)
            return None
        soup = BeautifulSoup(result.text, 'html.parser')
        return soup

    class _SO:
        def __init__(self,inp):
            self.data = inp # it is actually a list

        def __getitem__(self,index):
            return Soup(Soup._trusted(self.data[index]))

        def __len__(self):
            return len(self.data)

        def __str__(self):
            return self.data.__str__()

    class _trusted:
        def __init__(self,data):
            self._data = data
