__version__ = '0.1.4'
__mod_name__ = 'srblib'


from .colour import Colour # A class with color names and a static print function which prints coloured output to stderr

from .debugger import debug # a boolean whose value can be changed in ~/.config/srblib/debug.json
from .debugger import on_appveyor # a boolean value which is true if code is running on appveyor
from .debugger import on_ci # a boolean value which is true if it code is running on CI
from .debugger import on_srbpc # a boolean value which is true if it is my PC i.e. srb-pc
from .debugger import on_travis # a boolean value which is true if code is running on travis

from .dependency import install_arg_complete # A function to append line of argcomplete in ~/.bashrc
from .dependency import install_dependencies # A function that takes a special data-template to install dependencies
from .dependency import install_dependencies_pkg # similar but based on package-managers (Recommended)
from .dependency import is_installed # checks if the following application is installed on machine or not
from .dependency import remove_dependencies # Opposite of install_dependencies
from .dependency import remove_dependencies_pkg # Opposite of install_dependencies_pkg

from .email import email # a function
from .email import Email # a class to send email

from .files import file_extension # returns back the extention of a file from filepath, may return '' if no ext
from .files import file_name # returns filename from a filepath
from .files import remove # removes a path recursively. it deletes all files and folders under that path
from .files import verify_file # verify that a file exists. if not it will create one. also creates parents if needed
from .files import verify_folder # verify that a folder exists. creates one if not there. also creates parents if needed

from .file_importer import Module # a class to import modules

# one cant declare more attributes in frozen class
from .frozen import FrozenClass # A class to be inherited to make a class frozen. i.e. no more attributes can be added.

from .path import abs_path # returns absolute path of a path given. works on windows as well as linux.
from .path import is_child_of # returns if a given path is child(direct/indirect) of the second path given.
from .path import parent_dir # returns Nth parent of a path. default it returns 1st parent
from .path import relative_path # returns relative path if given absolute path

from .srb_bank import SrbBank # A class to store things for later use of a program. can act as a database
from .srb_json import SrbJson # A class to use json file more easily
from .srb_hash import path_hash # get hash of full path (recursively)
from .srb_hash import str_hash # get hash of string

from .soup import Soup # A class to make scrapping easier

from .system import get_os_name # returns OS name. values are windows, linux or mac
from .system import os_name # value of get_os_name
from .system import on_windows # True if system is windows OS

from .tabular import Tabular # A class to process dabular data

from .util import line_adder # append a line if not present in a given file
from .util import show_dependency_error_and_exit # display missing dependency error and exit
from .util import similarity # returns percentage of similarity of two strings
from .util import top # first element of list or set or dict(first key)
from .util import dump_output # variable containing string value ` > /dev/null 2>&1 ` or ` > nul 2>&1 `.
