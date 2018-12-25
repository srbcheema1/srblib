import pytest
import os

from srblib import on_travis, verify_folder, verify_file, remove, file_name, file_extension, abs_path

def test_files_verifiers():
    if(not on_travis):
        return
    verify_folder(abs_path('./hello/world'))
    assert(os.path.exists(abs_path('./hello')) == True)
    assert(os.path.exists(abs_path('./hello/world')) == True)
    remove(abs_path('./hello/world'))
    assert(os.path.exists(abs_path('./hello')) == True)
    assert(os.path.exists(abs_path('./hello/world')) == False)
    verify_file(abs_path('./hello/world/helloworld.py'))
    assert(os.path.exists(abs_path('./hello')) == True)
    assert(os.path.exists(abs_path('./hello/world')) == True)
    assert(os.path.exists(abs_path('./hello/world/helloworld.py')) == True)
    remove(abs_path('./hello'))
    assert(os.path.exists(abs_path('./hello')) == False)
    assert(os.path.exists(abs_path('./hello/world')) == False)
    assert(os.path.exists(abs_path('./hello/world/helloworld.py')) == False)

def test_file_name_and_extensions():
    if(not on_travis):
        return
    mapp = {
            '.a':'.a',
            'a':'a',
            'a.py':'a.py',
            '.a.py':'.a.py',
            './hello/good.py':'good.py',
            'hello/good.py':'good.py',
            'hello/good':'good',
            'hello/.good':'.good',
            'hello/.good.py':'.good.py',
    }
    for a in mapp.keys():
        assert(file_name(a) == mapp[a])

    mapp = {
            '.a':'',
            'a':'',
            'a.py':'py',
            '.a.py':'py',
            './hello/good.py':'py',
            'hello/good.py':'py',
            'hello/good':'',
            'hello/.good':'',
    }
    for a in mapp.keys():
        assert(file_extension(a) == mapp[a])

