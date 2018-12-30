import pytest
import os

from srblib import on_travis
from srblib import Tabular

def test_tabular():
    if(not on_travis):
        return

    a = Tabular('spike/excel.xlsx')
    print(a,a[0])
    assert(len(a) == 3)
    assert(len(a[0]) == 3)
    assert(a[0][0] == 'name')
    assert(a[1]['name'] == 'pagal')
    assert(a['name'][0] == 'pagal')
    assert(len(a['name']) == 2)
    a.write_csv('test.csv')
    a.write_json('test.json')
    a.write_xls('test.xlsx')


    b = Tabular('test.xlsx')
    assert(len(b) == 3)
    assert(len(b[0]) == 3)
    assert(b[0][0] == 'name')
    assert(b[1]['name'] == 'pagal')
    assert(b['name'][0] == 'pagal')
    assert(len(b['name']) == 2)

    c = Tabular('test.csv')
    c = Tabular('test.json')
