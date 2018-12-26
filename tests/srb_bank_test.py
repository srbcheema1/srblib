import pytest
import os

from srblib import on_travis, SrbBank

def test_SrbBank():
    if(not on_travis):
        return
    a = SrbBank('hello')
    a['hello'] = 'world'
    b = SrbBank('hello')
    assert(b['hello'] == 'world')
    b.setpass('password')
    try:
        c = SrbBank('hello','wrongpassword')
        c = SrbBank('hello') # no password
        assert(False) # it shouldn't have reached here
    except:
        pass

    c = SrbBank('hello','password')
    assert(c['hello'] == 'world')
