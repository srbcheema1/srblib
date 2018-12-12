import pytest
import os

from srblib.path import abs_path, _change_slash, _reactified
pwd = _change_slash(str(os.getcwd()))#always return without / at end;
parent_dir = _reactified(os.path.join(pwd,'..'))


def test_abs_path_windows():
    from srblib.path import _abs_path_windows
    home_path = os.getenv("userprofile")#always return without / at end, ex: C:\User\srb
    if(not home_path):home_path = 'C:\\User\\testing'
    home_path = _change_slash(home_path)

    path_tests = {
        "C:\\":"C:",
        "C:\\User\\srb\\hello":"C:/User/srb/hello",
        "C:\\User\\srb\\hello\\":"C:/User/srb/hello",
        "User\\srb\\hello\\":pwd+"/User/srb/hello",
        "..\\User\\srb\\hello\\":parent_dir+"/User/srb/hello",
        "~\\srb\\hello\\":home_path+"/srb/hello",

        "C:/":"C:",
        "C:/User/srb/hello":"C:/User/srb/hello",
        "C:/User/srb/hello/":"C:/User/srb/hello",
        "User/srb/hello/":pwd+"/User/srb/hello",
        "../User/srb/hello/":parent_dir+"/User/srb/hello",
        "~/srb/hello/":home_path+"/srb/hello",
    }

    for path in path_tests.keys():
        res = path_tests[path]
        assert(_abs_path_windows(path,debug=True)==res)

def test_abs_path_unix():
    from srblib.path import _abs_path_unix
    home_path = os.getenv("HOME")#always return without / at end, ex: C:\User\srb

    path_tests = {
        "User/srb/hello/":pwd+"/User/srb/hello",
        "../User/srb/hello/":parent_dir+"/User/srb/hello",
        "~/srb/hello/":home_path+"/srb/hello",
        "hell/../good":pwd+"/good",
    }

    for path in path_tests.keys():
        res = path_tests[path]
        assert(_abs_path_unix(path)==res)

def test_is_child_of():
    from srblib import is_child_of
    home_path = os.getenv("HOME")#always return without / at end, ex: C:\User\srb

    path_tests_true = {
        "User/srb/hello/":pwd+"/User/srb/hello/world/cpp",
        "../User/srb/hello/":parent_dir+"/User/srb/hello/world",
        "~/srb/hello/":home_path+"/srb/hello/world",
        "hell/../good":pwd+"/good",
    }

    path_tests_false = {
        "User/srb/hello/":pwd+"/User/srbcheema",
        "../User/srb/hello/":parent_dir+"/User/srb",
    }

    for path in path_tests_true.keys():
        res = path_tests_true[path]
        assert(is_child_of(path,res))

    for path in path_tests_false.keys():
        res = path_tests_false[path]
        assert(not is_child_of(path,res))
