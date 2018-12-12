import sys

from .Colour import Colour


_dependency_err_1 = """
    You haven't installed the required dependencies.
    Please install required dependencies using :"""
_dependency_err_2 = """        python3 -m pip install -r requirements.txt
"""
def show_dependency_error_and_exit():
    Colour.print(_dependency_err_1,Colour.RED)
    Colour.print(_dependency_err_2,Colour.YELLOW)
    sys.exit(1)
