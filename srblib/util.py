import sys


from .colour import Colour
from .debugger import debug, on_travis
from .system import os_name


dump_output = ' > /dev/null 2>&1 '
if os_name == 'windows':
    dump_output = ' > nul 2>&1 '

_dependency_err_1 = """
    You haven't installed the required dependencies.
    Please install required dependencies using :"""
_dependency_err_2 = """        python3 -m pip install -r requirements.txt
"""
def show_dependency_error_and_exit():
    Colour.print(_dependency_err_1,Colour.RED)
    Colour.print(_dependency_err_2,Colour.YELLOW)
    if(debug or on_travis):
        import traceback
        traceback.print_exc()
    sys.exit(1)


def line_adder(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        lines = [x.strip() for x in f.readlines()]
        if(not line in lines):
            f.seek(0, 0)
            f.write(content + '\n' + line + '\n')

def top(container):
    for item in container:
        return item
    return None


from difflib import SequenceMatcher
def similarity(a, b):
    def _lcs(a,b):
        def _lcs_rec(i=0,j=0):
            if(i==len(a) or j==len(b)): return 0
            if dp[i][j] != -1: return dp[i][j]
            if(a[i] == b[j]): return 1 + _lcs(i+1,j+1)
            ret1 = _lcs(i,j+1)
            ret2 = _lcs(i+1,j)
            dp[i][j] = max(ret1,ret2)
            return dp[i][j]
        dp = []

        for i in range(len(a)):
            arr = []
            for j in range(len(b)):
                arr.append(-1)
            dp.append(arr)
        return _lcs_rec(0,0)
    a = str(a).lower()
    b = str(b).lower()
    if(len(a) * len(b) >= 1000):
        if(len(a) * len(b) >= 100000): raise Exception('Too long strings')
        ret = SequenceMatcher(None, a, b).ratio() * 100
        return 100 - (100-ret)*90/100 # reduce mismatch by 10%
    lcs = _lcs(a,b)
    lcs = int(lcs / min(len(a),len(b)) * 100)
    ret = SequenceMatcher(None, a, b).ratio() * 100
    ret = (ret + (1.5)*lcs)/(2.5)
    ret = (ret * lcs)/100
    return int(ret)
