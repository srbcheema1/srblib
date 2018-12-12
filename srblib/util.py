import sys

from .colour import Colour


_dependency_err_1 = """
    You haven't installed the required dependencies.
    Please install required dependencies using :"""
_dependency_err_2 = """        python3 -m pip install -r requirements.txt
"""
def show_dependency_error_and_exit():
    Colour.print(_dependency_err_1,Colour.RED)
    Colour.print(_dependency_err_2,Colour.YELLOW)
    sys.exit(1)


def line_adder(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        lines = [x.strip() for x in f.readlines()]
        if(not line in lines):
            f.seek(0, 0)
            f.write(content + '\n' + line + '\n')
