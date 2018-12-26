import pytest
import os

from srblib import on_travis, SrbJson, remove

def test_srbbank():
    if(not on_travis):
        return
    a = SrbJson('hello',{'test':{'debug':False,'password':None}})
    a['debug'] = True
    a['password'] = 'helloworld'
    b = SrbJson('hello',{'test':{'debug':False,'password':None}})
    assert(b['debug'] == True)
    assert(b['password'] == 'helloworld')
    a['password'] = 'hello'
    assert(b.data['password'] == 'helloworld') # it gets updated in file and data of a but not in data of b
    assert(b['password'] == 'hello') # it gets updated automatically. while accesssing data using operators
    remove('hello')
    assert(b['debug'] == False) # it gets False value as the file was deleted and it is regenerated again

def test_srbbank_strict():
    if(not on_travis):
        return
    a = SrbJson('hello',{'test':{'debug':False,'password':None}},strict=True)
    a['debug'] = True
    a['password'] = 'helloworld'

    try:
        a['help'] = 'it will fail'
        del a['debug']
        assert(False) # it should not reach here
    except:
        pass

    try:
        b = SrbJson('hello',{'test':{'debug':False,'password':None,'good':False}},strict=True)
        assert(False) # it should not reach here
    except:
        pass
