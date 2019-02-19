from bs4 import BeautifulSoup
import requests

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
    def get_soup(url,*args,**kwargs):
        '''
        takes url and return soup.
        returns None if there is bad connection or bad response code.
        '''
        result = requests.get(url, *args, **kwargs)
        if(result is None or result.status_code is not 200):
            if(result == None):
                temp_result = requests.get('https://google.com')
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
            if type(inp) is Soup._trusted:
                self._data = inp._data
                return
            self._data = inp # it is actually a list

        def __getitem__(self,index):
            if(type(index) is slice): # a[1:9]
                return Soup._SO(Soup._trusted(self._data[index]))
            return Soup(Soup._trusted(self._data[index]))

        def __len__(self):
            return len(self._data)

        def __str__(self):
            return self._data.__str__()

    class _trusted:
        def __init__(self,_data):
            self._data = _data
