import pytest
from srblib import on_travis, Module

def test_Module():
    module = Module('spike/test_file.py')
    a = module.Test_class()
    assert(a.data == 1)
    assert(module.test_fun() == 1)
    assert(module.test_var == 1)
