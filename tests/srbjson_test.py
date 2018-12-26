import pytest
import os

from srblib import on_travis, srbjson, remove

def test_srbbank():
    if(not on_travis):
        return
    a = srbjson('hello',{'test':{'debug':False,'password':None}})
    a['debug'] = True
    a['password'] = 'helloworld'
    b = srbjson('hello',{'test':{'debug':False,'password':None}})
    assert(b['debug'] == True)
    assert(b['password'] == 'helloworld')
    a['password'] = 'hello'
    assert(b['password'] == 'helloworld') # it gets updated in file while it is not yet updated in data of b, it is outdated
    b.fetch_data() # update data
    assert(b['password'] == 'hello') # it gets updated in file while it is not yet updated in data of b, it is outdated
    remove('hello')
    assert(b['debug'] == True) # it gets updated in file while it is not yet updated in data of b, it is outdated
