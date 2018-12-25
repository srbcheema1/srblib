import pytest
import os

from srblib import on_travis, srbbank

def test_srbbank():
    if(not on_travis):
        return
    a = srbbank('hello')
    a['hello'] = 'world'
    b = srbbank('hello')
    assert(b['hello'] == 'world')
    b.setpass('password')
    try:
        c = srbbank('hello','wrongpassword')
        c = srbbank('hello') # no password
        assert(False) # it shouldn't have reached here
    except:
        pass

    c = srbbank('hello','password')
    assert(c['hello'] == 'world')
