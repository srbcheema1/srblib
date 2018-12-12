__version__ = '0.0.1'
__mod_name__ = 'srblib'

from .path import abs_path
from .path import is_child_of

from .colour import Colour

from .files import verify_file
from .files import verify_folder
from .files import remove

'''
return windows, linux or mac
'''
from .system import get_os_name

from .util import show_dependency_error_and_exit
