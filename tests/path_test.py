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

def test_abs_path_windows():
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
