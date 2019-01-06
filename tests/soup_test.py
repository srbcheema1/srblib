import pytest
from bs4 import BeautifulSoup
from srblib import on_travis, Soup

def test_soup():
    soup = BeautifulSoup('<p><div class="good">hello</div><div>world</div></p>','html.parser')
    a = Soup(soup)
    b = a['div']
    assert(len(b) == 2)
    b = a['div',{'class':'good'}]
    assert(len(b) == 1)
    b = a['div'][0].parent['div'] # cascading over [],find_all and parent
    assert(len(b) == 2)


